import connexion
import six

import subprocess
from os import listdir, mkdir, remove
from os.path import isfile, exists
from shutil import rmtree
from swagger_server.models.input_fichier_generation import InputFichierGeneration  # noqa: E501
from swagger_server.models.input_fichier_installation import InputFichierInstallation  # noqa: E501
from swagger_server.models.output import Output  # noqa: E501
from swagger_server import util

def send_symlink(src, dest):
    process = subprocess.Popen(["./apiEnv/Scripts/python", "./toolkit/symlink.py", "-src", src, "-dest", dest], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode == 0:
        print("Le subprocess s'est terminé avec succès.")
    else:
        print("Le subprocess a échoué avec le code de sortie :", process.returncode)


def add_fichier_installation(body, plateforme, nom_ia):  # noqa: E501
    """Ajoute un nouveau Modele d&#x27;IA

    Ajoute un nouveau Modele d&#x27;IA # noqa: E501

    :param body: Create a new Output in the store
    :type body: dict | bytes
    :param plateforme: Nom de l&#x27;IA retourné par /IA/trouverParCategorie
    :type plateforme: str
    :param nom_ia: Nom de l&#x27;IA retourné par /IA/trouverParCategorie
    :type nom_ia: str

    :rtype: Output
    """
    retour = {"output":""}
    chemin = f'./IA/{nom_ia}/install'
    if(not exists(chemin)):
        mkdir(chemin)
    
    existFichier = False
    for fichier in listdir(chemin):
        if(f"install_{plateforme}" in fichier):
            existFichier = True
    
    if(not existFichier):
        if(plateforme == "windows"):
            send_symlink(body['install_chemin_absolu'], chemin+f"/install_{plateforme}.ps1")
            retour["output"] = chemin+f"/install_{plateforme}.ps1"

    return retour


def ajout_fichier_lancement(body, nom_categorie, nom_ia):  # noqa: E501
    """Ajoute un fichier de generation

    Ajoute un fichier de generation et de paramètre # noqa: E501

    :param body: Create a new Output in the store
    :type body: dict | bytes
    :param nom_categorie: Nom de la categorie
    :type nom_categorie: str
    :param nom_ia: Nom de l&#x27;IA retourné par /IA/trouverParCategorie
    :type nom_ia: str

    :rtype: Output
    """
    retour = {"output":""}
    chemin = f'./toolkit/{nom_categorie}/{nom_ia}'
    if(not exists(chemin)):
        mkdir(chemin)
    
    existInference = False
    existParam = False
    for fichier in listdir(chemin):
        if(f"inference" in fichier):
            existInference = True
        if(f"param" in fichier):
            existParam = True   
    try:
        if(existInference and exists(body["inference_chemin_absolu"])):
            send_symlink(body["inference_chemin_absolu"], chemin+'/inference.py')

        if(existInference and exists(body["inference_chemin_absolu"])):
            send_symlink(body["inference_chemin_absolu"], chemin+'/inference.py')
        
        retour["output"] = chemin
    except:
        retour["output"] = "error"
    return retour


def get_fichier_generation(nom_categorie, nom_ia):  # noqa: E501
    """Retourne les fichiers de Generation

    Retourne les fichiers de Generation # noqa: E501

    :param nom_categorie: Nom de la categorie
    :type nom_categorie: str
    :param nom_ia: Nom de l&#x27;IA retourné par /IA/trouverParCategorie
    :type nom_ia: str

    :rtype: Output
    """
    if(exists(f'./toolkit/{nom_categorie}/{nom_ia}')):
        return {"output": f'./toolkit/{nom_categorie}/{nom_ia}'}
    else:
        return {"output": ""}


def get_fichier_installation(nom_ia):  # noqa: E501
    """Retourne les fichiers d&#x27;installation d&#x27;une IA

    Retourne les fichiers d&#x27;installation d&#x27;une IA # noqa: E501

    :param nom_ia: Nom de l&#x27;IA retourné par /IA/trouverParCategorie
    :type nom_ia: str

    :rtype: Output
    """
    if(exists(f'./IA/{nom_ia}/install')):
        return {"output": f'./IA/{nom_ia}/install'}
    else:
        return {"output": ""}

def lancement_fichier_installation(nom_ia, plateforme):  # noqa: E501
    """Lancement d&#x27;une installation d&#x27;une IA

    Lancement d&#x27;une installation d&#x27;une IA # noqa: E501

    :param nom_ia: Nom de l&#x27;IA retourné par /IA/trouverParCategorie
    :type nom_ia: str
    :param plateforme: Système d&#x27;exploitation
    :type plateforme: str

    :rtype: Output
    """
    retour = {"output":""}
    chemin = f'./IA/{nom_ia}/install'
    
    existFichier = False
    for fichier in listdir(chemin):
        if(f"install_{plateforme}" in fichier):
            existFichier = True

    if(existFichier):
        process = ""
        if(plateforme == "windows"):
            process = subprocess.Popen(["powershell.exe",f'./IA/{nom_ia}/install/install_{plateforme}.ps1'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        stdout,stderr = process.communicate()
        if process.returncode == 0:
            retour["output"] = f"./IA/{nom_ia}"
        else:
            print("Le subprocess a échoué avec le code de sortie :", process.returncode)


    return retour


def suppr_fichier_installation(nom_ia, plateforme):  # noqa: E501
    """Supprime un fichier d&#x27;installation

    Supprime un fichier d&#x27;installation # noqa: E501

    :param nom_ia: Nom de l&#x27;IA retourné par /IA/trouverParCategorie
    :type nom_ia: str
    :param plateforme: système d&#x27;exploitation
    :type plateforme: str

    :rtype: Output
    """
    retour = {"output": ""}
    chemin = f'./IA/{nom_ia}/install'
    if(exists(chemin)):
        for fichier in listdir(chemin):
            if(f"install_{plateforme}" in fichier):
                remove(chemin+'/'+fichier)
                retour["output"] = chemin+'/'+fichier
    return retour


def suppr_fichier_lancement(nom_categorie, nom_ia):  # noqa: E501
    """Supprime un fichier de Generation

    Supprime un fichier de Generation # noqa: E501

    :param nom_categorie: Nom de la categorie
    :type nom_categorie: str
    :param nom_ia: Nom de l&#x27;IA retourné par /IA/trouverParCategorie
    :type nom_ia: str

    :rtype: Output
    """
    retour = {"output": ""}
    chemin = f'./toolkit/{nom_categorie}/{nom_ia}'
    if(exists(chemin)):
        for fichier in listdir(chemin):
            remove(chemin+'/'+fichier)
        retour["output"] = chemin
    return retour
