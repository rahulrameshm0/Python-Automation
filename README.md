# Python Automation

A collection of small Python automation projects built while learning — covering file backups, currency conversion, Excel reporting, WhatsApp messaging, PDF table extraction, web scraping, browser automation with Playwright, and YouTube video downloading.

## Projects

### 1. Automation Basic
Everyday automation scripts.

| Script | What it does |
| --- | --- |
| `simposon.py` | Scrapes the Wikipedia page for *The Simpsons* episodes with `pandas.read_html`. |
| `backup.py` | Copies a source folder to a dated backup folder once a day using `schedule` and `shutil`. |
| `currency.py` | Converts an amount between currencies via the [FreeCurrencyAPI](https://freecurrencyapi.com/). Accepts a base currency and amount, prints the converted values. Type `Q` to quit. |

**Run:**
```bash
python "Automation Basic/currency.py"
python "Automation Basic/backup.py"
```

> `backup.py` and `currency.py` contain hard-coded paths and an API key — update them before running.

### 2. Automate Excel Report
Turns raw supermarket sales data into a formatted Excel report with a pivot table, totals, and a bar chart, using `pandas` and `openpyxl`.

| Script | What it does |
| --- | --- |
| `excel.py` | Builds a pivot table (Gender × Product line, summed sales) from `supermarket_sales.xlsx` and writes it to `pivot_table.xlsx`. |
| `format.py` | Adds a styled title to the report sheet. |
| `apply_formula.py` | Adds `SUM` totals per column with currency formatting. |
| `add_chart.py` | Adds a "Sales by Product line" bar chart. |
| `pivot_to_report.py` | Does the whole pipeline at once and saves `report_<month>.xlsx`. |
| `py_to_exe.py` | Same as above, but prompts for the month and is designed to be bundled into a standalone executable (PyInstaller). |

**Run:**
```bash
cd "Automate Excel Report"
python excel.py        # create pivot_table.xlsx
python pivot_to_report.py
```

### 3. Automate Whatsapp
Sends a WhatsApp message at a scheduled time using `pywhatkit`.

```bash
cd "Automate Whatsapp"
python whatsapp.py
```

Requires WhatsApp Web to be logged in on your default browser. Edit the phone number and time in the script.

### 4. Extract Tables
Extracts tables from a PDF into CSV with `camelot`.

```bash
cd "Extract  tables"
python tables.py
```

Produces `foo.csv` (and `food.zip` / `food.csv` for all pages).

### 5. Extract News
Scrapes football headlines (title, subtitle, link) from The Sun using Selenium, then saves them to a dated CSV (`headline<mmddyy>.csv`).

```bash
cd "Extract News"
python news.py
```

Update the ChromeDriver `path` in the script to match your machine. The `build/` and `dist/` folders are PyInstaller output from a previous packaging run.

### 6. Scrap with Play-Wright
Playwright practice code split into three folders:

- **`playwright-basic/`** — individual examples of core browser actions: navigation, locators, XPath, mouse actions, alerts, dropdowns, radio buttons/checkboxes, multiple pages, and cookies/screenshots.
- **`playwright/`** — pytest-style UI tests using Playwright's `expect` assertions (login flows, cart validation, hidden elements, alerts, frames, hover).
- **`pytest/`** — small examples of pytest fixtures (`scope`, `yield`, `skip`).

**Run:**
```bash
cd "scrap with play-wright"

# basic examples (opens a visible browser)
python playwright-basic/main.py

# tests
pytest playwright/
pytest pytest/
```

Install the browser binaries first:
```bash
playwright install
```

### 7. YouTube Video Downloader
A small `tkinter` + `yt-dlp` script that asks for a URL, opens a folder picker, and downloads the video.

```bash
cd "youtube video dowloder"
python video_downloader.py
```

> Note: the save directory is currently hard-coded in the script (`savepath`); the folder selected in the dialog is not used yet.

## Installation

Python 3.10+ is recommended. Install dependencies per project as needed:

```bash
# Core data / Excel
pip install pandas openpyxl

# Automation basics
pip install requests schedule

# WhatsApp
pip install pywhatkit

# PDF tables
pip install camelot-py[cv]

# Web scraping
pip install selenium

# Browser automation & tests
pip install playwright pytest
playwright install

# YouTube downloader
pip install yt-dlp
```

## Notes

- Several scripts contain hard-coded absolute paths (`/Users/rahul/...`) and, in `currency.py`, an API key. Replace these with your own values before running.
- Video files (`*.mp4`) and PyInstaller `build/`, `dist/`, and `__pycache__/` folders are included in the repo but are not required to run anything.
