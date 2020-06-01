from functions import Functions
from posts import Posts
from datetime import datetime
import re


class Flickr(Functions):
    """ Flickr class that will send requests to the flickr and download photos"""

    def __init__(self, username):
        """ Initialize username, get user id and user account informations."""
        self.username = username
        self.user_id, self.api_key = self._parse_user_id_and_api_key()
        self.get_profile_data()

    def get_profile_data(self):
        """ Send requests to the flickr and set user account information as 
        and attributes to the  class """

        url = "https://api.flickr.com/services/rest"
        params = {
            "datecreate": 1,
            "extras": "icon_urls,safe_search,galleries_view_layout_pref, has_stats,expand_bbml,social_urls,with_stats",
            "user_id": self.user_id,
            "viewerNSID": "",
            "method": "flickr.profile.getProfile",
            "csrf": "",
            "api_key": self.api_key,
            "format": "json",
            "hermes": 1,
            "hermesClient": 1,
            "reqId": "51cbd45e",
            "nojsoncallback": 1
        }

        r = self.send_requests(url, params=params).json()
        self._dict_to_object(r['profile'])
        self._dict_to_object(r['stats'])
        self.join_date = datetime.fromtimestamp(
            int(self.join_date)).strftime("%b %d %Y %H:%M:%S")

    def save_profile_data(self):
        """ Save profile in json format in current directory """
        self.dump_json(self.__dict__, self.username, ".")

    def get_posts(self):
        """ get_posts() -> Posts Instance 
            Create a Posts instance  """
        return Posts(self.user_id, self.api_key, download=True)._get_contents()
        

    def _parse_user_id_and_api_key(self):
        """ _parse_user_id() -> flickr user id, api_key """
        self.url = f"https://www.flickr.com/people/{self.username}"

        r = self.send_requests(self.url).text

        regex = re.compile(r"\d+@[N]\d\d")
        account_id =  regex.search(r)[0]

        api_key = re.compile(r"site_key.*").findall(r)[1]
        api_key = re.compile(r"\w+").findall(api_key)[1]
        
        return account_id, api_key
