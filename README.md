# Projet-Master

## Installation du projet

1. Windows

    1. Installation de git via https://gitforwindows.org/

    2. Installer les prérequis des IA
    ```commandline
    git clone https://github.com/Naejirah/NeoFD.git
    ./install_windows
    ``` 

## Falcon

IA pour la génération de texte

1. Lancement
```commandline
IA\falcon\stableEnv\Scripts\activate.ps1
py -3.8 ./toolkit/inference_falcon7b.py
``` 

2. Résultat

Les résultats sont visibles dans l'interpréteur de commande

3. Post lancement
```commandline
deactivate
``` 

## BLIP

IA pour la génération de texte à partir d'une image

1. Lancement
```commandline
IA\blip\stableEnv\Scripts\activate.ps1
py -3.8 ./toolkit/inference_blip.py
``` 

2. Résultat

Les résultats sont visibles dans l'interpréteur de commande

3. Post lancement
```commandline
deactivate
``` 

## Stable-diffusion

IA pour générer des images et améliorer des images
https://github.com/Stability-AI/stablediffusion?tab=readme-ov-file

1. Lancement
```commandline
IA\stable-diffusion\stableEnv\Scripts\activate.ps1
py -3.8 IA/stable-diffusion/stablediffusion/scripts/txt2img.py --prompt "a professional photograph of an astronaut riding a horse" --ckpt [ckpt] --config IA/stable-diffusion/stablediffusion/configs/stable-diffusion/v2-inference-v.yaml --H 512 --W 512 --bf16 --device cuda
``` 

2. Résultat

Les résultats sont visibles dans outputs/

3. Post lancement
```commandline
deactivate
``` 

## Liens importants :
<ul>
  <li>-Falcon 7b : https://huggingface.co/tiiuae/falcon-7b/tree/main</li>
  <li>-https://stablediffusionweb.com/</li>
  <li>-https://huggingface.co/</li>
  <li>-https://github.com/AUTOMATIC1111/stable-diffusion-webui</li>
</ul>
