from test_data.vetDTO_mock import get_mock_vets, get_mock_vet


class PVet:
    vVetList = None
    vVetEditForm = None

    def __init__(self, v_vet_list, v_vet_edit_form):
        self.vVetList = v_vet_list
        self.vVetEditForm = v_vet_edit_form

    # VVetList
    def show_vet_list_window(self):
        # TODO replace mock with proper model when it will be implemented!
        vets = get_mock_vets()
        self.vVetList.draw_vet_list_window(event_listener=self, vetDTO_list=vets)

    def close_vet_list_clicked(self):
        self.vVetList.close()

    # VVetEditForm
    def edit_vet_clicked(self, id):
        print("clicked", id)  # TODO fix it - it always get the last id - it is problem with lambda functions (solution is in the book)
        vetDTO = get_mock_vet()  # TODO replace mock with proper model when it will be implemented!
        self.vVetEditForm.show_form_window(event_listener=self, vetDTO=vetDTO)

    def save_vet_edit_form_clicked(self, vetDTO):
        print("debug")  # TODO debug only
        # TODO validate model. If good - close the window. If bad - show alert
        self.vVetEditForm.show_alert('Niepoprawne dane!')  # TODO print more specific information

    def close_vet_edit_form_clicked(self):
        self.vVetEditForm.close()


