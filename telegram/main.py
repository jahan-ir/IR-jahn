from telegram import Update, ReplyKeyboardMarkup , InlineKeyboardMarkup , InlineKeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters , CallbackQueryHandler


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        ["project 1", "project 2", "project 3", "project 4"],
        ["project 5", "project 6", "project 7", "project 8"],
        ["project 9"]
    ]
    reply_keyboard = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        f"Hello I am Robat CS50 and I have all the projects taught. "
        f"Just select the project option, {update.effective_user.first_name}!",
        reply_markup=reply_keyboard
    )


async def send_file(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text

    if text == "project 1":
        await update.message.reply_document(document=open("PSET1.rar", "rb"))
    elif text == "project 2":
        await update.message.reply_document(document=open("PSET2.rar", "rb"))
    elif text == "project 3":
        await update.message.reply_document(document=open("PSET3.rar", "rb"))
    elif text == "project 4":
        await update.message.reply_document(document=open("PSET4.rar", "rb"))
    elif text == "project 5":
        await update.message.reply_document(document=open("PSET5.rar", "rb"))
    elif text == "project 6":
        await update.message.reply_document(document=open("PSET6.rar", "rb"))
    elif text == "project 7":
        await update.message.reply_document(document=open("PSET7.rar", "rb"))
    elif text == "project 8":
        await update.message.reply_document(document=open("PSET8.rar", "rb"))
    elif text == "project 9":
        await update.message.reply_document(document=open("PSET9.rar", "rb"))
async def project(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Project 1", callback_data="project1")],
        [InlineKeyboardButton("Project 2", callback_data="project2")],
        [InlineKeyboardButton("Project 3", callback_data="project3")],
        [InlineKeyboardButton("Project 4", callback_data="project4")],
        [InlineKeyboardButton("Project 5", callback_data="project5")],
        [InlineKeyboardButton("Project 6", callback_data="project6")],
        [InlineKeyboardButton("Project 7", callback_data="project7")],
        [InlineKeyboardButton("Project 8", callback_data="project8")],
        [InlineKeyboardButton("Project 9", callback_data="project9")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "📥 Select a project to download:",
        reply_markup=reply_markup
    )


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == "project1":
        await query.message.reply_document(open("PSET1.rar", "rb"))
    elif query.data == "project2":
        await query.message.reply_document(open("PSET2.rar", "rb"))
    elif query.data == "project3":
        await query.message.reply_document(open("PSET3.rar", "rb"))
    elif query.data == "project4":
        await query.message.reply_document(open("PSET4.rar", "rb"))
    elif query.data == "project5":
        await query.message.reply_document(open("PSET5.rar", "rb"))
    elif query.data == "project6":
        await query.message.reply_document(open("PSET6.rar", "rb"))
    elif query.data == "project7":
        await query.message.reply_document(open("PSET7.rar", "rb"))
    elif query.data == "project8":
        await query.message.reply_document(open("PSET8.rar", "rb"))
    elif query.data == "project9":
        await query.message.reply_document(open("PSET9.rar", "rb"))

app = ApplicationBuilder().token("7569943161:AAEeY2epvTH8Gcwy2MFpHKiRYWz_rXIkOTM").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("project", project))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, send_file))
app.add_handler(CallbackQueryHandler(button))
app.run_polling()