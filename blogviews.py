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

class Mypostview:
    @signin_required
    def get(self,*args,**kwargs):
        userId=session["user"]["id"]
        myposts=[post for post in posts if post["userId"]==userId]
        return myposts


log_in=Loginview()
log_in.post(username="akhil",password="Password@123")
all_posts=Listpostview()
print(all_posts.get())
mypost=Mypostview()
print(mypost.get())