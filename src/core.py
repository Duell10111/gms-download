
import os
from loguru import logger
from gmusicapi import Musicmanager, Mobileclient
import json

def get_mobileclient(debug = True, deviceID = Mobileclient.FROM_MAC_ADDRESS):
    mc = Mobileclient(debug_logging=debug)
    if not mc.oauth_login(device_id = deviceID):
        mc.perform_oauth()
    return mc
    
def get_musicmanager(debug = True):
    mm = Musicmanager(debug_logging = debug)
    if not mm.login():
        mm.perform_oauth()
    return mm

def get_google_songs(mc : Mobileclient, mintimestamp : int = 0):
    arr = mc.get_all_songs()
    filterd = []
    mintimestamp *= 1000
    for elem in arr :
        if int(elem["creationTimestamp"]) > mintimestamp:
            filterd.append(elem["id"])
    return filterd

def download(mm : Musicmanager, songid,pathfile = ""):
    filename, audio = mm.download_song(songid)

    # if open() throws a UnicodeEncodeError, either use
    #   filename.encode('utf-8')
    # or change your default encoding to something sane =)
    with open(os.path.join(pathfile,filename), 'wb') as f:
        f.write(audio)
    

