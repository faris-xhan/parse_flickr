import requests
import json
import os

class Functions:
    """ Usefull functions that will help me later """
    def send_requests(url):
        """ Send requests and return the response object """
        r = requests.get(url)
        try:
            r.raise_for_status()
        except Exception as e:
            print(str(e))
            exit(1)
        
        return r
    
    def download_file(url, file_name, location):
        """ Download Files """
       r = self.send_requests(url)
       with open(f'{location}/{file_name}', 'wb') as f:
           for chunk in r.iter_contents(1000):
               f.write(chunk)
        print(f"{file_name} Downloaded Successfully.")
    