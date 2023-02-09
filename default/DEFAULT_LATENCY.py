# SYSTEM IMPORTS
import nextcord
import asyncio
from nextcord import Interaction
from nextcord.ext import commands


# Add cog to cog list in main file
class DEFAULT_LATENCY(commands.Cog):

    def __init__(self, client):
        self.client = client

    # When the cog boots up on bot launch:
    # It will print 'Latency Cog registered.'

    @commands.Cog.listener()
    async def on_ready(self):
        await asyncio.sleep(1)
        print("Latency Cog registered.") # Print when cog is functioning

    @nextcord.slash_command(name='latency', description="Display the latency for the bot in milliseconds.")  # Command                                                                                                            name and description
    async def latency(self, interaction: Interaction):
        embed = nextcord.Embed(
            title="Bot Latency:",
            color = 0x57E9F8,
            description=f":ping_pong: Bot latency: **{round(self.client.latency * 1000)}ms**"
        )
        await interaction.response.send_message(embed=embed, delete_after=10)  # Respond with embed and delete message                                                                                      after 10 seconds

def setup(client):
    client.add_cog(DEFAULT_LATENCY(client))
