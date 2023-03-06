import discord
import os

from keep_alive import keep_alive

client = discord.Client(intents=discord.Intents.all())
keyword = "accas help"
keyword2 = "frontier help"
keyword3 = "feedback stream help"
keyword4 = "event help"
keyword5 = "rice scene"
keyword6 = "ticket accas"
guild_id = int(os.environ['GUILD_ID'])
channel_id = int(os.environ['CHANNEL_ID'])
role_id = int(os.environ['ROLE_ID'])

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if keyword in message.content.lower():
        guild = client.get_guild(guild_id)
        role = guild.get_role(role_id)
        channel = client.get_channel(channel_id)
        await channel.send(f'{message.author.name}, If you have a question about the ACCAs, you can either ask a Community QnA Expert in the <#1080239744170082344> forum, or explore <https://accas.theaccommunity.com/>')

    if keyword2 in message.content.lower():
        guild = client.get_guild(guild_id)
        role = guild.get_role(role_id)
        channel = client.get_channel(channel_id)
        await channel.send(f'{message.author.name}, If you have a question about FRONTIER, you can either ask a FRONTIER staff member, or explore <https://frontier.theaccommunity.com/>')

    if keyword3 in message.content.lower():
        guild = client.get_guild(guild_id)
        role = guild.get_role(role_id)
        channel = client.get_channel(channel_id)
        await channel.send(f'{message.author.name}, If you have a question about Feedback Streams, you can either read the section for it in <#455487042990768130>, or ask a Host.')

    if keyword4 in message.content.lower():
        guild = client.get_guild(guild_id)
        role = guild.get_role(role_id)
        channel = client.get_channel(channel_id)
        await channel.send(f'{message.author.name}, If you have questions about AC Events, you can either direct them to <@424698436844126232> or events@theaccommunity.com')

    if keyword5 in message.content.lower():
        guild = client.get_guild(guild_id)
        role = guild.get_role(role_id)
        channel = client.get_channel(channel_id)
        await channel.send(f':rice_scene:')

    if keyword6 in message.content.lower():
        guild = client.get_guild(guild_id)
        role = guild.get_role(role_id)
        channel = client.get_channel(channel_id)
        await channel.send(f'{role.mention}, {message.author.name} has opened an ACCAs Support Ticket!')

keep_alive()
token = os.environ.get("TOKEN")
client.run(token)

token = os.environ.get("TOKEN")

client.run(os.environ['TOKEN'])