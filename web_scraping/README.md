# Books.toscrape.com Scraper

This script scrapes https://books.toscrape.com and extracts information for every book:

- Full title and detail URL
- Price (float)
- Rating (1-5)
- Main and secondary categories
- Full description (from detail page)
- Stock available (integer)
- High-resolution image URL

Features:

- Automatically follows pagination
- Structures data hierarchically by category
- Handles 404s on detail pages gracefully
- Saves output JSON with a timestamp in the filename

Requirements
------------

Install dependencies (recommended in a virtualenv):

```powershell
python -m pip install -r requirements.txt
```

Usage
-----

Run the scraper from the project root:

```powershell
python main.py
```

After completion a file named like `books_YYYYMMDD_HHMMSS.json` will be created.

Notes
-----

- The scraper is polite (small sleeps) but still performs many requests (site has ~1000 books). Expect the run to take a few minutes depending on network and throttling.
- If you want to limit to fewer pages for testing, modify `START_URL` in `main.py` or add a page counter loop.
- The JSON structure groups books as `{"categories": {"Main": {"Sub": [ ...books ] } } }`.
