#!/usr/bin/env python
import sys
import platform
import requests
import os
import stat
import subprocess

govc_binary = os.path.join(os.path.dirname(__file__), 'govc.bin')
def find_binary():
    return os.path.exists(govc_binary)
      
def download_binary():
    if platform.system() == 'Linux':
        url = 'https://github.com/vmware/govmomi/releases/download/v0.23.0/govc_linux_amd64.gz'
    else:
        url = 'https://github.com/vmware/govmomi/releases/download/v0.23.0/govc_darwin_amd64.gz'
    
    r = requests.get(url)
    f = open(govc_binary + '.gz', 'wb')
    for chunk in r.iter_content(chunk_size=512 * 1024): 
        if chunk: # filter out keep-alive new chunks
            f.write(chunk)
    f.close()
    subprocess.check_call(['gunzip', govc_binary + '.gz'])
    os.chmod(govc_binary, 0775)

def main():
    if not find_binary():
        download_binary()
    os.execv(govc_binary, sys.argv)

if __name__ == "__main__":
    sys.exit(main())
