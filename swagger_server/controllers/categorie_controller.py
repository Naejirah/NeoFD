import connexion
import six

from os import listdir, remove, symlink
from shutil import rmtree
from os.path import isfile, exists
from swagger_server.models.output import Output  # noqa: E501
from swagger_server import util


def add_categorie(nom_categorie):  # noqa: E501
    """Ajoute une nouvelle catégorie pour les IA

    Ajoute une nouvelle catégorie pour les IA # noqa: E501

    :param nom_categorie: Nom de la categorie
    :type nom_categorie: str

    :rtype: Output
    """
    return 'do some magic!'


def get_categorie():  # noqa: E501
    """Donne les catégories existantes

    Donne les catégories existantes # noqa: E501


    :rtype: List[Output]
    """
    liste_retour = []
    chemin = f'./toolkit'
    if(exists(chemin)):
        for fichier in listdir(chemin):
            if(not isfile(chemin+"/"+fichier)):
                liste_retour.append({"output":fichier})

    return liste_retour
