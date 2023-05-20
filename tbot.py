import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
from telegram import Update
import os
from splt import *

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

token = 'TOKEN HERE'
bot = telegram.Bot(token=token)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="""
    first upload a video and then you have 4 options.\n\
    1: /four_part for splitting the video you have sent into 4 equal parts\n\
    2: /three_part for splitting the video you have sent into 4 equal parts\n\
    3: /two_part for splitting the video you have sent into 4 equal parts\n\
    4: and a number to split the given video in customize parts, press /help for more information on how the bot works\n\
    programmer: @Erfan_Owl121""")



def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="First you need to send a video and then use the commands(/four_part,/three_part, /two_part)\n\
    If you want to customize the time, you have to send the time that you want the video to be splitted(in second).")



def download_video(update: Update, context):
    """Download the video that the user sent."""
    file_id = update.message.video.file_id
    
    video_file = context.bot.get_file(file_id)
    
    video_file.download("video.mp4")
    
    update.message.reply_text('Video downloaded successfully!')


def four_part(update, context):
    
    context.bot.send_message(chat_id=update.effective_chat.id, text="Ok. now im splitting the video into 4 diffrent parts.")
    four_equal_parts(filename='video.mp4')
    os.remove('video.mp4')
    context.bot.send_message(chat_id=update.effective_chat.id, text="I splitted it into 4 diffrent parts. and now im uploading it")
    for i in range(1,5):
        bot.send_video(update.message.chat_id, video=open(f"part{i}.mp4", 'rb'))
        os.remove(f"part{i}.mp4")




def three_part(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Ok. now im splitting the video into 3 diffrent parts.")
    three_equal_parts()
    os.remove('video.mp4')
    context.bot.send_message(chat_id=update.effective_chat.id, text="I splitted it into 3 diffrent parts. and now im uploading it")
    for i in range(1,4):
        bot.send_video(update.message.chat_id, video=open(f"part{i}.mp4", 'rb'))
        os.remove(f"part{i}.mp4")

    

def two_part(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Ok. now im splitting the video into 2 diffrent parts.")
    two_equal_parts()
    os.remove('video.mp4')
    context.bot.send_message(chat_id=update.effective_chat.id, text="I splitted it into 2 diffrent parts. and now im uploading it")
    for i in range(1,3):
        bot.send_video(update.message.chat_id, video=open(f"part{i}.mp4", 'rb'))
        os.remove(f"part{i}.mp4")





def two_custome_part(update, context):
    # context.bot.send_message(context.bot.send_message(chat_id=update.effective_chat.id, text="send me your custome time and i will ;las;'dcmles'lfm"))
    text2 = update.message.text
    # 10-30
    try:
        t = int(text2)
        custome(t)
        context.bot.send_message(chat_id=update.effective_chat.id, text="uploading...")
        bot.send_video(update.message.chat_id, video=open("part1.mp4", 'rb'))
        bot.send_video(update.message.chat_id, video=open("part2.mp4", 'rb'))
        os.remove("part1.mp4")
        os.remove("part2.mp4")
        os.remove("video.mp4")


    
    except:
        print("wrong format")
    





def main():
    """Start the bot."""
    updater = Updater(token, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    dp.add_handler(CommandHandler('four_part', four_part))
    dp.add_handler(CommandHandler('three_part', three_part))
    dp.add_handler(CommandHandler('two_part', two_part))
    dp.add_handler(MessageHandler(Filters.text, two_custome_part))



    dp.add_handler(MessageHandler(Filters.video, download_video))


    updater.start_polling()
    logger.info("Bot started.")

    updater.idle()

if __name__ == '__main__':
    main()
