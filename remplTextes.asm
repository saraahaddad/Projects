# Auteurs:   Cloé Chandonnet (20136319): cloe.chandonnet@umontreal.ca 
# 		   Sara Haddad (20208373): sara.haddad@umontreal.ca
#		   Snkar Saleh Mahmood Mam (20180113): snkar.mam@umontreal.ca

# Date: 13.04.2022

#--------------------------------------------------------------------------------------------------
# Ce programme forme un nouveau texte à partir d'un texte initial en remplaçant 
# une séquence de caractères spécifiques par une autre séquence de caractères 
#--------------------------------------------------------------------------------------------------

# segment de la mémoire contenant les données globales
.data
buffTxtI: 	.space 50
buffTxtF: 	.space 100
txt1:     	.space 10
txt2:          .space 10
dataSpace:     .space 10  # espace afin de s'assurer que txt2 ne chevauche pas tabSJ
tabSJ:         .space 402

msgD:          .asciiz "Débordement du tampon de saisie."
msgTxtI:       .asciiz "Entrez un texte: "
msgTxt1:       .asciiz "Entrez le mot a remplacer: "
msgTxt2:       .asciiz "Entrez le mot de remplacement: "
newline:       .asciiz "\n"

#--------------------------------------------------------------------------------------------------
# La fonction main fait appel a des fonctions auxiliaires, et se charge de l'affichage
# du texte initial, avant remplacement, et du texte final, apres remplacement.
#--------------------------------------------------------------------------------------------------

# segment de la mémoire contenant le code
.text
main:
	addi $sp, $sp, -16			# faire de l'espace sur la pile
	
	jal saisir				# Appel a saisir
	
	li $v0, 4					# Affichage du contenu de buffTxtI
	la $a0, buffTxtI        
     syscall

	la $a1, txt1 				# Appel a rempl
	la $a2, txt2 
	jal rempl     
	
	li $v0, 4
	la $a0, newline
	syscall        
	
	li $v0, 4				     # Affichage du contenu de buffTxtF
	la $a0, buffTxtF
     syscall
        
     addi $sp, $sp, 16			#restaurer l'espace sur la pile

     li $v0,10					# Terminer l'execution
	syscall
	
#--------------------------------------------------------------------------------------------------
# La fonction saisir permet de stocker les textes entres par l'utilisateur dans les
# variables respectives, et detecte le debordement du tampon de saisie s'il y'en a un.
#--------------------------------------------------------------------------------------------------

saisir:
	la $a0, msgTxtI        
	li $v0, 4 
	syscall
	
	# Stocke l'entree de l'utilisateur dans la variable correspondante
	li $v0, 8
	la $a0, buffTxtI
	li $a1, 100                    # accorder plus de place pour pouvoir detecter debordement
	syscall
	
	li $v0, 4
	la $a0, newline
	syscall
	syscall
	
	sw $ra, 12($sp)    			 # on met de l'espace sur la pile pour utiliser $ra
	
	la $a0, buffTxtI   			 # Placer le texte dans $a0
	addi $t2, $t2, 50  			 # fixer la limite du nombre de caracteres
	jal len            			 # verifier la longueur du texte entre
	add $t9, $t0, $0			 # $t9 = len(buffTxtI)
	
	la $a0, msgTxt1      
	li $v0, 4 
	syscall
	
	# Meme travail pour txt1
	li $v0, 8          
	la $a0, txt1        
	li $a1, 20           		  # accorder plus de place pour pouvoir detecter debordement
	syscall
	
	li $v0, 4
	la $a0, newline
	syscall
	
	la $a0, txt1
	addi $t2, $0, 0       		  # re initialiser la limite a 0 pour ne pas accumuler
	addi $t2, $t2, 10               # limite de 10 pour txt1
	jal len
	add $t8, $t0, $0                # $t8 = len(txt1)
	
	la $a0, msgTxt2        
	li $v0, 4 
	syscall
	
	li $v0, 8
	la $a0, txt2
	li $a1, 20				  # accorder plus de place pour pouvoir detecter debordement
	syscall
	
	li $v0, 4
	la $a0, newline
	syscall
	
	la $a0, txt2
	addi $t2, $0, 0                  # re initialiser la limite a 0
	addi $t2, $t2, 10                # limite de 10 pour txt2
	jal len
	
	lw $ra, 12($sp)                  # restaurer $ra
	jr $ra					   # revenir au point d'appel
	
	len:   
		addi $t0, $0, 0             # $t0 = compteur de caracteres

	loop:                            # on compte caractere par caractere
		lb $t1, 0($a0)     		   # commencer a l'indexe 0 de la chaine de caractere
		beqz $t1, fin      		   # caractere nul = fin du mot
		addi $t0, $t0, 1   		   # incrementer le compteur de caracteres
		addi $a0, $a0, 1		   # incrementer indexe
		j loop
	
	fin:	
		bgt $t0, $t2, debordement   # on a depasse la limite allouee
		jr $ra
	
	debordement:
		la $a0, msgD                # afficher message du debordement
		li $v0, 4 
		syscall
	
		li $v0, 10    		        # terminer le programme               
		syscall
		
