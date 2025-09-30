# Écrivez une fonction qui prend un entier comme paramètre et affiche « Vous avez perdu ! »
# si le paramètre est supérieur ou égal à 12.
import random
# charger une liste.txt dans une fonction 
def charger_listealéatoire():
    try:
        with open('mot.txt', 'r') as fichier:
            
            contenu = fichier.read().strip()
            # separer chaque mot avec le retour à la ligne``
            listemot=contenu.splitlines()
        
        print("mot chargé.",listemot)
        return listemot

        
    except FileNotFoundError:
        print("Aucune sauvegarde trouvée.")
        return None
score=0
def perdu():
    set_items2 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}  # bibliotheque de données on peut pas manipuler les index 
    print("print bibliotheque", set_items2)
    set_items2 = list(set_items2)  # conversion en liste de setitem2 pour pouvoir manipuler les index
    print("print liste convertie", set_items2)
    randomnumber = random.randint(set_items2[0], set_items2[-1])
    print("nombre aléatoire liste", randomnumber)
    print("element un liste", set_items2[0])
    print("element dernier liste", set_items2[-1])
    print("ramdom element de la liste", random.randint(set_items2[0], set_items2[-1]))
    if randomnumber >= 12:
        print("vous avez perdu!")

# Données de mots
set_item3=charger_listealéatoire()
# set_item3 = {
#     "AAH","AAHED","AAHING","AAHS","AAL","AALII","AALIIS","AALS","AARDVARK","AARDVARKS",
#     "AARDWOLF","AARDWOLVES","AARGH","AARRGH","AARRGHH","AARTI","AARTIS","AAS","AASVOGEL",
#     "AASVOGELS","AB","ABA","ABAC","ABACA","ABACAS"
# }
# set_item3 = list(set_item3)
# si la lettre est dans le mot qu'on veut trouver --> on la place dans le mot que l'on contruit sinon on donne une pénalité. 
compteurpenalité = 0

def penalite(unelementchaine, chr):  # le mot un element chaine est vu comme une liste et chr va donc boucler sur chaque lettre automatiquement. 
    global compteurpenalité  # pour recuperer int 0 ?????
    if not chr in unelementchaine:
        compteurpenalité = compteurpenalité + 1
        print("penalité de :", compteurpenalité)

def pendu():
    global compteurpenalité #sert à utiliser compteur de penalité ici 
    print("liste complète", set_item3)
    unelementchaine = random.choice(set_item3)  # selectionne un element au pif de la liste
    print("un element de la chaine aléatoire", unelementchaine)
    n = len(unelementchaine)
    print("taille d'un mot", n)
    chaine_cachee = "_" * n  # convertir en chaine de caractère (qui est deja une liste automatique) composé de _

    while "_" in chaine_cachee and compteurpenalité < 12:
    
    # A METTRE DANS LA BOUCLE DE JEU
        lettresaisie = input("saisis une lettre : ").strip().upper() #convertit toutes les lettres saisies en maj -> correspond à la liste mot.txt en maj
        if lettresaisie in unelementchaine:
            print("lettre saisi est dans le mot ", lettresaisie)
            index = 0
            print("la chaine cachée est:", chaine_cachee)
            for chr in unelementchaine:
                if chr == lettresaisie:  # si chr dans unelementchaine ( si un chr dans la liste str chaine est le m^me que la lettre saisie)
                # [star:stop:step] res= _arrêtes toi à cet index+ajoutelalettresaisie+ le reste de la chaine cachée
                # dans listecachée je souhaite remplacer le _ par la bonne lettre saisie
                    chaine_cachee = chaine_cachee[:index] + lettresaisie + chaine_cachee[index+1:]
                index = index + 1  # je passe à la lettre suivante, -1+1 =0 je prends l'index 0 au tout debut         
            print("chaine cachée remplacée : ", chaine_cachee)
        else:
        # on utilise ta fonction de pénalité si la lettre n'est pas dans le mot
         penalite(unelementchaine, lettresaisie)
        # affichage du mot caché séparé par des espaces (plus lisible)
        print(" ".join(chaine_cachee))

    if "_" not in chaine_cachee:
        print("bravo, tu as trouvé le mot :", unelementchaine)
        global score
        score=score+1
        print("ton score actuel est de", score)
   
    else: print("vous avez perdu ! Le mot était :", unelementchaine)
    print("ton score reste à",score)


def sauvegarder_progression():
    global score
    with open('sauvegarde.txt', 'w') as fichier:
        fichier.write(f'{score}\n')
    print("Progression sauvegardée.")
 
def charger_progression():
    try:
        with open('sauvegarde.txt', 'r') as fichier:
            
            score = int(fichier.readline().strip())
            
        print("Progression chargée.")
        return score
    except FileNotFoundError:
        print("Aucune sauvegarde trouvée.")
        return None
 
# Exemple d'utilisation
sauvegarder_progression()
score= charger_progression()
print("Score: "+str(score))

def jeu():
    global compteurpenalité
    """Lance une partie de pendu, puis propose de rejouer."""
    while True: #boucle infinie 
        #1) nouvelle manche compteur pénalité à zéro
        compteurpenalité=0
        # 2) une partie (pendu partage le score)
        pendu()
#3) si 12 penalité défaite: 
        if compteurpenalité >= 12:
            print("Vous avez perdu, vie terminée!")

        # demander si on rejoue dans tous les cas, strip enleve les espaces vides, lower en minuscule evite la casse
        reponse = input("Rejouer ? (o/n) : ").strip().lower()
        sauvegarder_progression() #pour sauvegarder le score des anciennes manches 
        if reponse not in ("o", "oui", "y", "yes"): #si la chaine de charactere saisie par l'utilisateur n'est pas o oui y yes on arrete le jeu
            print("Fin du jeu. Merci d'avoir joué !")
            break #force à sortir 
        
jeu() #lance le mode rejouer

 
# penalite("ASH", "B")  # test penalité 
# penalite("ASH", "C")
# penalite("ASH", "A")
