# NavMenu Component

## Purpose
The `NavMenu` component provides clear, uncrowded primary operational links (maximum 4 items) and moves secondary workspaces and documentation into a clean hairline "More" dropdown. This guarantees zero wrapping even on dense viewports (768px-1024px).

## Constraints Adherence
- Strictly 4 visible primary links on desktop; secondary items nested inside "More" dropdown.
- Hairline indicators (`border-bottom: 2px solid var(--color-accent)`) for active link.
- 44px minimum touch targets on mobile / interactive hitboxes.
- Keyboard accessible: closes on Escape, arrow navigation support.

## Props / Context
- `active_page` (string): Active route key (`"dashboard"`, `"pos"`, `"inbound"`, `"putaway"`, `"warehouse"`, `"procurement"`, `"audits"`).

## States
- **Normal**: Text color `var(--color-text-mid)`.
- **Hover**: Text color `var(--color-text-high)`.
- **Active**: Text color `var(--color-text-high)`, hairline accent underline.
- **Dropdown Open**: `aria-expanded="true"`, menu visible with hairline border and neutral surface.
