import os
while True:
	key = os.popen('curl -s --user-agent "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36" "http://miniplay.imbc.com/AACLiveURL.ashx?protocol=M3U8&channel=sfm&agent=android&androidVersion=24"').read()
	if key != "http://mfmtunein.imbc.com/tmfm/_definst_/tmfm.stream/playlist.m3u8":
		break
key = key.split('/')[6]
domain = "http://1.255.48.56/ssfm/_definst_/sfm.stream/"
url = domain + key

front = url[0:250]
end = url[250:]

f = open("/config/www/radio/mbc_fm_1.txt", 'w');
f.write(front)
f.close()
f = open("/config/www/radio/mbc_fm_2.txt", 'w');
f.write(end)
f.close()