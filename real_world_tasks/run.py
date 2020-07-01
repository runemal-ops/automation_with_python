#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import requests

BASEPATH='/data/feedback/'
CORPWEB_IP = "http://34.71.156.246/"
folder = os.listdir(BASEPATH)
list = []
for file in folder:
   with open(BASEPATH+file,'r') as f:
     list.append({"title":f.readline().rstrip("\n"),
         "name":f.readline().rstrip("\n"),
         "date":f.readline().rstrip("\n"),
         "feedback":f.read().rstrip("\n")})
for item in list:
    resp = requests.post(CORPWEB_IP+"feedback/", json= item)
    if resp.status_code != 201:
        raise Exception('POST error status={}', format(resp.status_code))
    print('Created feedback ID: {}'.format(resp.json()["id"]))

