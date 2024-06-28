# Coffee Scraper
Ever have an item you want to buy but it just about never goes on sale? I ran into this issue with a coffee mug. After consistently checking the price for several weeks, I decided to build a web scraper to do it for me. The web scraper is written in Python and uses Selenium along with a Chrome driver to load the item's webpage. The price is analyzed, and if on sale, an email is sent to you informing you of the new price. 

## How to Use
To use the app, add the urls of the items you want to track to the `/src/urls/new_urls.txt` file.  Create a `.env` file at the root and add the variables `RECEIVING_EMAIL`, `SENDING_EMAIL`, and `EMAIL_PASSWORD`. Then periodically run `src/main.py` to check for sales.
