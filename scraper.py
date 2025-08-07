import requests
from bs4 import BeautifulSoup

def scrape_inshorts_headlines():
    url = "https://inshorts.com/en/read"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/115.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        # Find all headlines inside <span itemprop="headline">
        headline_tags = soup.find_all("span", itemprop="headline")

        headlines = []
        for tag in headline_tags:
            text = tag.get_text(strip=True)
            if text and text not in headlines:
                headlines.append(text)

        # Save to file
        with open("headlines.txt", "w", encoding="utf-8") as file:
            for idx, headline in enumerate(headlines, 1):
                file.write(f"{idx}. {headline}\n")

        print(f"[✔] {len(headlines)} headlines scraped and saved to 'headlines.txt'.")

    except Exception as e:
        print("[✘] An error occurred:", e)

if __name__ == "__main__":
    scrape_inshorts_headlines()
