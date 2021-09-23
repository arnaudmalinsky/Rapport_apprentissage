# Rapport_apprentissage

NB : 
- VO = véhicule d'occasion
- Je ne peux pas vous faire parvenir les données mais il peut tout de même être intéressant de voir le code sans le faire tourner.

## Mission 1 : prédiction de chiffres d'affaires
dossier : Prediction_ca/

--> exploration

Script : Prediction_ca/exploration.ipynb

--> Selection des variables avec lasso

Script : Prediction_ca/norauto_var_sel_lasso.ipynb

--> Selection des variables avec stepwise

Script : Prediction_ca/norauto_var_sel_stepwise.ipynb

--> Entrainement du modèle et calcul des prédictions une fois les variables sélectionnées

Script : Prediction_ca/Norauto_run_prediction.ipynb
NB : le script est codé pour prédire aussi le CA de l'année 2023, c'est parce qu'on a mis à jour la mission en septembre, mais dans le rapport j'en suis resté à la version de juin dernier.

## Mission 2 : partie estimation de prix de VO
Dossier : Etude_vo/estimation_prix/

--> Scraping de leboncoin avec le package RPA pour les estimations de prix

Script : Etude_vo/estimation_prix/scraping_leboncoin.py

--> Estimation des prix des véhicules diesel et esssence 

Script : Etude_vo/estimation_prix/estimation_diesel.ipynb et Etude_vo/estimation_prix/estimation_essence.ipynb

--> courbes de décote

Script : Etude_vo/estimation_prix/courbes_decote.ipynb

## Mission 2 : partie stock VO
Dossier : Etude_vo/stock_vo/

--> Ratio immat sur stock VO par departement

Script : Etude_vo/stock_vo/run_ratio_par_departement.py

--> Série temporelle des immatriculations et des stocks depuis 2019

Script : Etude_vo/stock_vo/run_serie_temporelle.py

--> Temps de résidence médian des véhicules dans le stock par marque

Script : Etude_vo/stock_vo/run_tps_marque.py

--> Temps de résidence médian des véhicules dans le stock par modèle

Script : Etude_vo/stock_vo/run_tps_modele.py