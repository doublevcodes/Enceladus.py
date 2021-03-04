
class Colour:

    def __init__(self):
        self._RESET = '\033[0m'
        self._BOLD = '\033[01m'
        self._DISABLE = '\033[02m'
        self._UNDERLINE = '\033[04m'
        self._REVERSE = '\033[07m'
        self._STRIKETHROUGH = '\033[09m'
        self._INVISIBLE = '\033[08m'
        self._fg_colors = {
            'default': '\033[0m',
            'black': '\033[30m',
            'red': '\033[31m',
            'green': '\033[32m',
            'orange': '\033[33m',
            'blue': '\033[34m',
            'purple': '\033[35m',
            'cyan': '\033[36m',
            'lightgrey': '\033[37m',
            'darkgrey': '\033[90m',
            'lightred': '\033[91m',
            'lightgreen': '\033[92m',
            'yellow': '\033[93m',
            'lightblue': '\033[94m',
            'pink': '\033[95m',
            'lightcyan': '\033[96m'
        }
        self._bg_colours = {
            'default': '\033[0m',
            'black': '\033[40m',
            'red': '\033[41m',
            'green': '\033[42m',
            'orange': '\033[43m',
            'blue': '\033[44m',
            'purple': '\033[45m',
            'cyan': '\033[46m',
            'lightgrey': '\033[47m'
        }
        return

    def fancyprint(self, text, fg_colour = None, bg_colour = None, **modifiers):
        if fg_colour is None or bg_colour is None:
            if fg_colour is None:
                fg_colour = ''
            if bg_colour is None:
                bg_colour = ''
        else:
            if fg_colour not in self._fg_colors:
                raise NotImplementedError(f"This colour is not currently supported -> {fg_colour}")
                return
            elif bg_colour not in self._bg_colours:
                raise NotImplementedError(f"This colour is not currently supported -> {bg_colour}")
                return
            else:
                fg_colour = fg_colour.lower()
                bg_colour = bg_colour.lower()
        format_str = ''
        try:
            format_str += self._fg_colors[fg_colour]
        except KeyError:
            pass
        try:
            format_str += self._bg_colours[bg_colour]
        except KeyError:
            pass
        for modifier in modifiers:
            if modifier:
                format_str += self.__getattribute__(f'_{modifier.upper()}')
        format_str += f'{text}{self._RESET}'
        print(format_str)
        return

colour = Colour()