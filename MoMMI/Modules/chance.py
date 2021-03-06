import random
from MoMMI.commands import command

@command("pick", r"(?:pick|choose)\s*\((.*?)\)")
async def pick_command(channel, match, message):
    choices = [x.strip() for x in match.group(1).split(",")]
    if len(choices) < 2:
        await channel.send("You need to provide at least 2 options.")
        return

    choice = random.choice(choices)
    await channel.send(f"**{choice}**")

@command("roll", r"(\d+)d(\d+)")
async def roll_command(channel, match, message):
    result = "Results: "
    count = int(match.group(1))
    if count > 100:
        await channel.send("Ok look dude. A minute or two after this dice command got implemented bobda ran a god damn 10000000000000000000000000000d10. Now because it has to ITERATE those dice and 10000000000000000000000000000 is a giant fucking number, that locked up MoMMI completely because no amount of asyncio is gonna save this madness. Thank god for SIGKILL. THEN I got pinged by Intigracy telling me MoMMI locked up. *sigh*")
        return
    for i in range(0, count):
        if i > 0:
            result += ", "
        result += str(random.randint(1, int(match.group(2))))
    await channel.send(result)
