# Marylou Fauchard (20218608)     et       Sara Haddad (20208373)

###############################################################################
##########                          HTML                             ##########
###############################################################################

template = """
<html>
<link rel="preload" as="image" href="adresse de l'image">
<style>
table#jeu {
    border-spacing: 10px;
    border-collapse: separate;
    display: inline-block;
}

table#jeu td {
    background-color: #d0d0d0;
    border:1px solid #008CBA;
    width: 100px;
    height: 120px;
    background-position: center;
    background-size: cover;
}

#moyen{
    display:none
}

#difficile{
    display:none
}

.menu-element {
  margin: 10px;
  border:1px solid #008CBA;
  width: 100%;
}

.level-button {
  padding: 15px 30px;
  background-color: #008CBA;
  opacity: 0.7;
  border: none;
  color: white;
  text-align: center;
  font-size: 16px;
}

#score-box {
  padding: 5px 5px;
  text-align: center;
}

#score-text {
  font-family: OCR A Std, monospace;
}

.score-title {
  font-weight: bold;
}

.chronometre{
  margin: 10px;
  border:5px solid #800020;
  width: 100%;
  padding: 15px 20px;
  text-align: center;
  font-size: 18px;
  font-family: times new roman;
  background-color: #DCDCDC
}

@keyframes changeColors {
   from {color: #800020}
   to {color: black}
}

.texte-meilleur {
  font-size: small;
}

.active-level-button {
  opacity: 1 !important;
}

.menu {
  display: inline-block;
  width: 150px;
}
</style>
<div>
  <table id="jeu">
  <tbody id="niveau">
    <tr>
      <td id="carte0" onclick=revelerCase(0)></td>
      <td id="carte1" onclick=revelerCase(1)></td>
      <td id="carte2" onclick=revelerCase(2)></td>
      <td id="carte3" onclick=revelerCase(3)></td>
    </tr>
    <tr>
      <td id="carte4" onclick=revelerCase(4)></td>
      <td id="carte5" onclick=revelerCase(5)></td>
      <td id="carte6" onclick=revelerCase(6)></td>
      <td id="carte7" onclick=revelerCase(7)></td>
    </tr>
    <tr>
      <td id="carte8" onclick=revelerCase(8)></td>
      <td id="carte9" onclick=revelerCase(9)></td>
      <td id="carte10" onclick=revelerCase(10)></td>
      <td id="carte11" onclick=revelerCase(11)></td>
    </tr>
    <tr id="moyen">
      <td id="carte12" onclick=revelerCase(12)></td>
      <td id="carte13" onclick=revelerCase(13)></td>
      <td id="carte14" onclick=revelerCase(14)></td>
      <td id="carte15" onclick=revelerCase(15)></td>
   </tr>
   <tr id="difficile">
      <td id="carte16" onclick=revelerCase(16)></td>
      <td id="carte17" onclick=revelerCase(17)></td>
      <td id="carte18" onclick=revelerCase(18)></td>
      <td id="carte19" onclick=revelerCase(19)></td>
   </tr>
  </table></tbody>
</div>

  <div class="menu">
    <div id="score-box" class="menu-element">
      <div class="score-title">SCORE</div>
      <div id="score-text">100</div>
    </div>
    <div id="bouton"
    class="chronometre">
      <b>Chronomètre</b><br>
      <div onanimationiteration="countdown()" id="secondes">60</div>
    </div>
    <button id="niveauFacile" onclick="interrompre(1)" \
    class="level-button menu-element active-level-button">
      <b>Facile</b><br>
      <div class="texte-meilleur1">Meilleur: -</div>
    </button>
    <br>
    <button id="niveauMoyen" onclick="interrompre(2)" \
    class="level-button menu-element">
      <b>Moyen</b>
      <br>
      <div class="texte-meilleur2">Meilleur: -</div>
    </button>
    <br>
    <button id="niveauDifficile" onclick="interrompre(3)" \
    class="level-button menu-element">
      <b>Difficile</b>
      <br>
      <div class="texte-meilleur3">Meilleur: -</div>
    </button>
  </div>
</div>
</html>
"""


