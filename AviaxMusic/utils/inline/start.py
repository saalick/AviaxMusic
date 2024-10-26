from pyrogram.types import InlineKeyboardButton

import config
from AviaxMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_GROUP),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="🔎 How to use? Command Menu",
                callback_data="settings_back_helper",
            )
        ],
        [
            InlineKeyboardButton(text="📨Channel", url=config.SUPPORT_GROUP),
            InlineKeyboardButton(text="📨Support", url=config.SUPPORT_GROUP),
        ],
        [
            InlineKeyboardButton(
                text="➕ Add Me To Your Group ➕",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="👤 MIW AI Health Coach",
                url="https://app.miwonsol.com",
            )
        ],
    ]
    return buttons
