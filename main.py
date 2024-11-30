import discord
from discord.ext import commands
from discord import app_commands


# Intents are required for receiving certain events
intents = discord.Intents.all()
intents.messages = True

bot_tokin = 'Enter Your Tokin Here'

# ALLOWED_SERVERS = [1307589213612539904, 1300450066728747020 , 1307586580998783016]  # Replace with your server IDs


# Create bot instance
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    try:
        synced = await bot.tree.sync()  # Syncs the slash commands globally
        print(f"Synced {len(synced)} command(s).")
    except Exception as e:
        print(f"Error syncing commands: {e}" ,   ephemeral=True)


@bot.event
async def on_message(msg: discord.Message):
    content = msg.content

    # Embed responses for $ commands
    if content == "$hello":
        embed = discord.Embed(
            title="👋 Hello!",
            description="Hi there! Welcome to **Tirox Admin Bot**. 🎮\nEnjoy your stay here!",
            color=discord.Color.blue()
        )
        embed.set_footer(text="Powered by Tirox Bot")
        await msg.reply(embed=embed)

    elif content == "$hii":
        embed = discord.Embed(
            title="👋 Hi!",
            description="Hello! How can I assist you today? 😊",
            color=discord.Color.green()
        )
        await msg.reply(embed=embed)

    elif content == "$about bot":
        embed = discord.Embed(
            title="🤖 About Bot",
            description="This bot is owned by **Tirox Community**",
            color=discord.Color.orange()
        )
        await msg.reply(embed=embed)

    # elif content == "$Mr.Dark":
    #     embed = discord.Embed(
    #         title="👑 Mr.Dark",
    #         description="He is the **Owner** and **Creator** of this bot and the Guadian Games community.",
    #         color=discord.Color.gold()
    #     )
    #     await msg.reply(embed=embed)

    # elif content == "$you":
    #     embed = discord.Embed(
    #         title="🙋‍♂️ About You",
    #         description="You are an awesome user or owner of this bot!",
    #         color=discord.Color.purple()
    #     )
    #     await msg.reply(embed=embed)

    elif content == "$owner_username":
        embed = discord.Embed(
            title="Owner's Username",
            description="📛 **Mr.Dark** - Discord ID: `01_lost_hunter`",
            color=discord.Color.gold()
        )
        await msg.reply(embed=embed)

    elif content == "$uses bot":
        embed = discord.Embed(
            title="📜 Bot Uses",
            description="This bot can:\n"
                        "🔹 Ban and kick members\n"
                        "🔹 Manage your server\n"
                        "🔹 Send announcements\n"
                        "🔹 And much more!",
            color=discord.Color.teal()
        )
        await msg.reply(embed=embed)

@bot.event
async def on_guild_channel_create(channel : discord.abc.GuildChannel):
    print("Channel Created")
    print(channel.name)


@bot.event
async def on_guild_channel_update(before: discord.abc.GuildChannel, after: discord.abc.GuildChannel):
    print("before Chnages")
    print(before.name)
    print("Channel After")
    print(after.name)

@bot.event
async def on_guild_channel_delete(channel : discord.abc.GuildChannel):
    print("Channel Deleted")
    print(channel.name)


@bot.event
async def on_guild_role_create(role : discord.Role):
    print("Role Created")
    print(role.name)
    print(role.color)


@bot.event
async def on_guild_role_update(before, after):
    print("Update")
    print(before.name)
    print(before.color)
    print("After")
    print(after.name)
    print(after.color)


@bot.event
async def on_guild_role_delete(role : discord.Role):
    print("Role deleted")
    print(role.name)
    print(role.color)


# Slash command example
@bot.tree.command(name='hello', description='Send a greeting message')
async def hello(interaction: discord.Interaction):
    embed = discord.Embed(
        title="👋 Hello!",
        description=f"Hi, {interaction.user.mention}! Welcome to Kirox Bot. 🎮",
        color=discord.Color.blue()
    )
    embed.set_footer(text="Thank you for using Kirox Bot!")
    await interaction.response.send_message(embed=embed)


# @bot.tree.command(name='owner_username', description="Show owner's information")
# async def owner_username(interaction: discord.Interaction):
#     embed = discord.Embed(
#         title="Owner Information",
#         description="👑 **Mr.Dark**\n📛 Discord ID: 01_lost_hunter",
#         color=discord.Color.gold()
#     )
#     embed.set_footer(text="Guadian Games Bot")
#     await interaction.response.send_message(embed=embed)



