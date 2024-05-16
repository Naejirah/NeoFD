py -3.11 -m virtualenv apiEnv
apiEnv\Scripts\pip install -r .\requirements.txt 
apiEnv\Scripts\pip install Flask
apiEnv\Scripts\pip install connexion[uvicorn]
apiEnv\Scripts\pip install a2wsgi
apiEnv\Scripts\pip install pyuac
apiEnv\Scripts\pip install pypiwin32  
$installDir = Get-Location
Remove-Item .\toolkit\txt2img\stable-diffusion\inference.py
apiEnv\Scripts\python ./toolkit/symlink.py -src "$installDir/IA/stable-diffusion/stablediffusion/scripts/txt2img.py" -dest "./toolkit/txt2img/stable-diffusion/inference.py"
# Launch with apiEnv\Scripts\python -m swagger_server 

# Set-Location ../