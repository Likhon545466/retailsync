from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from datetime import timedelta

from retailsync_app.database import get_db
from retailsync_app import models, schemas, auth
from retailsync_app.config import settings

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/login", response_model=schemas.TokenResponse)
def login(request: schemas.LoginRequest, response: Response, db: Session = Depends(get_db)):
    user = (
        db.query(models.User)
        .filter(
            (models.User.username == request.username_or_email) |
            (models.User.email == request.username_or_email)
        )
        .first()
    )
    if not user or not auth.verify_password(request.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username/email or password.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = auth.create_access_token(
        data={"sub": user.username, "role": user.role.value if hasattr(user.role, "value") else str(user.role)}
    )

    # Set HTTP-only cookie for seamless browser/Jinja2 template navigation
    response.set_cookie(
        key="retailsync_token",
        value=access_token,
        httponly=True,
        max_age=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60,
        samesite="lax"
    )

    return schemas.TokenResponse(
        access_token=access_token,
        token_type="Bearer",
        expires_in_seconds=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60,
        user=schemas.UserResponse(
            user_id=user.user_id,
            username=user.username,
            email=user.email,
            full_name=user.full_name,
            role=user.role.value if hasattr(user.role, "value") else str(user.role)
        )
    )

@router.get("/me", response_model=schemas.UserResponse)
def get_current_user_profile(user: models.User = Depends(auth.get_current_user)):
    return schemas.UserResponse(
        user_id=user.user_id,
        username=user.username,
        email=user.email,
        full_name=user.full_name,
        role=user.role.value if hasattr(user.role, "value") else str(user.role)
    )

@router.post("/switch-role")
def switch_role(request: schemas.RoleSwitchRequest, response: Response, db: Session = Depends(get_db)):
    role_target = request.role.lower().strip()
    user_map = {
        "admin": "admin",
        "manager": "admin",
        "store_manager": "admin",
        "supervisor": "supervisor",
        "procurement": "procurement",
        "cashier": "cashier",
        "clerk": "clerk",
        "operator": "operator",
    }
    target_username = user_map.get(role_target, role_target)
    user = db.query(models.User).filter(models.User.username == target_username).first()
    if not user:
        try:
            role_enum = models.UserRole[role_target.upper()]
            user = db.query(models.User).filter(models.User.role == role_enum).first()
        except (KeyError, ValueError):
            pass

    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid persona or role '{request.role}' specified."
        )

    access_token = auth.create_access_token(
        data={"sub": user.username, "role": user.role.value if hasattr(user.role, "value") else str(user.role)}
    )

    response.set_cookie(
        key="retailsync_token",
        value=access_token,
        httponly=True,
        max_age=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60,
        samesite="lax"
    )

    return {
        "status": "SUCCESS",
        "message": f"Active persona switched to {user.full_name} ({user.role.value if hasattr(user.role, 'value') else str(user.role)})",
        "user": {
            "user_id": user.user_id,
            "username": user.username,
            "full_name": user.full_name,
            "role": user.role.value if hasattr(user.role, "value") else str(user.role)
        }
    }

@router.post("/logout")
def logout(response: Response):
    response.delete_cookie(key="retailsync_token")
    return {"status": "SUCCESS", "message": "Logged out successfully"}

