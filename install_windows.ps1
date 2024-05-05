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

# Installation Python 3.11.9 pour l'API 
if(-not $isInstalledPyScript)
{
    # Define the Python version and download URL
    $pythonVersion = "3.11.9"
    $pythonUrl = "https://www.python.org/ftp/python/$pythonVersion/python-$pythonVersion-amd64.exe"

    # répertoire d'install
    $installDir = Get-Location

    # Download the Python installer
    Invoke-WebRequest -Uri $pythonUrl -OutFile "python-$pythonVersion-amd64.exe"

    # Install Python silently
    Start-Process -FilePath "python-$pythonVersion-amd64.exe" -ArgumentList "/quiet InstallAllUsers=1 PrependPath=1" -Wait

    # Cleanup the downloaded installer
    Remove-Item "python-$pythonVersion-amd64.exe"
}

py -3.11 -m pip install virtualenv


if(-not $isInstalledPyIa)
{
    # Define the Python version and download URL
    $pythonVersion = "3.8.10"
    $pythonUrl = "https://www.python.org/ftp/python/$pythonVersion/python-$pythonVersion-amd64.exe"

    # répertoire d'install
    $installDir = Get-Location

    # Download the Python installer
    Invoke-WebRequest -Uri $pythonUrl -OutFile "python-$pythonVersion-amd64.exe"

    # Install Python silently
    Start-Process -FilePath "python-$pythonVersion-amd64.exe" -ArgumentList "/quiet InstallAllUsers=1 PrependPath=1" -Wait

    # Cleanup the downloaded installer
    Remove-Item "python-$pythonVersion-amd64.exe"
}
py -3.8 -m pip install virtualenv

