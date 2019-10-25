class Color:
    def __init__(self):
        self.colors = {
            "black": "\u001b[30m",
            "red": "\u001b[31m",
            "green": "\u001b[32m",
            "yellow": "\u001b[33m",
            "blue": "\u001b[34m",
            "magenta": "\u001b[35m",
            "cyan": "\u001b[36m",
            "white": "\u001b[37m",
        }
        self.reset = "\u001b[0m"
        self.bold = "\033[1m"

    def text_color(self, text, color, bold=False) -> str:
        if color in self.colors.keys():
            if bold == False: 
                text = str(self.colors[color] + text + self.reset)
            else:
                text = str(self.colors[color] + self.bold + text + self.reset)
        return text
    
    def bold(self, text):
        return self.bold + text + self.reset
    
    def get_colors(self) -> list:
        return self.colors.keys()