import requests
import json
from steam_data import get_new_games

WEBHOOK_URL = "https://discord.com/api/webhooks/1345189719243231313/V2CjGmcGEiepaS1ruIcrpxq6XyJG0n1hlX1YkrOrMvZb8dWvONnmEpF4sO60bAT-c6tg"

def send_to_discord():
    games = get_new_games()
    message = "**今月の注目新作ゲーム TOP5**\n"
    
    for game in games:
        message += f"🎮 [{game['title']}]({game['link']}) - {game['release_date']}\n"

    data = {"content": message}
    headers = {"Content-Type": "application/json"}
    
    response = requests.post(WEBHOOK_URL, data=json.dumps(data), headers=headers)
    if response.status_code == 204:
        print("送信成功！")
    else:
        print("送信失敗:", response.status_code, response.text)

if __name__ == "__main__":
    send_to_discord()

