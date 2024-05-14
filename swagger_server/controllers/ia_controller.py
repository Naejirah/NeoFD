import connexion
import six

from os import listdir
from os.path import isfile, exists
from swagger_server.models.input_ia import InputIA  # noqa: E501
from swagger_server.models.output import Output  # noqa: E501
from swagger_server import util


def add_ia(body, nom_ia, categorie, utilisable):  # noqa: E501
    """Ajoute une nouvelle IA

    Ajoute une nouvelle IA # noqa: E501

    :param body: Parametres pour ajouter une IA
    :type body: dict | bytes
    :param nom_ia: Nom de l&#x27;IA
    :type nom_ia: str
    :param categorie: Nom de la catégorie
    :type categorie: str
    :param utilisable: Si l&#x27;IA est déjà installé mettre true et le chemin de la virtualEnv dans le body sinon false et remplir au moins un champs install du body
    :type utilisable: bool

    :rtype: Output
    """
    if connexion.request.is_json:
        body = InputIA.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_ia(categorie):  # noqa: E501
    """Trouve une IA pour répondre à un besoin

    Trouve une IA pour répondre à un besoin # noqa: E501

    :param categorie: Status values that need to be considered for filter
    :type categorie: str

    :rtype: List[Output]
    """
    liste_retour = []
    chemin = f'./toolkit/{categorie}'
    if(exists(chemin)):
        for fichier in listdir(chemin):
            liste_retour.append({"output":fichier})

    return liste_retour
