import connexion
import six

from swagger_server.models.img import Img  # noqa: E501
from swagger_server import util


def add_img(body, nom_ia, categorie, utilisable):  # noqa: E501
    """Ajoute une nouvelle IA

    Add a new Img to the store # noqa: E501

    :param body: Create a new Img in the store
    :type body: dict | bytes
    :param nom_ia: Nom de l&#x27;IA
    :type nom_ia: str
    :param categorie: Nom de la catégorie
    :type categorie: str
    :param utilisable: Si l&#x27;IA est déjà installé mettre true et le chemin de la virtualEnv dans le body sinon false et remplir au moins un champs install du body
    :type utilisable: bool

    :rtype: Img
    """
    if connexion.request.is_json:
        body = Img.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def find_imgs_by_status(categorie):  # noqa: E501
    """Trouve une IA pour répondre à un besoin

    Multiple status values can be provided with comma separated strings # noqa: E501

    :param categorie: Status values that need to be considered for filter
    :type categorie: str

    :rtype: List[Img]
    """
    return 'do some magic!'
