# Crypto-News-Aggregator

Scrapes CryptoPanic API, organizes crypto news by sentiment and coin into Excel

Built by [Naadir](https://github.com/Naadir-Dev-Portfolio)

## Overview

Automatically fetch the latest cryptocurrency news from CryptoPanic, filter by sentiment (bullish, bearish, neutral), organize by assets, and export to Excel workbooks. Includes web scraping and API integration for comprehensive crypto market intelligence.

## Features

- CryptoPanic API integration for real-time news fetching
- Sentiment analysis and classification
- Organization by coin and category
- Automatic Excel workbook generation
- Web scraping for supplementary data
- CSV and XLSX export formats

## Tech Stack

Python · requests · pandas · openpyxl

## Setup

```
pip install -r requirements.txt
python main.py
```

## Notes

Configure your CryptoPanic API key via environment variable: `os.getenv("CRYPTOPANIC_API_KEY", "YOUR_KEY_HERE")`
