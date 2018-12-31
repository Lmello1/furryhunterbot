import discord

badWords = ["owo", "uwu", "arf", "woof", "purr", "meow", "howl", "awoo", "aroo", "fursuit", "murrsuit", "bad dragon", "good boy", "good boye", "dawg", "merp", "sergal", "ad", "after dark", "knot", "lewd", "yiff", "canine", "equine", "femboi fox", "femboy fox", "chee", "paws", "maws", "belly", "belly rub", "arcanine", "FA", "furaffinity", "e621", "collar", "leash", "whine", "pet", "rp", "roleplay", "role play", "pup", "puppy", "cub", "pups", "puppies", "cubs", "top", "bottom", "switch", "roo", "waff", "scalie", "scalies", "folf", "werewolf", "housepets!", "housepets", "dobe", "daddy", "bulge", "k9", "k-9", "anthrocon", "mff", "flop"]

client = discord.Client()


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    server = message.server
    author = message.author

    if 'owo' in message.content.lower() or 'uwu' in message.content.lower():
        msg = 'STOP YOU DEGENERATE {0.mention}'.format(author)
        await client.send_message(message.channel, msg)
        try:
            role = discord.utils.get(server.roles, name="FURRY")
        except:
            await client.send_message(message.channel, "Couldn't find the role")
        try:
            role = discord.utils.get(server.roles, name="FURRY")
            await client.add_roles(message.author, role)
            await client.send_message(message.channel, "Successfully added role {0}".format(role.name))
        except discord.Forbidden:
            await client.send_message(message.channel, "I don't have perms to add roles.")

    if ('yiff') in message.content.lower():
        msg = 'NO YIFF ITS BAD FOR YOUR HEALTH {0.mention}'.format(author)
        await client.send_message(message.channel, msg)
        try:
            role = discord.utils.get(server.roles, name="FURRY")
        except:
            await client.send_message(message.channel, "Couldn't find the role")
        try:
            role = discord.utils.get(server.roles, name="FURRY")
            await client.add_roles(message.author, role)
            await client.send_message(message.channel, "Successfully added role {0}".format(role.name))
        except discord.Forbidden:
            await client.send_message(message.channel, "I don't have perms to add roles.")

    if (';-;') in message.content.lower():
        msg = 'NO JUST STOP YOU FURRY {0.mention}'.format(author)
        await client.send_message(message.channel, msg)
        try:
            role = discord.utils.get(server.roles, name="FURRY")
        except:
            await client.send_message(message.channel, "Couldn't find the role")
        try:
            role = discord.utils.get(server.roles, name="FURRY")
            await client.add_roles(message.author, role)
            await client.send_message(message.channel, "Successfully added role {0}".format(role.name))
        except discord.Forbidden:
            await client.send_message(message.channel, "I don't have perms to add roles.")

    if ('!remove') in message.content.lower():
        msg = 'Fine But no more goddam OWOing {0.mention}'.format(author)
        await client.send_message(message.channel, msg)
        try:
            role = discord.utils.get(server.roles, name="FURRY")
        except:
            await client.send_message(message.channel, "Couldn't find the role")
        try:
            role = discord.utils.get(server.roles, name="FURRY")
            await client.remove_roles(message.author, role)
            await client.send_message(message.channel, "Successfully removed {0}".format(role.name))
        except discord.Forbidden:
            await client.send_message(message.channel, "I don't have perms to remove roles.")

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('NTI5MTIyNjgzNTUyNzkyNTc5.Dwswqw.MFjdOZNaKQCE8MB-UwUPQVQKJ_k')
