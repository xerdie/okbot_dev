import discord
import os
from discord.ext import commands

os.chdir(r'/storage/emulated/0/okbot/')
client = commands.Bot(command_prefix=".")
client.remove_command("help")

@client.event
async def on_ready():
  print("bot is ready")

@client.command()
async def help(ctx):
	
	embed=discord.Embed(colour=0xFFFF00)
	embed.add_field(name="ban", value="Bans players using there @.")
	
	await ctx.send(embed=embed)

@client.command()
@commands.has_any_role("Admin")
async def ban(ctx, member:discord.User=None, reason =None):
    if member == None or member == ctx.message.author:
        await ctx.channel.send("You cannot ban yourself")
        return
    if reason == None:
        reason = "No reason specified"
    message = (f"You have been banned from {ctx.guild.name} for {reason}")
    await member.send(message)
    await ctx.guild.ban(member, reason=reason)
    await ctx.channel.send(f"{member} was successfully banned for reason {reason}")


for filename in os.listdir('./modules'):
    if filename.endswith('.py'):
            client.load_extension(f'modules.{filename[:-3]}')
           
client.run("NzIwNzM2OTY0MTg5MzU2MDQ0.XuKUyQ.xeNOxzgeMlPhR46ueymp80cYQ4Q")
