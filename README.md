# Web_Scraper

A robust and efficient Python-based Web Scraper designed to extract dynamic JavaScript-rendered quotes from web pages without the overhead of heavy browser automation tools like Selenium or Playwright.

## Features
- **Lightweight & Fast:** Uses pure HTTP requests and HTML parsing instead of spinning up a headless browser.
- **Advanced String Manipulation:** Extracts hidden JavaScript variables directly from `<script>` tags.
- **Robust Error Handling:** Armed with safety nets against connection failures, missing tags, and invalid JSON formatting.
- **Clean JSON Output:** Automatically structures and saves the extracted data with structured indexing.

## ⚙️ How It Works
Instead of executing JavaScript to render the page, this scraper deep-dives into the source HTML, scans for the hidden data injection block (`var data = [...]`), extracts the raw text dynamically, parses it via Python's built-in `json` module, and filters out unnecessary noise.

##  Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/Stealth-JS-Web-Scraper.git](https://github.com/YOUR_USERNAME/Stealth-JS-Web-Scraper.git)
   cd Stealth-JS-Web-Scraper

    Install Required Packages:
    Ensure you have Python 3 installed. Then run:
    Bash

pip install requests beautifulsoup4

Run the Scraper:
Bash

    python3 Web_Scraper.py

📊 Output Schema

The data is sanitized and saved into Json.json in the following format:
JSON

[
    {
        "Number": 1,
        "Author_Name": "Albert Einstein",
        "Text": "“The world as we have created it is a process of our thinking...”"
    }
]

🔒 Security & Best Practices

    Custom Headers: Utilizes realistic user-agent strings to mimic legitimate browser traffic.

    Fail-Safe Mechanism: Returns defensive fallback structures (Empty Lists / None) to prevent runtime crashes if the website layout changes.