liensImages=["https://upload.wikimedia.org/wikipedia/commons/thumb/b/bb/\
Kittyply_edit1.jpg/320px-Kittyply_edit1.jpg",
"https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Felis_silvestris_\
catus_lying_on_rice_straw.jpg/320px-Felis_silvestris_catus_lying_on_rice_straw\
.jpg",
"https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Domestic_Cat_Face_\
Shot.jpg/320px-Domestic_Cat_Face_Shot.jpg",
"https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/Gato_enervado_pola_\
presencia_dun_can.jpg/308px-Gato_enervado_pola_presencia_dun_can.jpg",
"https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Felis_catus-cat_on\
_snow.jpg/320px-Felis_catus-cat_on_snow.jpg",
"https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/Feral_cat_Virginia_\
crop.jpg/206px-Feral_cat_Virginia_crop.jpg",
"https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/Black_Cat_\
%287983739954%29.jpg/320px-Black_Cat_%287983739954%29.jpg",
"https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Roo_Female_Somali_\
in_Cat_Caf%C3%A9_Tokyo.jpg/160px-Roo_Female_Somali_in_Cat_Caf%C3%A9_Tokyo.jpg",
"https://upload.wikimedia.org/wikipedia/commons/6/6e/Longhairedmunchkin.jpg",
"https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Niobe050905-Siamese\
_Cat.jpeg/179px-Niobe050905-Siamese_Cat.jpeg",
"https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/Charcoal_Bengal.jpg\
/320px-Charcoal_Bengal.jpg",
"https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Paintedcats_Red_\
Star_standing.jpg/187px-Paintedcats_Red_Star_standing.jpg",
"https://upload.wikimedia.org/wikipedia/commons/thumb/1/13/ChausieBGT.jpg/\
221px-ChausieBGT.jpg",
"https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Savannah_Cat_\
portrait.jpg/160px-Savannah_Cat_portrait.jpg",
"https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Plume_the_Cat.JPG/\
320px-Plume_the_Cat.JPG",
"https://upload.wikimedia.org/wikipedia/commons/e/e9/Persian_sand_CAT.jpg",
"https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Detalhe_nariz_Osk.\
jpg/180px-Detalhe_nariz_Osk.jpg",
"https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/Siam_blue_point.jpg\
/263px-Siam_blue_point.jpg",
"https://upload.wikimedia.org/wikipedia/commons/thumb/0/0e/Felis_silvestris_\
silvestris.jpg/208px-Felis_silvestris_silvestris.jpg",
"https://upload.wikimedia.org/wikipedia/commons/f/f7/Prionailurus_viverrinus_\
01.jpg"]




###############################################################################
##########                     INITIALISATION                        ##########
###############################################################################


grille = None
import random
import functools
document.querySelector("#main").innerHTML = template


tableau = []                  # on choisira les images a utiliser
urlsReveles = []              # mettre l'url de l'image sur laquelle on appuie
casesSelectionnees = []       # on ajoutera l'indexe de la case appuyee
casesDevinees=[]              # on ajoutera l'url des cases identiques
casesAppuyees = []            # on ajoute les indexes des cases appuyees
indexReveles=[]               # on ajoutera l'indexe des cases identiques

clics = False                 # le décompte ne commence pas tout de suite
niveau = 1                    # on commence le jeu au niveau facile

###############################################################################
##########               FONCTIONS COMPLÉMENTAIRES                  ###########
###############################################################################

#On crée le tableau des images qui seront assignées plus tard à chaque case de
#la grille selon le niveau choisi
def choisirImages(niveau):
    total = []
    tab = []
    possibilites = liensImages.copy()  # tous les liens des différentes photos
    
    for _ in range (0,4+2*niveau):     # deux fois moins de photos que de cases
        index = int(random.random()*len(possibilites))  # nombre aléatoire
        tab.append(possibilites[index])                 # lien du nombre
        possibilites.pop(index)                         # pas deux même images
        
    total = melanger(tab+tab.copy())   # les images et leur paire sont à des 
    return total                       # positions aléatoire

# cette fonction prend une liste et la retourne dans un ordre aléatoire
def melanger(tab):
    for i in range(len(tab)):  
        index=int(random.random()*len(tab)) # nouvelle position pour un index
        temp=tab[i]                 # échange des éléments des indexes i et j
        tab[i]=tab[index]
        tab[index]=temp
    return tab


