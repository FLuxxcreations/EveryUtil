# SYSTEM IMPORTS
import nextcord
import asyncio
from nextcord import Interaction
from nextcord.ext import commands


# Add cog to cog list in main file
class DEFAULT_WHOIS(commands.Cog):

    def __init__(self, client):
        self.client = client

    # When the cog boots up on bot launch:
    # It will print 'Who Is? Cog registered.'

    @commands.Cog.listener()
    async def on_ready(self):
        await asyncio.sleep(1)
        print("Who Is? Cog registered.")

    @nextcord.slash_command(
        name='whois',
        description="Find out some information about another member."
    )  # Command name and description
    async def invite(self, interaction: Interaction, member: nextcord.Member = None):
        embed = nextcord.Embed(  # Create new embed
            color=0xFCC758)  # Set colour for embed
        embed.add_field(name='Member Name:', value=f"```{member}```", inline=True)
        embed.add_field(name='Member ID:', value=f'```{member.mention}```', inline=True)
        embed.add_field(name='Account Created:', value=f'```{member.created_at}```')
        embed.add_field(name='Joined Server:', value=f'```{member.joined_at}```')
        embed.set_thumbnail(member.avatar)
        await interaction.response.send_message(embed=embed)  # Respond with embed


def setup(client):
    client.add_cog(DEFAULT_WHOIS(client))
