import connexion
import six

from os import listdir, mkdir
from os.path import isfile, join, exists
from swagger_server.models.output import Output  # noqa: E501
from swagger_server import util


def add_modele(body, nom_ia, modele_ia):  # noqa: E501
    """Ajoute un nouveau Modele d&#x27;IA

    Ajoute un nouveau Modele d&#x27;IA # noqa: E501

    :param body: Create a new Output in the store
    :type body: dict | bytes
    :param nom_ia: Nom de l&#x27;IA
    :type nom_ia: str
    :param modele_ia: Modele de l&#x27;IA
    :type modele_ia: str

    :rtype: Output
    """
    if connexion.request.is_json:
        body = Output.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def add_modele(output, nom_ia, modele_ia):  # noqa: E501
    """Ajoute un nouveau Modele d&#x27;IA

    Ajoute un nouveau Modele d&#x27;IA # noqa: E501

    :param output: 
    :type output: str
    :param nom_ia: Nom de l&#x27;IA
    :type nom_ia: str
    :param modele_ia: Modele de l&#x27;IA
    :type modele_ia: str

    :rtype: Output
    """
    return 'do some magic!'


def del_modele(nom_ia, modele_ia):  # noqa: E501
    """Supprime un Modele de l&#x27;IA

    Les noms des IA sont disponible via la méthode GET /IA/trouverParCategorie. Les noms des Modeles d&#x27;IA sont disponible via la méthode GET /modele/{nomIA} # noqa: E501

    :param nom_ia: Nom de l&#x27;IA
    :type nom_ia: str
    :param modele_ia: Modele de l&#x27;IA
    :type modele_ia: str

    :rtype: Output
    """
    return 'do some magic!'


def get_modele(nom_ia):  # noqa: E501
    """Donne les Modeles de l&#x27;IA

    Add a new Output to the store # noqa: E501

    :param nom_ia: Nom de l&#x27;IA retourné par /IA/trouverParCategorie
    :type nom_ia: str

    :rtype: Output
    """

    liste_retour = []
    chemin = f'outputs/{nom_categorie}/{nom_ia}'
    if(exists(chemin)):
        for fichier in listdir(chemin):
            liste_retour.append({"output":fichier})

    return liste_retour
