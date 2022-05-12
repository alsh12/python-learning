def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem).lower() == expected.lower():
            return elem
    raise RuntimeError(f"Could not able to find expected element {expected}.")


friends = [
    {"name": "Alok", "age": 30},
    {"name": "Praveen", "age": 35},
    {"name": "Srikanth", "age": 29}
]


def find_name_of_friend(friend):
    return friend["name"]


print(search(friends,"Praveen",find_name_of_friend))
# print(search(friends,"praeen",find_name_of_friend))
print(search(friends,"praveen",find_name_of_friend))
