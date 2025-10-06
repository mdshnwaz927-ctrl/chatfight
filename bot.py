
- Contains all Telegram bot logic using aiogram.
- Tracks stickers sent by users in group chats.
- Handles commands:
    • /start — Starts the bot and shows welcome message with inline buttons.
    • /mystats — Shows the sticker count for the user.
    • /topstickers — Displays the group leaderboard.
    • /resetstickers — Admin-only command to reset the leaderboard.
    • /botinfo — Shows bot uptime, active groups, and database info.
- Handles new user joins and sends a welcome message.
- Stores data in SQLite (stickers.db) for persistence.
- Includes inline buttons for quick access to stats, leaderboard, and bot info.
- Fully asynchronous using asyncio for smooth operation.
