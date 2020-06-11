import discord
import time
import os
import json
import datetime
import random
from random import seed
from random import randint
from discord import Member
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, MissingPermissions
from itertools import cycle

client = commands.Bot(command_prefix = [''.'])
start_time = time.time() 

class unban(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        print('Cog Started: unban')

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, id: int):
    	'Command to unban people with there ID.'
    	await ctx.guild.unban(discord.Object(id))
    	embed = discord.Embed(
            color=discord.Color.from_rgb(255, 255, 0)
        )
    	sender = ctx.author
    	embed.set_author(name=f"{sender}")
    	embed.add_field(name="Unban command", value=f"<@{id}> → has returned! We hope you hae learnt your leason.👋")
    	await ctx.send(embed=embed)

def setup(client):
	client.add_cog(unban(client))
