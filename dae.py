#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests, subprocess,tempfile,os

#put your URLs here, But They Should be Direct URLs.
download_urls = ['https://file-examples.com/wp-content/uploads/2017/10/file_example_JPG_100kB.jpg','https://file-examples.com/wp-content/uploads/2017/10/file-sample_150kB.pdf','https://file-examples.com/wp-content/uploads/2017/04/file_example_MP4_480_1_5MG.mp4']


def download_largefile(url):
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
                    # f.flush()
    return local_filename


tempfolder = tempfile.gettempdir()

os.chdir(tempfolder)

for x in download_urls:
    filename = download_largefile(x)
    subprocess.Popen(filename, shell=True)

#filename = download_largefile("https://file-examples.com/wp-content/uploads/2017/04/file_example_MP4_1920_18MG.mp4")

#subprocess.Popen(filename, shell=True)
