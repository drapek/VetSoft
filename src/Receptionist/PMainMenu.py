from PyQt5.QtCore import QCoreApplication
from Receptionist.Vets import PVet


class PMainMenu:
    vMainMenu = None

    def __init__(self, v_main_menu):
        self.vMainMenu = v_main_menu

    def show_menu_window(self):
        self.vMainMenu.draw_main_menu(event_listener=self)

    def show_vets_clicked(self):
        PVet.show_vet_list_window()

    def close_app_clicked(self):
        QCoreApplication.instance().quit()
