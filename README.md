# Telegram Bot README

## Overview
This is a Telegram bot built using the Telebot library for Python. Its main function is to ensure that users in a specific chat are also members of a designated channel. If a user tries to send a message in the chat without being a member of the channel, they will receive an alert and a prompt to join the channel. Once they've joined the channel, they can interact in the chat normally.

## Installation
1. Ensure you have Python installed on your system.
2. Install the required libraries:

    ```bash
    pip install pyTelegramBotAPI
    ```

## Setup
1. Create a new bot on Telegram using the BotFather and obtain your TOKEN.
2. Replace the placeholder `'000'` in the `TOKEN` variable with your actual bot token.
3. Specify the Telegram channel's username in the `CHANNEL_ID` variable, ensuring it begins with an "@" symbol. For instance, `@myChannelName`.

## How it Works
- When a user sends a message in the chat, the bot checks if they're a member of the specified channel.
- If they aren't, their message is deleted, and they're sent an alert asking them to join the channel. This alert message auto-deletes after a set time (default is 10 seconds, but you can modify this).
- If the user joins the channel and returns to the chat, they can click a button to verify their membership. Once verified, they can chat normally.

## Key Lines to Modify
- `TOKEN = '000'`: Replace `'000'` with your actual bot token.
- `CHANNEL_ID = '@userChannel'`: Replace `@userChannel` with your channel's username.
- `threading.Timer(10, lambda: bot.delete_message(chat_id, message_id)).start()`: Modify the number `10` to change the time (in seconds) before the alert message is auto-deleted.

## Running the Bot
To run the bot, navigate to the directory containing the script and execute:

    ```
    python main.py
    ```

Replace `main.py` with the name of your script.

> **Note:** Ensure you have the appropriate permissions to access and manage the specified channel and chat for the bot to function correctly.
