# This is a basic FireAMP module you can use with other python scripts
# it just has functions to do different queries against FireAMP.
# You still need to pass it your API information
#
# Tom Yarrish
# Version 0.1
import requests

def fireamp_query_activity(client_id, client_api, query_limit):
    search_term = input('Enter the term to search for: ')
    # Set up a requests session, in order to do the authorization portion
    fireamp_req = requests.Session()
    # This handles the API authorization
    fireamp_req.auth = (client_id, client_api)
    # So this part will end up being appended to the fireamp_baseurl
    fireamp_filename = "/computers/activity?q={}&limit={}".format(search_term, query_limit)
    # This part does the actual search
    req = fireamp_req.get(fireamp_baseurl + fireamp_filename)
    return req.json()


def fireamp_query_hostname(client_id, client_api, query_limit):
    hostname = input('Enter the hostname to search for: ')
    # Set up a requests session, in order to do the authorization portion
    fireamp_req = requests.Session()
    # This handles the API authorization
    fireamp_req.auth = (client_id, client_api)
    # So this part will end up being appended to the fireamp_baseurl
    fireamp_filename = "/computers?hostname={}&limit={}".format(hostname, query_limit)
    # This part does the actual search
    req = fireamp_req.get(fireamp_baseurl + fireamp_filename)
    return req.json()


def fireamp_query_internalip(client_id, client_api, query_limit):
    internal_ip = input('Enter the internal ip to search for: ')
    # Set up a requests session, in order to do the authorization portion
    fireamp_req = requests.Session()
    # This handles the API authorization
    fireamp_req.auth = (client_id, client_api)
    # So this part will end up being appended to the fireamp_baseurl
    fireamp_filename = "/computers?internal_ip={}&limit={}".format(internal_ip, query_limit)
    # This part does the actual search
    req = fireamp_req.get(fireamp_baseurl + fireamp_filename)
    return req.json()


def fireamp_query_externalip(client_id, client_api, query_limit):
    external_ip = input('Enter the external ip to search for: ')
    # Set up a requests session, in order to do the authorization portion
    fireamp_req = requests.Session()
    # This handles the API authorization
    fireamp_req.auth = (client_id, client_api)
    # So this part will end up being appended to the fireamp_baseurl,
    fireamp_filename = "/computers?external_ip={}&limit={}".format(external_ip, query_limit)
    # This part does the actual search
    req = fireamp_req.get(fireamp_baseurl + fireamp_filename)
    return req.json()

def main():
    pass

# The base URL is the starting point. Everything gets added on to that
fireamp_baseurl = "https://api.amp.cisco.com/v1/"

# The headers are recommended by the API docs
fireamp_headers = {"Accept-Encoding" : "gzip, deflate", 'user-agent' : "FireAMP Python Script 1.0"}

if __name__ == '__main__':
    main()