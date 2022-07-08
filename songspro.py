import json
import random
from functools import reduce
with open("songs.json",encoding="utf-8") as f:
    data=json.load(f)

# num_song=[song for song in data if song["album"]=="album1"]
# print(len(num_song))
num_song=list(filter(lambda s:s["album"]=="album1",data))
print(len(num_song))

higest_rating=max([song["rating"] for song in data])
# print(higest_rating)
higest_rating_song=[s for s in data if s["rating"]==higest_rating]
print(higest_rating_song)

t_songs=reduce(lambda s1,s2:s1 if s1["rating"]>s2["rating"] else s2,data)
print(t_songs)

sad_songs=[s for s in data if s["mode"]=="sad"]
random_song=random.sample(sad_songs,2)
print(random_song)

total_albums=set([s["album"] for s in data])
print(len(total_albums))

s_count={}
for s in data:
    album_name=s.get("album")
    if album_name in s_count:
        s_count[album_name]+=1
    else:
        s_count[album_name]=1
print(s_count)
max_song_album=max(s_count.items(),key=lambda s:s[1])
print(max_song_album)
