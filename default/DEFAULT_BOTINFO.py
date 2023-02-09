# SYSTEM IMPORTS
import nextcord
import asyncio
from nextcord import Interaction
from nextcord.ext import commands


# Add cog to cog list in main file
class DEFAULT_BOTINFO(commands.Cog):

    def __init__(self, client):
        self.client = client

    # When the cog boots up on bot launch:
    # It will print 'Bot Information Cog registered.'

    @commands.Cog.listener()
    async def on_ready(self):
        await asyncio.sleep(1)
        print("Bot Information Cog registered.") # Print when cog is functioning

    @nextcord.slash_command(name='information',
                            description="General Information about ModzBott."
                            )  # Command name and description
    async def information(self, interaction: Interaction):
        embed = nextcord.Embed(title="Bot Informaton:", color = 0x57E9F8)
        embed.add_field(name="Bot Creator:",
                        value="```FLuxx#2567```",
                        inline=True)
        embed.add_field(name="Creation Date:",
                        value="```01/12/2022```",
                        inline=True)
        embed.add_field(name="Bot Language:",
                        value="```discord.py (nextcord)```",
                        inline=True)
        embed.add_field(name="Bot Shards:", value="```0```", inline=True)
        embed.add_field(name='Bot Version:', value="```v1.2.1```", inline=True)
        embed.set_thumbnail(self.avatar)
        await interaction.response.send_message(embed=embed
                                                )  # Respond with embed


def setup(client):
    client.add_cog(DEFAULT_BOTINFO(client))
