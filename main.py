import telebot
from telebot import types
import threading

TOKEN = '000' #token bot
CHANNEL_ID = '@userChannel' #@username Channel
bot = telebot.TeleBot(TOKEN)

def auto_delete_message(chat_id, message_id):
    threading.Timer(10, lambda: bot.delete_message(chat_id, message_id)).start() # To modify the time to delete the alert message, edit number 10

@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_mention = f"[{user_name}](tg://user?id={user_id})"

    channel_member = bot.get_chat_member(CHANNEL_ID, user_id)
    if channel_member.status not in ['member', 'administrator', 'creator']:
        bot.delete_message(message.chat.id, message.message_id)

        markup = types.InlineKeyboardMarkup()
        join_btn = types.InlineKeyboardButton("انضمام بالقناة", url="https://t.me/" + CHANNEL_ID.replace("@", ""))
        check_btn = types.InlineKeyboardButton("تحقق من الانضمام", callback_data="check_subscription")
        markup.add(join_btn, check_btn)

        sent_message = bot.send_message(message.chat.id, f"{user_mention}، لايمكنك الدردشة هنا لعدم انضمامك في القناة الرئيسية. اشترك وعد الى هنا للاشتراك.", reply_markup=markup, parse_mode="Markdown")
        auto_delete_message(sent_message.chat.id, sent_message.message_id)

@bot.callback_query_handler(func=lambda call: call.data == "check_subscription")
def check_subscription(call):
    user_id = call.from_user.id
    channel_member = bot.get_chat_member(CHANNEL_ID, user_id)

    if channel_member.status in ['member', 'administrator', 'creator']:
        bot.restrict_chat_member(call.message.chat.id, user_id, can_send_messages=True, can_send_media_messages=True, can_send_polls=True, can_send_other_messages=True, can_add_web_page_previews=True)
        bot.delete_message(call.message.chat.id, call.message.message_id)
    else:
        bot.answer_callback_query(call.id, "اشترك بالقناة ثم عد للدردشة", show_alert=True)

bot.polling()
