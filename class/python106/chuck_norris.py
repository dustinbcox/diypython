#!/usr/bin/env python3

"""http://www.icndb.com/api/"""


import requests # pip install requests
import json
import time



class Chuck(object):
    """Use the www.icndb.com to get a random joke"""

    API_DOMAIN = 'api.icndb.com'

    def __init__(self):
        self._exclude = 'explicit'
        self._use_tls = False
        self._debug = False

    def _get_url(self, path):
        """Return the URL for the icndb"""
        if self._use_tls:
            scheme = 'https'
        else:
            scheme = 'http'
        return '{0}://{1}/{2}'.format(scheme, Chuck.API_DOMAIN, path)

    def joke(self):
        query= {'exclude': self._exclude}
        response = requests.get(self._get_url('jokes/random'), params= query)
        # Be respectful to the server - 1 per second is good
        time.sleep(1)

        if self._debug:
            print("DEBUG URL: ", response.url)
            print("DEBUG DATA: ", response.text)
        data = json.loads(response.text)
        if data['type'] != 'success':
            raise ValueError('Error when getting joke: ' + str(data))
        if self._debug:
            print("JOKE ID:", data['value']['id'])
        return data['value']['joke']

        

if __name__ == "__main__":
    chuck = Chuck()
    #chuck._debug = True
    for i in range(3):
        #print("Loop i = " + str(i))
        print(chuck.joke())
