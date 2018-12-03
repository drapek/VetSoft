from Receptionist.Vets.VetDTO import VetDTO


def get_mock_vets():
    return [
        VetDTO(1, 'Janusz', 'Ryszkiewicz', '660023423'),
        VetDTO(2, 'Andrzej', 'Hrykon', '87323421'),
        VetDTO(3, 'Robert', 'Brzydki', '74293464'),
    ]


def get_mock_vet():
    return VetDTO(1, 'Janusz', 'Ryszkiewicz', '660023423')
