#Date: 11 octobre 2021
#Auteurs: Marylou Fauchard et Sara Haddad

# question 
### pq le y marche pas pour tracer murs verticaux 
### pq marche pas quand on met le error, pas supposé passer...
### est ce que mieux de mettre variable xaseX et caseY pour pas répéter? 
### règle le problème de pas de chemin? 

#Ce code permet de générer un labyrinthe d'une largeur et hauteurs specifiques,
#avec des cases composées d'un certain nombre de pixels

#Cette fonction retourne une liste composée de n éléments
def iota(n):               
    liste = list(range(n))
    return liste

#Cette fonction retourne un booleen: True si x est dans le tableau et False 
#s'il ne l'est pas
def contient (tab, x):      
    return(x in tab)

#Cette fonction ajoute le nombre x au contenu de la table, s'il n'est pas
#déjà dedans
def ajouter(tab, x): 
    if contient(tab, x)== False : # pour éviter les répétitions
        tab.append(x)
    return(tab)

#Cette fonction retire le nombre x du contenu de la table, s'il était dedans
def retirer(tab, x): 
    if contient (tab, x)== True:  # jamais de duplication dans la liste
        tab.remove(x)              
    return tab

#Cette fonction compléente la fonction "trier"(prise des notes de cours)
def positionMin(liste,debut):       
    positionMin = debut
    for i in range(debut+1, len(liste)):
        if liste[i] < liste[positionMin]:
            positionMin = i
    return positionMin

#Cette fonction trie le contenu d'une liste (orise des notes de cours)
def trier(liste):                
    for i in range(len(liste)-1):
        m = positionMin(liste, i)
        temporaire = liste[i]
        liste[i] = liste[m]
        liste[m] = temporaire

#Cette fonction retourne un tableau contenant les numéros des cellules voisines
#d'une case de coordonnées (x,y)
def voisins(x,y,nX,nY): 
    numeroCase= x + y * nX
    voisins=[]
    if x<nX-1:
        voisins.append(numeroCase+1)
    if x>0:
        voisins.append(numeroCase-1)
    if y>0:
        voisins.append(numeroCase-nX)
    if y<nY-1:
        voisins.append(numeroCase+nX)  
    trier(voisins)

    return voisins

#Cette fonction retourne les coordonnées des 4 murs d'une case
def coordonneesMurs(x,y,nX):   
        N = x + y * nX               #mur nord
        E = 1 + x + y * (nX+1)       #mur est
        S = x + (y+1) * nX           #mur sud
        O = x + y * (nX+1)           #mur ouest
        return list((N,E,S,O))

#Cette fonction choisit aléatoirement un élément d'une liste
def choisirElement(liste):    
    choix = len(liste)

    numeroChoisie = math.floor(random()*choix)

    elementChoisie = liste[numeroChoisie]

    return(elementChoisie)

#Cette fonction identifie le mur qui relie deux cases
def murEntreCase(case1,case2,nX,nY):   
    if case1+1==case2:
        murContact=coordonneesMurs(coordonneeCase(case1,nX,nY)[0],
                                 coordonneeCase(case1,nX,nY)[1],nX)[1]
    if case1-1==case2:
        murContact=coordonneesMurs(coordonneeCase(case1,nX,nY)[0],
                                 coordonneeCase(case1,nX,nY)[1],nX)[3]
    if case1+nX==case2:
        murContact=coordonneesMurs(coordonneeCase(case1,nX,nY)[0],
                                 coordonneeCase(case1,nX,nY)[1],nX)[2]
    if case1-nX==case2:
        murContact=coordonneesMurs(coordonneeCase(case1,nX,nY)[0],
                                 coordonneeCase(case1,nX,nY)[1],nX)[0]
    return(murContact)

#Cette fonction donne les coordonnées x et y de la case N
def coordonneeCase(N,nX,nY):  
    x = 0
    y = 0
    if N >= 0 :#and N <=nX*nY-1 :
        x = (N%nX)
        y = (N-N%nX)/nX
    else:
        return("error")
    return(list((x,y)))  # est ce qu'on retourne mal une liste? pourtant les test passent!!

#Cette fonction retourne toutes les cases adjacentes à une autre case qui se 
#retrouve dans la cavitée
def caseAdjacente(cave,prochaineCase,nX,nY): 
    contour=voisins(coordonneeCase(prochaineCase,nX,nY)[0],
                  coordonneeCase(prochaineCase,nX,nY)[1],nX,nY)
    caseVoisine=[]
    for voisin in contour:
        if contient(cave,voisin):
            ajouter(caseVoisine,voisin)       
    return(caseVoisine)

