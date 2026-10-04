# WorkspaceRow Component

## Purpose
The `WorkspaceRow` renders an individual system module in the `WorkspaceIndex`. It displays an index number (`01`), the module title, a shortcut key badge, a single-line operational description (<12 words), and a right-aligned indicator arrow.

## Constraints Adherence
- Zero card containers, zero gradient fills, zero drop shadows, zero emoji icons.
- Hairline bottom border (`var(--hairline-w) solid var(--border-hairline)`).
- Monospaced index number (`var(--font-mono)`).
- Hover transition: arrow translates 4px right (`transform: translateX(4px)`).
- Primary role styling: larger type size (20px) and accent indicator when prioritized.

## Props
- `num` (string, e.g. "01")
- `title` (string, e.g. "Checkout POS")
- `href` (string, e.g. "/pos")
- `shortcut` (string, e.g. "P")
- `desc` (string, e.g. "Fast barcode checkout terminal with real-time stock allocation.")
- `is_primary` (boolean)

## States
- Default: Neutral background, hairline bottom border.
- Hover: Arrow moves 4px to the right, title color shifts to high contrast.
- Primary: Elevated font size and visual priority for the selected role.
