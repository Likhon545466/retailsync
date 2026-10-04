# AttentionList Component

## Purpose
The `AttentionList` presents operational exceptions requiring prompt human triage (quarantined pallets, impending expiry batches, safety-stock alerts, overdue purchase orders). Instead of alert banners, cards, or warning modals, it formats issues as a clean ruled list with a hairline border between entries.

## Constraints Adherence
- Strictly ruled list structure (`border-bottom: var(--hairline-w) solid var(--border-hairline)`).
- Zero cards, zero background fills, zero drop shadows.
- Items sorted by urgency (Critical / Warning / Notice).
- Role-aware filtering: displays exceptions pertinent to the selected role.

## Structure
- Section header with title "Needs attention" and count indicator.
- List container containing multiple `AttentionRow` components.
- Empty state: clean, single-line text confirmation ("No pending operational exceptions").
