class Beautifier:
    @staticmethod
    def reset():
        return "\u001b[0m"

    @staticmethod
    def red(text="", bright=False):
        if not bright:
            return u"\u001b[31m" + text + "\u001b[0m"

        else:
            return u"\u001b[31;1m" + text + "\u001b[0m"

    @staticmethod
    def green(text="", bright=False):
        if not bright:
            return u"\u001b[32m" + text + "\u001b[0m"
        
        else:
            return u"\u001b[32;1m" + text + "\u001b[0m"

    @staticmethod
    def black(text="", bright=False):
        if not bright:
            return u"\u001b[30m" + text + "\u001b[0m"

        else:
            return u"\u001b[30;1m" + text + "\u001b[0m"

    @staticmethod
    def yellow(text="", bright=False):
        if not bright:
            return u"\u001b[33m" + text + "\u001b[0m"

        else:
            return u"\u001b[33;1m" + text + "\u001b[0m"

    @staticmethod
    def blue(text="", bright=False):
        if not bright:
            return u"\u001b[34m" + text + "\u001b[0m"

        else:
            return u"\u001b[34;1m" + text + "\u001b[0m"

    @staticmethod
    def magenta(text="", bright=False):
        if not bright:
            return u"\u001b[35m" + text + "\u001b[0m"

        else:
            return u"\u001b[35;1m" + text + "\u001b[0m"

    @staticmethod
    def cyan(text="", bright=False):
        if not bright:
            return u"\u001b[36m" + text + "\u001b[0m"

        else:
            return u"\u001b[36;1m" + text + "\u001b[0m"

    @staticmethod
    def white(text="", bright=False):
        if not bright:
            return u"\u001b[37m" + text + "\u001b[0m"

        else:
            return u"\u001b[37;1m" + text + "\u001b[0m"

    @staticmethod
    def always_red(text="", bright=False):
        if not bright:
            return u"\u001b[31m" + text

        else:
            return u"\u001b[31;1m" + text

    @staticmethod
    def always_green(text="", bright=False):
        if not bright:
            return u"\u001b[32m" + text

        else:
            return u"\u001b[32;1m" + text

    @staticmethod
    def always_black(text="", bright=False):
        if not bright:
            return u"\u001b[30m" + text

        else:
            return u"\u001b[30;1m" + text

    @staticmethod
    def always_yellow(text="", bright=False):
        if not bright:
            return u"\u001b[33m" + text

        else:
            return u"\u001b[33;1m" + text

    @staticmethod
    def always_blue(text="", bright=False):
        if not bright:
            return u"\u001b[34m" + text

        else:
            return u"\u001b[34;1m" + text

    @staticmethod
    def always_magenta(text="", bright=False):
        if not bright:
            return u"\u001b[35m" + text

        else:
            return u"\u001b[35;1m" + text

    @staticmethod
    def always_cyan(text="", bright=False):
        if not bright:
            return u"\u001b[36m" + text

        else:
            return u"\u001b[36;1m" + text

    @staticmethod
    def always_white(text="", bright=False):
        if not bright:
            return u"\u001b[37m" + text

        else:
            return u"\u001b[37;1m" + text

    @staticmethod
    def background_black(text="", bright=False):
        if not bright:
            return u"\u001b[40m" + text + "\u001b[0m"

        else:
            return u"\u001b[40;1m" + text + "\u001b[0m"

    @staticmethod
    def background_red(text="", bright=False):
        if not bright:
            return u"\u001b[41m" + text + "\u001b[0m"

        else:
            return u"\u001b[41;1m" + text + "\u001b[0m"

    @staticmethod
    def background_green(text="", bright=False):
        if not bright:
            return u"\u001b[42m" + text + "\u001b[0m"

        else:
            return u"\u001b[42;1m" + text + "\u001b[0m"

    @staticmethod
    def background_yellow(text="", bright=False):
        if not bright:
            return u"\u001b[43m" + text + "\u001b[0m"

        else:
            return u"\u001b[43;1m" + text + "\u001b[0m"

    @staticmethod
    def background_blue(text="", bright=False):
        if not bright:
            return u"\u001b[44m" + text + "\u001b[0m"

        else:
            return u"\u001b[44;1m" + text + "\u001b[0m"

    @staticmethod
    def background_magenta(text="", bright=False):
        if not bright:
            return u"\u001b[45m" + text + "\u001b[0m"

        else:
            return u"\u001b[45;1m" + text + "\u001b[0m"

    @staticmethod
    def background_cyan(text="", bright=False):
        if not bright:
            return u"\u001b[46m" + text + "\u001b[0m"

        else:
            return u"\u001b[46;1m" + text + "\u001b[0m"

    @staticmethod
    def background_white(text="", bright=False):
        if not bright:
            return u"\u001b[47m" + text + "\u001b[0m"

        else:
            return u"\u001b[47;1m" + text + "\u001b[0m"

    @staticmethod
    def always_background_black(text="", bright=False):
        if not bright:
            return u"\u001b[40m" + text

        else:
            return u"\u001b[40;1m" + text

    @staticmethod
    def always_background_red(text="", bright=False):
        if not bright:
            return u"\u001b[41m" + text

        else:
            return u"\u001b[41;1m" + text

    @staticmethod
    def always_background_green(text="", bright=False):
        if not bright:
            return u"\u001b[42m" + text

        else:
            return u"\u001b[42;1m" + text

    @staticmethod
    def always_background_yellow(text="", bright=False):
        if not bright:
            return u"\u001b[43m" + text

        else:
            return u"\u001b[43;1m" + text

    @staticmethod
    def always_background_blue(text="", bright=False):
        if not bright:
            return u"\u001b[44m" + text

        else:
            return u"\u001b[44;1m" + text

    @staticmethod
    def always_background_magenta(text="", bright=False):
        if not bright:
            return u"\u001b[45m" + text

        else:
            return u"\u001b[45;1m" + text

    @staticmethod
    def always_background_cyan(text="", bright=False):
        if not bright:
            return u"\u001b[46m" + text

        else:
            return u"\u001b[46;1m" + text

    @staticmethod
    def always_background_white(text="", bright=False):
        if not bright:
            return u"\u001b[47m" + text

        else:
            return u"\u001b[47;1m" + text

    @staticmethod
    def bold(text="", always=False):
        if not always:
            return u"\u001b[1m" + text + "\u001b[0m"

        else:
            return u"\u001b[1m" + text

    @staticmethod
    def underline(text="", always=False):
        if not always:
            return u"\u001b[4m" + text + "\u001b[0m"

        else:
            return u"\u001b[4m" + text

    @staticmethod
    def reverse(text="", always=False):
        if not always:
            return u"\u001b[7m" + text + "\u001b[0m"

        else:
            return u"\u001b[7m" + text

    @staticmethod
    def conceal(text="", always=False):
        if not always:
            return u"\u001b[8m" + text + "\u001b[0m"

        else:
            return u"\u001b[8m" + text

    @staticmethod
    def reset_intensity():
        return u"\u001b[22m"

    @staticmethod
    def reset_foreground_color():
        return u"\u001b[39m"

    @staticmethod
    def reset_background_color():
        return u"\u001b[49m"