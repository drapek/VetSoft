import sys

from PyQt5.QtWidgets import QApplication

from Receptionist.PMainMenu import PMainMenu
from Receptionist.VMainMenu import VMainMenu


def main():
    app = QApplication(sys.argv)
    v_main_menu = VMainMenu()
    p_main_menu = PMainMenu(v_main_menu)
    p_main_menu.show_menu_window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
