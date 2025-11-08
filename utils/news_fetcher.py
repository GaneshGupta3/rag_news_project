import requests
import json

API_KEY = "9afe2aca8af74b4ba2009c4c13018e2a"

def fetch_news():
    url = f"https://newsapi.org/v2/everything?q=bitcoin&apiKey={API_KEY}"
    res = requests.get(url)
    data = res.json()

    print("API Status:", data.get("status"))
    print("Total Results:", data.get("totalResults"))
    if data.get("message"):
        print("Message:", data.get("message"))

    articles = [
        {"title": a["title"], "content": a["description"] or ""}
        for a in data.get("articles", [])
        if a["description"]
    ]

    with open("data/news_data.json", "w", encoding="utf-8") as f:
        json.dump(articles, f, indent=2)

    return articles

if __name__ == "__main__":
    articles = fetch_news()
    print(f"✅ Fetched {len(articles)} news articles and saved to data/news_data.json")
