from core import mes_core
from flask import request, jsonify
import requests
import json
import cv2
import base64
import os 
import pandas as pd
from core import mes_core, get_table, get_table_by_genre

@mes_core.route('/get_json_movie_by_image', methods=['POST'])
def get_json_movie_by_image():
    image = request.data[30:-1]
    image = base64.decodestring(image)
    with open('tmp.png','wb') as f:
        f.write(image)
    image = cv2.imread('tmp.png')
    cv2.imwrite("tmp.jpg", image)
    
    files = {'refImage': open(os.getcwd()+"/tmp.jpg", "rb")} 
    r = requests.post('http://jolscube.tilab.com/instore/products/query', files=files)
    # print r
    json_data = json.loads(r.text)

    # print "os.getcwd() " + os.getcwd()
    # print "os.path.dirname" + os.path.dirname(__file__)
   
    # Starting from the obtained ID we get the imdb one.
    df = pd.read_csv(os.getcwd() + "/csv/movies_info.csv")
    # print df.columns.values
    col_to_keep = ["IMDB_ID", "TITLE", "GENRES", "YEAR",
               "LENGTH", "POSTER", "YOU_TUBE_ID", "IMDB_RATING", "IMDB_VOTES",
               "f1", "f2", "f4", "f6"]
    # print("Init translation: "+ json_data) 
    
    path = os.getcwd() + "/csv/movie_info_reduced_with_genre.csv"
    movie_table_all = pd.read_csv(path, ",")  # dtype=object)
    movie_table_all.drop("Unnamed: 0", 1, inplace=True)
    movieLineServer = movie_table_all[movie_table_all["TITLE"].str.lower() == json_data[0]["name"].lower()][col_to_keep]
    # movieIMDB = movieLineServer["IMDB_ID"].values[0]
    # json_data.append({'IMDB_ID':movieIMDB})
    
    movieLineServer = movieLineServer.values
    
    movieLineServer2 = movieLineServer.reshape((-1,13))
    df = pd.DataFrame({'IMDB_ID':movieLineServer2.item(0),'TITLE':movieLineServer2.item(1),'GENRES':movieLineServer2.item(2), \
                       'YEAR':movieLineServer2.item(3),'LENGTH':movieLineServer2.item(4),'POSTER':movieLineServer2.item(5), \
                       'YOU_TUBE_ID':movieLineServer2.item(6),'IMDB_RATING':movieLineServer2.item(7),'IMDB_VOTES':movieLineServer2.item(8), \
                       'f1':movieLineServer2.item(9),'f2':movieLineServer2.item(10),'f4':movieLineServer2.item(11),'f6':movieLineServer2.item(12)}, index=[0])
    
  
    df2= df.iloc[0]

    print df2.to_json()
    print("-----------------------------------------------------------------------------")

 
    movieLine = df2.to_json()
    resp = {}
    resp.update({len(resp): movieLine})

    return jsonify(resp)

