# ETREvivant   ---> Classe Parent
# Chat & Personne ---> classe enfant
# APPRENTISSAGE DE L'heritage

class Etrevivant:
    ESPECE_ETRE_VIVANT = "Etre vivant non identifié"
    def AficherInfoEtreVivant(self): #Fonction statique
        print("Info être vivant : " + self.ESPECE_ETRE_VIVANT)

class Chat(Etrevivant):
    ESPECE_ETRE_VIVANT = "Chat (Mammifère félin)"

class Personne(Etrevivant):
    ESPECE_ETRE_VIVANT = "Humain (Mammifère Homo sapiens)" # Variable de classe (1 pour toutes les personnes)

    def __init__(self, nom: str = "", age: int = 0):
        self.nom = nom #crée une variable d'instance : nom
        self.age = age
        if nom == "":
            self.DemanderNom()
        print("Constructeur personne " + self.nom)

    def SePresenter(self):
        # Bonjour, je m'appelle Jean, j'ai 30 ans
        # Je suis majeur
        info_personne = "Bonjour, je m'appelle " + self.nom
        if self.age != 0:
            info_personne += ", j'ai " + str(self.age) + "ans"

        print(info_personne)

        if self.age != 0: 
            if self.EstMajeur():
                print("Je suis majeur")
            else:
                print("Je suis mineur")
    def EstMajeur(self):
        return self.age >= 18
    
    def DemanderNom(self):
        self.nom = input("Nom de la personne : ")

class Etudiant(Personne):
    def __init__(self, nom: str, age: int, etudes: str):
        super().__init__(nom, age)
        self.etudes = etudes
    
    def SePresenter(self):
        super().SePresenter()
        print("Je suis etudiant en " + self.etudes)

# UTILISATION

liste_personne = [Personne("Jean", 30), 
                  Personne("Paul", 15), 
                  Personne("Titi", 20)]

#Personne.ESPECE_ETRE_VIVANT = "Mutant"

for personne in liste_personne:
    personne.SePresenter()
    personne.AficherInfoEtreVivant()
    print()

chat = Chat()
chat.AficherInfoEtreVivant()

Etrevivant = Etrevivant()
Etrevivant.AficherInfoEtreVivant()

etudiant = Etudiant("Marc", 22, "Ecole d'ingenieur informatique")
etudiant.SePresenter()
etudiant.AficherInfoEtreVivant()