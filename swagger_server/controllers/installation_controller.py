import connexion
import six

from swagger_server.models.img import Img  # noqa: E501
from swagger_server import util


def ajout_fichier_installation(body, plateforme, fichiers, nom_ia):  # noqa: E501
    """Ajoute un nouveau Modele d&#x27;IA

    Add a new Img to the store # noqa: E501

    :param body: Create a new Img in the store
    :type body: dict | bytes
    :param plateforme: Nom de l&#x27;IA retourné par /IA/trouverParCategorie
    :type plateforme: str
    :param fichiers: Un fichier setup.py (si hugging face) ou un fichier shell + requires.txt
    :type fichiers: str
    :param nom_ia: Nom de l&#x27;IA retourné par /IA/trouverParCategorie
    :type nom_ia: str

    :rtype: Img
    """
    if connexion.request.is_json:
        body = Img.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def ajout_fichier_installation(base64, plateforme, fichiers, nom_ia):  # noqa: E501
    """Ajoute un nouveau Modele d&#x27;IA

    Add a new Img to the store # noqa: E501

    :param base64: 
    :type base64: str
    :param plateforme: Nom de l&#x27;IA retourné par /IA/trouverParCategorie
    :type plateforme: str
    :param fichiers: Un fichier setup.py (si hugging face) ou un fichier shell + requires.txt
    :type fichiers: str
    :param nom_ia: Nom de l&#x27;IA retourné par /IA/trouverParCategorie
    :type nom_ia: str

    :rtype: Img
    """
    return 'do some magic!'


def ajout_fichier_lancement(body, plateforme, fichier, nom_ia):  # noqa: E501
    """Ajoute un fichier d&#x27;installation

    Add a new Img to the store # noqa: E501

    :param body: Create a new Img in the store
    :type body: dict | bytes
    :param plateforme: Nom de l&#x27;IA retourné par /IA/trouverParCategorie
    :type plateforme: str
    :param fichier: Un fichier inference.py
    :type fichier: str
    :param nom_ia: Nom de l&#x27;IA retourné par /IA/trouverParCategorie
    :type nom_ia: str

    :rtype: Img
    """
    if connexion.request.is_json:
        body = Img.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def ajout_fichier_lancement(base64, plateforme, fichier, nom_ia):  # noqa: E501
    """Ajoute un fichier d&#x27;installation

    Add a new Img to the store # noqa: E501

    :param base64: 
    :type base64: str
    :param plateforme: Nom de l&#x27;IA retourné par /IA/trouverParCategorie
    :type plateforme: str
    :param fichier: Un fichier inference.py
    :type fichier: str
    :param nom_ia: Nom de l&#x27;IA retourné par /IA/trouverParCategorie
    :type nom_ia: str

    :rtype: Img
    """
    return 'do some magic!'


def get_fichier_installation(nom_ia, plateforme=None):  # noqa: E501
    """Retourne les fichiers d&#x27;installation d&#x27;une IA

    Add a new Img to the store # noqa: E501

    :param nom_ia: Nom de l&#x27;IA retourné par /IA/trouverParCategorie
    :type nom_ia: str
    :param plateforme: Nom de l&#x27;IA retourné par /IA/trouverParCategorie
    :type plateforme: str

    :rtype: Img
    """
    return 'do some magic!'


def get_fichier_lancement(nom_ia, plateforme=None):  # noqa: E501
    """Retourne les fichiers de Generation

    Add a new Img to the store # noqa: E501

    :param nom_ia: Nom de l&#x27;IA retourné par /IA/trouverParCategorie
    :type nom_ia: str
    :param plateforme: Nom de l&#x27;IA retourné par /IA/trouverParCategorie
    :type plateforme: str

    :rtype: Img
    """
    return 'do some magic!'


def lancement_fichier_installation(nom_ia, plateforme):  # noqa: E501
    """Lancement d&#x27;une installation d&#x27;une IA

    Add a new Img to the store # noqa: E501

    :param nom_ia: Nom de l&#x27;IA retourné par /IA/trouverParCategorie
    :type nom_ia: str
    :param plateforme: Nom de l&#x27;IA retourné par /IA/trouverParCategorie
    :type plateforme: str

    :rtype: Img
    """
    return 'do some magic!'


def suppr_fichier_installation(nom_ia, plateforme):  # noqa: E501
    """Supprime un fichier d&#x27;installation

    Add a new Img to the store # noqa: E501

    :param nom_ia: Nom de l&#x27;IA retourné par /IA/trouverParCategorie
    :type nom_ia: str
    :param plateforme: Nom de l&#x27;IA retourné par /IA/trouverParCategorie
    :type plateforme: str

    :rtype: Img
    """
    return 'do some magic!'


def suppr_fichier_lancement(nom_ia):  # noqa: E501
    """Supprime un fichier de Generation

    Add a new Img to the store # noqa: E501

    :param nom_ia: Nom de l&#x27;IA retourné par /IA/trouverParCategorie
    :type nom_ia: str

    :rtype: Img
    """
    return 'do some magic!'
