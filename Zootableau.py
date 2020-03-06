# Cours-Python
Suivie du cours et des codes fait en cours


class animaux:

    def __init__(self, name, nombres , regime_alimentaire, Nombres_de_pattes, Quantite_de_nourriture):
        self.name = name
        self.nombres = nombres
        self.regime_alimentaire = regime_alimentaire
        self.Nombres_de_pattes = Nombres_de_pattes
        self.Quantite_de_nourriture = Quantite_de_nourriture

    def __str__(self):
        return "Cest animal est un " + self.name  + "\nIl y a  " + str(self.nombres) + " " + self.name + "\nCet animal est un " + self.regime_alimentaire + "\nCet animal a " + str(self.Nombres_de_pattes) +" " +  "pattes" "\n Cet animal mange " + str(self.Quantite_de_nourriture) +" " +  "grammes de nourritures."

class animaux_different:
    def __init__(self,name,nombres,regime_alimentaire,Nombres_de_pattes,Quantite_de_nourriture):
        self.name = name
        self.nombres = nombres
        self.regime_alimentaire = regime_alimentaire
        self.Nombres_de_pattes = Nombres_de_pattes
        self.Quantite_de_nourriture = Quantite_de_nourriture

    def __str__(self):
        return "Cest animal est un " + self.name  + "\nIl y a  " + str(self.nombres) ,  self.name + "\nCet animal est un " + self.regime_alimentaire + "\nCet animal a " + str(self.Nombres_de_pattes) + "pattes" "\n Cet animal mange " + str(self.Quantite_de_nourriture) + "grammes de nourritures."

serpent = animaux_different ('serpent',2,'Carnivore',0,200)
autruche = animaux_different ('autruche',4,'Omnivire',2,1000)


class mammifere(animaux):
    pass

humain = mammifere ('humain',2,'omnivore',2,600)
Lion = mammifere ('lion',1,'carnivore',1,3000)
mouton = mammifere ('mouton',5,'Végétarien',4,500)
chien = mammifere ('chien', 2, 'Omnivore', 4, 500)




class domestique(animaux) :
    pass

mouton = mammifere ('mouton',5,'Végétarien',4,500)
chien = mammifere ('chien', 2, 'Omnivore', 4, 500)
poule = domestique ('poule',8,'Omnivore',2,200000)



class animaux_marins(animaux) :
    pass

pieuvre = animaux_marins ('pieuvre',1,'Carnivore',0,200)




if __name__ == "__main__":

    print(humain)
    print(mouton)
    