#---------------------------------------------------------------------------------------------------
#  La fonction remplacer(txt1, txt2):
#	- remplace le text1 par le text2 dans le buffTxtI et 
# 	- prend ce nouveau texte et le stocke dans buffTxtF
#---------------------------------------------------------------------------------------------------

rempl:		
	    	la $a0,buffTxtI	# $a0 = adresse de debut de stockage de buffTxtI
    		la $a1, txt1	     # $a1 = adresse de debut de stockage de txt1
    		sw $ra, 8($sp)
    		jal split
    		
    		la $a2, txt2		# $a2 = adresse de debut de stockage de txt2
    		jal join
    		
    		lw $ra, 8($sp)
    		jr $ra	
    		
#--------------------------------------------------------------------------------------------------
# split(textInit,motAremplacer): 
# 	- sous fonction de rempl qui transforme le buffTxtI en un tableau de sous texte séparés 
#      par un séparateur
#--------------------------------------------------------------------------------------------------

	split:
		addi $t0,$0,0				# debut = 0
    		addi $t1,$0,0				# fin = 0
   		addi $t2,$0,0				# indexe de buffTxtI = 0
    		add $s0,$0,$t9				# $s0 = len(buffTxtI)
    		subi $s0,$s0,1				# retire char \n
    		add $s1,$0,$t8				# $s1 = len(txt1)
    		subi $s1,$s1,1				# retire char \n
    		addi $t5,$0,0				# longueurTrouve = 0
    		addi $t6,$0,0				# nombre de sous chaines
    		la $t7, tabSJ				# $t7 = adresse de debut de stockage de tabSJ
    		lui $s4,0xffff				# $s4 = -1
    		ori $s4,0xffff
    		la $a3, newline
    		lb $t9, 0($a3)				# $t9 = code acii de \n
    		
    		for:						# for lettre in texte:
    			lb $s2,0($a0)			# lettre
    			lb $s3,0($a1)			# sep[longueurTrouve]
    			beq $s2,$t9, end
    			bne $s2,$s3, pasPareille
    			beq $s2,$s3, lettreTrouve 			
    		
    		pasPareille:				# if lettre != sep[longueurTrouve]:
    			addi $t5,$0,0			# longueurTrouve  = 0
    			la $a1,txt1 			# reset adress to first one of sep  	
    			addi $t2,$t2,1			# index+1
    			addi $a0,$a0,1			# next adress
    			beq $s0,$t2,texteFini	# if longueurTexte == index+1: 
    			j for
    						
    		texteFini:
    			subi $t2,$t2,1 		# get index back: index -= 1
    			addi $t1,$t2,0			# fin = index
    			sb $t0,0($t7)			# tabSJ.append(debut)
    			addi $t7,$t7,4
    			sb $t1,0($t7)			# tabSJ.append(fin)
    			addi $t7,$t7,4
    			addi $t6,$t6,1			# qttSep += 1
    			j end
    			
    		lettreTrouve:
    			beqz $t5, setFin		# if longueurTrouve == 0:
    		
    		next1:
    			addi $t2,$t2,1 		# index += 1
    			addi $a0,$a0,1			# next adress
    			addi $t5,$t5,1			# longueurTrouve += 1
    			addi $a1,$a1,1			# next adress
    			beq $t5,$s1, trouveTxt1	# if longueurTrouve == longueurSep:
    			j for
    			
    		setFin:
    			subi $t1,$t2,1			# fin = index-1
    			j next1
    			
    		trouveTxt1:
    			addi $t5,$0,0			# longueurTrouve = 0
    			la $a1,txt1 			# reset adress to first one of sep  			
    			bne $s4, $t1, continue	# if fin >= 0: 
    			    			
    		next:
    			addi $t0,$t2,0			# debut = index	
    			j for
    			    			
    		continue: 
    			bge $t1,$t0, ajouter     # if fin >= debut
    			j next
    			
    		ajouter: 
    			addi $t6,$t6,1			# qttSep += 1
    			sb $t0,0($t7)			# tabSJ.append(debut)
    			addi $t7,$t7,4
    			sb $t1,0($t7)			# tabSJ.append(fin)
    			addi $t7,$t7,4
    			j next
    			
		end:	
			la $t7,tabSJ
			subi $t4,$t7,4			# insert(0,qttSep) dans l'espace alloue a tabSJ
			sb $t6,0($t4)
			jr $ra
			
