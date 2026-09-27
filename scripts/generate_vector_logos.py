#!/usr/bin/env python3
"""
RetailSync: Vector Logo & Brand Asset Generator
Generates clean, scalable SVG assets:
1. retailsync_logo.svg - Minimalist Geometric Logo Mark (Icon)
2. retailsync_wordmark.svg - Full Horizontal Corporate Identity with Typography
3. favicon.svg - High-contrast browser favicon
"""

import os

SVG_ICON = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="100%" height="100%" fill="none">
  <defs>
    <!-- Background Gradient -->
    <radialGradient id="bgGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#0e2a4a" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="#090d16" stop-opacity="0"/>
    </radialGradient>

    <!-- Electric Cyan Gradient -->
    <linearGradient id="cyanGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#0ea5e9"/>
    </linearGradient>

    <!-- Deep Azure Gradient -->
    <linearGradient id="azureGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>

    <!-- Sapphire Accent Gradient -->
    <linearGradient id="sapphireGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#2563eb"/>
      <stop offset="100%" stop-color="#1d4ed8"/>
    </linearGradient>

    <!-- Subtle Glow Filter -->
    <filter id="neonGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="8" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>

  <!-- Ambient Glow -->
  <circle cx="256" cy="256" r="230" fill="url(#bgGlow)" />

  <!-- Outer Orbital Sync Ring (Circulating Flow) -->
  <g opacity="0.9">
    <!-- Top-Right Sync Arc -->
    <path d="M 380 180 A 170 170 0 0 1 426 256 A 170 170 0 0 1 310 412" 
          stroke="url(#cyanGrad)" stroke-width="12" stroke-linecap="round" fill="none" stroke-dasharray="260 20" />
    <!-- Arrowhead 1 -->
    <polygon points="305,404 316,428 296,424" fill="#0ea5e9" />

    <!-- Bottom-Left Sync Arc -->
    <path d="M 132 332 A 170 170 0 0 1 86 256 A 170 170 0 0 1 202 100" 
          stroke="url(#azureGrad)" stroke-width="12" stroke-linecap="round" fill="none" stroke-dasharray="260 20" />
    <!-- Arrowhead 2 -->
    <polygon points="207,108 196,84 216,88" fill="#38bdf8" />
  </g>

  <!-- Central Isometric Warehouse Cube ("R" & "S" Synthesis) -->
  <g transform="translate(0, -6)">
    <!-- Top Facet (Warehouse Roof / Storage Node) -->
    <polygon points="256,128 356,186 256,244 156,186" 
             fill="url(#cyanGrad)" filter="url(#neonGlow)" opacity="0.95" />
    <!-- Subtle Top Highlight -->
    <polygon points="256,134 346,186 256,238 166,186" 
             fill="none" stroke="#ffffff" stroke-width="2" opacity="0.4" />

    <!-- Left Facet: Stylized "R" Structure -->
    <path d="M 150,198 
             L 248,254 
             L 248,374 
             L 204,348 
             L 204,284 
             L 174,302 
             L 174,330 
             L 150,316 
             Z" 
          fill="url(#azureGrad)" />
    <!-- Inner R Eye Cutout -->
    <polygon points="174,232 224,260 204,272 174,254" fill="#090d16" />

    <!-- Right Facet: Stylized "S" Structure -->
    <path d="M 264,254 
             L 362,198 
             L 362,238 
             L 308,270 
             L 362,302 
             L 362,342 
             L 264,398 
             L 264,358 
             L 318,326 
             L 264,294 
             Z" 
          fill="url(#sapphireGrad)" />
  </g>

  <!-- Center Sync Core Node (Glowing Pulse) -->
  <circle cx="256" cy="250" r="10" fill="#ffffff" filter="url(#neonGlow)" />
  <circle cx="256" cy="250" r="4" fill="#0ea5e9" />

  <!-- Bottom Barcode Accent Bars (Warehouse Inventory Anchor) -->
  <g opacity="0.7" transform="translate(196, 440)">
    <rect x="0" y="0" width="6" height="18" rx="2" fill="#38bdf8" />
    <rect x="12" y="0" width="12" height="18" rx="2" fill="#0ea5e9" />
    <rect x="30" y="0" width="6" height="18" rx="2" fill="#38bdf8" />
    <rect x="42" y="0" width="18" height="18" rx="2" fill="#0ea5e9" />
    <rect x="66" y="0" width="6" height="18" rx="2" fill="#38bdf8" />
    <rect x="78" y="0" width="12" height="18" rx="2" fill="#0ea5e9" />
    <rect x="96" y="0" width="6" height="18" rx="2" fill="#38bdf8" />
    <rect x="108" y="0" width="12" height="18" rx="2" fill="#0284c7" />
  </g>
