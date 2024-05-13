import connexion
import six

import subprocess
from os import listdir, remove, symlink
from shutil import rmtree
from os.path import isfile, exists
from swagger_server.models.chemin_modele import CheminModele  # noqa: E501
from swagger_server.models.output import Output  # noqa: E501
from swagger_server import util

def add_modele(body, nom_ia):  # noqa: E501
    """Ajoute un nouveau Modele d&#x27;IA

    Ajoute un nouveau Modele d&#x27;IA # noqa: E501

    :param body: Chemin absolu du modèle
    :type body: dict | bytes
    :param nom_ia: Nom de l&#x27;IA
    :type nom_ia: str

    :rtype: Output
    """
    modele_ia = body["chemin"]
    retour = {"output":""}
    nom_modele = modele_ia.split("/")[-1]
    chemin_dest = f'./IA/{nom_ia}/models/{nom_modele}'
    print(chemin_dest)
    # "-Src", modele_ia, "-Dest", chemin_dest
    process = subprocess.Popen(["./apiEnv/Scripts/python", "./toolkit/symlink.py", "-src", modele_ia, "-dest", chemin_dest], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Attendre que le subprocess se termine et récupérer la sortie
    stdout, stderr = process.communicate()

    retour["output"] = chemin_dest

    # Vérifier si le subprocess s'est terminé avec succès
    if process.returncode == 0:
        print("Le subprocess s'est terminé avec succès.")
    else:
        print("Le subprocess a échoué avec le code de sortie :", process.returncode)

    print("Sortie standard :", stdout.decode())
    print("Erreur standard :", stderr.decode())


    return retour


def del_modele(nom_ia, modele_ia):  # noqa: E501
    """Supprime un Modele de l&#x27;IA

    Les noms des IA sont disponible via la méthode GET /IA/trouverParCategorie. Les noms des Modeles d&#x27;IA sont disponible via la méthode GET /modele/{nomIA} # noqa: E501

    :param nom_ia: Nom de l&#x27;IA
    :type nom_ia: str
    :param modele_ia: Modele de l&#x27;IA
    :type modele_ia: str

    :rtype: Output
    """
    retour = {"output":""}
    chemin = f'IA/{nom_ia}/models/{modele_ia}'
    if(exists(chemin)):
        if(isfile(chemin)):
            remove(chemin)
        else:    
            rmtree(chemin)
        retour["output"] = chemin
    return retour


def get_modele(nom_ia):  # noqa: E501
    """Donne les Modeles de l&#x27;IA

    Add a new Output to the store # noqa: E501

    :param nom_ia: Nom de l&#x27;IA retourné par /IA/trouverParCategorie
    :type nom_ia: str

    :rtype: List[Output]
    """
    liste_retour = []
    chemin = f'IA/{nom_ia}/models'
    if(exists(chemin)):
        for fichier in listdir(chemin):
            liste_retour.append({"output":fichier})

    return liste_retour
