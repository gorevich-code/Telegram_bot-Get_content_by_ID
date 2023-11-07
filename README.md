# Telegram_bot-Get_content_by_ID

Adding content: 
- User sends command /add, recieve advice to message any input (text, sticker, video, document)
- Bot returns added content ID to the User
- User can abort add content flow after /add command by /add_cancel command.

Getting content:
- User sends command /get, recieves advice to message content ID
- Bot sends to the User relevant content if exists.
- Bot sends to the User message that no content exists under specified ID if no content exists.

Tech stack: aiogram, sqlite3, virtualenv
