import customtkinter as ctk
from tkinter import messagebox
from sign_up_app.sign_up_app_logic.constants import *
from sign_up_app.sign_up_app_logic.localization import *
from sign_up_app.sign_up_app_logic.styles import *
from sign_up_app.sign_up_app_logic.helpers import try_find_unique_fonts


class App(ctk.CTk):
    __window_size: str
    __appearance: str
    __lang: str


    def __init__(self, appearance: str, lang: str = EN, window_size: str = DEFAULT_WINDOW_SIZE):
        super().__init__()

        self.__config = TRANSLATIONS.get(lang, TRANSLATIONS[EN])

        self.__window_size = window_size
        self.__appearance = appearance
        self.__lang = lang

        self.font_var = ctk.StringVar(value=SOFT_FONT)
        self.theme_var = ctk.StringVar(value=APPEARANCE_DARK)
        self.title(self.__config[TITLE])
        self.geometry(window_size)
        ctk.set_appearance_mode(self.__appearance)

        self.__setup_ui()

    def __setup_ui(self):

        self.label_header = ctk.CTkLabel(self, text=self.__config[HEADER], font=HEADER_FONT)
        self.label_header.pack(**LABEL_PADDING)

        self.entry_name = ctk.CTkEntry(self, placeholder_text=self.__config[NAME_PH], width=ENTRY_NAME_WIDTH)
        self.entry_name.pack(**ENTRY_PADDING)

        self.entry_email = ctk.CTkEntry(self, placeholder_text=self.__config[EMAIL_PH], width=ENTRY_EMAIL_WIDTH)
        self.entry_email.pack(**ENTRY_PADDING)

        self.entry_age = ctk.CTkEntry(self, placeholder_text=self.__config[AGE_PH], width=ENTRY_AGE_WIDTH)
        self.entry_age.pack(**ENTRY_PADDING)

        self.btn_submit = ctk.CTkButton(self, text=self.__config[BTN_SEND], command=self.__validate, fg_color=SUBMIT_BUTTON_COLOR,
                                        hover_color=HOVER_COLOR)
        self.btn_submit.pack(pady=SUBMIT_PADDING)

        self.label_settings = ctk.CTkLabel(self, text=self.__config[SETTINGS], font=(SOFT_FONT, 12, "italic"))
        self.label_settings.pack(pady=(20, 0))

        unique_fonts = try_find_unique_fonts()
        self.font_menu = ctk.CTkOptionMenu(
            self,
            values=unique_fonts,
            variable=self.font_var,
            command=self.__update_styles
        )
        self.font_menu.pack(pady=10)

        self.theme_switch = ctk.CTkSwitch(
            self,
            text=self.__config[DARK_MODE],
            command=self.__change_theme,
            variable=self.theme_var,
            onvalue=APPEARANCE_DARK,
            offvalue=APPEARANCE_LIGHT
        )
        self.theme_switch.pack(pady=10)

        self.lang_var = ctk.StringVar(value=EN if self.__lang == EN else RU)
        self.lang_menu = ctk.CTkOptionMenu(
            self,
            values=[EN, RU],
            variable=self.lang_var,
            command=self.__update_language
        )
        self.lang_menu.pack(pady=10)

    def __update_styles(self, selected_font):
        new_font = (selected_font, 14)
        header_font = (selected_font, 20, "bold")

        self.label_header.configure(font=header_font)
        self.entry_name.configure(font=new_font)
        self.entry_email.configure(font=new_font)
        self.entry_age.configure(font=new_font)
        self.btn_submit.configure(font=(selected_font, 13, "bold"))

    def __update_language(self, selected_lang_name):
        lang_map = {EN: EN, RU: RU}
        new_lang_code = lang_map.get(selected_lang_name, EN)

        self.__lang = new_lang_code
        self.__config = TRANSLATIONS.get(new_lang_code, TRANSLATIONS[EN])

        self.title(self.__config[TITLE])
        self.label_header.configure(text=self.__config[HEADER])
        self.label_settings.configure(text=self.__config[SETTINGS])
        self.entry_name.configure(placeholder_text=self.__config[NAME_PH])
        self.entry_email.configure(placeholder_text=self.__config[EMAIL_PH])
        self.entry_age.configure(placeholder_text=self.__config[AGE_PH])
        self.btn_submit.configure(text=self.__config[BTN_SEND])
        self.theme_switch.configure(text=self.__config[DARK_MODE])


    def __change_theme(self):
        ctk.set_appearance_mode(self.theme_var.get())

    def __validate(self):
        name = self.entry_name.get().strip()
        email = self.entry_email.get().strip()
        age = self.entry_age.get().strip()

        if not name or not email or not age:
            messagebox.showerror(self.__config[ERROR], self.__config[ERR_EMPTY])
        elif COMM_AT not in email:
            messagebox.showerror(self.__config[ERROR], self.__config[ERR_EMAIL])
        elif not age.isdigit() or int(age) <= 0:
            messagebox.showerror(self.__config[ERROR], self.__config[ERR_AGE])
        else:
            messagebox.showinfo(self.__config[SUCCESS], f"{self.__config[WELCOME]}, {name}!\n{self.__config[SUCCESS]}")
            self.__clear_form()

    def __clear_form(self):
        self.entry_name.delete(0, 'end')
        self.entry_email.delete(0, 'end')
        self.entry_age.delete(0, 'end')

