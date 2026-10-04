# RoleSwitcher Component

## Purpose
The `RoleSwitcher` allows users and demonstrators to switch active operational personas (`cashier`, `clerk`, `operator`, `supervisor`, `procurement`, `admin`). When a role is selected, the Overview page dynamically updates:
1. Re-orders the Workspaces Index so the role's primary workflow appears first in large type.
2. Filters the Attention Queue to prioritize items relevant to that role.
3. Persists the role selection in `localStorage` and synchronizes with server sessions.

## Constraints Adherence
- Clean hairline border (`var(--hairline-w) solid var(--border-hairline)`).
- Monospaced indicator tag or clean subtle select.
- Zero pill badges, zero emoji icons.
- Strict 44px touch target height.

## Roles Supported
- `cashier`: Cashier (Primary: Checkout POS)
- `clerk`: Dock Clerk (Primary: Inbound Receiving)
- `operator`: Floor Operator (Primary: Putaway & Picking)
- `supervisor`: Shift Supervisor (Primary: Warehouse Spatial Twin)
- `procurement`: SCM Officer (Primary: Replenishment DSS)
- `admin`: Operations Director (Full System Overview)

## States
- **Default**: Neutral surface, subtle hairline border.
- **Focus / Active**: Single accent outline ring (`var(--color-accent)`).
- **Disabled**: Dimmed text and border.
