import connexion
import six

from swagger_server.models.img import Img  # noqa: E501
from swagger_server import util


def generation_par_ia(nom_categorie, nom_ia, modele_ia, nom_fichier_parametre=None):  # noqa: E501
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
    return 'do some magic!'


def get_resultat(nom_categorie, nom_ia=None, modele_ia=None):  # noqa: E501
    """Accède aux résultats d&#x27;une IA

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
