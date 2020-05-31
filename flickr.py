from datetime import datetime
from functions import Functions
import re


class Flickr(Functions):
    """ Flickr class that will send requests to the flickr and download photos"""

    def __init__(self, username):
        """ Initialize username, get user id and user account informations."""
        self.username = username
        self.user_id = self._parse_user_id()
        self.get_profile()
    
    def get_profile(self):
        """ Send requests to the flickr and set user account information as 
        and attributes to the  class """

        url = "https://api.flickr.com/services/rest"
        params = {
            "datecreate":1,
            "extras":"icon_urls,safe_search,galleries_view_layout_pref, has_stats,expand_bbml,social_urls,with_stats",
            "user_id":self.user_id,
            "viewerNSID": "",
            "method":"flickr.profile.getProfile",
            "csrf": "",
            "api_key":"86b092183ba9d6f48fe217d2b48f3a1c",
            "format":"json",
            "hermes":1,
            "hermesClient":1,
            "reqId":"51cbd45e",
            "nojsoncallback":1 
        }

        r = self.send_requests(url, params=params).json()
        self._dict_to_object(r['profile'])
        self._dict_to_object(r['stats'])
        self.join_date = datetime.fromtimestamp(int(self.join_date)).strftime("%b %d %Y %H:%M:%S")

    def save_profile(self):
        """ Save profile in json format in current directory """
        self.dump_json(self.__dict__, self.username, ".")
        
    def _get_contents(self, per_page=100):
        """ _get_content() -> posts in json format"""

        url = "https://api.flickr.com/services/rest"
        params = {
            "per_page": per_page,
            "page": 1,
            "extras": "can_addmeta,can_comment,can_download,can_share,contact,count_comments,count_faves,count_views,date_taken,date_upload,description,icon_urls_deep,isfavorite,ispro,license,media,needs_interstitial,owner_name,owner_datecreate,path_alias,perm_print,realname,rotation,safety_level,secret_k,secret_h,url_sq,url_q,url_t,url_s,url_n,url_w,url_m,url_z,url_c,url_l,url_h,url_k,url_3k,url_4k,url_f,url_5k,url_6k,url_o,visibility,visibility_source,o_dims,publiceditability",
            "get_user_info": 1,
            "jump_to": "",
            "user_id": self.user_id,
            "view_as": "use_pref",
            "sort": "use_pref",
            "viewerNSID": "",
            "method": "flickr.people.getPhotos",
            "csrf": "",
            "api_key": "86b092183ba9d6f48fe217d2b48f3a1c",
            "format": "json",
            "hermes": 1,
            "hermesClient": 1,
            "reqId": "e2d77112",
            "nojsoncallback": 1,
        }

        r = self.send_requests(url, params=params).json()
        self._parse_posts(r)
    
    def _parse_posts(self, query_response):
        """ _parse_posts() -> json data of a single posts
            parse data and return single posts's useful data 
            query_response: Flikcr API response """
        pass
    
    def _parse_user_id(self):
        """ _parse_user_id() -> flickr user id """
        self.url = f"https://www.flickr.com/photos/{self.username}"

        r = self.send_requests(self.url)
        regex = re.compile(r"\d+@[N]\d\d")
        return regex.search(r.text)[0]