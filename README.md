# Play Music in Telegram Calls

A standalone Telegram bot that plays audio and video in Telegram group voice/video chats using a Telegram bot account plus a Pyrogram assistant user session.

## Required Railway variables

- `BOT_TOKEN`: token from BotFather.
- `API_ID`: Telegram API ID from https://my.telegram.org.
- `API_HASH`: Telegram API hash.
- `SESSION_STRING`: Pyrogram assistant-user session string. Keep it private; anyone with it may access that Telegram account.
- `OWNER_ID` (optional): numeric Telegram user ID treated as an owner/admin.

The assistant account must be able to join the target group call. The bot must be added to the group and have permission to send messages. Use a group where voice/video chats are available.

## Commands

- `/play`: play replied-to audio/video, or a supported public media URL handled by yt-dlp.
- `/audio`: audio-only playback; reply to a Telegram media message or provide a supported media URL.
- `/video`: video playback; reply to a Telegram media message or provide a supported media URL, including direct video and compatible HLS/M3U8 links.
- `/pause`, `/resume`: pause/resume.
- `/skip`: skip the current item.
- `/stop`, `/leave`, Arabic `انهاء` or `إنهاء`: stop playback, clear the queue, and leave the call.
- `/queue`: show current item and queue.
- `/now`: show playback state and position.
- `/clear`: clear queued items.
- `/shuffle`: shuffle queued items.
- `/repeat off|one|all`: set repeat mode.

Inline controls include pause/resume, seek back/forward 10 seconds, skip, stop, queue, repeat, and hide controls. Playback controls are restricted to group administrators and the configured owner.

## Deploy on Railway

Create a service from this repository and deploy with the included Dockerfile. Add the required variables in the service's Variables panel. The container installs both FFmpeg and FFprobe, which the player checks before starting.

## Important limitations

- URL playback depends on yt-dlp extractors and each source site's current access rules; unsupported sites, sign-in challenges, expiring links, or blocked media may prevent downloads.
- The player downloads media before playback rather than streaming while downloading.
- Queue/player state is in memory and is reset when the service restarts.
- Telegram group-call playback requires a valid assistant session and an active/available call. This repository does not guarantee that every Telegram group or media URL will work.
- Never publish `BOT_TOKEN`, `API_HASH`, or `SESSION_STRING`.
