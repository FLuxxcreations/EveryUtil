# SYSTEM IMPORTS
import nextcord
import asyncio
from nextcord import Interaction
from nextcord.ext import commands

# Add cog to cog list in main file
class UTILITY_CLEAR(commands.Cog):

    def __init__(self, client):
        self.client = client

    # When the cog boots up on bot launch:
    # It will print 'Clear Cog registered.'

    @commands.Cog.listener()
    async def on_ready(self):
        await asyncio.sleep(1)
        print("Clear Cog registered.")

    @nextcord.slash_command(
        name='clear',
        description="Remove messages from a channel."
    )  # Command name and description
    async def clear(self, ctx, amount: int, member: nextcord.Member = None):
        if ctx.user.guild_permissions.manage_messages: # you could also use guild_permissions.kick_members
            if member is None:
                await ctx.channel.purge(limit = amount + 1)
                embed = nextcord.Embed(  # Create new embed
                    color= 0xFCC758,  # Set colour for embed
                    title='Messages Purged',
                    description=f'Successfully purged {amount} messages from the channel.'
                )
                await ctx.response.send_message(embed=embed, delete_after=5)  # Respond with embed
        else:
            permissionErrorEmbed = nextcord.Embed(
                color=0xD41C0B,
                title=':x: Insufficient Permission',
                description='You need the **Manage Messages** permission to do this.\nCheck with a member of staff if this is incorrect'
            )
            await ctx.response.send_message(embed=permissionErrorEmbed, delete_after=5)


def setup(client):
    client.add_cog(UTILITY_CLEAR(client))
