from telegram.ext import Application, MessageHandler, CommandHandler, filters

BOT_TOKEN = "8566367254:AAGdkD0DB2vvORuGVOeUU6yh6BcacK__1eI"

async def start(update, context):
    await update.message.reply_text("مرحبًا 👋\nأرسل صورة الشارت لتحليلها 📸")

def analyze_image(image_path):
    return """🔎 تحليل الصورة:
- SELL | السعر: 1495.20
  السبب: RSI عالي + شمعة انعكاس
- BUY | السعر: 1492.50
  السبب: دعم قوي
"""

async def handle_image(update, context):
    photo = update.message.photo[-1]
    file = await photo.get_file()
    await file.download_to_drive("chart.jpg")
    await update.message.reply_text(analyze_image("chart.jpg"))

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.PHOTO, handle_image))
    app.run_polling()

if __name__ == "__main__":
    main()
