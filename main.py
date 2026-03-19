from sign_up_app.app import App
from sign_up_app.constants import *

def main():
    app = App(appearance=APPEARANCE_DARK)

    app.mainloop()


if __name__ == "__main__":
    main()