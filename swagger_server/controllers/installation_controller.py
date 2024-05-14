import connexion
import six

from os import listdir, mkdir, remove
from os.path import isfile, exists
from swagger_server.models.input_fichier_generation import InputFichierGeneration  # noqa: E501
from swagger_server.models.input_fichier_installation import InputFichierInstallation  # noqa: E501
from swagger_server.models.output import Output  # noqa: E501
from swagger_server import util


def add_fichier_installation(body, plateforme, nom_ia):  # noqa: E501
    """Ajoute un nouveau Modele d&#x27;IA

    Ajoute un nouveau Modele d&#x27;IA # noqa: E501

    :param body: Create a new Output in the store
    :type body: dict | bytes
    :param plateforme: Nom de l&#x27;IA retourné par /IA/trouverParCategorie
    :type plateforme: str
    :param nom_ia: Nom de l&#x27;IA retourné par /IA/trouverParCategorie
    :type nom_ia: str

    :rtype: Output
    """
    if connexion.request.is_json:
        body = InputFichierInstallation.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def ajout_fichier_lancement(body, nom_ia):  # noqa: E501
    """Ajoute un fichier de generation

    Ajoute un fichier de generation et de paramètre # noqa: E501

    :param body: Create a new Output in the store
    :type body: dict | bytes
    :param nom_ia: Nom de l&#x27;IA retourné par /IA/trouverParCategorie
    :type nom_ia: str

    :rtype: Output
    """
    if connexion.request.is_json:
        body = InputFichierGeneration.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_fichier_generation(nom_ia):  # noqa: E501
    """Retourne les fichiers de Generation

    Retourne les fichiers de Generation # noqa: E501

    :param nom_ia: Nom de l&#x27;IA retourné par /IA/trouverParCategorie
    :type nom_ia: str

    :rtype: Output
    """
    return 'do some magic!'


def get_fichier_installation(nom_ia):  # noqa: E501
    """Retourne les fichiers d&#x27;installation d&#x27;une IA

    Retourne les fichiers d&#x27;installation d&#x27;une IA # noqa: E501

    :param nom_ia: Nom de l&#x27;IA retourné par /IA/trouverParCategorie
    :type nom_ia: str

    :rtype: Output
    """
    return {"output": f'./IA/{nom_ia}/install'}


def lancement_fichier_installation(nom_ia, plateforme):  # noqa: E501
    """Lancement d&#x27;une installation d&#x27;une IA

    Lancement d&#x27;une installation d&#x27;une IA # noqa: E501

    :param nom_ia: Nom de l&#x27;IA retourné par /IA/trouverParCategorie
    :type nom_ia: str
    :param plateforme: Système d&#x27;exploitation
    :type plateforme: str

    :rtype: Output
    """
    return 'do some magic!'


def suppr_fichier_installation(nom_ia, plateforme):  # noqa: E501
    """Supprime un fichier d&#x27;installation

    Supprime un fichier d&#x27;installation # noqa: E501

    :param nom_ia: Nom de l&#x27;IA retourné par /IA/trouverParCategorie
    :type nom_ia: str
    :param plateforme: système d&#x27;exploitation
    :type plateforme: str

    :rtype: Output
    """
    retour = {"output": ""}
    chemin = f'./IA/{nom_ia}/install'
    if(exists(chemin)):
        for fichier in listdir(chemin):
            if(f"install_{plateforme}" in fichier):
                remove(chemin+'/'+fichier)
                retour["output"] = chemin+'/'+fichier
    return retour


def suppr_fichier_lancement(nom_ia):  # noqa: E501
    """Supprime un fichier de Generation

    Supprime un fichier de Generation # noqa: E501

    :param nom_ia: Nom de l&#x27;IA retourné par /IA/trouverParCategorie
    :type nom_ia: str

    :rtype: Output
    """
    return 'do some magic!'
