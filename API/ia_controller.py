import connexion
import six

import subprocess
from os import listdir, mkdir
from os.path import isfile, exists
from swagger_server.models.input_ia import InputIA  # noqa: E501
from swagger_server.models.output import Output  # noqa: E501
from swagger_server import util

def send_symlink(src, dest):
    process = subprocess.Popen(["./apiEnv/Scripts/python", "./toolkit/symlink.py", "-src", src, "-dest", dest], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode == 0:
        print("Le subprocess s'est terminé avec succès.")
    else:
        print("Le subprocess a échoué avec le code de sortie :", process.returncode)

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
    retour = {"output":""}
    chemin_ia = f'./IA/{nom_ia}'
    chemin_toolkit = f'./toolkit/{categorie}/{nom_ia}'
    if(not exists(chemin_ia) and exists(f'./toolkit/{categorie}')):
        mkdir(chemin_ia)
        mkdir(chemin_toolkit)
        chemin_install = chemin_ia+'/'+"install"
        if(body["install_windows_chemin_absolu"] != ""):
            mkdir(chemin_install)
            send_symlink(body["install_windows_chemin_absolu"], chemin_install+'/'+"install_windows.ps1")
        if(body["install_mac_chemin_absolu"]):
            if(not exists(chemin_install)):
                mkdir(chemin_install)
            send_symlink(body["install_mac_chemin_absolu"], chemin_install+'/'+"install_mac.ps1")
        if(body["install_linux_chemin_absolu"]):
            if(not exists(chemin_install)):
                mkdir(chemin_install)
            send_symlink(body["install_linux_chemin_absolu"], chemin_install+'/'+"install_linux.ps1")
        if(body["inference_chemin_absolu"]):
            send_symlink(body["inference_chemin_absolu"], chemin_toolkit+'/'+"inference.py")
        if(body["param_chemin_absolu"]):
            send_symlink(body["param_chemin_absolu"], chemin_toolkit+'/'+"param.json")
        if(body["venv_chemin_absolu"]):
            send_symlink(body["venv_chemin_absolu"], chemin_ia+'/'+nom_ia+"Env")
        retour["output"] = chemin_ia
    return retour


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
