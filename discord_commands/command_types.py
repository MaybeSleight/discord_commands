from .errors import SlashCommandError

class Command:
    '''
    Base class for a command

    Attributes
    ----------
    `name`: str - Name of the command
    `description`: str - Description of the command
    `guilds`: list[int] - Guilds of the command
    '''

    def __init__(self , name: str , description: str , dm: bool , guilds: list = []):
        if len(guilds) > 0:
            self.guilds_ = guilds

        else:
            self.guilds_ = 'global'

        self.name_ = name
        self.description_ = description
        self.dm_ = dm

    @property
    def name(self):
        '''
        Name of the command
        '''

        return self.name_

    @property
    def description(self):
        '''
        Description of the command
        '''

        return self.description_

    @property
    def type(self):
        '''
        Type of the command
        '''

        if self.guilds_ != 'global':
            return 'private'

        else:
            return 'global'

    @property
    def guilds(self):
        '''
        Guilds of the server
        '''

        if self.type == 'private':
            return self.guilds_

        else:
            return []

    @property
    def is_available_in_dms(self):
        '''
        Tells if the command available in Direct Messages
        '''
        return self.dm_

class SlashCommand(Command):
    '''
    Represents a slash command

    Attributes
    ----------
    `name`: str - Name of the slash command
    `description`: str - Description of the slash command
    `options`: list[dict] - Options for the slash command
    `guilds`: list[int] - Guilds of this slash command
    `permissions`: list[str] - Permissions required for running this command
    '''
    def __init__(self , name: str , description: str , dm: bool , guilds: list , options: list):
        super().__init__(name=name , description=description , guilds=guilds , dm=dm)
        self.options_ = []

        if len(options) > 25:
            raise SlashCommandError("Slash command can only have a maximum of 25 options. {} were provided".format(len(options)))

        else:
            for opt in options:
                self.options_.append(opt)

        self.TYPE_ = 1

    @property
    def TYPE(self):
        '''
        Type of the command. Returns 1 for slash command
        '''
        return 1

    @property
    def options(self):
        '''
        Options of the command
        '''
        return self.options_

class UserCommand(Command):
    def __init__(self , name: str , description: str , dm: bool , guilds: list):
        super().__init__(name=name , description=description , guilds=guilds , dm=dm)
        self.TYPE_ = 2

    @property
    def TYPE(self):
        return self.TYPE_

class MessageCommand(Command):
    def __init__(self , name: str , description: str , dm: bool , guilds: list):
        super().__init__(name=name , description=description , guilds=guilds , dm=dm)
        self.TYPE_ = 3

    @property
    def TYPE(self):
        return self.TYPE_