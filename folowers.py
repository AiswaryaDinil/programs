import json
import random

try:
    with open("followers.json") as f:
        data=json.load(f)
    # print(data)

    all_users=list(map(lambda user:user["id"],data))
    # print(all_users)
    my_following=[user["followers"] for user in data if user["username"]=="akhil"][0]
    # print(my_following)
    my_id=[user["id"] for user in data if user["username"]=="akhil"].pop()
    # print(my_id)
    to_follow=set(all_users)-set(my_following)
    to_follow.remove(my_id)
    print(to_follow)
    suggession=random.sample([*to_follow],2)
    print(suggession)


except Exception as e:
    print(e)