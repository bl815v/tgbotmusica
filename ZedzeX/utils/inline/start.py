from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="Agregame al grupo!",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="✯ Ayuda ✯",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="✯ Configuracion ✯", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="Agregame al grupo!",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="✯ Creador original ✯", url=f"https://t.me/katil_your_dad"
            ),
            InlineKeyboardButton(
                text="✯ Ayuda ✯", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="✯ Soporte ✯", url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text="✯ Actualizaciones ✯", url=f"https://t.me/katil_bots",
            )
        ],
        [
            InlineKeyboardButton(
                text="🌱ƨσʋяcɛ🌱",
                url=f"https://github.com/team-katil/zedzemusic",
            )
        ],
     ]
    return buttons
