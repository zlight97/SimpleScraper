#/usr/bin/python

# This is a sample run function for using the SimpleScraper
# Some websites will require accurate headers to access them
# You can obtain these through a standard web browser's network console
from SimpleScraper import SimpleScraper
import time

if __name__ == "__main__":
    headers = {
    "Host": "https://urlgoeshere",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv125.0) Gecko/20100101 Firefox/125.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "TE": "trailers"
    }
    # Scraper takes headers, url, list of emails to notify, keyword to trigger an email, and a keyword to reset
    # The reset is needed so the program doesn't spam you with emails. Leaving this empty will work in most cases.
    scraper = SimpleScraper(headers, "https://urlgoeshere",['sample@email'],"add_to_cart", "To be Restocked")
    while True:
        # Running in a while true is fine on a stable connection. There is a try around the request anyway so it won't crash
        scraper.check()
        # Make sure to use a sleep so you don't spam the website.
        time.sleep(60)