# SiteHeader Component

## Purpose
The `SiteHeader` is a 56px sticky, top-level navigation bar for the Swiss Minimalist design system. It anchors the application with the uppercase wordmark on the left, primary navigation links with an overflow dropdown in the center, and the utility controls (RoleSwitcher, ThemeToggle, and Documentation menu) on the right.

## Constraints Adherence
- Strict 56px fixed height (`var(--space-7)`).
- Hairline bottom border (`var(--hairline-w) solid var(--border-hairline)`).
- Sticky positioning (`position: sticky; top: 0; z-index: var(--z-sticky)`).
- Backdrop blur with neutral background for content passthrough (`backdrop-filter: blur(12px)`).
- Zero drop shadows, gradients, or pill badge containers.

## Props / Context
- `active_page` (string): Key of currently active route (`"dashboard"`, `"pos"`, `"inbound"`, etc.).
- `current_user` (models.User | null): Currently authenticated user object.

## States
- **Default**: Transparent/translucent background, hairline divider visible.
- **Scrolled**: Solidified background to ensure contrast when scrolling under page content.
- **Mobile (<768px)**: NavMenu collapses to hamburger icon button; drawer expands on toggle.
