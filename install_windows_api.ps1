py -3.11 -m virtualenv apiEnv
apiEnv\Scripts\pip install -r .\requirements.txt 
apiEnv\Scripts\pip install Flask
apiEnv\Scripts\pip install connexion[uvicorn]
apiEnv\Scripts\pip install a2wsgi
# Launch with apiEnv\Scripts\python -m swagger_server 

# Set-Location ../