# SYSTEM IMPORTS
import nextcord
import asyncio
from nextcord import Interaction
from nextcord.ext import commands

# Add cog to cog list in main file
class DEFAULT_INVITE(commands.Cog):
    def __init__(self, client):
        self.client = client

    # When the cog boots up on bot launch:
    # It will print 'Help Cog registered.'

    @commands.Cog.listener()
    async def on_ready(self):
        await asyncio.sleep(1)
        print("Invite Cog registered.")

    @nextcord.slash_command(name = 'invite', description = "Have the bot send an invite to add it to your server.")    # Command name and description   
    async def invite(self, interaction: Interaction):
        embed = nextcord.Embed( # Create new embed
        title = 'Invite ModzBott', # Set title for embed
        description = ':x: You are unable to do this as this is the experimental bot.', # Set description for embed
        color = 0x4C82D9 # Set colour for embed
    )
        await interaction.response.send_message(embed=embed) # Respond with embed

def setup(client):
    client.add_cog(DEFAULT_INVITE(client))