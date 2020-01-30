#coding:utf8

import videoobject
import m3u8

def main():
    url = "http://cdn2.diexuewang.com:8091/20190129/EbIrZQ2i/600kb/hls/index.m3u8"
    ts = "http://cdn2.diexuewang.com:8091/20190129/EbIrZQ2i/600kb/hls/"
    thead = "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36"
    #video = videoobject.VideoObject(indexurl=url, tsurl=ts, tshead=thead)
    #video.ts_downLoad("")
    #video.key_download("http://cdn2.diexuewang.com:8091/20190129/EbIrZQ2i/600kb/hls/key.key")
    m3u8.M3u8.ToLocalLinkFile("F:/1")


if __name__ == '__main__':
    main()