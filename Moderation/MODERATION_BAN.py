# SYSTEM IMPORTS
import nextcord
import asyncio
from nextcord import Interaction
from nextcord.ext import commands

# Add cog to cog list in main file
class MODERATION_BAN(commands.Cog):
    def __init__(self, client):
        self.client = client

    guild = nextcord.guild
        
    # When the cog boots up on bot launch:
    # It will print 'Ban Cog registered.'

    @commands.Cog.listener()
    async def on_ready(self):
        await asyncio.sleep(1)
        print("Ban Cog registered.")

    @nextcord.slash_command(
        name='ban',
        description="Bans a member **permanently** from the server with a reason."
    )  # Command name and description
    async def ban(self, interaction: Interaction, user: nextcord.Member, *, reason=None):
        if interaction.user.guild_permissions.ban_members: # you could also use guild_permissions.kick_members
            await user.ban(reason=reason) # Bans the user
            bannedEmbed = nextcord.Embed( # Creates the embed
                title='User Banned',
                description=f'**{user.name}** has been banned from the server by **{interaction.user}** for reason **{reason}**',
                color=0xD41C0B
            )
            await interaction.response.send_message(embed=bannedEmbed) # Send the embed to channel
        else: # If the user does not have permission
            permissionErrorEmbed = nextcord.Embed(
                title=':x: Insufficient Permissions',
                description='You need the **Ban Members** permission to do this.\nCheck with a member of staff if this is incorrect.',
                color=0xD41C0B
            )
            await interaction.response.send_message(embed=permissionErrorEmbed, delete_after=5)
        


def setup(client):
    client.add_cog(MODERATION_BAN(client))
