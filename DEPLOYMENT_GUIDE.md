# 🚀 RetailSync Live Website Deployment Guide

This repository is configured for **instant, zero-configuration static web deployment** to **GitHub Pages**, **Vercel**, **Netlify**, or **Offline Local Defense**.

---

## 🌐 1. Deploying to GitHub Pages (Recommended for Academic Portfolios)

Your repository now includes an automated GitHub Actions deployment workflow ([`.github/workflows/deploy.yml`](.github/workflows/deploy.yml)).

### Steps:
1. **Push your code to GitHub:**
   ```bash
   git init
   git add .
   git commit -m "feat: complete RetailSync interactive defense portal & presentation deck"
   git branch -M main
   git remote add origin https://github.com/<YOUR_GITHUB_USERNAME>/<YOUR_REPOSITORY_NAME>.git
   git push -u origin main
   ```
2. **Enable GitHub Pages:**
   * Go to your repository on GitHub.
   * Click **Settings** (top navigation tab) → **Pages** (left sidebar).
   * Under **Build and deployment > Source**, select **GitHub Actions**.
3. **Done!**
   * GitHub will automatically trigger the workflow and publish your site at:
   * `https://<YOUR_GITHUB_USERNAME>.github.io/<YOUR_REPOSITORY_NAME>/`

---

## ⚡ 2. Deploying to Vercel (Instant 60-Second Setup)

The repository includes a ready-to-use [`vercel.json`](vercel.json) with clean URL routing.

### Option A: Using the Vercel Web Dashboard (Drag & Drop / Import)
1. Go to [vercel.com](https://vercel.com) and log in.
2. Click **Add New...** → **Project**.
3. Import your GitHub repository (or use the Vercel CLI).
4. Leave all build settings as default (Framework Preset: **Other**, Root Directory: `./`).
5. Click **Deploy**. Your site will be live instantly with a custom URL (e.g., `https://retailsync.vercel.app`).

### Option B: Deploying from Terminal (One Command)
```bash
npx -y vercel
```
* Follow the 3 prompts (Set up and deploy? `Y`, Link to existing project? `N`, Project name: `retailsync`).
* Your live production URL will be displayed in your terminal.

---

## 🛡️ 3. Deploying to Netlify (Drag-and-Drop)

The repository includes [`netlify.toml`](netlify.toml).

1. Go to [app.netlify.com/drop](https://app.netlify.com/drop).
2. Drag and drop this project folder into the browser window.
3. Netlify will deploy it in seconds and give you a public URL (e.g., `https://retailsync-defense.netlify.app`).

---

## 💻 4. Running Locally / Offline Defense Mode

If you are presenting in the DIU defense room with limited or no Wi-Fi:
* The website has zero runtime server dependencies and works completely offline!

### Quick Start:
```bash
# Using Python (built-in on Linux & macOS):
python3 -m http.server 3000

# Or using Node.js:
npm run serve
```
Open your browser to: `http://localhost:3000`

---

## 📁 Live URL Structure

When deployed, the following clean routes are active:
* **`/`** or **`/index.html`** → Main Executive Showcase & Interactive Simulators
* **`/slides`** or **`/presentation_deck.html`** → Fullscreen Interactive Defense Slide Deck
* **`/deck`** → Direct download of `RetailSync_Capstone_Proposal_Defense_Deck.pptx`
* **`/proposal`** → Direct download/view of `RetailSync_WMS_Project_Proposal.pdf`
* **`RetailSync_WMS_Project_Proposal.docx`** → Direct download of Word Proposal

---

## 🔄 Keeping the Deployment in Sync

If you modify anything inside the `proposal/` directory (such as updating slide text or adding proposal sections), run:
```bash
python3 scripts/sync_site.py
```
This automatically updates the root `index.html`, `slides.html`, `assets/`, and downloadable documents.
