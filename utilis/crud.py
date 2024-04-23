def read(users: list[dict[str, str]])->None:
    for user in users[1:]:
        print(f'twoj znajomy {user["name"]} opublikowal {user["post"]} posty ')