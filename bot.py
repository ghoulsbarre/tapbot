import os
from telegram import Update, InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import ApplicationBuilder, InlineQueryHandler, ContextTypes
from uuid import uuid4

async def inline_tap(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.inline_query.query.strip()

    if not query:
        return

    words = "_".join(query.lower().split())
    
    option1 = "/" + words
    option2 = "/tap_to_" + words

    results = [
        InlineQueryResultArticle(
            id=uuid4(),
            title=option1,
            input_message_content=InputTextMessageContent(option1)
        ),
        InlineQueryResultArticle(
            id=uuid4(),
            title=option2,
            input_message_content=InputTextMessageContent(option2)
        ),
    ]

    await update.inline_query.answer(results)

app = ApplicationBuilder().token(os.environ["TELEGRAM_BOT_TOKEN"]).build()
app.add_handler(InlineQueryHandler(inline_tap))
app.run_polling()
