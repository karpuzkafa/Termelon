#Copyright 2025 Hasan Agit Ünal



import os

def rcolorize(hex_color, text):
    """
    -colorize returner-
    
    this function same with colorize but dont prints text,
    returns colored text
    
    useful for colorful one line print
    """
    if os.name == 'nt' and not init:
        support = False
    else:
        support = os.environ.get('TERM', '') in ('xterm-256color', 'screen-256color')
    
    hex_color = hex_color.lstrip("#")
    r, g, b = (int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    color_code = 16 + (36 * (r // 51)) + (6 * (g // 51)) + (b // 51)
    colored_text = f"\033[38;5;{color_code}m{text}\033[0m"
    
    return colored_text if support != False else text
    
def rcoloredline(color):
    """
    -colored line returner-
    
    this function same with colorize but dont prints text,
    returns colored text
    """
    return rcolorize(color, "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
