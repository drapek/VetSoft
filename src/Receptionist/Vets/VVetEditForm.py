from PyQt5.QtWidgets import QGridLayout, QLabel, QSizePolicy, QPushButton, QDialog, QLineEdit, QMessageBox

from config.settings import WINDOW_WIDTH, WINDOW_HEIGHT, APP_NAME


class VVetEditForm(QDialog):
    def __init__(self, parent):
        super().__init__(parent=parent)

    def show_form_window(self, event_listener, vetDTO):
        self.setGeometry(300, 200, 500, 300)
        self.setWindowTitle(f"{APP_NAME} - Edytuj weterynarza")
        self.layout = QGridLayout()
        self.layout.setSpacing(10)

        text_header = QLabel("Edycja weterynarza", self)
        text_header.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        text_header.setStyleSheet("QLabel {font-size: 30px;}")
        text_header.move(0, 0)
        self.layout.addWidget(text_header, 0, 0)

        self.layout.addWidget(QLabel('imię'), 1, 0)
        self.layout.addWidget(QLineEdit(vetDTO.first_name), 1, 1)

        self.layout.addWidget(QLabel('nazwisko'), 2, 0)
        self.layout.addWidget(QLineEdit(vetDTO.last_name), 2, 1)

        self.layout.addWidget(QLabel('telefon'), 3, 0)
        self.layout.addWidget(QLineEdit(vetDTO.tel_number), 3, 1)

        btn_close = QPushButton('< Wróć', self)
        btn_close.clicked.connect(lambda: event_listener.close_vet_edit_form_clicked())
        self.layout.addWidget(btn_close)

        btn_save = QPushButton('Zapisz', self)
        btn_save.clicked.connect(lambda: event_listener.save_vet_edit_form_clicked(vetDTO))
        self.layout.addWidget(btn_save)

        self.setLayout(self.layout)
        self.show()

    def show_alert(self, message):
        QMessageBox.about(self, "Niepoprawne dane weterynarza", message)
