
function Run{
    start powershell {Appium}
    start powershell {emulator -avd Pixel_4_API_30}
    start-sleep -seconds 5
    echo pwd
    Set-Location ".\ArcGIS-Earth-Mobile"; python script.py
    Get-Location | select -ExpandProperty Path
    echo "finished testing"
}

Run






