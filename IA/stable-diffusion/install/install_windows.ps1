Set-Location ../

if(-not(Test-Path -Path "models"))
{
    mkdir models
}

py -3.8 -m virtualenv stableEnv
stableEnv\Scripts\activate.ps1

Set-Location stablediffusion/

try {
    #Gestion des cuda
    py -3.8 -m pip install -r .\requirements.txt 
    py -3.8 -m pip install transformers==4.19.2 diffusers invisible-watermark
    py -3.8 -m pip install -e .
    py -3.8 -m pip uninstall torch
    py -3.8 -m pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

}
catch {
    Write-Host "Erreur installation Falcon7b" -ForegroundColor Red
}

deactivate 

Set-Location ../../../

