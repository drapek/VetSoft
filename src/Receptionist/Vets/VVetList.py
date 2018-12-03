from PyQt5.QtWidgets import QLabel, QSizePolicy, QPushButton, QDialog, QTableWidget, QTableWidgetItem, QGridLayout

from config.settings import APP_NAME, WINDOW_HEIGHT, WINDOW_WIDTH


class VVetList(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent=parent)

    def draw_vet_list_window(self, event_listener, vetDTO_list):
        self.setGeometry(300, 200, WINDOW_WIDTH, WINDOW_HEIGHT)
        self.setWindowTitle(f"{APP_NAME} - Lista weterynarzy")
        self.layout = QGridLayout()
        self.layout.setSpacing(10)

        text_header = QLabel("Lista weterynarzy", self)
        text_header.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        text_header.setStyleSheet("QLabel {font-size: 30px;}")
        text_header.move(0, 0)
        self.layout.addWidget(text_header)

        vets_table = QTableWidget(len(vetDTO_list), 5)
        vets_table.setHorizontalHeaderLabels(['id', 'imię', 'nazwisko', 'telefon', 'edytuj'])
        if vetDTO_list:
            for i, vet in enumerate(vetDTO_list):
                vets_table.setItem(i, 0, QTableWidgetItem(str(vet.id)))
                vets_table.setItem(i, 1, QTableWidgetItem(str(vet.first_name)))
                vets_table.setItem(i, 2, QTableWidgetItem(str(vet.last_name)))
                vets_table.setItem(i, 3, QTableWidgetItem(str(vet.tel_number)))
                edit_vet_button = QPushButton('Edytuj', self)
                edit_vet_button.clicked.connect(lambda x: event_listener.edit_vet_clicked(vet.id))
                vets_table.setCellWidget(i, 4, edit_vet_button)
        self.layout.addWidget(vets_table)

        btn_close = QPushButton('< Wróć', self)
        btn_close.clicked.connect(lambda: event_listener.close_vet_list_clicked())
        self.layout.addWidget(btn_close)

        self.setLayout(self.layout)
        self.show()
