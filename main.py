import requests
import csv
from datetime import datetime, timedelta

# Function to convert published_at to a datetime object
def parse_date(published_at):
    return datetime.strptime(published_at, '%Y-%m-%dT%H:%M:%SZ')

# Current time and 24 hours ago
now = datetime.utcnow()
one_day_ago = now - timedelta(days=3)

# CryptoPanic API URL for fetching news
api_url = "https://cryptopanic.com/api/v1/posts/?public=true"

def fetch_news(api_url):
    all_news = []
    page = 1
    while True:
        response = requests.get(f"{api_url}&page={page}")
        if response.status_code != 200:
            break
        data = response.json()
        all_news.extend(data['results'])
        # Check the last news item's date; break if older than 24 hours
        last_news_date = parse_date(data['results'][-1]['published_at'])
        if last_news_date < one_day_ago:
            break
        page += 1
    return all_news

# Fetch all news from the past 24 hours
all_news = fetch_news(api_url)

# Filter news from the last 24 hours
recent_news = [news for news in all_news if parse_date(news['published_at']) >= one_day_ago]

# Save to CSV
with open('crypto_news_headlines_last_24_hours.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Headline', 'Published At'])
    for news in recent_news:
        writer.writerow([news['title'], news['published_at']])
        
print(f"CSV file with news from the last 24 hours has been created, containing {len(recent_news)} articles.")
