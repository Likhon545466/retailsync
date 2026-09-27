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

@router.post("/logout")
def logout(response: Response):
    response.delete_cookie(key="retailsync_token")
    return {"status": "SUCCESS", "message": "Logged out successfully"}
