import random
import asyncio
from pyrogram import filters
from BullyRobot import pbot as BullyRobot



"""
    |----╒════════════╕----|
          |  Kang with credits |
          |----- Coded by: ----|
          |@jehrilla_cockroach |
          |----(2078119261)----|
          |      on telegram   |
    |----╘════════════╛----|
"""

QUOTES_STRINGS = [
                   "I am gonna put some dirt in your eye!",
                   "Look at little Goblin Junior. Gonna cry?",
                   "I am really gonna enjoy this...",
                   "Take your hand off me. Now.", 
                   "Who am I? You sure you want to know?", 
                   "Sorry I'm late, it's a Jungle out there.", 
                   "I don't wanna fight you Flash.", 
                   "That's a cute outfit! Did your husband give it to you?",
                   "I'd love to shoot you some time.",
                   "I missed the part where that's my problem.",
                   "Stings, doesn't it?",
                   "Now dig on this.", 
                   "You're trash!",
                   "Something's different, I'll figure it out, stop lecturing me, please!", 
                   "I had to beat an old lady with a stick to get these cranberries.", 
                   "Thanks, hot legs!", 
                   "Go flock yourself, feather face!", 
                   "See ya, chump!",
                   "Good riddance!", 
                   "You want forgiveness? Get religion.",
                   "Fly!",
                   "How'd that get in there?",
                   "My back... Oh, my back!",
                   "Shazam!",
                   "Up up and away web!",
                   "Staff job. Double the money.",
                   "Got any with nuts in them? Go make me some!",
                   "Get me some milk.",
                   "He despised you. You were an embarassment to him.",
                   "You'll get you your rent when you fix this damn door!", 
                   "You should've thought of that earlier.",
                   "I never thought he'd really do that!",
                   "You got my name wrong!",
                   "This is something else!", 
                   "We always have a choice, you had a choice when you killed my Uncle.", 
                   "Work out, plenty of rest. You know, eat your green vegetables.",
                   "What about my Uncle? Did you give him a chance?! Did you?!",
                   "A hundred bucks? The ad said three thousand.",
                   "I can't see! there are cars in the way motherf*ker!",
                 ]

"""
    Hello kangers, 
    How are you all??
    So if you want to add more quotes add it between '', example 'Yes I'm kanging your codes', 
    I hope it's clear to you!

    So if you're really kanging this atleast don't remove this line it takes a lot of time to code things.
    Coded by : @Cyberxron on telegram...
"""

@BullyRobot.on_message(filters.command(["quote", "spider"]))
async def lel(bot, message):
    ran = random.choice(QUOTES_STRINGS)
    await bot.send_chat_action(message.chat.id, "typing")
    await asyncio.sleep(1.5)
    return await message.reply_text(text=ran)


