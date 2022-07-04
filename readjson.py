import json

with open("blogs.json",encoding="utf-8") as f:
    data=json.load(f)
    # print(data)

# no of post

print(len(data))

# no of post by userid=1

post_user1=[post for post in data if post['userId']==1]
print(len(post_user1))

# no of likes for postid 6

like_of_post6=[len(post['liked_by']) for post in data if post['postId']==6]
print(like_of_post6)

# no of post liked by user 2

post_liked_by_user2=len([post for post in data if 2 in post['liked_by']])
print(post_liked_by_user2)




