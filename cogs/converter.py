import discord
from discord.ext import commands
import os

from datetime import datetime
import pytz

# from dotenv import load_dotenv
# load_dotenv()


class TimezoneConverter(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.HELP_EMBED_MESSAGE = discord.Embed()
        self.HELP_EMBED_MESSAGE.add_field(name='!tz help', value='Timezone Converter の使い方(このメッセージ)を表示するにゃ!', inline=False)
        self.HELP_EMBED_MESSAGE.add_field(name='!tz {Timezone}', value='指定された Timezone の現在時刻を表示するにゃ!', inline=False)


    def is_bot():
        def check_bot(ctx):
            return not ctx.author.bot
        return commands.check(check_bot)


    @commands.group(name='tz')
    @is_bot()
    async def tz(self, ctx):
        if ctx.invoked_subcommand is None:
            # 登録されていないサブコマンドが実行されたとき
            self.HELP_EMBED_MESSAGE.title = '登録されたサブコマンドを利用して欲しいにゃ!'
            self.HELP_EMBED_MESSAGE.description = 'このわかりやすいヘルプをよく読むにゃ。'
            self.HELP_EMBED_MESSAGE.color = discord.Color.red()
            await ctx.send(content=None, embed=self.HELP_EMBED_MESSAGE)

    @tz.group(name='help')
    @is_bot()
    async def _help(self, ctx):
        self.HELP_EMBED_MESSAGE.title = '吾輩は Timezone Converter である!'
        self.HELP_EMBED_MESSAGE.description='わからないことがあったら OJI に聞くにゃ！'
        self.HELP_EMBED_MESSAGE.color = discord.Color.green()
        await ctx.send(content=None, embed=self.HELP_EMBED_MESSAGE)

    @tz.group(name='now')
    async def _now(self, ctx, *target_timezone):
        EMBED_MESSAGE = discord.Embed()

        if not target_timezone:
            current_time = datetime.now().strftime('%Y年%m月%d日 %H時%M分')
            EMBED_MESSAGE.title = f'現在は{current_time}ですにゃ!'
            EMBED_MESSAGE.color = discord.Color.green()
        else:
            EMBED_MESSAGE.title = '現在その機能は実装されてないにゃ。'
            EMBED_MESSAGE.color = discord.Color.red()

        await ctx.send(content=None, embed=EMBED_MESSAGE)


def setup(bot):
    bot.add_cog(TimezoneConverter(bot))