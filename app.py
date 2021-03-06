import requests
from bs4 import BeautifulSoup
import json
import crawler

FeedPediaURL = "https://www.feedipedia.org/"
FeedPediaFeedUrl = FeedPediaURL + "/content/feeds?category=All"
ExportFileName = "feedpedia_data.json"

full_feed_items = []
dic = {}

def export_feedpedia_data():

    page_feed_ipedia = requests.get(FeedPediaFeedUrl)
    soup = BeautifulSoup(page_feed_ipedia.text, 'html.parser')

    print("getting main page items")
    feed_items = crawler.get_feed_items(soup)

    extra_attributes =crawler.feedcrawler.get_extra_attributes(soup)

    for feed_item in feed_items:
        full_feed_items.append(crawler.enrich_feed_item(feed_item))

    dic['feed_items'] = full_feed_items
    dic['extra'] = extra_attributes
    print("writing data to file")

    with open(ExportFileName, 'w') as f:
        json.dump(dic, f)

    print("data is exported to " + ExportFileName)
    print("finished")

export_feedpedia_data()
