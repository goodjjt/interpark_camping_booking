import schedule
import time
import asyncio
import telegram
import requests
import os

if os.name == 'nt':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# Telegram
async def bot_send(msg):
    telegram_token = "5128692345:AAHkO-3JZ9tZYP2hrS5UAlnYCrO0PiO09_A"
    telegram_id = "444879086"
    bot = telegram.Bot(token = telegram_token)
    await bot.sendMessage(chat_id=telegram_id, text=msg)

request_url_working = 'https://api-ticketfront.interpark.com/v1/goods/21005592/playSeq/PlaySeq/C63/REMAINSEAT'
request_url = 'https://api-ticketfront.interpark.com/v1/goods/21005592/playSeq/PlaySeq/C64/REMAINSEAT'
camping_site_name = '한탄강 오토캠핑장'
site_url = 'https://tickets.interpark.com/goods/21005592'

print(camping_site_name + " " + site_url)
asyncio.run(bot_send(camping_site_name + " " + site_url))

def crawling():
    response = requests.get(request_url, headers={'User-Agent': 'Mozilla/5.0'})
    message = "[" + camping_site_name + "]" + "  " + site_url  + '\n'
    cnt = 0
    if response.status_code == 200:
        jsonData = response.json()

        for data in jsonData.get("data").get("remainSeat"):
            message = message + data.get("seatGradeName") + " : " + str(data.get("remainCnt")) + '\n'
            if data.get("remainCnt") > 0:
                cnt += 1
        print(time.strftime('%Y-%m-%d %H:%M:%S'), ":", cnt, ":", camping_site_name)
    if cnt > 0:
        asyncio.run(bot_send(message))

# step3.실행 주기 설정
schedule.every(10).seconds.do(crawling)
# schedule.every(30).minutes.do(message1)

while True:
    schedule.run_pending()
    time.sleep(1)