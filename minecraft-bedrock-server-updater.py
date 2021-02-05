#!/usr/bin/python3

import os
import re
import sys
import urllib.request

base_install_dir='/opt/minecraft'
install_symlink=os.path.join(base_install_dir, 'bedrock-server')

# we need to parse this to find the current download url, and from that
# the current server version
download_page='https://www.minecraft.net/en-us/download/server/bedrock/'

download_url = None
version = None
with urllib.request.urlopen(download_page) as resp:
    html_bytes = resp.read()
    html_str = html_bytes.decode('utf-8') # probably not quite safe to just assume this is utf-8?
    # "Never use regex to parse HTML" (unless you're in a hurry)
    # This will probably break someday...
    dlmatch = re.match(
            r'.*href="(?P<download_url>https://minecraft.azureedge.net/bin-linux/bedrock-server-(?P<version>[^"]+).zip)".*',
            html_str, re.DOTALL)
    if dlmatch is None:
        sys.exit('Could not find bedrock-server download link!')

    download_url = dlmatch.group('download_url')
    version = dlmatch.group('version')

print(f'Current Minecraft Bedrock Server release: {version} ({download_url})')