#Le labyrinthe sera traite sous forme de tableau. Cette fonction retourne deux 
#listes: mursH et mursV, qui contiennent les murs horizontaux et verticaux
#qui ne seront pas retirés du labyrinthe
def laby(nX,nY,largeurCase):

    setScreenMode(nX+1+nX*largeurCase,nY+1+nY*largeurCase) #écran noir de base
    mursH=iota(nX*(nY+1))                   #ensemble des murs horizontaux                 
    mursV=iota((nX+1)*nY)                   #ensemble des murs verticaux

  #itération 0 
    cave=[] 
    front=[]
    depart = choisirElement(iota(nX*nY))    #élément de départ dans la cavité
    ajouter(cave,depart)

    for voisin in voisins(coordonneeCase(depart,nX,nY)[0],
                        coordonneeCase(depart,nX,nY)[1],nX,nY):
        ajouter(front,voisin)               #voisins de l'élément de départ 

    prochaineCase = choisirElement(front)  
    ajouter(cave,prochaineCase)
    retirer(front, prochaineCase)

    
    for voisin in voisins(coordonneeCase(prochaineCase,nX,nY)[0],             
                            coordonneeCase(prochaineCase,nX,nY)[1],nX,nY):
            if voisin not in cave:   #front ne prend pas les cases de la cavité
                ajouter(front,voisin)
    
    if (prochaineCase==depart+1 or prochaineCase==depart-1): 
                                                         # sur une même ligne
        retirer(mursV,murEntreCase(depart,prochaineCase,nX,nY)) 
                                                         # dessine pas ce mur
                               # plus disponible dans les voisins hors cavité

    else:                                                     # sur une colonne
        retirer(mursH,murEntreCase(depart,prochaineCase,nX,nY)) 

  #irération restante
    while len(cave) < nX*nY:                 #passer sur toutes les cases                        
        prochaineCase = choisirElement(front)
        ajouter(cave,prochaineCase)          #mise à jour de la cavité
        retirer(front,prochaineCase)         #mise à jour des voisins 

        for voisin in voisins(coordonneeCase(prochaineCase,nX,nY)[0],
                            coordonneeCase(prochaineCase,nX,nY)[1],nX,nY):
            if voisin not in cave:
                ajouter(front,voisin)


        caseDeCave = choisirElement(caseAdjacente(cave,prochaineCase,nX,nY))
        #choix aléatoire parmis case avec un mur collé avec la case de 
        #l'itération

        if ((caseDeCave + 1 == prochaineCase) or 
            (caseDeCave - 1 == prochaineCase)):
          #le mur est vertical
            retirer(mursV,murEntreCase(caseDeCave,prochaineCase,nX,nY))


        if ((caseDeCave + nX == prochaineCase)
            or (caseDeCave - nX== prochaineCase)):
          #le mur est horizontal
          retirer(mursH,murEntreCase(caseDeCave,prochaineCase,nX,nY))
    retirer(mursH,0)
    retirer(mursH,(nX*(nY+1)-1))
    
    # mettre la grille en blanc
    for x in range(nX*largeurCase+nX+1):
        for y in range(nY*largeurCase+nY+1):
            setPixel(x,y,struct(r=15,g=15,b=15))
    
    # tracer les murs horizontaux
    for mur in mursH:
        for i in range (mur%nX*largeurCase+mur%nX+1,mur%nX*largeurCase+mur%nX+largeurCase+2): 
               setPixel(i,mur//nX*largeurCase+mur//nX,struct(r=1,g=1,b=1))
    # tracer les murs verticaux
    for mur in mursV:
        for j in range(mur//(nX+1)*largeurCase+mur//(nX+1)+1,mur//(nX+1)*largeurCase+mur//(nX+1)+largeurCase+2,1):
            setPixel(mur%(nX+1)*largeurCase+mur%(nX+1),j,struct(r=1,g=1,b=1))
        
   
    return(len(mursV)+len(mursH))
        


#Tests unitaires qui permettent de s'assurer du bon fonctionnement du code
def testIota():
    assert iota(0)==[]
    assert iota(1)==[0]
    assert iota(2)==[0,1]
    assert iota(3)==[0,1,2]
    assert iota(4)==[0,1,2,3]
    assert iota(5)==[0,1,2,3,4]
    assert iota(-4)==[]
testIota()

def testContient():
    assert contient([9,2,5], 2) == True
    assert contient([9,2,5], 4) == False
testContient()

def testAjouter():
    assert ajouter([9,2,5], 2) == [9,2,5]
    assert ajouter([4,5,7], 8) == [4,5,7,8]
testAjouter()

def testRetirer():
    assert retirer([9,2,5], 2) == [9,5]
    assert retirer([9,2,5], 4) == [9,2,5]
testRetirer()

def testVoisins():
    assert voisins(0,0,8,4) == [1,8]
    assert voisins(3,0,8,4) == [2,4,11]
    assert voisins(7,0,8,4) == [6,15]
    assert voisins(0,2,8,4) == [8,17,24]
    assert voisins(0,3,8,4) == [16,25]
    assert voisins(3,3,8,4) == [19,26,28]
    assert voisins(7,3,8,4) == [23,30]
    assert voisins(7,1,8,4) == [7,14,23]
    assert voisins(4,2,8,4) == [12,19,21,28]
testVoisins()

def testCoordonneesMurs():
    assert coordonneesMurs(5,1,8) == [13,15,21,14]
    assert coordonneesMurs(0,0,8) == [0,1,8,0]
    assert coordonneesMurs(7,0,8) == [7,8,15,7]
    assert coordonneesMurs(0,3,8) == [24,28,32,27]
testCoordonneesMurs()

def testCoordonneeCase():
    assert coordonneeCase(0,8,4) == [0,0]
    assert coordonneeCase(11,8,4) == [3,1]
    assert coordonneeCase(0,8,4) == [0,0]
    assert coordonneeCase(22,8,4) == [6,2]
   # assert coordonneeCase(32,8,4) == "error"
   # assert coordonneeCase(-1,8,4) == "error"
testCoordonneeCase()

def testMurEntreCase():
    assert murEntreCase(0,1,8,4) == 1
    assert murEntreCase(2,10,8,4) == 10
    assert murEntreCase(14,22,8,4) == 22
testMurEntreCase()
