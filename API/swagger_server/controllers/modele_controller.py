import connexion
import six

from swagger_server.models.img import Img  # noqa: E501
from swagger_server import util


def add_modele(body, nom_ia):  # noqa: E501
    """Ajoute un nouveau Modele d&#x27;IA

    Add a new Img to the store # noqa: E501

    :param body: Create a new Img in the store
    :type body: dict | bytes
    :param nom_ia: Nom de l&#x27;IA retourné par /IA/trouverParCategorie
    :type nom_ia: str

    :rtype: Img
    """
    if connexion.request.is_json:
        body = Img.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def add_modele(base64, nom_ia):  # noqa: E501
    """Ajoute un nouveau Modele d&#x27;IA

    Add a new Img to the store # noqa: E501

    :param base64: 
    :type base64: str
    :param nom_ia: Nom de l&#x27;IA retourné par /IA/trouverParCategorie
    :type nom_ia: str

    :rtype: Img
    """
    return 'do some magic!'


def del_modele(nom_ia, modele_ia):  # noqa: E501
    """Supprime un Modele de l&#x27;IA

    Les noms des IA sont disponible via la méthode GET /IA/trouverParCategorie. Les noms des Modeles d&#x27;IA sont disponible via la méthode GET /modele/{nomIA} # noqa: E501

    :param nom_ia: Nom de l&#x27;IA
    :type nom_ia: str
    :param modele_ia: Modele de l&#x27;IA à supprimer
    :type modele_ia: str

    :rtype: Img
    """
    return 'do some magic!'


def get_modele(nom_ia):  # noqa: E501
    """Donne les Modeles de l&#x27;IA

    Add a new Img to the store # noqa: E501

    :param nom_ia: Nom de l&#x27;IA retourné par /IA/trouverParCategorie
    :type nom_ia: str

    :rtype: Img
    """
    return 'do some magic!'
