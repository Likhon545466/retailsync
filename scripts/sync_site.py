#!/usr/bin/env python3
"""
Sync site files from proposal/ to root for static hosting deployments
(GitHub Pages, Vercel, Netlify, Cloudflare Pages, etc.)
"""
import os
import shutil

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROPOSAL_DIR = os.path.join(ROOT_DIR, "proposal")
PROPOSAL_ASSETS = os.path.join(PROPOSAL_DIR, "assets")
ROOT_ASSETS = os.path.join(ROOT_DIR, "assets")

def sync():
    print(f"Syncing site assets from {PROPOSAL_DIR} to {ROOT_DIR}...")
    
    # 1. Sync assets folder
    if os.path.exists(ROOT_ASSETS):
        shutil.rmtree(ROOT_ASSETS)
    shutil.copytree(PROPOSAL_ASSETS, ROOT_ASSETS)
    print("✓ Copied assets/ directory to root.")

    # 2. Sync main index.html (from interactive_showcase.html)
    src_showcase = os.path.join(PROPOSAL_DIR, "interactive_showcase.html")
    dest_index = os.path.join(ROOT_DIR, "index.html")
    shutil.copy2(src_showcase, dest_index)
    print("✓ Copied interactive_showcase.html -> index.html")

    # 3. Sync presentation deck
    src_deck = os.path.join(PROPOSAL_DIR, "presentation_deck.html")
    dest_deck = os.path.join(ROOT_DIR, "presentation_deck.html")
    dest_slides = os.path.join(ROOT_DIR, "slides.html")
    shutil.copy2(src_deck, dest_deck)
    shutil.copy2(src_deck, dest_slides)
    print("✓ Copied presentation_deck.html -> presentation_deck.html & slides.html")

    # 4. Sync downloadable files
    downloads = [
        "RetailSync_Capstone_Proposal_Defense_Deck.pptx",
        "RetailSync_WMS_Project_Proposal.docx",
        "RetailSync_WMS_Project_Proposal.pdf"
    ]
    for filename in downloads:
        src = os.path.join(PROPOSAL_DIR, filename)
        dest = os.path.join(ROOT_DIR, filename)
        if os.path.exists(src):
            shutil.copy2(src, dest)
            print(f"✓ Copied {filename} to root.")
        else:
            print(f"⚠️ Warning: {filename} not found in {PROPOSAL_DIR}")

    print("\n✅ Static website distribution synced successfully!")

if __name__ == "__main__":
    sync()
