"""Scraper for https://books.toscrape.com

Extracts for each book:
- full title and detail URL
- price (float)
- rating (1-5)
- main and secondary categories (from breadcrumb)
- full description (from detail page)
- stock available (int)
- high-resolution image URL"""

import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
from urllib.parse import urljoin

BASE_URL = "https://books.toscrape.com/"

def get_rating(star_tag):
    classes = star_tag.get('class', []) if star_tag else []
    for c in ['One', 'Two', 'Three', 'Four', 'Five']:
        if c in classes:
            return {'One':1,'Two':2,'Three':3,'Four':4,'Five':5}[c]
    return None

def get_book_info(detail_url):
    try:
        resp = requests.get(detail_url)
        if resp.status_code != 200:
            return None
        soup = BeautifulSoup(resp.content, 'html.parser')
    except Exception:
        return None
    title = soup.select_one('div.product_main h1')
    price = soup.select_one('p.price_color')
    rating = get_rating(soup.select_one('p.star-rating'))
    desc_tag = soup.select_one('#product_description')
    desc = desc_tag.find_next_sibling('p').get_text(strip=True) if desc_tag and desc_tag.find_next_sibling('p') else ''
    stock_tag = soup.select_one('p.instock.availability')
    stock = None
    if stock_tag:
        import re
        m = re.search(r'(\d+)', stock_tag.get_text())
        if m:
            stock = int(m.group(1))
    img_tag = soup.select_one('div.item.active img') or soup.select_one('img.thumbnail') or soup.select_one('img')
    img_url = urljoin(detail_url, img_tag['src']) if img_tag and img_tag.get('src') else None
    crumbs = [li.get_text(strip=True) for li in soup.select('ul.breadcrumb li')]
    cat_main = crumbs[1] if len(crumbs)>1 else ''
    cat_sub = crumbs[2] if len(crumbs)>2 else ''
    return {
        'title': title.get_text(strip=True) if title else '',
        'url': detail_url,
        'price': float(price.get_text(strip=True).replace('£','')) if price else None,
        'rating': rating,
        'category_main': cat_main,
        'category_sub': cat_sub,
        'description': desc,
        'stock': stock,
        'image_url': img_url
    }

def scrape_books():
    books = []
    page_url = BASE_URL
    page_num = 1
    MAX_PAGES = 5
    while page_num <= MAX_PAGES:
        print(f"Scraping page {page_num}: {page_url}")
        resp = requests.get(page_url)
        if resp.status_code != 200:
            print(f"Failed to fetch {page_url} (status {resp.status_code})")
            break
        soup = BeautifulSoup(resp.content, 'html.parser')
        for book in soup.select('article.product_pod h3 a'):
            detail_url = urljoin(page_url, book['href'])
            info = get_book_info(detail_url)
            if info:
                books.append(info)
                if len(books) % 20 == 0:
                    print(f"Checkpoint: {len(books)} books scraped so far...")
        next_link = soup.select_one('li.next > a')
        if next_link and page_num < MAX_PAGES:
            page_url = urljoin(page_url, next_link['href'])
            page_num += 1
        else:
            break
    print(f"Scraping finished. Total books scraped: {len(books)}")
    return books

if __name__ == '__main__':
    books = scrape_books()
    filename = f"books_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(books, f, ensure_ascii=False, indent=2)
    print(f"Saved {len(books)} books to {filename}")


