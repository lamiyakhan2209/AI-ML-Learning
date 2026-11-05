contacts = {
    "lamia": "1234",
    "mariya": "5678",
    "alvi": "9012"
}

name = input("Enter name to search:")
if name in contacts:
    print("phone no.:", contacts[name])
else:
    print("contact not found !")