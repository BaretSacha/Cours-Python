#coding: utf-8 

import datetime

class animal :
    """
        Cette classe est la classe mère, toutes les classes filles
        héritent des attributs de cette classe

    """

    def __init__(self, name, age, sexe):
        self.name = name
        self.age = age
        self.sexe = sexe

    def __str__(self):
        return "Un " + self.name + " âgé(e) de " + str(self.age) + "an(s) et c est un(e) " + self.sexe
class Farm :

    def __init__(self, name):
        self.name = name
        self.Farm_animals = [20]

    def __str__(self):

        out = "Nous avons dans cette ferme\n"
        print (out)
        out=""
        for my_key in self.Farm_animals:
            out += str(my_key)+"\n"
            out += "_____________________________________\n"

        return out


if __name__ == "__main__":

    Farm_list = []
    Farm_list.append(Farm("Première ferme"))
    Farm_list.append(Farm("Deuxième ferme"))
    Farm_list.append(Farm("Troisième ferme"))
    Farm_list[0].Farm_animals.append(animal("Mouton", 2, "mâle"))
    Farm_list[1].Farm_animals.append(animal("Mouton", 4, "femelle"))
    Farm_list[2].Farm_animals.append(animal("Mouton", 3, "femelle"))
    Farm_list[0].Farm_animals.append(animal("Mouton", 8, "mâle"))
    Farm_list[2].Farm_animals.append(animal("Mouton", 5, "femelle"))
    Farm_list[1].Farm_animals.append(animal("Poule", 10, "femelle"))
    Farm_list[0].Farm_animals.append(animal("Poule", 3, "mâle"))
    Farm_list[1].Farm_animals.append(animal("Poule", 1, "mâle"))
    Farm_list[2].Farm_animals.append(animal("Poule", 6, "femelle"))
    Farm_list[1].Farm_animals.append(animal("Poule", 47, "mâle"))
    Farm_list[0].Farm_animals.append(animal("Poule", 4, "femelle"))
    Farm_list[0].Farm_animals.append(animal("Poule", 4, "mâle"))
    Farm_list[1].Farm_animals.append(animal("Poule", 2, "femelle"))
    Farm_list[2].Farm_animals.append(animal("Vache", 6, "mâle"))
    Farm_list[2].Farm_animals.append(animal("Vache", 7, "femelle"))
    Farm_list[1].Farm_animals.append(animal("Vache", 8, "mâle"))

    requette = int(input("Vous sélectionnez quelle ferme ?\n"))
    print(Farm_list[requette])


    datetime_today = datetime.datetime.now()
    print(datetime_today)
    print(datetime_today.year)
    my_delta = datetime.timedelta(weeks = 2, days = 5, hours = 1, seconds = 33)
    print("my delta : " + str(my_delta))
    print("Time delta days : " + str(my_delta.days))
    new_date = datetime_today + my_delta
    print(new_date)
