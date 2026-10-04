# StatusStrip Component

## Purpose
The `StatusStrip` provides a unified horizontal operational summary across the full content width. Rather than disjointed, multicolored KPI tiles or cards, it presents a continuous data strip partitioned by vertical hairline dividers. The primary metric (Inventory Valuation) is deliberately emphasized at 31px (`--type-5`), creating an immediate typographic focal point.

## Constraints Adherence
- Strictly hairline dividers between items (`border-right: var(--hairline-w) solid var(--border-hairline)`).
- Zero card containers, zero background fills, zero drop shadows.
- Single accent color used only for the primary metric value; secondary metrics use neutral high-contrast color.
- Plain operational English labels (no internal database jargon).
- Fully responsive: wraps smoothly to 2 columns on tablet and 1 column on mobile without clipping.

## Metrics Displayed
1. **Total Inventory Valuation** (Primary, 31px mono, count-up animation)
2. **Active SKUs** (Catalog items currently in distribution)
3. **Active Batches** (FEFO batches stocked in warehouse)
4. **Open Orders** (Purchase orders pending receiving)
5. **Checkout Latency** (Operational transaction response, e.g., "118 ms")
