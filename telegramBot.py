
import time,datetime
import telepot
from telepot.loop import MessageLoop

now = datetime.datetime.now()

def action(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print 'Received: %s' % command

    if command == '/hi':
        telegram_bot.sendMessage (chat_id, str("Hi! 4842Bot"))
    elif command == '/time':
        telegram_bot.sendMessage(chat_id, str(now.hour)+str(":")+str(now.minute))
    elif command == '/logo':
        telegram_bot.sendPhoto (chat_id, photo = "http://www.spiritanimal.info/wp-content/uploads/Lion-Spirit-Animal-1.jpg")
    elif command == '/file':
        telegram_bot.sendDocument(chat_id, document=open('/home/pi/picode/sampleApp/README.MD'))
    elif command == '/photo':
        telegram_bot.sendPhoto (chat_id, photo = open("/home/pi/picode/huracan.png")
    #elif command == '/audio':
    #    telegram_bot.sendAudio(chat_id, audio=open('/home/pi/test.mp3'))

telegram_bot = telepot.Bot('533632062:AAH3xLwfkDFS0N_XAfruytvFg1--K_VMWo8')
print (telegram_bot.getMe())

MessageLoop(telegram_bot, action).run_as_thread()
print 'Up and Running....'

while 1:
    time.sleep(10)
