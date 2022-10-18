from .option_types import OptionType

class OptionChoice:
    def __init__(self , name , value_type , value):
        if len(value) > 100:
            raise Exception("e")

        else:
            self.name = name
            self.value = value
            self.value_type = value_type


class Option:
    def __init__(self , option_type: int , name: str , description: str , required: bool , choices: list = None , min_value: int = None , max_value: int=None , min_length: int = None , max_length: int = None , autocomplete: bool = None):
        self.option_type = option_type
        self.name = name
        self.description = description
        self.required = required
        self.choices = choices
        self.min_value = min_value
        self.max_value = max_value
        self.min_length = min_length
        self.max_length = max_length
        self.autocomplete = autocomplete