# on met a jour le niveau actuel de jeu      
def mettreAJourNiveau(tableau):
    if len(tableau)==12 or len(tableau)==0: # niveau facile ou premiere 
                                            # fois qu'on joue
        niveau=1
    elif len(tableau)==16:       # on est au niveau moyen
        niveau=2
    else:                        # niveau difficile
        niveau=3
    return niveau

###############################################################################
##########                    MISE À JOUR DU CONTENU                 ##########
###############################################################################

# remet la grille de départ au niveau choisit
def interrompre(niveau):
    reinitialiser()         # revient à la grille vide du niveau
    init(niveau)            # on prépare la partie

# permet de changer le style d'un element du html
def mettreAJourStyle(identifiant,attribut):
    document.querySelector(identifiant).setAttribute("style",attribut)

# permet de retirer le style appliqué a un element du html
def retirerStyle(id1,id2):
    document.querySelector(id1).removeAttribute("style")
    document.querySelector(id2).removeAttribute("style")

#Cette fonction se charge du changement de la taille de la grille selon le 
#niveau de difficulté 
def niveauJeu(niveau):
    global grille
    #niveau facile
    if niveau == 1:
        mettreAJourStyle("#moyen","display:none")
        mettreAJourStyle("#difficile","display:none")
        mettreAJourStyle("#niveauFacile","opacity: 1")
        retirerStyle("#niveauMoyen","#niveauDifficile")
    #niveau moyen
    elif niveau == 2:               #ajouter une rangée de cases
        mettreAJourStyle("#moyen","display:table-row")
        mettreAJourStyle("#difficile","display:none")
        mettreAJourStyle("#niveauMoyen","opacity: 1")
        retirerStyle("#niveauFacile","#niveauDifficile")
        mettreAJourStyle(".active-level-button","opacity:0.75 !important")
    #niveau difficile
    elif niveau == 3:               #ajouter deux rangées de cases
        mettreAJourStyle("#moyen","display:table-row")
        mettreAJourStyle("#difficile","display:table-row")
        mettreAJourStyle("#niveauDifficile","opacity: 1")
        retirerStyle("#niveauMoyen","#niveauFacile")
        mettreAJourStyle(".active-level-button","opacity:0.75 !important")


#Reveler la photo generée aleatoirement parmis le tableau d'urls choisis
#selon le niveau du jeu
def revelerCase(i):
    global casesSelectionnees; global etat
    global casesAppuyees ; global casesDevinees; global clics
    image = tableau[i]             # retourner image correspondante à la case
    
    if image not in casesDevinees: # carte n'est pas deja retournée
        case = document.querySelector("#" +"carte"+ str(i))  
        case.setAttribute("style","background-image: " + "url("+image + ");" +
                      " background-position: center; background-size: cover;")
        if clics == False:
            countdown()
            
        if len(indexReveles)==0:  # première des deux cases retournées
            urlsReveles.append(image)   
            casesSelectionnees.append(i)
            indexReveles.append(i)
            updateScore(i)
                          # pas la même case que la précédente
        if len(indexReveles)==1 and i!=indexReveles[0]: # deuxième case
            urlsReveles.append(image)   
            casesSelectionnees.append(i)
            indexReveles.append(i)
            updateScore(i)
    else:                        # ignorer le clic sur une case deja retournee
        pass         
          
