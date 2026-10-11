# floodlens-nwm-archive

Hourly GitHub Actions archiver of NOAA National Water Model short-range forecasts (18 leads/cycle, ~256 reaches in `config/reaches.csv`).
Output goes to the orphan branch `nwm-archive` (parquet per cycle + `manifest.csv`); `main` stays code-only. Format: `docs/nwm_forecast_archive_README.md`.

## Setup
1. Create an empty **public** repo on GitHub (no README/license), then: `git init -b main && git add -A && git commit -m init && git remote add origin <url> && git push -u origin main`
2. Repo → Settings → Actions → General → Workflow permissions: **Read and write** (the workflow also declares `contents: write`).
3. Actions tab → `nwm-live` → **Run workflow** (main). First run backfills 72 h (~1300 downloads); later runs add ~1 cycle.
4. Check the run is green and the `nwm-archive` branch exists.

## Local run
`pip install -r requirements.txt && python src/nwm_backfill.py 72` (writes `data/forecasts/`, git-ignored).
