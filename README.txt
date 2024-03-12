Licence 3 - UPJV
Intelligence Artificielle : Apprentissage Artificiel

Par KHALED Sara et THOMAS Johann

Le but de ce projet est de concevoir un réseau de neurone et de le tester sur différents exemples.
Le réseau de neurone essaie de déterminer des valeurs en fonction des données qu'il a pu apprendre durant une phase d'apprentissage.

I) Prérequis :
    - Ce projet nécessite Python3 pour fonctionner

II) Utilisation :
        Afin de tester ce programme, il est d'abord nécessaire d'entrainer le réseau de neurone sur des jeux de données situés dans le dossier Data.
        L'apprentissage est tout d'abord effectué en effectuant la commande :
            - python3 apprentissage.py FileSave DataFile NombreCouche TauxApprentissage ParamSigmoide MargeErreur
            ou
            - python3 apprentissageBatch.py FileSave DataFile NombreCouche TauxApprentissage ParamSigmoide MargeErreur
        Le test s'effectue ensuite en tapant la commande où DataFile est un fichier de test située dans le dossier Test :
            - python3 test.py FileSave DataFile 

Ce projet contient trois jeux de données, un jeux permettant d'apprendre le XOR, un autre permettant d'apprendre le XORNAND et un dernier concernant une étude des résultats d'étudiants selon divers paramètres.

Dans le cas où, pendant l'apprentissage, les valeurs restent inchangées pendant de trop nombreuses itérations, il est fort probable que le programme soit tombé dans un minimum local aussi il est conseillé de supprimer la sauvegarde et recréer un nouveau réseau.