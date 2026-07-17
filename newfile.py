from rubka import Robot
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote

TOKEN = "BICAGB0SZXZSXDGXLSORLPNLLOBVHTNXYBPTWSBMROFLETWWEOHOPPWMLBAOKALG"

bot = Robot(TOKEN)


@bot.on_message()
def commands(client, message):

    text = message.text.strip()

    # جستجو
    if text.startswith("جستجو "):

        query = text.replace("جستجو ", "", 1)

        url = f"https://html.duckduckgo.com/html/?q={quote(query)}"

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        try:
            r = requests.get(url, headers=headers, timeout=10)

            if r.status_code == 200:

                soup = BeautifulSoup(r.text, "html.parser")

                results = soup.select(".result__title a")

                if results:
                    title = results[0].get_text(strip=True)
                    link = results[0]["href"]

                    message.reply(
                        f"🔎 {title}\n\n{link}"
                    )

                else:
                    message.reply("❌ نتیجه‌ای پیدا نشد.")

            else:
                message.reply("❌ خطا در اتصال.")

        except Exception as e:
            message.reply(f"❌ خطا:\n{e}")


bot.run()