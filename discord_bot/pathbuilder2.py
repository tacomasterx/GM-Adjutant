import json
import requests

# Pathbuilder
async def get_pathbuilder_character(char_code):
    url = f"https://pathbuilder2e.com/json.php?id={char_code}"
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0"
    }
    req = requests.get(url, headers=headers, timeout=10)
    if req.status_code == 200:
        return(json.dumps( req.json() ))
    else:
        return(json.dumps({"success": False, "status_code": req.status_code}))


