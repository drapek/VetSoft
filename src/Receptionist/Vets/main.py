from .VVetEditForm import VVetEditForm
from .VVetList import VVetList
from .PVet import PVet


def open_vet_list_window(parent_window):
    v_vet_list = VVetList(parent=parent_window)
    v_vet_edit_form = VVetEditForm(parent=v_vet_list)
    p_vets = PVet(v_vet_list, v_vet_edit_form)
    p_vets.show_vet_list_window()
