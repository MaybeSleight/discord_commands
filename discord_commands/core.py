import requests

from discord_commands.option import Option, OptionChoice

from .command_types import Command

def register(command: Command , application_id: int , token: str):
    '''
    Register a command
    '''

    if command.TYPE == 1:
        raw = {
            "name": command.name_,
            "type": 1,
            "description": command.description_,
            "options": []
        }

        for opt in command.options:
            opt_raw = {
                "name": opt.name,
                "description": opt.description,
                "type": opt.option_type,
                "required": opt.required,
                "choices": []
            }

            if opt.option_type == 3:
                opt_raw['min_length'] = opt.min_length
                opt_raw['max_length'] = opt.max_length

            elif opt.option_type == 4 or opt.option_type == 10:
                opt_raw['min_value'] = opt.min_value
                opt_raw['max_value'] = opt.max_value

            if not opt.choices is None:
                for choice in opt.choices:
                    opt_raw['choices'].append({
                        "name": choice.name,
                        "value": choice.value
                    })

            raw["options"].append(opt_raw)

    elif command.TYPE == 2 or command.TYPE == 3:
        raw = {
            "name": command.name_,
            "type": command.TYPE_
        }

    headers = {
        "Authorization": "Bot {}".format(token)
    }

    if command.type == 'private':
        URLs = []

        for guild in command.guilds_:
            URLs.append(f"https://discord.com/api/v10/applications/{application_id}/guilds/{guild}/commands")
    else:
        URLs = [f"https://discord.com/api/v10/applications/{application_id}/commands"]

    for url in URLs:
        print(raw)
        r = requests.post(url, headers=headers, json=raw)
        print(r.text)