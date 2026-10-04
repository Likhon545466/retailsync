# WorkspaceIndex Component

## Purpose
The `WorkspaceIndex` organizes the system's operational modules into a clean, typography-led ruled index. It eliminates the 6 identical emoji bento cards in favor of a clear, role-prioritized 2-column index with hairline dividers.

## Constraints Adherence
- Strictly ruled index layout; zero card boxes, zero drop shadows, zero gradient borders.
- Numbered index headers (`01`, `02`, `03`...) using `var(--font-mono)`.
- Reordered dynamically based on the active role selected in `RoleSwitcher`.
- The active role's primary workflow is elevated with prominent type scale and accent indicator.

## Workspaces Included
1. **Checkout POS** (`/pos`) - Shortcut `[P]`
2. **Inbound Receiving** (`/inbound`) - Shortcut `[I]`
3. **Directed Putaway** (`/putaway`) - Shortcut `[U]`
4. **Spatial Twin** (`/warehouse`) - Shortcut `[W]`
5. **Replenishment DSS** (`/procurement`) - Shortcut `[R]`
6. **Stock Ledger** (`/audits`) - Shortcut `[L]`

## Role Prioritization Matrix
- `cashier`: Checkout POS (01, Primary)
- `clerk`: Inbound Receiving (01, Primary)
- `operator`: Directed Putaway (01, Primary)
- `supervisor`: Spatial Twin (01, Primary)
- `procurement`: Replenishment DSS (01, Primary)
- `admin`: Standard balanced ordering (01 to 06)
