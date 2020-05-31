""" 
Arguments Settings for the flickr script.

options:
  -h, --help            show this help message and exit
  -u USERNAME, --username USERNAME
                        Username of the flickr account.
  -s, --save_info       Save the details about photos and user in json
  
"""
import argparse
import os

parser = argparse.ArgumentParser(description="Download Photos from Flickr!")

parser.add_argument('-u', '--username', help="Username of the flickr account.")
parser.add_argument("-s", "--save_info", action="store_true", help="Save the details about photos and user in json")

args = parser.parse_args()