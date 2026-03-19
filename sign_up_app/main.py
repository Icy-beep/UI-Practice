from sign_up_app_logic.app import App
from sign_up_app_logic.constants import *

def main():
    app = App(appearance=APPEARANCE_DARK)

    app.mainloop()


if __name__ == "__main__":
    main()