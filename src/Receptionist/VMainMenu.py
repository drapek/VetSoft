from PyQt5.QtWidgets import QPushButton, QWidget, QLabel, QSizePolicy

from config.settings import APP_NAME


class VMainMenu(QWidget):

    def __init__(self):
        super().__init__()

    def draw_main_menu(self, event_listener):
        text_header = QLabel("Menu", self)
        text_header.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        text_header.setStyleSheet("QLabel {font-size: 30px;}")
        text_header.move(105, 0)

        btn_show_vets = QPushButton('Pokaż weterynarzy', self)
        btn_show_vets.clicked.connect(event_listener.show_vets_clicked)
        btn_show_vets.move(80, 50)

        btn_close = QPushButton('Zamknij', self)
        btn_close.clicked.connect(event_listener.close_app_clicked)
        btn_close.move(105, 100)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle(f"{APP_NAME} - Main menu")
        self.show()

