# Shubh Wishes

Send a Dussehra, Diwali or birthday wish that the other person has to open: they light the diyas, burn Ravana or blow out the candles, and your message appears.

Live: https://sreekumarkr777.github.io/shubh/

- No sign-up and no database. The names and message travel inside the link.
- `index.html` is the whole app. `python3 build.py` regenerates the per-festival pages (`/dussehra/`, `/diwali/`, `/birthday/`), which exist so each gets its own WhatsApp link preview.
- `config.js` holds the UPI ID for the optional shagun section, which stays hidden while it is empty.
