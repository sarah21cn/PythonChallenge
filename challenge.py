import requests
import re
import urllib
import pickle
import os

# 参考答案：https://blog.csdn.net/qq_22709065/article/details/72594335

# http://www.pythonchallenge.com/pcc/def/map.html 
def transfer():
  s = "map"
  text_trans = ""
  for i in s:
    if str.isalpha(i):
      n = ord(i)
      if i >= 'y':
        n = ord(i) + 2 - 26
      else:
        n = ord(i) + 2
      text_trans += chr(n)
    else:
      text_trans += i
  print(text_trans)


# http://www.pythonchallenge.com/pcc/def/ocr.html 
def findChar():
  url = "http://www.pythonchallenge.com/pc/def/ocr.html"
  res = requests.get(url).text
  text = re.findall('.*?<!--.*-->.*<!--(.*)-->', res, re.S)
  str = ''.join(text)
  map = {}
  for i in str:
    num = map.get(i, 0)
    map[i] = num+1
  print(map)

# http://www.pythonchallenge.com/pcc/def/equality.html 
def findFormat():
  url = "http://www.pythonchallenge.com/pc/def/equality.html"
  res = requests.get(url).text
  chars = re.findall('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', res)
  print(chars)

# http://www.pythonchallenge.com/pc/def/linkedlist.php
def executeUrl():
  next = '45439'
  while next:
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s" % next
    res = urllib.request.urlopen(url)
    response = res.read().decode('utf-8')
    print("response is " + response)
    if re.findall(r'\.html$', response):
      break
    code = re.findall(r'\d+$', response)
    print("code is " + code)
    if(code):
      next = code[0]
      print("next is " + next)
    else:
      next = str(int(next)/2)
      
# http://www.pythonchallenge.com/pc/def/peak.html
def peakHeal():
  path = "/Users/shanyin/Workspace/sarah21cn/PythonChallenge"
  banner = pickle.load(open(path + '/banner.p', 'rb'))
  for linelist in banner:
    print("".join(ch * count for ch, count in linelist))

peakHeal()