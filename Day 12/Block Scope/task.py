game_level =3
enemies = ["Skeletons","Zombies","Aliens"]

def create_enemy():
    if game_level <5:
        new_enemy = enemies[0]
    print(new_enemy)

create_enemy()