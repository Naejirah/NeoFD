import connexion
import six
import json
import subprocess

from swagger_server.models.img import Img  # noqa: E501
from swagger_server import util


def generation_par_ia(nom_categorie, nom_ia, modele_ia:str, nom_fichier_parametre=None):  # noqa: E501
    """Génère du texte à partir de texte

    Génère du texte à partir de texte # noqa: E501

    :param nom_categorie: ID of Img to update
    :type nom_categorie: str
    :param nom_ia: ID of Img to update
    :type nom_ia: str
    :param modele_ia: ID of Img to update
    :type modele_ia: str
    :param nom_fichier_parametre: Fichier de paramètre pour le lancement de l&#x27;IA au format json
    :type nom_fichier_parametre: strstr

    :rtype: Img
    """

    
    # Chemin vers l'interpréteur Python dans l'environnement virtuel
    python_virtualenv = f'./IA/{nom_ia}/{nom_ia}Env/Scripts/python'  # Pour Windows
    # python_virtualenv = f'./IA/{nom_ia}/{nom_ia}Env/bin/python'  # Pour macOS/Linux

    # Chemin vers le script Python à exécuter
    inference = f'./toolkit/{nom_categorie}/{nom_ia}/inference.py'

    tabParam = [python_virtualenv, inference, 'launch']
    nom_fichier = ""
    if(nom_fichier_parametre == None):
        nom_fichier = f'./toolkit/{nom_categorie}/{nom_ia}/param.json'
    else:
        nom_fichier = nom_fichier_parametre
        print(nom_fichier)
        nom_fichier = f'./toolkit/{nom_categorie}/{nom_ia}/param.json'
    
    paramFile = open(nom_fichier)
    param = json.load(paramFile)

    for p in param.keys():
        tabParam.append(p)
        print(p[0])
        if param[p] != "modele_ia":
            tabParam.append(param[p])
        else:
            tabParam.append(f'./IA/{nom_ia}/models/{modele_ia}')



    print(tabParam, modele_ia)

    # Exécuter le script Python dans l'environnement virtuel
    process = subprocess.Popen(tabParam, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    paramFile.close()

    # Attendre que le subprocess se termine et récupérer la sortie
    stdout, stderr = process.communicate()

    # Vérifier si le subprocess s'est terminé avec succès
    if process.returncode == 0:
        print("Le subprocess s'est terminé avec succès.")
    else:
        print("Le subprocess a échoué avec le code de sortie :", process.returncode)

    print("Sortie standard :", stdout.decode())
    print("Erreur standard :", stderr.decode())

    return stdout.decode()


def get_resultat(nom_categorie, nom_ia=None, modele_ia=None):  # noqa: E501
    """Accède aux résultats d'une IA

    Génère du texte à partir de texte # noqa: E501

    :param nom_categorie: ID of Img to update
    :type nom_categorie: str
    :param nom_ia: ID of Img to update
    :type nom_ia: str
    :param modele_ia: ID of Img to update
    :type modele_ia: str

    :rtype: Img
    """
    return 'do some magic!'
