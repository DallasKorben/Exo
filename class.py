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