# @bot.tree.command(name='hiddencommands', description='Display hidden commands')
# async def hidden_commands(interaction: discord.Interaction):
#     embed = discord.Embed(
#         title="🔒 Hidden Commands",
#         description="Here are the hidden commands:\n"
#                     "⭐ `$hello`\n"
#                     "⭐ `$hii`\n"
#                     "⭐ `$about bot`\n"
#                     # "⭐ `$Mr.Dark`\n"
#                     # "⭐ `$you`\n"
#                     # "⭐ `$owner_username`\n"
#                     "⭐ `$uses bot`",
#         color=discord.Color.purple()
#     )
#     embed.set_footer(text="Happy Exploring!")
#     await interaction.response.send_message(embed=embed)




@bot.tree.command(name='help', description='Get help for using the bot')
async def help(interaction: discord.Interaction):
    embed = discord.Embed(
        title="🆘 Help Menu",
        description=f"Hi {interaction.user.mention}, how can I assist you?\n"
                    "📜 For a list of all commands, try `/about`.",
        color=discord.Color.green()
    )
    embed.set_footer(text="We're here to help!")
    await interaction.response.send_message(embed=embed, ephemeral=True)



@bot.tree.command(name='about', description='Learn more about the bot')
async def about(interaction: discord.Interaction):
    embed = discord.Embed(
        title="⚡ About Kirox Bot",
        description="This bot is made for manage your server, make announcements, and more! 🎮\n"
                    "Here are some of the commands you can try:\n"
                    "👉 `/hello`\n"
                    "👉 `/help`\n"
                    "👉 `/about`\n"
                    "👉 `/ban`\n"
                    "👉 `/ban`\n"
                    "👉 `/avatar`\n"
                    "👉 `/kick`\n"
                    "👉 `/announce`\n\n"
                    "😊 Don't forget to rate us with stars ⭐!",
        color=discord.Color.orange()
    )
    embed.set_footer(text="Bot created by Kirox Community")
    await interaction.response.send_message(embed=embed)




# Kick command
@bot.tree.command(name="kick", description="Kick a member from the server")
@app_commands.checks.has_permissions(kick_members=True)
async def kick(interaction: discord.Interaction, member: discord.Member, reason: str = "No reason provided"):
    try:
        await member.kick(reason=reason)
        embed = discord.Embed(
            title="✅ Member Kicked",
            description=f"{member.mention} has been kicked.\n**Reason:** {reason}",
            color=discord.Color.red()
        )
        embed.set_footer(text="Kick action performed successfully.")
        await interaction.response.send_message(embed=embed)
    except discord.Forbidden:
        await interaction.response.send_message("❌ I don't have permission to kick this user.", ephemeral=True)
    except discord.HTTPException as e:
        await interaction.response.send_message(f"❌ An error occurred: {e}", ephemeral=True)

# Error handling for insufficient permissions
@kick.error
async def kick_error(interaction: discord.Interaction, error):
    if isinstance(error, app_commands.errors.MissingPermissions):
        await interaction.response.send_message("❌ You do not have the required permissions to use this command." , ephemeral=True)
    else:
        await interaction.response.send_message(f"❌ An unknown error occurred: {error}" , ephemeral=True)


@bot.tree.command(name="ban", description="Ban a member from the server")
@app_commands.checks.has_permissions(ban_members=True)
async def ban(interaction: discord.Interaction, member: discord.Member, reason: str = "No reason provided"):
    try:
        await member.ban(reason=reason)
        embed = discord.Embed(
            title="✅ Member Banned",
            description=f"{member.mention} has been banned.\n**Reason:** {reason}",
            color=discord.Color.dark_red()
        )
        embed.set_footer(text="Ban action performed successfully.")
        await interaction.response.send_message(embed=embed)
    except discord.Forbidden:
        await interaction.response.send_message("❌ I don't have permission to ban this user.", ephemeral=True)
    except discord.HTTPException as e:
        await interaction.response.send_message(f"❌ An error occurred: {e}", ephemeral=True)

# Error handling for insufficient permissions
@ban.error
async def ban_error(interaction: discord.Interaction, error):
    if isinstance(error, app_commands.errors.MissingPermissions):
        await interaction.response.send_message("❌ You do not have the required permissions to use this command.",ephemeral=True)
    else:
        await interaction.response.send_message(f"❌ An unknown error occurred: {error}",ephemeral=True)



