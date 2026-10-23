"""Standalone Telegram audio/video voice-chat player."""
import logging
import os
import sys

from telegram.ext import Application

from media_play import register_media_play

logging.basicConfig(
    level=os.getenv("LOG_LEVEL", "INFO").upper(),
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
log = logging.getLogger("media-bot")


def main() -> None:
    token = os.getenv("BOT_TOKEN", "").strip() or os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
    if not token:
        raise RuntimeError("Missing BOT_TOKEN (or TELEGRAM_BOT_TOKEN) environment variable.")

    app = Application.builder().token(token).build()
    register_media_play(app)
    log.info("Media bot starting; polling Telegram updates.")
    app.run_polling(drop_pending_updates=False, allowed_updates=["message", "callback_query"])


if __name__ == "__main__":
    main()
