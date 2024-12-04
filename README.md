# web_scraper
A code that will send you a msg(to buy) if desired product is in your price range

# Amazon Price Tracker

This Python script uses Selenium to track the price of a product on Amazon. If the price drops below a specified threshold, the script sends an email notification to the user.

## Features

- **Automated Price Scraping**: Retrieves the product price dynamically from Amazon using Selenium.
- **Email Alerts**: Sends an email notification if the price drops below ₹500.
- **Dynamic Waiting**: Ensures reliability by waiting for the page to load completely before extracting the price.

## Requirements

- Python 3.8 or later
- Google Chrome browser
- ChromeDriver (compatible with your Chrome version)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Pooja389/web_scraper.git
   cd web_scraper```
   
## Install required python packages
```bash
pip install selenium
```
##  Run the script
``bash
python web_scraper.py```

