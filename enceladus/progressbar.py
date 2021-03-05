import os

class ProgressBar:

    def __init__(self, max = os.get_terminal_size()[1]):
        super().__init__()