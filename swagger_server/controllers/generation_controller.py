import connexion
import six
import json
import subprocess

from os import listdir, mkdir
from os.path import isfile, join, exists
from swagger_server.models.img import Img  # noqa: E501
from swagger_server import util


def generation_par_ia(nom_categorie, nom_ia, modele_ia):  # noqa: E501
    """Génèration par ia

    Génèration par ia # noqa: E501

    :param nom_categorie: Nom de la catégorie
    :type nom_categorie: str
    :param nom_ia: Nom de l&#x27;IA
    :type nom_ia: str
    :param modele_ia: Modele de l&#x27;IA
    :type modele_ia: str

    :rtype: Output
    """
    # Chemin vers l'interpréteur Python dans l'environnement virtuel
    python_virtualenv = f'./IA/{nom_ia}/{nom_ia}Env/Scripts/python'  # Pour Windows
    # python_virtualenv = f'./IA/{nom_ia}/{nom_ia}Env/bin/python'  # Pour macOS/Linux

    # Chemin vers le script Python à exécuter
    inference = f'./toolkit/{nom_categorie}/{nom_ia}/inference.py'

    tab_param = [python_virtualenv, inference]
    nom_fichier = f'./toolkit/{nom_categorie}/{nom_ia}/param.json'

    
    paramFile = open(nom_fichier)
    param = json.load(paramFile)

    for p in param.keys():
        if p == param[p]:
            tab_param.append(p)
        else:
            tab_param.append(p)
            if param[p] != "modele_ia":
                tab_param.append(param[p])
            else:
                tab_param.append(f'./IA/{nom_ia}/models/{modele_ia}')

    print(tab_param)
    # Exécuter le script Python dans l'environnement virtuel
    process = subprocess.Popen(tab_param, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

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

    chemin = f'outputs/{nom_categorie}/{nom_ia}'
    fichier = "00000.txt"

    if(not exists("outputs/")):
        mkdir("outputs/")

    if(not exists(f'outputs/{nom_categorie}')):
        mkdir(f'outputs/{nom_categorie}')

    if(not exists(chemin)):
        mkdir(chemin)

    if(nom_categorie.split("2")[-1] == "txt"):
        print("Write inside a txt file")
        if(exists(chemin+'/'+fichier)):
            fichier = listdir(chemin)[-1]
            num_fichier = str(int(fichier[:-4])+1)
            fichier = '0'*(5-len(num_fichier)) + num_fichier + ".txt"
        with open(chemin+'/'+fichier, 'w') as f:
            f.write(stdout.decode())
    else:
        fichier = listdir(chemin)[-1]
        if(not isfile(chemin+'/'+fichier)):
            fichier = listdir(chemin+'/'+fichier)[-1]

    dictionnaire_retour = { "output": f'{chemin}/{fichier}'}
    return dictionnaire_retour


def get_resultat(nom_categorie, nom_ia):  # noqa: E501
    """Accède aux résultats d&#x27;une IA

    Accède aux résultats d&#x27;une IA # noqa: E501

    :param nom_categorie: Nom de la catégorie
    :type nom_categorie: str
    :param nom_ia: Nom de l&#x27;IA
    :type nom_ia: str

    :rtype: List[Output]
    """
    liste_retour = []
    chemin = f'outputs/{nom_categorie}/{nom_ia}'
                
    for fichier in listdir(chemin):
        dictionnaire_pour_json = {}
        if isfile(join(f'outputs/{nom_categorie}/{nom_ia}', fichier)):
            dictionnaire_pour_json['img'] = f'outputs/{nom_categorie}/{nom_ia}/{fichier}'
            
        else:
            for fichier_fils in listdir(chemin + "/" + fichier):
                if isfile(join(f'outputs/{nom_categorie}/{nom_ia}/{fichier}', fichier_fils)):
                    dictionnaire_pour_json['img'] = f'outputs/{nom_categorie}/{nom_ia}/{fichier}/{fichier_fils}'
        liste_retour.append(dictionnaire_pour_json)
    return liste_retour
