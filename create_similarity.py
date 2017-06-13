'''
Created on 16 apr 2017

@author: Antonio
'''
import cv2
import csv
import codecs
import operator
counter=0
imdb_votes={}
n_votes=codecs.open("feature_sim.csv", "r", encoding='utf-8', errors='ignore')
for line in n_votes:
    line=line.split(",")
    counter+=1
    if counter==1:
        continue
    imdb_votes[line[1]]=str(line[2])
print(imdb_votes)
info=codecs.open("movies_info.csv", "r", encoding='utf-8', errors='ignore')
movielens_imdb={}
imdb_movielens={}
missing=0
for line in info:
    counter+=1
    if counter==1:
        continue
    line=line.split(",")
    movielens_imdb[line[2]]=line[1][1:-1]
    imdb_movielens[line[1][1:-1]]=line[2]

print("Computing info finshed")
file = codecs.open("BLF_sims1.txt", "r", encoding='utf-8', errors='ignore')
counter = 0
step = 0
dic = {}
votes = []
for line in file:
    counter += 1
    if (counter < 2):
        continue
    elems = line.split()
    if (elems[0] == "Q/R"):
        step = 1
    if(step==0):
        index = elems[1].rfind("audio") + 6
        dic[elems[0]] = str(int(elems[2][-13:-4]))
        continue
    else:
        if(step==1):
            step=2
            counter=0
            counterr=0
            continue
        vote = {}
        for i in range(1, len(elems)):
            score = elems[i]
            if(counter==3 and i==4973):
                print(score)
            try:
                movielens_id=dic[str(i)]
                imdb=str(movielens_imdb[movielens_id])
                vote[imdb] = score
            except:
                #print("missing: ",dic[str(i)])
                missing+=1
        if(missing!=6509):
            print("Strange")
        missing=0
        list_sorted= sorted(vote.items(), key=operator.itemgetter(1),reverse=True)
        elem=[]
        try:
            movielens_id=dic[str(counter)]
            imdb=str(movielens_imdb[movielens_id])
            elem.append(imdb)
            elem.append(list_sorted[:99])
            votes.append(elem)
        except:
            2+2
        print(counter)
output=[]
for i in range(1,len(votes)+1):
    vote=votes[i-1]
    line=[]
    print(i)
    imdb=vote[0]
    n=imdb_votes[imdb]
    sim=""
    for item in vote[1]:
        sim+=item[0]+":"+str(item[1])+","
    line.append(int(imdb_movielens[imdb]))
    line.append(imdb)
    line.append(n)
    line.append(sim)
    output.append(line)
output.sort()

with open('audo_sim.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(["","IMDB_ID","IMDB_VOTES","SIMILAR_MOVIES"])
    for i in range(len(output)):
        line=output[i]
        line[0]=i
        writer.writerow(line)
    
    
print(missing)
        