#------------------------------------------------------------------------------------------------------
# la fonction join permet d'integrer le separateur entre les sous chaines extraites par split
#------------------------------------------------------------------------------------------------------

join:
	la $t0, tabSJ       	  # $t0 = adresse de debut de stockage de tabSJ	
	la $a0, buffTxtI     	  # $a0 = adresse de debut de stockage de buffTxtI
	la $a1, buffTxtF    	  # $a1 = adresse de debut de stockage de buffTxtF

	addi $s0, $0, 0            # compteur du nombre de copies.On s'arrete lorsque s0 = taille de tabSJ
	beqz $t6, copySep          # txtI = txt1
	
	lb $t2, 0($t0)             # si tabSJ[1] != 0, le separateur est au debut du mot
	bnez $t2, sepFirst
	
	j delimit
	
	condition:			  # $s0 = $t6 -> on a atteint le nombre de copies voulues
		beq $s0, $t6, test    # verifier si un separateur se trouve a la fin du mot	
	     	
	copySep:
		lb $t1, 0($a2)        # charger code ascii de chaque lettre de txt2
		beq $t1, $t9, nextEl  # on a fini de copier, on passe au prochain element
		sb $t1, 0($a1)        # stocker dans buffTxtF
	
		addi $a1, $a1, 1      # passer a l'adresse suivante pour stocker prochain caractere
		addi $a2, $a2, 1      # passer a l'adresse suivant pour charger prochain caractere

		j copySep             # on n'a pas copie tout le mot
	
	sepFirst:				  # le separateur est au debut du texte initial
		lb $t1, 0($a2)        
		beq $t1, $t9, delimit # on a copie tout txt2 
		sb $t1, 0($a1)        # copier le caractere dans buffTxtF 
	
		addi $a1, $a1, 1
		addi $a2, $a2, 1
		j sepFirst  
	
	nextEl:
		addi $t3, $t3, 4      # avancer dans le tableau
		addi $t0, $t3, 0      # fixer $t0 a l'element apres la fin de
				     	  # la chaine precedente
		j delimit
	
	test: 	
		# on a atteint le nombre de copies voulu, si la prochaine lettre de texteI
        	# n'est pas newline, on detecte le separateur
		addi $a0, $a0,1
        	lb $t2, 0($a0)
       	bne $t2,$t9, copySep  # separateur a la fin du mot
        	j copyDone            # sinon, on a termine

#---------------------------------------------------------------------------------------------------								
# La fonction copy effectue la copie du bloc d'octets debutant a une adresse adr1, jusqu'a
# l'adresse adr2 de buffTxtI, dans buffTxtF a partir de adr3.	
#---------------------------------------------------------------------------------------------------

copy:	
	lb $t1, 0($a0)                # $t1 = code ascii du caractere de buffTxtI
	sb $t1, 0($a1)                # placer le caractere dans buffTxtF
	
	beq $a0, $t8, count           # adr1 = adr2, copie terminee

	addi $a0, $a0, 1              # incrementer l'indexe de buffTxtI
	addi $a1, $a1, 1              # incrementer l'indexe de buffTxtF
	
	j copy		         	     # continuer tant que adr1 != adr2
	
	# delimiter les paires d'adresses pour recopier tout ce qu'il y a entre les deux
	delimit:
		beq $s0, $t6, copyDone   # on a fini de former buffTxtF
	
		lui $s7, 0x1001          # adresse de debut de stockage des donnees (celle de buffTxtI)
		ori $s7, 0x0000          # concatenation avec les 4 low order bytes
	
		lb $t2, 0($t0)           # charger element de tabSJ
		
		la $a0, buffTxtI
		add $a0, $a0, $t2        # additionner a l'adresse de buffTxtI pour obtenir adr1
	
		addi $t3, $t0, 4         # charger prochain element de tabSJ
		lb $t2, 0($t3)
		add $t8, $s7, $t2        # additionner a l'adresse de buffTxtI pour obtenir adr2
	
		j copy
	
	count:	
	     lb $t2, 0($a1)           # iterer a travers buffTxtF    
		la $a2, txt2 
		beqz $t2, copiesDone     # caractere nul = fin du mot
		addi $a1, $a1, 1         # incrementer indexe
	
		j count
	
	copiesDone:
		addi $s0, $s0, 1         # incrementer le nombre de copies faires
		j condition

	copyDone:
		jr $ra			     # revenir au point d'appel
