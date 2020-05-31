"""
Download Photos from Flickr!

usage: main.py [-h] [-u USERNAME] [-s]
optional arguments:

  -h, --help            show this help message and exit
  -u USERNAME, --username USERNAME
                        Username of the flickr account.
  -s, --save_info       Save the details about photos and user in json
"""
from arguments import args
from flickr import Flickr

if args.username:
    account = Flickr(args.username)
    if args.save_info:
        account.save_profile()