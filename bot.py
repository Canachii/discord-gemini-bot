import discord
import google.generativeai as genai
from dotenv import load_dotenv
import os

# 환경 변수 로드
load_dotenv()

# Discord Intents 구성
intents = discord.Intents.default()
intents.message_content = True  # 메시지 콘텐츠에 액세스하려면 필요

# Discord 클라이언트 및 Gemini API 초기화
client = discord.Client(intents=intents)
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash-exp")

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$hello"):
        await message.reply("Hello!")

    elif message.content.startswith("$gemini"):
        # Gemini API와 상호 작용
        prompt = message.content[len("$gemini"):].strip()
        try:
            response = model.generate_content(prompt)
            await message.reply(response.text)
        except Exception as e:
            await message.reply(f"An error occurred: {e}")

client.run(os.getenv("DISCORD_BOT_TOKEN"))