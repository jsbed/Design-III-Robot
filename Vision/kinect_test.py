# -*- coding: utf-8 -*-

import sys, time, cv2

captObj = cv2.VideoCapture(cv2.CAP_OPENNI)
cv2.namedWindow('Affichage RGB')
cv2.namedWindow('Affichage profondeur')

# Necessaire pour assurer une initialisation correcte
flags, img = captObj.read()
time.sleep(1)

while True:
	# On recupere une nouvelle image
	captObj.grab()
	
	# On va chercher les infos
	flags_i, img_i = captObj.retrieve(None, cv2.CAP_OPENNI_BGR_IMAGE)
	flags_p, img_p = captObj.retrieve(None, cv2.CAP_OPENNI_DEPTH_MAP)
	flags_g, img_g = captObj.retrieve(None, cv2.CAP_OPENNI_GRAY_IMAGE)

	# Pas d'image, peut se produire si on boucle trop vite
	if not flags_i or not flags_p or not flags_g:
		continue

	# Affichage
	cv2.imshow('Affichage RGB', img_i)
	cv2.imshow('Affichage profondeur', img_p)
	cv2.imshow('Affichage Gris', img_g)

	cc = cv2.waitKey(10) # Necessaire pour l'affichage effectif des images
	if cc == 27: # Touche Echap quitte
		break
