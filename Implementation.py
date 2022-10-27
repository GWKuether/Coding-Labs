




months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

print(months[2])



fruits_and_veggies = {"banana", "pear", "watermelon", "asparagus", "broccoli"}

fruits_and_veggies.update(["apple", "strawberry", "corn", "beans"])

print(fruits_and_veggies)


student = {
    "first_name": "George",
    "last_name": "Kuether",
    "email_address": "gwkuether@gmail.com",
    "phone_number": "414-555-5555"
}

print("First Name: " + student["first_name"])
print("Last Name: " + student["last_name"])
print("Email Address: " + student["email_address"])
print("Phone Number: " + student["phone_number"])


mom = {
    "first_name": "Eva",
    "last_name": "Kuether",
    "relation": "Mother"
}

dad = {
    "first_name": "Brian",
    "last_name": "Kuether",
    "relation": "Father"
}

sister = {
    "first_name": "Emily",
    "last_name": "Rutowski",
    "relation": "Sister"
}

family = [mom, dad, sister]


def print_family_names():
    for member in family:
        print(member["first_name"])
        print(member["relation"])
       

print_family_names()








