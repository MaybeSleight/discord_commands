# Discord Commands
A python library which makes editing application commands easier.

## Installation
You can install the project using [pip](https://pypi.org/) and [git](https://git-scm.com/).

```cmd
pip install requests

pip install git+https://github.com/MaybeSleight/discord-commands.git
```

## Examples

- Creating a global slash command

```py
import discord_commands as dc

TOKEN = "BOT TOKEN"
APPLICATION_ID = 1234 # .... replace 1234 with your application ID

option = dc.Option(
    option_type=dc.OptionType.STRING,
    name="animal",
    description="The type of animal",
    required=True,
    choices=[
        dc.OptionChoice("Dog" , dc.ValueType.STRING , "animal_dog"),
        dc.OptionChoice("Cat" , dc.ValueType.STRING , "animal_cat"),
        dc.OptionChoice("Penguin" , dc.ValueType.STRING , "animal_penguin")
    ]
)

slash = dc.SlashCommand(
    name="blep",
    description="Send a random adorable animal photo",
    dm=False,
    guilds=[],
    options=[option]
)

dc.register(slash , APPLICATION_ID , TOKEN)
```

- Creating a global user command
```py
import discord_commands as dc

TOKEN = "BOT TOKEN"
APPLICATION_ID = 1234 # .... Replace 1234 with your application ID

user = dc.UserCommand(
    name="Greet User",
    description="Greet the user!",
    guilds=[],
    dm=False
)

dc.register(user , APPLICATION_ID , TOKEN)
```

- Creating a global message command
```py
import discord_commands as dc

TOKEN = "BOT TOKEN"
APPLICATION_ID = 1234 # .... Replace 1234 with your application ID

user = dc.UserCommand(
    name="Delete Message",
    description="Delete the message",
    guilds=[],
    dm=False
)

dc.register(user , APPLICATION_ID , TOKEN)
```

## Package
```py
discord_commands.Command
discord_commands.SlashCommand
discord_commands.UserCommand
discord_commands.MessageCommand

discord_commands.Option
discord_commands.OptionChoice

discord_commands.OptionType
discord_commands.OptionType.COMMAND
discord_commands.OptionType.COMMAND_GROUP
discord_commands.OptionType.STRING
discord_commands.OptionType.INTEGER
discord_commands.OptionType.BOOLEAN
discord_commands.OptionType.USER
discord_commands.OptionType.CHANNEL
discord_commands.OptionType.ROLE
discord_commands.OptionType.MENTIONABLE
discord_commands.OptionType.NUMBER
discord_commands.OptionType.ATTACHMENT

discord_commands.ValueType.STRING
discord_commands.ValueType.INTEGER
discord_commands.ValueType.DOUBLE

discord_commands.regsiter()
```