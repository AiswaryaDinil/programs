from blog.blogmodels import users,posts

# print(users)

def signin_required(fn):
    def wrapper(*args,**kwargs):
        if "user" in session:
            return fn(*args,**kwargs)
        else:
            print("invalid session user must login")
    return wrapper


def authenticate(**kwargs):
    username =kwargs.get("username")
    password =kwargs.get("password")
    user=[user for user in users if user["username"]==username and user["password"]==password]
    return user

# print(authenticate(username="akhil",password="Password@123"))

session={}
class Loginview:
    def post(self,**kwargs):
        username=kwargs.get("username")
        password=kwargs.get("password")
        user=authenticate(username=username,password=password)
        if user:
            session["user"]=user[0]

        print(session)

class Listpostview:
    @signin_required
    def get(self,*args,**kwargs):
        return posts
    @signin_required
    def post(self,*args,**kwargs):
        userId=session["user"]["id"]
        my_post["userId"]=userId
        posts.append(my_post)
        print(posts[-1])

class Mypostview:
    @signin_required
    def get(self,*args,**kwargs):
        userId=session["user"]["id"]
        myposts=[post for post in posts if post["userId"]==userId]
        return myposts

class Addlike:
    @signin_required
    def post(self,*args,**kwargs):
        postid=kwargs.get("postid")
        post=[post for post in posts if post["postId"]==postid]
        if post:
            post=post[0]
            userid=session["user"]["id"]
            post["liked_by"].append(userid)
            print(post["liked_by"])


log_in=Loginview()
log_in.post(username="akhil",password="Password@123")
all_posts=Listpostview()
my_post={ "postId":9,"title":"hello goodmorning","content":"mycontent","liked by":[] }
all_posts.post(data=my_post)

like=Addlike()
like.post(postid=2)
# print(all_posts.get())
mypost=Mypostview()
# print(mypost.get())