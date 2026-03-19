from sign_up_app_logic.styles import FONT
import tkinter.font


def try_find_unique_fonts():
    raw_fonts = list(set(FONT.values()))

    if not raw_fonts:
        return ["Arial"]

    system_fonts = tkinter.font.families()

    valid_fonts = []
    for f in raw_fonts:
        if f in system_fonts:
            valid_fonts.append(f)

    if not valid_fonts:
        return ["Arial", "Courier New", "Verdana"]

    return sorted(valid_fonts)