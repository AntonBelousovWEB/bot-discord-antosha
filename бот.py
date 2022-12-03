import discord

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.role_message_id = 1048600764077064233# ID of the message that can be reacted to to add/remove a role.
        self.emoji_to_role = {
            discord.PartialEmoji(name='💚'): 0, # ID of the role
        }

    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent):
        """Gives a role based on a reaction emoji."""
        # Make sure that the message the user is reacting to is the one we care about.
        if payload.message_id != self.role_message_id:
            return

        guild = self.get_guild(payload.guild_id)
        if guild is None:
            # Check if we're still in the guild and it's cached.
            return

        try:
            role_id = self.emoji_to_role[payload.emoji]
        except KeyError:
            # If the emoji isn't the one we care about then exit as well.
            return

        role = guild.get_role(911327693247758336)
        if role is None:
            # Make sure the role still exists and is valid.
            return
        role1 = guild.get_role(901466978336800780)
        if role is None:
            # Make sure the role still exists and is valid.
            return
        role2 = guild.get_role(901465022407012362)
        if role is None:
            # Make sure the role still exists and is valid.
            return
        role3 = guild.get_role(901478986855624714)
        if role is None:
            # Make sure the role still exists and is valid.
            return
        role4 = guild.get_role(922463923226173460)
        if role is None:
            # Make sure the role still exists and is valid.
            return

        try:
            # Finally, add the role.
            await payload.member.add_roles(role)
        except discord.HTTPException:
            # If we want to do something in case of errors we'd do it here.
            pass
        try:
            # Finally, add the role.
            await payload.member.add_roles(role1)
        except discord.HTTPException:
            # If we want to do something in case of errors we'd do it here.
            pass
        try:
            # Finally, add the role.
            await payload.member.add_roles(role2)
        except discord.HTTPException:
            # If we want to do something in case of errors we'd do it here.
            pass
        try:
            # Finally, add the role.
            await payload.member.add_roles(role3)
        except discord.HTTPException:
            # If we want to do something in case of errors we'd do it here.
            pass
        try:
            # Finally, add the role.
            await payload.member.add_roles(role4)
        except discord.HTTPException:
            # If we want to do something in case of errors we'd do it here.
            pass

    async def on_raw_reaction_remove(self, payload: discord.RawReactionActionEvent):
        """Removes a role based on a reaction emoji."""
        # Make sure that the message the user is reacting to is the one we care about.
        if payload.message_id != self.role_message_id:
            return

        guild = self.get_guild(payload.guild_id)
        if guild is None:
            # Check if we're still in the guild and it's cached.
            return

        try:
            role_id = self.emoji_to_role[payload.emoji]
        except KeyError:
            # If the emoji isn't the one we care about then exit as well.
            return

        role = guild.get_role(911327693247758336)
        if role is None:
            # Make sure the role still exists and is valid.
            return
        role1 = guild.get_role(901466978336800780)
        if role is None:
            # Make sure the role still exists and is valid.
            return
        role2 = guild.get_role(901465022407012362)
        if role is None:
            # Make sure the role still exists and is valid.
            return
        role3 = guild.get_role(901478986855624714)
        if role is None:
            # Make sure the role still exists and is valid.
            return
        role4 = guild.get_role(922463923226173460)
        if role is None:
            # Make sure the role still exists and is valid.
            return

        # The payload for `on_raw_reaction_remove` does not provide `.member`
        # so we must get the member ourselves from the payload's `.user_id`.
        member = guild.get_member(payload.user_id)
        if member is None:
            # Make sure the member still exists and is valid.
            return

        try:
            # Finally, remove the role.
            await member.remove_roles(role)
        except discord.HTTPException:
            # If we want to do something in case of errors we'd do it here.
            pass
        try:
            # Finally, remove the role.
            await member.remove_roles(role1)
        except discord.HTTPException:
            # If we want to do something in case of errors we'd do it here.
            pass
        try:
            # Finally, remove the role.
            await member.remove_roles(role2)
        except discord.HTTPException:
            # If we want to do something in case of errors we'd do it here.
            pass
        try:
            # Finally, remove the role.
            await member.remove_roles(role3)
        except discord.HTTPException:
            # If we want to do something in case of errors we'd do it here.
            pass
        try:
            # Finally, remove the role.
            await member.remove_roles(role4)
        except discord.HTTPException:
            # If we want to do something in case of errors we'd do it here.
            pass

intents = discord.Intents.default()
intents.members = True

client = MyClient(intents=intents)
client.run('')
