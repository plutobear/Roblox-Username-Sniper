import requests, threading, random, time, os
from keep_alive import keep_alive
from discordwebhook import Discord
def check():
    try:
        users = ""
        for x in range(5):
            letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'l', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8','9', '0']
            users = users + str(random.choice(letters))
        print(users)
        username = requests.get(f'https://auth.roblox.com/v1/usernames/validate?birthday=2006-09-21T07:00:00.000Z&context=Signup&username={users}')
        if username.json()['message'] == "Username is valid":
           discord = Discord(url="")
           discord.post(
    embeds=[
        {
            "title": "Join Us! https://discord.gg/64hu8tNPw8",
            "fields": [
                {"name": "Letters:", "value": 5},
                {"name": "Username:", "value": users},
            ],
            "footer": {
                "text": "Tool Developed by Plutobear#0001 - https://discord.gg/64hu8tNPw8",
                "icon_url": "https://cdn.discordapp.com/attachments/971742832098435122/978478620601384980/unknown.png",
            },
        }
    ],
)
           open("available.txt", "a").write(users + '\n')
           time.sleep(1)
    except:
        pass
keep_alive()

while True:
    threading.Thread(target=check,).start()