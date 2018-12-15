import discord
TOKEN = 'NTIzMzAwNDkxNzcwMjAwMDY2.DvXhag.UhsHyNYExtCS-jt2m7gCJiXgO7U'
client = discord.Client()

@client.event
async def on_message(message):
        if message.author == client.user:
                return
        if message.content.contains("sarah" or "SARAH" or "Sarah"):
                message = 'I can\'t see your comment {0.author.mention}? It\'s just blank?'.format(message)
                await.client.send_message(message.channel, msg)
client.run(TOKEN)

