import hikari
import time

bot = hikari.GatewayBot(token='MTAyNzIzMTg2Nzk2NTAyMjI0OA.Gplj-z.bxXv0qdwDJPy2ydlhp6d2jXy2cNQMXVcfqHhGY')

@bot.listen(hikari.StartedEvent)
async def on_started(event):
    global cnt1
    print('Bot has started!')
    while True:
        with open('message_bot\msg.txt')as f:
            cnt1 = f.read()
        if cnt1 == '':
            False
        else:
            await bot.rest.create_message(channel=1027232130956279821, content=cnt1)
            with open('message_bot\msg.txt', 'w')as f2:
                f2.write('')

        time.sleep(2)

bot.run()