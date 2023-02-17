#cars = {
    #"model":"ford",
    #"year":1998,
    #"colour":"red",
#"country":"Kenya"
#}
#accessing dictionary items
#print(cars["year"])

#person= {
   # "name":"ace",
   # "age":"18",
   # "pets":["dogs","cats"]
#}
#print(person["pets"])
#person["pets"][0]
#(person["pets"][0])



#person = {
    #"mane":"cathy",
    #"age":23,
    #"pets":{"dog":"bosco",
            #"cat":"kitty"
            #}
#}
#print(person["pets"]["dog"])
#print(len(person))

#profile = {}
#profile["age"] = 20
#print(profile)
profile = {}

def register():
    username = input("enter username:")
    email = input("enter email:")
    password = input("enter password")


    profile["username"]= username
    profile["email"] = email
    profile["password"]= password

def get_profile():
    #print the user profile
    print(profile)

def change_username():
    new_username = input("enter new username")
    profile["username"]= new_username


register()
get_profile()
change_username()
get_profile()





