
import core
import sys
import os
from loguru import logger

def do_download(args):
    logger.success("Logging in to Music Manager")
    mm = core.get_musicmanager(debug=False)
    if not mm.is_authenticated:
        sys.exit("Failed to authenticate Music Manager")
    
    logger.success("Logging in to Mobile Client")
    mc = core.get_mobileclient(debug=False)
    if not mc.is_authenticated:
    	sys.exit("Failed to authenticate Mobile Client")

    logger.success("Loading Google songs")
    songs = core.get_google_songs(mc,args.mint)
    if args.n:
        logger.success("Gefunden : "+str(len(songs)))
    else:
        if not os.path.exists(args.o):
            os.mkdir(args.o)
        for s in songs:
            core.download(mm,s,args.o)
            logger.info("Downloaded "+s)
    mm.logout()
    mc.logout()


