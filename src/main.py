import sys
from PyQt5.QtWidgets import QApplication, QWidget

from Receptionist.VMainMenu import VMainMenu
from Receptionist.PMainMenu import PMainMenu


def main():
    # TODO this is only scratch code - reformat it to proper modules
    # app, window = init_qt_env()
    app = QApplication(sys.argv)
    v_main_menu = VMainMenu()
    p_main_menu = PMainMenu(v_main_menu)
    p_main_menu.show_menu_window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
