import discord
import os # default module
bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")
    for guild in bot.guilds:
        print(guild.name) # prints all server's names

@bot.slash_command(name="kick", description="Kick a player from your server.")
@discord.default_permissions(kick_members = True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.respond(f'{member.mention} has been kicked!')
        
@bot.slash_command(name="ban", description="Ban a player from your server.")
@discord.default_permissions(ban_members = True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.respond(f'{member.mention} has been banned!')
    
@bot.slash_command(name="support", description="Get a link to the support server")
async def hello(ctx: discord.ApplicationContext):
    await ctx.respond("discord.gg/BQcRt77Pkp")
    

bot.run("nuh uh")
