from arguments import args
from flickr import Flickr

if args.username:
    account = Flickr(args.username)
    if args.save_info:
        account.save_profile()