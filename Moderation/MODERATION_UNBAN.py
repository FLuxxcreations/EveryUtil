# SYSTEM IMPORTS
import nextcord
import asyncio
from nextcord import Interaction
from nextcord.ext import commands


# Add cog to cog list in main file
class MODERATION_UNBAN(commands.Cog):

    def __init__(self, client):
        self.client = client

    guild = nextcord.guild  # Defines guild
    # When the cog boots up on bot launch:
    # It will print 'Unban Cog registered.'

    @commands.Cog.listener()
    async def on_ready(self):
        await asyncio.sleep(1)
        print("Unban Cog registered.")

    @nextcord.slash_command(
        name='unban',
        description="Removes the ban from a member from the server."
    )  # Command name and description
    async def unban(self, interaction: Interaction, member, *, reason=None):
        if interaction.user.guild_permissions.manage_guild:  # you could also use guild_permissions.kick_members
            # ^ Double checks user permission for manage server permission
            banned_users = interaction.guild.bans(
            )  # Lists all banned members for server
            member_name, member_discriminator = member.split(
                "#")  # Formats the user name into FLuxx#4837 (Example)
            async for ban_entry in banned_users:  # Double checks if user used in argument is banned
                user = ban_entry.user  # Defines user in argument as targeted user
                if (user.name, user.discriminator) == (
                        member_name, member_discriminator
                ):  # If the name matches the argument and list
                    await interaction.guild.unban(user)  # Unbans the user
                    unbannedEmbed = nextcord.Embed(  # Creates embed
                        title=
                        ':white_check_mark: User Unbanned',  # Sets embed title
                        description=
                        f'**{user.name}#{user.discriminator}** has been unbanned from the server by **{interaction.user}**',  # Sets embed description
                        color=0x0ED510  # Sets embed colour
                    )
                    await interaction.response.send_messgae(embed=unbannedEmbed
                                   )  # Send the embed to the channel
                else:  # If the user does not have permissions
                    permissionErrorEmbed = nextcord.Embed(  # Creates the error embed
                        title=
                        ':x: Insufficient Permissions',  # Sets the embed title
                        description=
                        'You need the **Manage Server** permission to do this.\nCheck with a member of staff if this is incorrect.',  # Sets the embed description
                        color=0xD41C0B  # Sets the embed colour
                    )
                    await interaction.response.send_message(
                        embed=permissionErrorEmbed, delete_after=5
                    )  # Send the error embed to the channel and delete after 5 seconds


def setup(client):
    client.add_cog(MODERATION_UNBAN(client))
