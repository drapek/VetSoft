from test_data.vetDTO_mock import get_mock_vets


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
        print("hide my ass")  # TODO debug only - delete it later
        self.vVetList.close()

    # VVetEditForm
    def edit_vet_clicked(self):
        pass  # TODO implement it

    def save_vet_edit_form_clicked(self, VetDTO):
        pass  # TODO implement it

    def close_vet_edit_form_clicked(self):
        pass  # TODO implement it


