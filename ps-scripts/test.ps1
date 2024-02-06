# This will move all items from this dependencies folder over to the actual script
# Does this have access to the envs?

function Run{
    Set-Location ".\dir2\ArcGIS-Earth-Mobile"
    python script.py
}


Run