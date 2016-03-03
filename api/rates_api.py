from flask_restful import Resource
from random import shuffle
from flaskapp import api, db

class GetUnratedSong(Resource):
########################################
    def get(self, user_id):
        already_voted=self.getAlreadyVotedSongs(user_id)
        print "song already voted {}".format(len(already_voted))
        available_song=self.getAvailableSongs(already_voted)
        print "song available {}".format(len(available_song))

        if(len(available_song)==0):
            all_songs=db.songs.find({})
            shuffle(all_songs)
            s = all_songs[0]
            del (s["_id"])
            return s

        shuffle(available_song)
        s = available_song[0]
        del (s["_id"])
        return s

########################################
    def getAlreadyVotedSongs(self,user):
        if((db.rates is None)):
            return []

        rates_by_user=list(db.rates.find({
            "voted_by":user
        }))
        print "song rated {}".format(len(rates_by_user))
        return rates_by_user

########################################
    def getAvailableSongs(self,already_voted):
        already_voted_id=[]
        for a in already_voted:
            already_voted_id.append(a["_id"])
        all_songs=db.songs.find({})
        available_song=[]

        #for s in all_songs:
          #  if s["song"]
        return list(all_songs)

api.add_resource(GetUnratedSong, '/api/get_song/<user_id>')


class GetSongsByGenre(Resource):
    def get(self, genre):
        songs = db.songs
        f = songs.find(
                {
                    "s_genres": {"$in": [genre]}
                }
        )
        f = list(f)
        for s in f:
            del (s["_id"])
        return f


api.add_resource(GetSongsByGenre, '/api/songs/<genre>')
