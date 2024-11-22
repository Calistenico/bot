from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import requests

# Token do bot
BOT_TOKEN = "6640349473:AAGAwbWw5MKZeHpoKcm2BUS9rM5wl1wNnpo"

# URLs específicas para cada botão
WEBHOOK_URLS = {
    "eliteflix-star": "https://starplay.qpanel.top/api/chatbot/RvWGnzYDe3/b8K1x6DvGN",
    "eliteflix-alpha": "https://alpha-server-oficial.qpanel.top/api/chatbot/r0WZJB2Wa7/8241Kg1mxd",
    "eliteflix-onlive": "https://onlive.sigma-billing.com/api/chatbot/7V01p0o1dO/b8K1x6DvGN",
    "eliteflix-uni": "https://onlive.sigma-billing.com/api/chatbot/uni",
    "eliteflix-imperial": "https://onlive.sigma-billing.com/api/chatbot/imperial",
    "eliteflix-fire": "https://onlive.sigma-billing.com/api/chatbot/fire",
    "eliteflix-yellow": "https://onlive.sigma-billing.com/api/chatbot/yellow",
    "eliteflix-xcloud": "https://starplay.qpanel.top/api/chatbot/RvWGnzYDe3/JOALy014wx",
    "eliteflix-iphone": "https://starplay.qpanel.top/api/chatbot/RvWGnzYDe3/Yxl1jB1Mjm",
    "eliteflix-2horas": "https://onlive.sigma-billing.com/api/chatbot/7V01p0o1dO/boQ1Ye1ONY"
}

# Função para exibir o menu principal
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("Eliteflix-Star-12H", callback_data="eliteflix-star"),
            InlineKeyboardButton("Eliteflix-Alpha", callback_data="eliteflix-alpha"),
        ],
        [
            InlineKeyboardButton("Eliteflix-Onlive-2H", callback_data="eliteflix-onlive"),
            InlineKeyboardButton("Eliteflix-Uni", callback_data="eliteflix-uni"),
        ],
        [
            InlineKeyboardButton("Eliteflix-Imperial", callback_data="eliteflix-imperial"),
            InlineKeyboardButton("Eliteflix-Fire", callback_data="eliteflix-fire"),
        ],
        [
            InlineKeyboardButton("Eliteflix-Yellow", callback_data="eliteflix-yellow"),
            InlineKeyboardButton("Eliteflix-Xcloud-12H", callback_data="eliteflix-xcloud"),
        ],
        [
            InlineKeyboardButton("Eliteflix-Iphone-star-12H", callback_data="eliteflix-iphone"),
            InlineKeyboardButton("Eliteflix-onlive-2H", callback_data="eliteflix-2horas"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Escolha uma opção:", reply_markup=reply_markup)

# Função para tratar os cliques nos botões
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    callback_data = query.data
    webhook_url = WEBHOOK_URLS.get(callback_data)

    if not webhook_url:
        await query.edit_message_text(
            text="Webhook não configurado para esta opção."
        )
        return

    try:
        # Realiza a chamada ao webhook específico
        response = requests.post(webhook_url)

        if response.status_code == 200:
            response_data = response.json()

            # Extrai os dados da resposta
            username = response_data.get("username", "N/A")
            password = response_data.get("password", "N/A")
            created_at = response_data.get("createdAtFormatted", "N/A")
            expires_at = response_data.get("expiresAt", "N/A")

            if callback_data == "eliteflix-xcloud":  # Formato personalizado
                message = (
                    "*Aproveite o Melhor da EliteFlix Agora*\n"
                    "*TESTE COMPLETO 12HR*\n\n"
                    "*PROVIDER* = star10\n\n"
                    f"2- ✅ *Usuário:* {username}\n"
                    f"3- ✅ *Senha:* {password}\n"
                    "4- ✅ ENTRAR"
                    "\n"
                    "Qualquer Duvida Me Chama!"
                )
            else:  # Formato padrão
                message = (
                    "*Aproveite o Melhor da EliteFlix Agora*\n\n"
                    f"✅USUARIO: {username}\n"
                    f"✅SENHA: {password}\n\n"
                    "TESTE COMPLETO - EliteFlix \n\n"
                    f"🗓️ Criado em: {created_at}\n"
                    f"🗓️ Vencimento: {expires_at}\n"
                    "🔐 Senha Adultos:0000"
                    "\n"
                    "Qualquer Duvida Me Chama!"
                )

            # Botões para gerar novamente
            keyboard = [
                [
                    InlineKeyboardButton("Eliteflix-Star-12H", callback_data="eliteflix-star"),
                    InlineKeyboardButton("Eliteflix-Alpha", callback_data="eliteflix-alpha"),
                ],
                [
                    InlineKeyboardButton("Eliteflix-Onlive-2H", callback_data="eliteflix-onlive"),
                    InlineKeyboardButton("Eliteflix-Uni", callback_data="eliteflix-uni"),
                ],
                [
                    InlineKeyboardButton("Eliteflix-Imperial", callback_data="eliteflix-imperial"),
                    InlineKeyboardButton("Eliteflix-Fire", callback_data="eliteflix-fire"),
                ],
                [
                    InlineKeyboardButton("Eliteflix-Yellow", callback_data="eliteflix-yellow"),
                    InlineKeyboardButton("Eliteflix-Xcloud-12H", callback_data="eliteflix-xcloud"),
                ],
                [
                    InlineKeyboardButton("Eliteflix-Iphone-star-12H", callback_data="eliteflix-iphone"),
                    InlineKeyboardButton("Eliteflix-onlive-2H", callback_data="eliteflix-2horas"),
                ]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)

            # Envia a mensagem formatada com os botões
            await query.edit_message_text(text=message, parse_mode="Markdown", reply_markup=reply_markup)
        else:
            await query.edit_message_text(
                text="Erro na requisição ao servidor. Tente novamente mais tarde."
            )

    except Exception as e:
        # Mensagem de erro em caso de falha
        await query.edit_message_text(
            text="Ocorreu um erro ao processar sua solicitação. Tente novamente mais tarde.",
        )

# Configuração do bot
def main():
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("teste", start))
    application.add_handler(CallbackQueryHandler(button_handler))

    application.run_polling()

if __name__ == "__main__":
    main()
