Set-Location ../

if(-not(Test-Path -Path "models"))
{
    mkdir models
}

py -3.8 -m virtualenv stableEnv
stableEnv\Scripts\activate.ps1
pip --version 
Set-Location stablediffusion/

try {
    #Gestion des cuda
    ..\stableEnv\Scripts\pip install -r .\requirements.txt 
    ..\stableEnv\Scripts\pip install transformers==4.19.2 diffusers invisible-watermark
    
    ..\stableEnv\Scripts\pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
    #Cp ldm
    # pip install
    Copy-Item -Path "ldm/" -Destination "../stableEnv/Lib/site-packages" -Recurse
    ..\stableEnv\Scripts\pip install pytorch-lightning==1.4.2   
    ..\stableEnv\Scripts\pip install kornia==0.6 
    ..\stableEnv\Scripts\pip install open-clip-torch==2.7.0   
}
catch {
    Write-Host "Erreur installation Falcon7b" -ForegroundColor Red
}

deactivate 

Set-Location ../../../

