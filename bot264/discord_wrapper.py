import os
from typing import List
import discord

from bot264.common import create_simple_message


def get_int_env(name):
    env_str = os.getenv(name)
    return 0 if env_str in [None, ''] else int(env_str)


def init_discord_wrapper():
    # Channel Settings
    DiscordWrapper.queue_channel = get_int_env('QUEUE_CHANNEL_ID')
    DiscordWrapper.history_channel = get_int_env('HISTORY_CHANNEL_ID')

    # Role IDS
    DiscordWrapper.uta_role_id = get_int_env('UTA_ROLE_ID')
    DiscordWrapper.gta_role_id = get_int_env('GTA_ROLE_ID')
    DiscordWrapper.prof_role_id = get_int_env('PROFESSOR_ROLE_ID')


class DiscordWrapper:
    client = None
    queue_channel = None
    history_channel = None

    uta_role_id = None
    gta_role_id = None
    prof_role_id = None

    @staticmethod
    def is_emoji_channels(channel_id):
        return channel_id in [DiscordWrapper.queue_channel, DiscordWrapper.history_channel]

    @staticmethod
    def is_admin(roles: List[discord.role.Role]):
        for i in roles:
            if i.id in [DiscordWrapper.uta_role_id, DiscordWrapper.gta_role_id, DiscordWrapper.prof_role_id]:
                return True
        return False

    @staticmethod
    async def add_history(message: discord.message.Message):
        embed_message = create_simple_message(message.author.name, message.content)
        if DiscordWrapper.history_channel is not None:
            history_channel: discord.TextChannel = DiscordWrapper.client.get_channel(DiscordWrapper.history_channel)
            message = await history_channel.send(embed=embed_message)
            for i in ["🔄", "❌"]:
                await message.add_reaction(i)
