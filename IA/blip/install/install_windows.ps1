Set-Location ../

if(-not(Test-Path -Path "models"))
{
    mkdir models
}

try {
    py -3.8 -m virtualenv blipEnv
    blipEnv\Scripts\activate.ps1

    #Gestion des cuda
    py -3.8 -m pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118  
    py -3.8 -m pip install transformers einops 

    #gpu
    py -3.8 -m pip install accelerate
    git lfs install

    py -3.8 install/deploy.py
}
catch {
    Write-Host "Erreur installation BLIP" -ForegroundColor Red
}

Set-Location ../../

