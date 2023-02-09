# SYSTEM IMPORTS
import nextcord
import asyncio
from webserver import keep_alive
from nextcord.ext import commands
import os

TOKEN = os.environ['TOKEN'] # Identify token in the secret

# Give the bot Discord intents
intents = nextcord.Intents.default()
intents.members = True # Give the bot the intent from Discord Developer Portal

client = commands.Bot(command_prefix='!', intents=intents) # ! prefix will not work as slash commands are implemented


@client.event  # Code to run on bot start
async def on_ready():
    print('ModzBott Experimental is running!'
          )  # Print startup message to console
    print('----------------------------------')
    await asyncio.sleep(0.5) # Waiting 0.5 seconds before printing next lines to console
    print('Loading cogs:')  # Start loading cogs
    await client.change_presence(activity=nextcord.Game(name='Updates for ModzBott')) # Show server count and /help command


# Loading bot cogs
initial_extensions = []  # Will add to array when running
for filename in os.listdir('./commands/default'):  # Checking the cogs folder
    if filename.endswith('.py'):  # Searching in the folder for files that end in .py
        initial_extensions.append('commands.default.' + filename[:-3])  # Loading them to the array for registration
for filename in os.listdir('./commands/moderation'):  # Checking the cogs folder
    if filename.endswith('.py'):  # Searching in the folder for files that end in .py
        initial_extensions.append('commands.moderation.' + filename[:-3])  # Loading them to the array for registration
for filename in os.listdir('./commands/utility'):  # Checking the cogs folder
    if filename.endswith('.py'):  # Searching in the folder for files that end in .py
        initial_extensions.append('commands.utility.' + filename[:-3])  # Loading them to the array for registration

if __name__ == '__main__':
    for extension in initial_extensions:  # If the cog is in the cog list then prepare
        client.load_extension(extension)  # Launching the cog

keep_alive()  # Runs the keep bot alive function in webserver.py
client.run(TOKEN)  # Run bot token found in private files
