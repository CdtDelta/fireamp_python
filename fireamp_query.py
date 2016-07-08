# This script is utilized to query the fireAMP database
#
# This is a python 3 version of the script
# it will search against hash, file names, IP whatever the API takes
#
# Tom Yarrish
# Version 0.1
import requests
import argparse
import collections

FireampResult = collections.namedtuple(
    'FireampResult',
    'active, connector_guid, hostname, links'
)

def query_fireamp_server(client_id, client_api):
    limit = 25  # We'll add this as an option later
    search_term = input('Enter the term to search for: ')
    # If you do a requests session, you can do the authorization portion
    fireamp_req = requests.Session()
    # This handles the API authorization
    fireamp_req.auth = (client_id, client_api)
    # So this part will end up being appended to the fireamp_baseurl, you can modify this line to do other searches
    # IP, Hash, etc
    fireamp_filename = "/computers/activity?q=" + search_term + "&limit=" + str(limit)
    # This part does the actual search
    req = fireamp_req.get(fireamp_baseurl + fireamp_filename)
    return req.json()


def parse_fireamp_results(query_results):
    data_results = query_results['data']

    fireamp_hits = [
        FireampResult(**f)
        for f in data_results
    ]
    fireamp_hits.sort(key=lambda f:f.hostname)

    return fireamp_hits

# The base URL is the starting point. Everything gets added on to that
fireamp_baseurl = "https://api.amp.sourcefire.com/v0/"

# The headers are recommended by the API docs
fireamp_headers = {"Accept-Encoding" : "gzip, deflate"}

def main():
    parser = argparse.ArgumentParser(description='Query the FireAMP server.')
    parser.add_argument('-c', dest='client_id', help='FireAMP Client ID', required=True)
    parser.add_argument('-a', dest='client_api', help='FireAMP API Key', required=True)
    args = parser.parse_args()

# If you want to hardcode the client ID and FireAMP API, uncomment out these lines and comment out
# the argparse section above
#     fireamp_client_id = ''
#     fireamp_client_api = ''
#     fireamp_results = query_fireamp_server(fireamp_client_id, fireamp_client_api)

    fireamp_results = query_fireamp_server(args.client_id, args.client_api)
    search_hits = parse_fireamp_results(fireamp_results)

    for hit in search_hits:
        print('Hostname: {}'.format(hit.hostname))

if __name__ == '__main__':
    main()