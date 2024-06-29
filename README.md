# Coffee Scraper
Ever have an item you want to buy but it just about never goes on sale? I ran into this issue with a coffee mug. After consistently checking the price for several weeks, I decided to build a web scraper to do it for me. The web scraper is written in Python and uses Selenium along with a Chrome driver to load the item's webpage. The price is analyzed, and if on sale, an email is sent to you informing you of the new price. 

## How to Use
- Clone the repo
- Set `RECEIVING_EMAIL`, `SENDING_EMAIL`, and `EMAIL_PASSWORD` as repository secrets
- Add the urls of the items you want to the `/src/urls/new_urls.txt` file

And that's it! The item's price will be checked every two days, and you will notified of any sales.
