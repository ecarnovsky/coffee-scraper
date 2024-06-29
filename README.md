# Coffee Scraper
This app uses Selenium to periodically check Meijer’s website for sales. Just copy and paste the urls of the items you want into the `new_urls.txt` file and configure your email information. GitHub actions are set up to run the app every two days. If an item is found to be on sale, the item’s url is moved from `new_urls.txt` to `orl_urls.txt` and an email containing the item’s link is sent to the receiving email address.

## How to Use
- Fork the repo
- Set `RECEIVING_EMAIL`, `SENDING_EMAIL`, and `EMAIL_PASSWORD` as repository secrets
- Add the urls of the items you want to the `src/urls/new_urls.txt` file. Put each url on a new line.

And that's it! The item's price will be checked every two days, and you will notified of any sales.
