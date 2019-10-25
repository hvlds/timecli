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
        self.underline = "\033[4m"

    def text_color(self, text, color, bold=False, underline=False) -> str:
        if color in self.colors.keys():
            new_text = self.colors[color]
            if bold:
                new_text += self.bold
            if underline:
                new_text += self.underline
            new_text += text + self.reset
        else:
            new_text = text
        return new_text
    
    def text_bold(self, text, underline=False) -> str:
        new_text = self.bold
        if underline:
            new_text += self.underline
        new_text += text + self.reset
        return new_text
    
    def get_colors(self) -> list:
        return self.colors.keys()