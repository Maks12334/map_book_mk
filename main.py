users:list[dict[str, str]]=[
    {'name': 'maks','surname':'Kaluzny','post':1},
    {'name': 'kacper','surname':'macioch','post':2},
    {'name': 'michal','surname':'krzywinski','post':3},
    {'name': 'tymon','surname':'leszczyc','post':2},
    {'name': 'michal','surname':'lebryk','post':2},
]
print(f'witaj{users[0]["name"]}')

def read(users: list[dict[str, str]])->None:
    for user in users[1:]:
        print(f'twoj znajomy {user["name"]} opublikowal {user["post"]} posty ')

read(users)


