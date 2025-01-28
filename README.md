# Discord Bot with Generative AI (Gemini)

A Python-based Discord bot that integrates with Google's Gemini Generative AI API to provide dynamic responses. The bot is capable of replying to specific commands such as `$hello` and `$gemini`.

---

## Features
- **Greeting Command**: Responds with a simple `"Hello!"` message when a user types `$hello`.
- **AI Response**: Processes user input provided after the `$gemini` command and generates AI-based responses using Google's Gemini API.
- **Fully Configured Intents**: The bot is set up to work with Discord's message content intent.

---

## Prerequisites

Before you start, ensure you have the following tools and libraries:
1. **Python**: Version 3.8 or later.
2. **Discord Development Account**: Necessary for generating your bot token.
3. [**Google Bard / Gemini API Access**](https://ai.google/tools/) and an API key.
4. [**dotenv** Library](https://pypi.org/project/python-dotenv/): To securely manage API keys.
5. Required Python packages:
    - `discord.py`
    - `google-generativeai`
    - `python-dotenv`

---

## Setup Instructions

1. Clone this repository:
```shell script
git clone <repository-url>
cd <repository-folder>
```

2. Install dependencies:
```shell script
pip install -r requirements.txt
```
   *(Make sure `discord.py`, `google-generativeai`, and `python-dotenv` are included in the `requirements.txt`.)*

3. Create a `.env` file in the project's root directory and include the following variables:
```
DISCORD_BOT_TOKEN=<Your_Discord_Bot_Token>
GOOGLE_API_KEY=<Your_Gemini_API_Key>
```

4. Run the bot:
```shell script
python bot.py
```
   *(Replace `bot.py` with the name of your file if it differs.)*

---

## Environment Variables

The bot relies on a `.env` file to safely load sensitive keys:
- `DISCORD_BOT_TOKEN`: Token for your Discord bot (from Discord Developer Portal).
- `GOOGLE_API_KEY`: API Key for the Gemini Generative AI.

---

## Commands

### **1. `$hello`**
- **Description**: Sends a friendly `"Hello!"` back to the user.
- **Example**:
```
User: $hello
Bot: Hello!
```

### **2. `$gemini <text>`**
- **Description**: Interacts with the Gemini AI. The bot will process `<text>` as input and return a generative text response from the Gemini model.
- **Example**:
```
User: $gemini Tell me a story about space.
Bot: [Gemini's response]
```

---

## Handling Errors

- If any errors occur while using Gemini API (e.g., invalid API key, quota exceeded),