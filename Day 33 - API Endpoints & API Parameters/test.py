import requests

response    = requests.get(url="http://api.open-notify.org/iss-now.json")
status_code = response.status_code
data        = response.json()

response.raise_for_status()

""" Manually handling Exceptions """
# try:
#     if status_code == 404:
#         raise Exception("That resource does not exist.")
#     elif response.status_code == 401:
#         raise Exception("You are not authorized to access this data!.")
# except Exception as e:
#     print(e)
