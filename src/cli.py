import argparse
import commands
import os
import sys

def run():    
    try:
        parser = argparse.ArgumentParser(description="")
        parser.add_argument("-n", action="store_true")
        parser.add_argument("-mint", type=int,  default = 0, help = "Minimum Timestamp")
        parser.add_argument("-o",default = os.path.dirname(os.path.realpath(__file__)))
        args = parser.parse_args()
        commands.do_download(args)
    except KeyboardInterrupt:
        sys.exit("Interrupted by user")

    