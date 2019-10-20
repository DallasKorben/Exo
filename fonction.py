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
