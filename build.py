#!/usr/bin/env python3
"""Generate /dussehra/, /diwali/ and /birthday/ from index.html, each with its own static share preview."""
import os, re

BASE = "https://sreekumarkr777.github.io/shubh/"
PAGES = {
    "dussehra": ("🏹 You have a Dussehra wish. Tap to open.", "Someone made this for you. Shoot three arrows, burn Ravana, and read your message."),
    "diwali": ("🪔 You have a Diwali wish. Tap to open.", "Someone made this for you. Light the diyas and read your message."),
    "birthday": ("🎂 You have a birthday wish. Tap to open.", "Someone made this for you. Blow out the candles and read your message."),
}
src = open("index.html", encoding="utf-8").read()
for key, (title, desc) in PAGES.items():
    html = src
    html = re.sub(r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{title}">', html)
    html = re.sub(r'<meta property="og:description" content="[^"]*">', f'<meta property="og:description" content="{desc}">', html)
    html = html.replace(f'{BASE}og.jpg', f'{BASE}og-{key}.jpg')
    html = html.replace(f'<meta property="og:url" content="{BASE}">', f'<meta property="og:url" content="{BASE}{key}/">')
    html = html.replace('<script src="config.js"></script>', f'<script>window.FEST_KEY = "{key}";</script>\n<script src="../config.js"></script>')
    os.makedirs(key, exist_ok=True)
    open(os.path.join(key, "index.html"), "w", encoding="utf-8").write(html)
    print("built", key)
