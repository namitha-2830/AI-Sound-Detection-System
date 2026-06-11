import requests
from datetime import datetime

url = "https://script.google.com/macros/s/AKfycbxWMxDqok_p7x1LBwQCYQBPdzkkEJqw8gV2cE45qbkifJlD0Szzsfy8H-QscMYneThg2Q/exec"

data = {
    "time": str(datetime.now()),
    "sound": predicted_class,
    "alert": "Visual Alert"
}

requests.post(url, json=data)