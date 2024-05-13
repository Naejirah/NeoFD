import connexion
import six

from swagger_server.models.output import Output  # noqa: E501
from swagger_server import util


def add_categorie(body, nom_categorie):  # noqa: E501
    """Ajoute un nouveau Modele d&#x27;IA

    Add a new Output to the store # noqa: E501

    :param body: Create a new Output in the store
    :type body: dict | bytes
    :param nom_categorie: Nom de l&#x27;IA retourné par /IA/trouverParCategorie
    :type nom_categorie: str

    :rtype: Output
    """
    if connexion.request.is_json:
        body = Output.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def add_categorie(output, nom_categorie):  # noqa: E501
    """Ajoute un nouveau Modele d&#x27;IA

    Add a new Output to the store # noqa: E501

    :param output: 
    :type output: str
    :param nom_categorie: Nom de l&#x27;IA retourné par /IA/trouverParCategorie
    :type nom_categorie: str

    :rtype: Output
    """
    return 'do some magic!'


def get_categorie():  # noqa: E501
    """Donne les catégories existantes

    Add a new Output to the store # noqa: E501


    :rtype: Output
    """
    return 'do some magic!'
