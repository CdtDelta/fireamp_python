# Just playing around with the FireAMP API
#
# Tom Yarrish
# Version 0.1

import requests

fa_client_id = ""
fa_api_key = ""
fireamp_baseurl = "https://api.amp.cisco.com/v1/"
fireamp_headers = {"Accept-Encoding" : "gzip, deflate"}

fireamp_req = requests.Session()
fireamp_req.auth = (fa_client_id, fa_api_key)

search_filename = raw_input("Enter the file to search for: ")

fireamp_filename = "/computers/activity?q=" + search_filename + "&limit=5"

req = fireamp_req.get(fireamp_baseurl + fireamp_filename)

print req.text
# print req.json()