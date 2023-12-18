#!/usr/bin/env python3

# pour faire des tests
#file = open("petit-fichier")

# Vrai fichier
file = open("fichier")

# La somme des nombres trouvés
somme_total = 0

while True:    
    # On lit une ligne du fichier
    line = file.readline()
        
    # On valide que la ligne existe et non vide
    if line:   
        # Créer une liste vide pour récupérer tout les numéros de la ligne
        liste_nombres = []
        # On boucle sur chaque caractère de la ligne
        for char in line:
            
            # On valide que le caractère est un chiffre
            if char.isdigit():
                # On ajoute le chiffre à la liste
                liste_nombres.append(int(char))
        
        # On valide que la liste n'est pas vide
        if len(liste_nombres) >= 2:
            # On doit extraire dernier chiffre pour les deux situations
            # Soit si nous avons un nombre entre 10 et 99 OU 100 et +, ça revient au même
            premier_chiffre = liste_nombres[0]
            dernier_chiffre = liste_nombres[-1]
            somme_total = somme_total + (premier_chiffre * 10) + dernier_chiffre
        
        else:
            # Nous avons alors un nombre à un digit, donc on doit le multiplier
            seul_chiffre = liste_nombres[0]
            somme_total = somme_total + (seul_chiffre * 11)            
    else:
        break
    
file.close()
# On affiche la somme total
print("La somme total est de: ", somme_total)    
'''
La somme total est de:  55002
real    0m0,061s
user    0m0,041s
sys     0m0,020s
'''
# Fin du script
