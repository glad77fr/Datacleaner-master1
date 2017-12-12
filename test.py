class Personne:
    """Classe définissant une personne caractérisée par :

    - son nom

    - son prénom

    - son âge

    - son lieu de résidence"""

    def __init__(self):
        """Constructeur de notre classe"""

        self.age = 33

        self.lieu_residence = "Paris"

toto = Personne()

print(toto.lieu_residence)

