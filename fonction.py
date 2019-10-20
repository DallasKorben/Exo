def parier():
    ''' Demander le montant du pari au joueur '''

    global pari
    pari = 0

    print('Combien de jetons vous voulez parier ? (Un entier SVP) ')

    # Boucle while pour demander le montant du pari
    while pari == 0:
        compo_pari = input()  # bet_comp est utiliser pour vérifier la réponse
        compo_pari = int(compo_pari)
        # On vérifie que la valeur demandée n'est pas supérieure au montant de jetons restants
        if compo_pari >= 1 and compo_pari <= jetons:
            pari = compo_pari
        else:
            print("Montant invalide, il ne vous reste que " + str(jetons) + " jetons")


def distribue_cartes():
    ''' Cette fonction distribue les cartes et mets en place un tour de jeu '''

    # Préparer toutes les variables globales
    global resultat, jouer, paquet, main_joueur, main_banque, jetons, pari

    # Crée le paquet
    paquet = Paquet()

    # Le mélanger
    paquet.mélanger()

    # Faire un pari
    parier()

    # Préparer les mains du joueur et de la banque
    main_joueur = Main()
    main_banque = Main()

    # Distribuer les premières cartes
    main_joueur.ajoute_carte(paquet.donne())
    main_joueur.ajoute_carte(paquet.donne())

    main_banque.ajoute_carte(paquet.donne())
    main_banque.ajoute_carte(paquet.donne())

    resultat = "(J)oue ou (P)asse? tapez J ou P : "
    if main_joueur.calc_val() == 21:
        resultat = "BLACK JACK ! 21 !" + rejouer_phrase
        jetons += 1.5 * pari
        jouer = False
        print("Total de jetons : " + str(jetons))

    if jouer == True:
        print('Je me couche, désolé')
        jetons -= pari


    # Mise en place pour avoir la main en cours de jeu
    jouer = True
    tour_de_jeu()
