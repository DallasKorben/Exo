class Carte:

    def __init__(self, couleur, hauteur):
        self.couleur = couleur
        self.hauteur = hauteur

    def __str__(self):
        return self.hauteur + " de " + self.couleur

    def affiche_couleur(self):
        return self.couleur

    def affiche_hauteur(self):
        return self.hauteur

    def tirer(self):
        print(self.hauteur + " de " + self.couleur)

class Main:

    def __init__(self):
        self.cartes = []
        self.valeur = 0
        # l'as peut valoir 1 ou 11, ce qui est pris en compte ici
        # AS étant un mot réservé Python, j'ai choisi d'utiliser petit
        self.petit = False

    def __str__(self):
        ''' Renvoie une chaine avec la composition de la main'''
        compo_main = ""

        # Meilleure façon de faire ceci ? Comprehension de liste ?
        for carte in self.cartes:
            nom_carte = carte.__str__()
            compo_main += " " + nom_carte

        return 'Contenu de la main %s' % compo_main

    def ajoute_carte(self, carte):
        ''' Ajoute une carte à la main'''
        self.cartes.append(carte)

        # Test pour les AS
        if carte.hauteur == 'As':
            self.petit = True
        self.valeur += valeur_carte[carte.hauteur]

    def calc_val(self):
        '''Calcule la valeur de la main, les AS valent 11 s'il ne font pas sauter la main'''
        if (self.petit == True and self.valeur < 12):
            return self.valeur + 10
        else:
            return self.valeur

    def tirer(self, caché):
        if caché == True and jouer == True:
            # On ne montre pas la première carte cachée
            première_carte = 1
        else:
            première_carte = 0
        for x in range(première_carte, len(self.cartes)):
            self.cartes[x].tirer()
