import connexion
import six

from swagger_server.models.img import Img  # noqa: E501
from swagger_server import util


def add_categorie(body, nom_categorie):  # noqa: E501
    """Ajoute un nouveau Modele d&#x27;IA

    Add a new Img to the store # noqa: E501

    :param body: Create a new Img in the store
    :type body: dict | bytes
    :param nom_categorie: Nom de l&#x27;IA retourné par /IA/trouverParCategorie
    :type nom_categorie: str

    :rtype: Img
    """
    if connexion.request.is_json:
        body = Img.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def add_categorie(base64, nom_categorie):  # noqa: E501
    """Ajoute un nouveau Modele d&#x27;IA

    Add a new Img to the store # noqa: E501

    :param base64: 
    :type base64: str
    :param nom_categorie: Nom de l&#x27;IA retourné par /IA/trouverParCategorie
    :type nom_categorie: str

    :rtype: Img
    """
    return 'do some magic!'


def get_categorie():  # noqa: E501
    """Donne les catégories existantes

    Add a new Img to the store # noqa: E501


    :rtype: Img
    """
    return 'do some magic!'
