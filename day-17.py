#Creating your own classes





class User:
    def __init__(self, username, id):
        self.username = username
        self.id = id
        #Default value:
        self.followers = 0


#Now you have to pass the username and id info into the parameters of the User() class. This will set the values for the objects
user_1 = User("Kazim", "529590")

#To add attribute you just use dot notation. This is bad practice though
# user_1.id = "529590"
# user_1.username = "Kazim"

print(user_1.id)