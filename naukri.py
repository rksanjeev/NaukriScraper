from Scraper.url_build import build_url
from Scraper.scraper import scrape_page, export_result

URLS=build_url()
scrape_page(URLS)
export_result()
