from playwright.sync_api import sync_playwright
import time
import json

url = "https://www.reddit.com/r/healthIT/.json?limit=10"
start_time = time.time()

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.set_extra_http_headers({"User-Agent": "healthcare-nlp-assignment/1.0 (by /u/Similar_Road_6567)"})
    page.goto(url)
    raw_text = page.inner_text("body")
    raw_json = json.loads(raw_text)
    browser.close()

posts = raw_json["data"]["children"]
playwright_results = []

for post in posts:
    post_data = post["data"]
    title = post_data["title"]
    post_url = post_data["url"]
    selftext = post_data["selftext"] if post_data["selftext"] else ""
    playwright_results.append({"title": title, "url": post_url, "selftext": selftext})

end_time = time.time()
playwright_time = end_time - start_time

for result in playwright_results:
    print(result["title"])

print(f"\nPlaywright total time: {playwright_time:.2f} seconds")
print(f"Posts scraped: {len(playwright_results)}")