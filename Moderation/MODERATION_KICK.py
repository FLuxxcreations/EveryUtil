# SYSTEM IMPORTS
import nextcord
import asyncio
from nextcord import Interaction
from nextcord.ext import commands

# Add cog to cog list in main file
class MODERATION_KICK(commands.Cog):
    def __init__(self, client):
        self.client = client

    guild = nextcord.guild
        
    # When the cog boots up on bot launch:
    # It will print 'Kick Cog registered.'

    @commands.Cog.listener()
    async def on_ready(self):
        await asyncio.sleep(1)
        print("Kick Cog registered.")

    @nextcord.slash_command(
        name='kick',
        description="Kicks a member from the server with a reason."
    )  # Command name and description
    async def kick(self, interaction: Interaction, user: nextcord.Member, *, reason=None):
        if interaction.user.guild_permissions.kick_members: # you could also use guild_permissions.kick_members
            await user.kick(reason=reason)
            kickedEmbed = nextcord.Embed(
                title='User Kicked',
                description=f'**{user.name}** has been kicked from the server by **{interaction.user}** for reason **{reason}**',
                color=0xD41C0B
            )
            await interaction.response.send_message(embed=kickedEmbed)
        else:
            permissionErrorEmbed = nextcord.Embed(
                title=':x: Insufficient Permissions',
                description='You need the **Kick Members** permission to do this.\nCheck with a member of staff if this is incorrect.',
                color=0xD41C0B
            )
            await interaction.response.send_message(embed=permissionErrorEmbed, delete_after=5)
        


def setup(client):
    client.add_cog(MODERATION_KICK(client))
