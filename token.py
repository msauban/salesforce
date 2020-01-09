import requests

params = {
    "grant_type": "password",
    "client_id": "3MVG92u_V3UMpV.iafsw913291i7s54wwHg3MuYNaQySYeX7sxooy6DlZ9Y2juG.CLmGqAV0Sd_1QzAA4j.zE", # Consumer Key
    "client_secret": "3293548326932855383", # Consumer Secret
    "username": "info@sesam.io.sesamdemo", # The email you use to login
    "password": "BouvetSesam1234" # Concat your password and your security token
        }
r = requests.post("https://test.salesforce.com/services/oauth2/token",params=params)
access_token = r.json().get("access_token")
instance_url = r.json().get("instance_url")
print("Access Token:", access_token)
print("Instance URL", instance_url)
