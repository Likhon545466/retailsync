# AttentionRow Component

## Purpose
The `AttentionRow` represents a single operational action item inside the `AttentionList`. It contains a 6px semantic status indicator dot, a monospaced reference tag, an issue title, a concise plain-English explanation, and a text action link (`Resolve →`).

## Constraints Adherence
- Status dot is strictly 6px by 6px (`width: 6px; height: 6px; border-radius: 50%`).
- Semantic colors (`#EF4444` danger, `#F59E0B` warning, `#10B981` success) appear only on this dot.
- Plain operational English description with fewer than 12 words.
- Hairline bottom divider.
- Hovering the row shifts the action arrow 4px to the right via CSS transition.

## Props
- `status_type` ("danger" | "warning" | "success" | "info")
- `tag` (string, e.g. "BATCH-402")
- `title` (string, e.g. "Quarantine inspection required")
- `detail` (string, e.g. "Milk carton damage reported at Dock 2 during receiving sweep.")
- `action_url` (string, e.g. "/inbound")
- `action_label` (string, e.g. "Inspect dock")
- `role` (string, e.g. "clerk")

## States
- Default: Neutral background, subtle hairline bottom border.
- Hover: Background highlights softly (`var(--color-surface-hover)`), action arrow shifts 4px right.