</svg>
'''

SVG_WORDMARK = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 220" width="100%" height="100%" fill="none">
  <defs>
    <linearGradient id="wmCyanGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#0ea5e9"/>
    </linearGradient>
    <linearGradient id="wmAzureGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>
    <linearGradient id="wmSapphireGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#2563eb"/>
      <stop offset="100%" stop-color="#1d4ed8"/>
    </linearGradient>
    <filter id="wmGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>

  <!-- Left: Logo Icon Mark (Scaled down to 180x180 at x=20, y=20) -->
  <g transform="translate(10, 10) scale(0.39)">
    <!-- Outer Sync Arcs -->
    <path d="M 380 180 A 170 170 0 0 1 426 256 A 170 170 0 0 1 310 412" 
          stroke="url(#wmCyanGrad)" stroke-width="14" stroke-linecap="round" fill="none" stroke-dasharray="260 20" />
    <polygon points="305,404 316,428 296,424" fill="#0ea5e9" />

    <path d="M 132 332 A 170 170 0 0 1 86 256 A 170 170 0 0 1 202 100" 
          stroke="url(#wmAzureGrad)" stroke-width="14" stroke-linecap="round" fill="none" stroke-dasharray="260 20" />
    <polygon points="207,108 196,84 216,88" fill="#38bdf8" />

    <!-- Isometric Cube -->
    <g transform="translate(0, -6)">
      <polygon points="256,128 356,186 256,244 156,186" fill="url(#wmCyanGrad)" filter="url(#wmGlow)" opacity="0.95" />
      <path d="M 150,198 L 248,254 L 248,374 L 204,348 L 204,284 L 174,302 L 174,330 L 150,316 Z" fill="url(#wmAzureGrad)" />
      <polygon points="174,232 224,260 204,272 174,254" fill="#090d16" />
      <path d="M 264,254 L 362,198 L 362,238 L 308,270 L 362,302 L 362,342 L 264,398 L 264,358 L 318,326 L 264,294 Z" fill="url(#wmSapphireGrad)" />
    </g>
    <circle cx="256" cy="250" r="10" fill="#ffffff" filter="url(#wmGlow)" />
  </g>

  <!-- Vertical Divider Line -->
  <line x1="225" y1="45" x2="225" y2="175" stroke="#334155" stroke-width="2" stroke-linecap="round" />

  <!-- Right: Typography Wordmark -->
  <!-- "RETAIL" in crisp bold white -->
  <text x="250" y="118" 
        font-family="'Plus Jakarta Sans', 'Inter', system-ui, sans-serif" 
        font-size="64" 
        font-weight="800" 
        letter-spacing="-1.5" 
        fill="#ffffff">RETAIL</text>

  <!-- "SYNC" in glowing electric cyan -->
  <text x="500" y="118" 
        font-family="'Plus Jakarta Sans', 'Inter', system-ui, sans-serif" 
        font-size="64" 
        font-weight="800" 
        letter-spacing="-1.5" 
        fill="url(#wmCyanGrad)"
        filter="url(#wmGlow)">SYNC</text>

  <!-- Subtitle: Enterprise Descriptor -->
  <text x="252" y="156" 
        font-family="'Plus Jakarta Sans', 'Inter', system-ui, sans-serif" 
        font-size="16" 
        font-weight="700" 
        letter-spacing="3" 
        fill="#94a3b8" 
        text-transform="uppercase">Centralized Super Shop WMS</text>

  <!-- Tech Telemetry Pill -->
  <g transform="translate(680, 142)">
    <rect x="0" y="0" width="130" height="24" rx="6" fill="#1e293b" stroke="#334155" stroke-width="1"/>
    <circle cx="12" cy="12" r="4" fill="#10b981" />
    <text x="24" y="16" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700" fill="#38bdf8">v2.0-RELEASE</text>
  </g>
</svg>
'''

SVG_FAVICON = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64">
  <defs>
    <linearGradient id="favCyan" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#0ea5e9"/>
    </linearGradient>
    <linearGradient id="favAzure" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#1d4ed8"/>
    </linearGradient>
  </defs>
  <rect width="64" height="64" rx="14" fill="#090d16"/>
  <!-- Top Roof -->
  <polygon points="32,14 46,22 32,30 18,22" fill="url(#favCyan)"/>
  <!-- Left Side -->
  <polygon points="18,24 30,31 30,48 18,41" fill="url(#favAzure)"/>
  <!-- Right Side -->
  <polygon points="34,31 46,24 46,41 34,48" fill="#2563eb"/>
  <!-- Sync Dot -->
  <circle cx="32" cy="31" r="2.5" fill="#ffffff"/>
</svg>
'''

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    assets_dir = os.path.join(project_root, "proposal", "assets")
    os.makedirs(assets_dir, exist_ok=True)

    icon_path = os.path.join(assets_dir, "retailsync_logo.svg")
    wordmark_path = os.path.join(assets_dir, "retailsync_wordmark.svg")
    favicon_path = os.path.join(assets_dir, "favicon.svg")

    with open(icon_path, "w", encoding="utf-8") as f:
        f.write(SVG_ICON)
    with open(wordmark_path, "w", encoding="utf-8") as f:
        f.write(SVG_WORDMARK)
    with open(favicon_path, "w", encoding="utf-8") as f:
        f.write(SVG_FAVICON)

    print(f"Generated Vector Logo Icon: {icon_path}")
    print(f"Generated Vector Wordmark:  {wordmark_path}")
    print(f"Generated Vector Favicon:   {favicon_path}")

if __name__ == "__main__":
    main()
