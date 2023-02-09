# SYSTEM IMPORTS
import nextcord
import asyncio
from nextcord import Interaction
from nextcord.ext import commands


# Add cog to cog list in main file
class DEFAULT_HELP(commands.Cog):

    def __init__(self, client):
        self.client = client

    # When the cog boots up on bot launch:
    # It will print 'Invite Cog registered.'

    @commands.Cog.listener()
    async def on_ready(self):
        await asyncio.sleep(1)
        print("Help Cog registered.")

    @nextcord.slash_command(
        name='help',
        description="Have the bot send a link to the support server."
    )  # Command name and description
    async def invite(self, interaction: Interaction):
        embed = nextcord.Embed(  # Create new embed
            title='Need some help?',  # Set title for embed
            description=
            ':x: You are unable to do this as this is the experimental bot.',  # Set description for embed
            color=0xe2f6f3  # Set colour for embed
        )
        await interaction.response.send_message(embed=embed
                                                )  # Respond with embed


def setup(client):
    client.add_cog(DEFAULT_HELP(client))
