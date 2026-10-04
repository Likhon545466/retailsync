# Metric Component

## Purpose
The `Metric` component renders an isolated quantitative data point: a small muted uppercase label on top, a large monospaced value below, and an optional concise operational note beneath.

## Constraints Adherence
- Strictly monospaced figures (`font-family: var(--font-mono); font-feature-settings: "tnum" 1;`).
- Zero cards, colored pills, or icon containers.
- Hairline borders or typographic hierarchy for grouping.

## Props
- `label` (string): Uppercase caption (e.g., "Active SKUs").
- `value` (string | number): Formatted numerical value.
- `subtext` (string): Plain operational detail (<6 words).
- `is_primary` (boolean): If true, renders in display mono size (31px) with the single accent color.

## States
- Default: Neutral high-contrast text.
- Primary: Accent color (`var(--color-accent)`).
