# Création de la def principale
def Conversion():

    # Définit le nombre à convertir
    Nombre = int(input('Choisissez un nombre'))

    # Tableau où sont rentrer les différents nombres (normal et romain)
    tab = [[1000, 'M'], [900, 'CM'], [500, 'D'], [400, 'CD'], [100, 'C'], [90, 'XC'], [50, 'L'], [40, 'XL'], [10, 'X'], [9, 'IX'], [5, 'V'], [4, 'IV'], [1, 'I']]

    # Création des variables
    NombreRomain = ''
    Cpt = 0

    # Boucle qui permet de convertir en nombre romain
    while Nombre > 0:
        while tab[Cpt][0] > Nombre:
            Cpt = Cpt + 1

        NombreRomain = NombreRomain + tab[Cpt][1]
        Nombre = Nombre - tab[Cpt][0]

    # Affichage du résultat final en nombre romain sur la console python
    print(NombreRomain)

# On appelle la def
Conversion()