'''
Created on 11 mag 2017

@author: Antonio
'''
from core import mes_core
from flask import request, jsonify
import requests

@mes_core.route('/load_page', methods=['POST'])
def load_page():
    print("IM HERE")
    text=request.data
    out_file = open("test.txt","w")
    out_file.write(text)
    out_file.close()