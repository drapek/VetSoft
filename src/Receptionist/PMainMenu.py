from PyQt5.QtCore import QCoreApplication
from Receptionist.Vets import main as receptionist_vet


class PMainMenu:
    vMainMenu = None

    def __init__(self, v_main_menu):
        self.vMainMenu = v_main_menu

    def show_menu_window(self):
        self.vMainMenu.draw_main_menu(event_listener=self)

    def show_vets_clicked(self):
        receptionist_vet.open_vet_list_window(parent_window=self.vMainMenu)

    def close_app_clicked(self):
        QCoreApplication.instance().quit()
