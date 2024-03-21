import telepot
import time

# Token do seu bot do Telegram e ID do grupo
bot_token = '6640349473:AAGAwbWw5MKZeHpoKcm2BUS9rM5wl1wNnpo'  # Substitua pelo token real do seu bot
group_chat_id = '1967378125'  # Substitua pelo ID do seu grupo Telegram

# Inicialize o bot do Telegram
bot = telepot.Bot(bot_token)

# Modelos de sinais
modelos_sinais = [
    """
🤑 NOVA OPORTUNIDADE!

🎮 JOGO: 🐭 Fortune Mouse 🐭
⚡️ 6X - Turbo
🔃 Alternando
🎰 6X - Normal
⏰ Validade: 3 minutos

🚨 FUNCIONA APENAS NESTA PLATAFORMA ⬇️
🎰 𝗣𝗹𝗮𝘁𝗮𝗳𝗼𝗿𝗺𝗮: https://abrir.link/Ggggame
⚠️ NÃO TENTE EM OUTRO SITE! ⬆️

👇 APLICATIVO DOS SLOTS 👇
https://abrir.link/Pirata-Script-Sinais
""",
    """
🤑 NOVA OPORTUNIDADE!

🎮 JOGO: 🐯 Fortune Tiger 🐯
⚡️ 5X - Turbo
🔃 Alternando
🎰 7X - Normal
⏰ Validade: 3 minutos

🚨 FUNCIONA APENAS NESTA PLATAFORMA ⬇️
🎰 𝗣𝗹𝗮𝘁𝗮𝗳𝗼𝗿𝗺𝗮: https://abrir.link/Ggggame
⚠️ NÃO TENTE EM OUTRO SITE! ⬆️

👇 APLICATIVO DOS SLOTS 👇
https://abrir.link/Pirata-Script-Sinais
""",
    """
🤑 NOVA OPORTUNIDADE!

🎮 JOGO: 🐭 Fortune Mouse 🐭
⚡️ 3X - Turbo
🔃 Alternando
🎰 10X - Normal
⏰ Validade: 3 minutos

🚨 FUNCIONA APENAS NESTA PLATAFORMA ⬇️
🎰 𝗣𝗹𝗮𝘁𝗮𝗳𝗼𝗿𝗺𝗮: https://abrir.link/Ggggame
⚠️ NÃO TENTE EM OUTRO SITE! ⬆️

👇 APLICATIVO DOS SLOTS 👇
https://abrir.link/Pirata-Script-Sinais
""",
    """
🤑 NOVA OPORTUNIDADE!

🎮 JOGO: 🐯 Fortune Tiger 🐯
⚡️ 6X - Turbo
🔃 Alternando
🎰 8X - Normal
⏰ Validade: 3 minutos

🚨 FUNCIONA APENAS NESTA PLATAFORMA ⬇️
🎰 𝗣𝗹𝗮𝘁𝗮𝗳𝗼𝗿𝗺𝗮: https://abrir.link/Ggggame
⚠️ NÃO TENTE EM OUTRO SITE! ⬆️

👇 APLICATIVO DOS SLOTS 👇
https://abrir.link/Pirata-Script-Sinais
""",
    """
🤑 NOVA OPORTUNIDADE!

🎮 JOGO: 🐭 Fortune Mouse 🐭
⚡️ 9X - Turbo
🔃 Alternando
🎰 7X - Normal
⏰ Validade: 3 minutos

🚨 FUNCIONA APENAS NESTA PLATAFORMA ⬇️
🎰 𝗣𝗹𝗮𝘁𝗮𝗳𝗼𝗿𝗺𝗮: https://abrir.link/Ggggame
⚠️ NÃO TENTE EM OUTRO SITE! ⬆️

👇 APLICATIVO DOS SLOTS 👇
https://abrir.link/Pirata-Script-Sinais
""",
    """
🤑 NOVA OPORTUNIDADE!

🎮 JOGO: 🐯 Fortune Tiger 🐯
⚡️ 7X - Turbo
🔃 Alternando
🎰 4X - Normal
⏰ Validade: 3 minutos

🚨 FUNCIONA APENAS NESTA PLATAFORMA ⬇️
🎰 𝗣𝗹𝗮𝘁𝗮𝗳𝗼𝗿𝗺𝗮: https://abrir.link/Ggggame
⚠️ NÃO TENTE EM OUTRO SITE! ⬆️

👇 APLICATIVO DOS SLOTS 👇
https://abrir.link/Pirata-Script-Sinais
""",
    """
🤑 NOVA OPORTUNIDADE!

🎮 JOGO: 🐭 Fortune Mouse 🐭
⚡️ 4X - Turbo
🔃 Alternando
🎰 11X - Normal
⏰ Validade: 3 minutos

🚨 FUNCIONA APENAS NESTA PLATAFORMA ⬇️
🎰 𝗣𝗹𝗮𝘁𝗮𝗳𝗼𝗿𝗺𝗮: https://abrir.link/Ggggame
⚠️ NÃO TENTE EM OUTRO SITE! ⬆️

👇 APLICATIVO DOS SLOTS 👇
https://abrir.link/Pirata-Script-Sinais
""",
    """
🤑 NOVA OPORTUNIDADE!

🎮 JOGO: 🐯 Fortune Tiger 🐯
⚡️ 9X - Turbo
🔃 Alternando
🎰 6X - Normal
⏰ Validade: 3 minutos

🚨 FUNCIONA APENAS NESTA PLATAFORMA ⬇️
🎰 𝗣𝗹𝗮𝘁𝗮𝗳𝗼𝗿𝗺𝗮: https://abrir.link/Ggggame
⚠️ NÃO TENTE EM OUTRO SITE! ⬆️

👇 APLICATIVO DOS SLOTS 👇
https://abrir.link/Pirata-Script-Sinais
"""
]

while True:
    try:
        # Intercale entre os modelos de sinais
        for modelo in modelos_sinais:
            # Envie o sinal para o grupo do Telegram
            bot.sendMessage(group_chat_id, modelo)

            # Aguarde 1 minuto antes de enviar o próximo sinal
            time.sleep(240)  # 240 segundos = 4 minuto

    except Exception as e:
        # Lida com exceções, se ocorrerem
        print(f"Erro: {str(e)}")
