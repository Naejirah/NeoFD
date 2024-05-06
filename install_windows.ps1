try{
    $listPythonVersion = py --list
}
catch{}

$isInstalledPyScript = $false
$isInstalledPyIa = $false

if($listPythonVersion -match "Python 3.11")
{
    $isInstalledPyScript = $true
}
if($listPythonVersion -match "Python 3.8")
{
    $isInstalledPyIa = $true
}

$installDir = Get-Location

# 1 - Installation Python 3.11.9 pour l'API 
if(-not $isInstalledPyScript)
{
    # Define the Python version and download URL
    $pythonVersion = "3.11.9"
    $pythonUrl = "https://www.python.org/ftp/python/$pythonVersion/python-$pythonVersion-amd64.exe"

    # Download the Python installer
    Invoke-WebRequest -Uri $pythonUrl -OutFile "python-$pythonVersion-amd64.exe"
    
    # Install Python silently
    Start-Process -FilePath "python-$pythonVersion-amd64.exe" -ArgumentList "/quiet PrependPath=1" -Wait

    # Cleanup the downloaded installer
    Remove-Item "python-$pythonVersion-amd64.exe"
}

py -3.11 -m pip install virtualenv


# 2 - Installation de la version de python pour les IA
if(-not $isInstalledPyIa)
{
    # Define the Python version and download URL
    $pythonVersion = "3.8.10"
    $pythonUrl = "https://www.python.org/ftp/python/$pythonVersion/python-$pythonVersion-amd64.exe"

    # Download the Python installer
    Invoke-WebRequest -Uri $pythonUrl -OutFile "python-$pythonVersion-amd64.exe"

    # Install Python silently
    Start-Process -FilePath "python-$pythonVersion-amd64.exe" -ArgumentList "/quiet PrependPath=1" -Wait

    # Cleanup the downloaded installer
    Remove-Item "python-$pythonVersion-amd64.exe"
}
py -3.8 -m pip install virtualenv
py -3.8 -m pip install --upgrade pip

# 3 - Installation falcon
Write-Host "`n`n Installation de Falcon `n`n"
Set-Location IA/falcon/install
.\install_windows.ps1
 
# 4 - Installation blip
Write-Host "`n`n Installation de BLIP `n`n"
Set-Location IA/blip/install
.\install_windows.ps1

# 5 - Installation stable-diffusion
Write-Host "`n`n Installation de Stable-diffusion `n`n"
Set-Location IA/stable-diffusion/install
.\install_windows.ps1
