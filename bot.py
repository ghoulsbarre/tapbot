import os
from telegram import Update, InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import ApplicationBuilder, InlineQueryHandler, ContextTypes
from uuid import uuid4

async def inline_tap(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.inline_query.query.strip()

    if not query:
        return

    formatted = "/" + "_".join(query.lower().split())

    result = InlineQueryResultArticle(
        id=uuid4(),
        title=formatted,
        input_message_content=InputTextMessageContent(formatted)
    )

    await update.inline_query.answer([result])

app = ApplicationBuilder().token(os.environ["TELEGRAM_BOT_TOKEN"]).build()
app.add_handler(InlineQueryHandler(inline_tap))
app.run_polling()
