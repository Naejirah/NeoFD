Set-Location ../

if(-not(Test-Path -Path "models"))
{
    mkdir models
}

try {
    py -3.8 -m virtualenv falconEnv
    falconEnv\Scripts\activate.ps1

    #Gestion des cuda
    falconEnv\Scripts\pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118  
    falconEnv\Scripts\pip install transformers einops 

    #gpu
    falconEnv\Scripts\pip install accelerate
    git lfs install

    falconEnv\Scripts\python install/deploy.py
}
catch {
    Write-Host "Erreur installation Falcon7b" -ForegroundColor Red
}

deactivate

Set-Location ../../

