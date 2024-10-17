import colorama
import colorsys
import os
import json


themes_fldr = os.path.join(os.getcwd(), 'themes')

def load_theme(theme_name: str):
    for thm in os.listdir(themes_fldr):
        print(thm)
        if thm.lower == theme_name.lower:
            return 'yes'
        else:
            return 'hell naw'