# cette fonction s'occuppe d'actualiser le score à chaque étape
def updateScore(i):
    global casesSelectionnees; global urlsReveles
    global casesDevinees; global casesAppuyees ; global indexReveles
    
    if len(casesSelectionnees) != 1:          # seulement une case de retournée
        if urlsReveles[0]  == urlsReveles[1] \
        and casesSelectionnees[0]!=casesSelectionnees[1] and \
        casesSelectionnees[0]!=casesSelectionnees[1]:  
            # les deux urls sont pareils et ce n'est pas la meme case
            
            casesDevinees.append(urlsReveles[0]) # on les a trouvée
            
            victoire()               # vérifie si c'était la dernière paire
            urlsReveles = []         # réinitialise les listes nécessaires
            casesSelectionnees = []
            indexReveles=[]
            
        else:              # il y a deux cartes différentes de retournées
            
                           # on a retournée une cartes déjà vue sans la gagner
            if (indexReveles[0] in casesAppuyees or indexReveles[1]\
            in casesAppuyees) and casesSelectionnees[0]!=casesSelectionnees[1]:
                
                                                        # le score est positif
                if int(document.querySelector("#score-text").innerHTML) > 0:
                    document.querySelector("#score-text").innerHTML = \
                    str(int(document.querySelector("#score-text").innerHTML)-5)
                                                        # enlève 5 points
                    flash()
                    
                else:
                    flash()
                
            else: 
                sleep(0.5)   # on ne flash pas, mais on veut montrer les cartes
                    
            casesAppuyees.append(indexReveles[0])  # on a déjà vue ces cases
            casesAppuyees.append(indexReveles[1])
            
            # identifiants des cases 1 et 2 qui ne sont pas pareilles                 
            case1 ="#carte" + str(casesSelectionnees[0])
            case2 = "#carte" + str(casesSelectionnees[1])
            # on retourne les cases
            retirerStyle(case1,case2)
            # on réinitialise pour pouvoir comparer d'autres cases entre elles
            casesSelectionnees = []; urlsReveles = [] ; indexReveles=[]
    else:
        pass
                
# annonce la victoire au joueur et met fin à la partie             
def victoire(): 
    sleep(0.3)   # afficher la grille pleine
    if len(casesDevinees) == len(tableau)/2: # toutes les paires sont trouvées
        alert("FéliCHATations! Toutes les paires ont été trouvées! MIAW")  
        niveau = mettreAJourNiveau(tableau)
        document.querySelector("#secondes").removeAttribute("style")
        interrompre(niveau)  

        
# remise à neuf et actualisation de l'espace après la fin de la partie
def reinitialiser():
    
    global tableau; global urlsReveles; global casesSelectionnees
    global casesDevinees; global casesAppuyees; global secondes; global clics
    
    niveau = mettreAJourNiveau(tableau)
        
    score = int(document.querySelector("#score-text").innerHTML)
    case = document.querySelector(".texte-meilleur"+str(niveau)).innerHTML
    tab = case.split(" ")
    meilleurActuel = tab[1]
    if len(casesDevinees) == len(tableau)/2:
                                # le nouveau score est meilleur que l'ancien
        if meilleurActuel == '-' or score > int(meilleurActuel):  
            meilleurActuel = str(score)
            tab = ["Meilleur: ",meilleurActuel]
            document.querySelector(".texte-meilleur"+str(niveau)).innerHTML = \
            functools.reduce(lambda x,y: x+y, tab)
        
                                # remet le score à 100 pour la prochaine partie
    (document.querySelector("#score-text").innerHTML) = "100" 
    
    for i in range (len(tableau)): # enlève les images
        document.querySelector("#carte"+str(i)).removeAttribute("style") 
    
    document.querySelector("#secondes").innerHTML = "60"
    document.querySelector("#secondes").removeAttribute("style")
    sleep(0.5)
    secondes = 60
    clics = False
    # tous les intermédiaires sont remis à neuf    
    tableau = []                
    total = []
    urlsReveles = []               
    casesSelectionnees = []
    casesDevinees=[]
    casesAppuyees = []
    indexReveles=[]

    
# contrôle de l'animation du chronomètre
secondes = 60
def countdown():
    global secondes; global clics; global tableau
    clics = True
    count=document.querySelector("#secondes")
    count.setAttribute("style","animation: changeColors 1s 61;")
    # ne pas commencer tant qu'on n'a pas encore retourne de cases
    secondes-=1
    count.innerHTML = str(secondes)
    if secondes == 0:
        sleep(0.1)
        alert("CHATperlipopette! Vous avez perdu :/")
        sleep(0.1)
        niveau=mettreAJourNiveau(tableau)
        interrompre(niveau)       
        
# consiste à mettre la boîte du score en rouge si on perd des points
def flash():
    mettreAJourStyle("#score-box","background-color: red")
    sleep(0.5)                 # en attente, cartes retournées et boîte rouge
    mettreAJourStyle("#score-box","background-color: white")
    

# consiste à initialiser le jeu à un certain niveau donné
def init(niveau):                     
    global tableau
    niveauJeu(niveau)                 # crée la grille
    tableau =  choisirImages(niveau)  # choisit les images aléatoirement
    
# début de la partie, initialement au niveau 1
init(niveau)