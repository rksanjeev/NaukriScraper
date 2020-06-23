
from requests_html import HTMLSession
from time import sleep
from bs4 import BeautifulSoup as soup
import pandas as pd
from datetime import datetime

session = HTMLSession()

OUTPUT_RESULTSET = [["Title", "Company", "Experience", "Salary", "Location", "Posted On", "URL"]] 

def scrape_page(URLS):
    for url in URLS:
        raw_scrape = session.get(url)
        raw_scrape.html.render(timeout=900)
        build_resultset(raw_scrape)
        sleep(5)


def build_resultset(resp):
    articles = soup(resp.html.html, "lxml").find_all("article", {"class":"jobTuple"})
    for article in articles:
        # tags = [tag  for tag in article.findChildren()[17] if tag != '\n']
        OUTPUT_RESULTSET.append([article.findChildren()[0].div.a.text,
                   article.findChildren()[0].div.div.a.text, 
                   article.findChildren()[0].div.ul.findChildren()[0].span.text,
                   article.findChildren()[0].div.ul.findChildren()[3].span.text,
                   article.findChildren()[0].div.ul.findChildren()[6].span.text,
                   article.find("span", {"class":"fleft fw500"}).text,
                #    ",".join([tag[0] for tag in tags]) ,
                   article.findChildren()[0].div.a['href']
                   ])

def export_result():
    dt = datetime.now()
    df = pd.DataFrame(OUTPUT_RESULTSET[1:], columns=OUTPUT_RESULTSET[0])
    filename = "NaukriScrape"+str(dt.strftime('%d-%m-%Y'))+".xlsx"
    df.to_excel(filename, index=False)
    print(f'Done! Result written to file {filename}') 
