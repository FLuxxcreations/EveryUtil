# SYSTEM IMPORTS
import nextcord
import asyncio
from nextcord import Interaction
from nextcord.ext import commands

# Add cog to cog list in main file
class UTILITY_LOCK(commands.Cog):

    def __init__(self, client):
        self.client = client

    guild = nextcord.guild
        
    # When the cog boots up on bot launch:
    # It will print 'Lock Cog registered.'

    @commands.Cog.listener()
    async def on_ready(self):
        await asyncio.sleep(1)
        print("Lock Cog registered.")

    @nextcord.slash_command(
        name='lock',
        description="Locks the channel for members who do not have administrator permissions."
    )  # Command name and description
    async def lock(self, interaction: Interaction):
        if interaction.user.guild_permissions.manage_channels: # you could also use guild_permissions.kick_members
            embed = nextcord.Embed(  # Create new embed
                color= 0xD41C0B,  # Set colour for embed
                title=':lock: Channel Locked',
                description=f'This channel has been locked by {interaction.user}. Check back later.'
            )
            await interaction.response.send_message(embed=embed)  # Respond with embed
            overwrite = interaction.channel.overwrites_for(interaction.guild.default_role) # Defines @everyone and checks permissions
            overwrite.send_messages = False # Stop users from sending messages
            await interaction.channel.set_permissions(interaction.guild.default_role, overwrite=overwrite) # Set permissions for @everyone
        else:
            permissionErrorEmbed = nextcord.Embed(
                color=0xD41C0B,
                title=':x: Insufficient Permission',
                description='You do not have the correct permission to do this. Check with a member of staff if this is incorrect'
            )
            await interaction.response.send_message(embed=permissionErrorEmbed, delete_after=5)
        


def setup(client):
    client.add_cog(UTILITY_LOCK(client))