# Slash command for making announcements
@bot.tree.command(name="announce", description="Make an announcement in a specific channel")
@app_commands.checks.has_permissions(manage_messages=True)
async def announce(interaction: discord.Interaction, channel: discord.TextChannel, message: str):
    try:
        # Send the message to the selected channel
        announcement_embed = discord.Embed(
            title="📢 Announcement",
            description=message,
            color=discord.Color.blue()
        )
        announcement_embed.set_footer(text="Announcement by Kirox Bot")
        await channel.send(embed=announcement_embed)

        confirmation_embed = discord.Embed(
            title="✅ Announcement Sent",
            description=f"The announcement was successfully sent to {channel.mention}.",
            color=discord.Color.green()
        )
        await interaction.response.send_message(embed=confirmation_embed, ephemeral=True)
    except discord.Forbidden:
        error_embed = discord.Embed(
            title="❌ Permission Denied",
            description="I don't have permission to send messages in that channel.",
            color=discord.Color.red()
        )
        await interaction.response.send_message(embed=error_embed, ephemeral=True)
    except discord.HTTPException as e:
        error_embed = discord.Embed(
            title="❌ Error",
            description=f"An error occurred while sending the announcement: {e}",
            color=discord.Color.red()
        )
        await interaction.response.send_message(embed=error_embed, ephemeral=True)



# Unban command
@bot.tree.command(name="unban", description="Unban a user by their ID")
@app_commands.describe(user_id="The ID of the user to unban", reason="Reason for the unban (optional)")
async def unban(interaction: discord.Interaction, user_id: str, reason: str = "No reason provided"):
    try:
        # Fetch the banned users as a list
        banned_users = [entry async for entry in interaction.guild.bans()]  # Correct way to iterate async generators
        user = discord.Object(id=int(user_id))  # Create a user object with the ID

        # Check if the user is banned
        for ban_entry in banned_users:
            if ban_entry.user.id == int(user_id):
                await interaction.guild.unban(user, reason=reason)

                # Creating an embed to confirm the unban
                embed = discord.Embed(
                    title="User Unbanned",
                    description=f"User with ID `{user_id}` has been successfully unbanned.",
                    color=discord.Color.green()
                )
                embed.add_field(name="Reason", value=reason, inline=False)
                embed.set_footer(text=f"Unbanned by {interaction.user}")
                await interaction.response.send_message(embed=embed)
                return

        # If the user is not found in the banned list
        await interaction.response.send_message(
            f"User with ID `{user_id}` is not in the banned list.", ephemeral=True
        )

    except Exception as e:
        # Handle any errors that occur
        await interaction.response.send_message(
            f"An error occurred while trying to unban: {e}", ephemeral=True
        )




# Avatar command
@bot.tree.command(name="avatar", description="Fetch and display a user's avatar")
@app_commands.describe(user="The user whose avatar you want to see")
async def avatar(interaction: discord.Interaction, user: discord.Member = None):
    # If no user is specified, use the command author
    user = user or interaction.user

    # Get the avatar URL
    avatar_url = user.avatar.url if user.avatar else "No avatar available."

    # Create an embed with the avatar
    embed = discord.Embed(
        title=f"{user.name}'s Avatar",
        color=discord.Color.blue()
    )
    embed.set_image(url=avatar_url)
    embed.set_footer(text=f"Requested by {interaction.user}", icon_url=interaction.user.avatar.url)
    
    # Send the embed
    await interaction.response.send_message(embed=embed)

# Slash command for warning
@bot.tree.command(name="warn", description="Warn a user via DM")
@app_commands.describe(member="The user to warn", reason="The reason for the warning")
async def warn(interaction: discord.Interaction, member: discord.Member, reason: str = "No reason provided"):
    if not interaction.user.guild_permissions.manage_messages:
        embed = discord.Embed(
            title="❌ Permission Denied",
            description="You do not have permission to use this command.",
            color=discord.Color.red()
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)
        return

    # DM Embed to the warned user
    warn_embed = discord.Embed(
        title="⚠️ Warning",
        description=f"You have been warned in **{interaction.guild.name}**.",
        color=discord.Color.blue()
    )
    warn_embed.add_field(name="Reason", value=reason, inline=False)
    warn_embed.set_footer(text="Please adhere to the server rules to avoid further actions.")
    
    # Response Embed for admin
    admin_embed = discord.Embed(
        title="✅ User Warned",
        description=f"{member.mention} has been warned.",
        color=discord.Color.green()
    )
    admin_embed.add_field(name="Reason", value=reason, inline=False)
    
    try:
        # Send DM to the warned user
        await member.send(embed=warn_embed)
        # Acknowledge the command with an embed to the admin
        await interaction.response.send_message(embed=admin_embed)
    except discord.Forbidden:
        error_embed = discord.Embed(
            title="⚠️ Warning Failed",
            description=f"Could not send a DM to {member.mention}. They might have DMs disabled.",
            color=discord.Color.red()
        )
        await interaction.response.send_message(embed=error_embed, ephemeral=True)






# Run the bot
bot.run(bot_tokin)
