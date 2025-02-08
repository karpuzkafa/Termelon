#Copyright 2025 Hasan Agit Ünal




import os

def colorize(hex_color, text):
    """
    Print text in the specified color.
    
    Args:
        color (str): Hexadecimal color code (e.g., '#FF5733').
        text (str): The text to colorize.
    
    Example:
        colorize("00ee00", "example") will print this:
        \033[38;5;40mexample\033[0m
    """
    if os.name == 'nt' and not init:
        support = False
    else:
        support = os.environ.get('TERM', '') in ('xterm-256color', 'screen-256color')
    
    hex_color = hex_color.lstrip("#")
    r, g, b = (int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    color_code = 16 + (36 * (r // 51)) + (6 * (g // 51)) + (b // 51)
    colored_text = f"\033[38;5;{color_code}m{text}\033[0m"
    
    print(colored_text if support != False else text)


def coloredline(color):
    """
    Print a colored decorative line.

    Args:
        color (str): Hexadecimal color code (e.g., '#FF5733').
    """
    colorize(color, "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    