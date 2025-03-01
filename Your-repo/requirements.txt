import requests
from bs4 import BeautifulSoup

STEAM_NEW_RELEASES_URL = "https://store.steampowered.com/explore/new/"

def get_new_games():
    response = requests.get(STEAM_NEW_RELEASES_URL)
    soup = BeautifulSoup(response.text, "html.parser")

    games = []
    for item in soup.select(".tab_item"):
        title = item.select_one(".tab_item_name").text
        link = item["href"]
        release_date_text = item.select_one(".tab_item_details span").text.strip()

        games.append({
            "title": title,
            "link": link,
            "release_date": release_date_text
        })

    return games[:5]  # 上位5件

if __name__ == "__main__":
    top_games = get_new_games()
    for game in top_games:
        print(f"{game['title']} - {game['link']} ({game['release_date']})")

