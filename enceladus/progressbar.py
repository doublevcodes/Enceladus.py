import os

class ProgressBar:

    def __init__(self, max_width = os.get_terminal_size()[1]):
        super().__init__()