# ThemeToggle Component

## Purpose
The `ThemeToggle` component toggles the root document between Dark and Light mode (`data-theme="dark"` / `data-theme="light"`). It uses sharp geometric SVG icons (sun and moon) instead of emoji, respecting the Swiss Minimalist hard constraint against emoji icons.

## Constraints Adherence
- Strictly geometric SVG icons with hairline strokes (1.5px).
- Zero emoji icons (`☀️`, `🌙` are forbidden).
- Hairline border container, 36x36px size, 44x44px interactive touch area.
- Instant localStorage update and DOM mutation without layout shift or FOUC.

## States
- **Dark Mode Active**: Renders Sun SVG icon (to switch to light).
- **Light Mode Active**: Renders Moon SVG icon (to switch to dark).
- **Hover**: Subtle hairline border darkening/lightening.
- **Focus**: 2px single accent focus ring with 2px offset.
