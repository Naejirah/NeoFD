Set-Location ../

if(-not(Test-Path -Path "models"))
{
    mkdir models
}

py -3.8 -m virtualenv stable-diffusionEnv
stable-diffusionEnv\Scripts\activate.ps1
pip --version 
Set-Location stablediffusion/

try {
    #Gestion des cuda
    ..\stable-diffusionEnv\Scripts\pip install -r .\requirements.txt 
    ..\stable-diffusionEnv\Scripts\pip install transformers==4.19.2 diffusers invisible-watermark
    
    ..\stable-diffusionEnv\Scripts\pip uninstall torch
    ..\stable-diffusionEnv\Scripts\pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
    #Cp ldm
    # pip install
    Copy-Item -Path "ldm/" -Destination "../stable-diffusionEnv/Lib/site-packages" -Recurse
    ..\stable-diffusionEnv\Scripts\pip install pytorch-lightning==1.4.2   
    ..\stable-diffusionEnv\Scripts\pip install kornia==0.6 
    ..\stable-diffusionEnv\Scripts\pip install open-clip-torch==2.7.0   
}
catch {
    Write-Host "Erreur installation Falcon7b" -ForegroundColor Red
}

deactivate 

Set-Location ../../../

