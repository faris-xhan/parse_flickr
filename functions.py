from user_agents import USER_AGENTS
import requests
import random
import json
import os

class Functions:
    """ Usefull functions that will help me later """
    
    def send_requests(self, url, params=None):
        """ send_requests(url) -> response object
            send requests to url and return the response object 
            url: url to send requests 
            params: parameters for the request """

        if params:
            r = requests.get(url, params=params, headers=self.get_user_agent())
        else:
            r = requests.get(url, headers=self.get_user_agent())

        try:
            r.raise_for_status()
        except Exception as e:
            print(str(e))
            exit(1)
            
        print(f"{url} Request made successfully.")
        return r
    
    def download_file(self, url, file_name, location):
        """ download_file(url, file_name, location) -> Download file from url
            url: url of the file to be download
            file_name: name of the file 
            location: location to download the file """
        location = self.make_dir(location)
        r = self.send_requests(url)
        
        with open(f'{location}/{file_name}', 'wb') as f:
            for chunk in r.iter_contents(1000):
                f.write(chunk)

        print(f"{file_name} Downloaded Successfully.")
    
    def get_user_agent(self):
        """ get_user_agent() -> fake_user_agent 
            Get a fake user agent from user_agents.py to send requests"""
        return {
            "User-Agent": random.choice(USER_AGENTS)
        }
    
    def dump_json(self, dict_obj, file_name, location):
        """ dump_json(dict_obj, file_name, location) -> Create json file of that data 
            dump_json saves the given data in json format 
            dict_obj: Dictionary Data to be saved
            file_name: Name of the file to be saved (.json extension is optional)
            location: Directory you want to save it in """
        location = self.make_dir(location)

        if not file_name.endswith(".json"):
            file_name = file_name + ".json"
        try:
            with open(f"{location}/{file_name}", "w") as f:
                json.dump(dict_obj, f, indent=3)
            print(f"{file_name} Saved Successfully")
        
        except Exception as e:
            print(str(e))
            exit(1)
    
    def _dict_to_object(self, dict_obj):
        """ _dict_to_object(dict_obj) -> turn dictionary key values pair to attributes 
            of that class.
            dict_obj: Dictionary Data """

        for key, value in dict_obj.items():
            setattr(self, key, value)
    
    def make_dir(self, location):
        """ make_dirs(dir_location) -> abslute path if possible
            make sure that the given directory is valid or not.
            location: str or path of dir"""
        try:
            if not os.path.exists(location):
                os.makedirs(location)
                return os.path.abspath(location)
            return os.path.abspath(location)
        except Exception as e:
            print(str(e))
            exit(1)