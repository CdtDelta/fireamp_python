# Just playing around with the FireAMP API
#
# Link to API docs
# https://api-docs.amp.sourcefire.com/?api_host=api.amp.sourcefire.com
#
# Tom Yarrish
# Version 0.1
#
# TODO: Write output from trajectory to a file to look at in order to parse

import requests
import json
import itertools

def parse_data(output_list):
    for items in output_list:
        event_list = items['hostname'], items['links']['trajectory']
    return event_list

# If the client ID and API Key ever change, then just change the next two variables
fa_client_id = ""
fa_api_key = ""

# The base URL is the starting point. Everything gets added on to that
fireamp_baseurl = "https://api.amp.cisco.com/v1/"

# The headers are recommended by the API docs
fireamp_headers = {"Accept-Encoding" : "gzip, deflate"}

# If you do a requests session, you can do the authorization portion
fireamp_req = requests.Session()

# This handles the API authorization
fireamp_req.auth = (fa_client_id, fa_api_key)

search_filename = raw_input("Enter the file to search for: ")

# So this part will end up being appended to the fireamp_baseurl, you can modify this line to do other searches
# IP, Hash, etc
fireamp_filename = "/computers/activity?q=" + search_filename + "&limit=10"

# This part does the actual search
req = fireamp_req.get(fireamp_baseurl + fireamp_filename)

# Ok if we do the output in json, then it seems a bit easier to parse the output.
# if you use text, the type is "Unicode"
output_text = req.json()
#output_text = req.text

print type(output_text)

# The json output ends up in a Python dict.  However the structure is a dict then list then a dict again.
# For the first key in the dict, your options are version, data, and metadata
# Then you have a numbered list, and within the list is another dict
# So the example below prints out the first hostname that matches
#print output_text['data'][0]['hostname']

#print output_text['version']
#print output_text['metadata']['results']['total']

#test_one = output_text['data'][0]
#for keys, values in test_one.iteritems():
#    print keys

#test_two = output_text['data']
#print test_two[0]

fireamp_alerts = parse_data(output_text['data'])

print type(fireamp_alerts)
print fireamp_alerts

new_req = fireamp_req.get(fireamp_alerts[1])

new_req_output = new_req.json()
print new_req_output