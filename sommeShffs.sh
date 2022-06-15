#! /bin/bash
# Date: 10 decembre 2021
# Auteurs: Sara Haddad, Marianne Schmitt, Catina Beaulieu

# Ce script calcul et affiche la somme des chiffres composants une valeur
# numerique saisie comme argument du script

nombre=$1          # on pose notre nombre etant l'argument fourni
entier="^[0-9]+$"  # ensemble des entiers
# On verifie tout d'abord le nombre et type d'argument
if [ $# -gt 1 ] || ! [[ $nombre =~ $entier ]]; then
echo Erreur! Il doit y avoir un seul argument: un entier positif.
exit               # terminer execution
fi

# Cette partie du code est executee apres la validation
# de l'argument et retourne la somme de ses chiffres
somme=0
for (( i; i <= ${#nombre}; i++ ))
do chiffre=${nombre:i:1};   # iterer a travers chaque chiffre
let somme+=chiffre          # mettre somme a jour
done
echo $somme