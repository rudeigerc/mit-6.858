#!/usr/bin/env python3

import sys
import zookconf

def main():
    if len(sys.argv) == 2:
        zookconf.boot(sys.argv[1])
    else:
        zookconf.boot()
        
if __name__ == "__main__":
    main()
