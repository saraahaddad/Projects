#! /bin/bash

# Date: 10 decembre 2021
# Auteurs: Sara Haddad, Marianne Schmitt, Catina Beaulieu

# Ce programme prend en entree trois arguments: un fichier csv, le seuil de
# passage en pourcents, ainsi que la session, dont nous verifierons la validite, et
# genere en sortie un fichier csv contenant le nom, prenom, ID, ainsi que les notes
# des etudiants du fichier pris en entree.

# Commencer par verifier qu'il y'a exactement trois arguments
if [ $# -ne 3 ] ; then
echo Mauvais nombre d"'"arguments!
exit
fi

# Verifier que le premier argument est un fichier de type csv qui existe
fichier=$1
if [ ! -f $fichier ] || ! [[ $1 == *.csv ]]; then
echo Argument un invalide
exit
fi

# Verifier que le deuxieme argument est un entier inferieur a 100, indiquant
# le seuille de passage
entier="^[0-9]+$"
if [ $2 -gt 100 ] || ! [[ $2 =~ $entier ]] ; then
echo Argument deux invalide!
exit
fi

# Verifier que le troisieme argument debute par les lettres A, H ou E, et est 
# suivi de deux entiers symbolisant une annee
argument=$3
if [[ ${argument:0:1} != [A,E,H] ]] || ! [[ ${argument:1:2} =~ $entier ]] || ! [[ ${#argument} = 3 ]] ; then
echo Argument trois invalide!
exit
fi

# Extraction de la premiere ligne d'informations du fichier en entree
fichier=$1
read ligneBase < $fichier

# Extraction des ponderations des differents elements: TP1, TP2, TP3, TP4, Intra et Final
pondtp1=${ligneBase:18:2}   # Recuperer les chiffres entre parentheses
pondtp2=${ligneBase:27:2}
pondtp3=${ligneBase:36:2}
pondtp4=${ligneBase:45:2}
pondIntra=${ligneBase:56:2}
pondFinal=${ligneBase:67:2} 

# Cette constante permet de faire les calculs avec les differentes ponderations (exemple: 25 -> 0.25)
constante1=0.01

# Cacul du seuil de passage a l'aide des ponderations de l'intra et du final
seuilDefini=$2
seuil=$( echo "($pondIntra+$pondFinal)*$seuilDefini*$constante1" | bc -l ) 

# Creer le fichier et lui donner le nom correspondant
aCreer="notes"$3".csv"
titre1="IetF"
titre2="Total"
# Inscrire tout d'abord la premiere ligne du nouveau fichier qui contient la ligne extraite
# ainsi que les nouvelles colonnes ajoutees
echo "$ligneBase","$titre1""($seuil%)","$titre2" >> $aCreer


# On effectue la lecture du fichier fourni en argument en excluant la premiere ligne et on redirige
# vers une nouvelle variable
# Ceci aidera a effectuer tous les calculs
corpsFichier='l.csv'
sed -e '1d' $fichier > $corpsFichier

# On delimite les differents elements. Ils sont separes par des virgules. On extrait le prenom
# nom, id, les notes des TP et des examens de chaque eleve.
while IFS="," read -r prenom nom id tp1 tp2 tp3 tp4 intra final
do     # Calcul de la moyenne de l'eleve pour l'intra et le final
IetF=$( echo "(($pondIntra*$constante1*$intra)+($pondFinal*$constante1*$final))" | bc -l )
comparaison=$(echo "$IetF>=$seuil" | bc)   # on compare ce resultat au seuil de passage
if [[ $comparaison -eq 1 ]]; then          # si la condition est vraie, l'eleve a reussi
total=$( echo "($IetF+$pondtp1*$constante1*$tp1+$pondtp2*$constante1*$tp2+$pondtp3*$constante1*$tp3+$pondtp4*$constante1*$tp4)" | bc )
else   # L'eleve n'a pas reussi, le total de ses notes de TP est divise par deux
total=$( echo "($IetF+($pondtp1*$constante1*$tp1+$pondtp2*$constante1*$tp2+$pondtp3*$constante1*$tp3+$pondtp4*$constante1*$tp4)/2)" | bc )
fi     # on cree le contenu du nouveau fichier
echo "$prenom","$nom","$id","$tp1","$tp2","$tp3","$tp4","$intra","$final","$IetF","$total" >> $aCreer
done < $corpsFichier