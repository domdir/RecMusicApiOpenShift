from core import mes_core
from flask import request, jsonify
import requests
import json
import cv2
import base64
import os 
import pandas as pd

@mes_core.route('/get_json_img', methods=['POST'])
def get_json_img():
    image = request.data[30:-1]
    image = base64.decodestring(image)
    with open('tmp.png','wb') as f:
        f.write(image)
    image = cv2.imread('tmp.png')
    cv2.imwrite("tmp.jpg", image)
    
    files = {'refImage': open(os.getcwd()+"/tmp.jpg", "rb")} 
    r = requests.post('http://jolscube.tilab.com/instore/products/query', files=files)
    json_data = json.loads(r.text)

   # print "os.getcwd() " + os.getcwd()
   # print "os.path.dirname" + os.path.dirname(__file__)
   
    # Starting from the obtained ID we get the imdb one.
   # df = pd.read_csv(os.getcwd() + "/csv/movies_info.csv")
   # print df.columns.values

  #  print("Init translation: "+ json_data) 

    #print(json_data)
    return jsonify(json_data)
