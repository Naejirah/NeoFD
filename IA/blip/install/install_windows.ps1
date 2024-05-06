Set-Location ../

if(-not(Test-Path -Path "models"))
{
    mkdir models
}

try {
    py -3.8 -m virtualenv blipEnv
    blipEnv\Scripts\activate.ps1

    #Gestion des cuda
    blipEnv\Scripts\pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
    blipEnv\Scripts\pip install install transformers einops --ignore-installed

    #gpu
    blipEnv\Scripts\pip install install accelerate --ignore-installed

    blipEnv\Scripts\python install/deploy.py
}
catch {
    Write-Host "Erreur installation BLIP" -ForegroundColor Red
}

deactivate

Set-Location ../../

