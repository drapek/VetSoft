class VetDTO:
    id = 0
    first_name = ''
    last_name = ''
    tel_number = ''

    def __init__(self, vet_id, first_name, last_name, tel_number):
        self.id = vet_id
        self.first_name = first_name
        self.last_name = last_name
        self.tel_number = tel_number
