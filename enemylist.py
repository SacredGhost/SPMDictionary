import dolphin_memory_engine as dme
from bighexlist import HexList
from watches import game_region, game_revision

class EnemyEntry():
    def __init__ (self, EnemyName, EnemyID, DropTemplate, DropPercent, EnemyDrops):
        self.EnemyName = EnemyName
        self.EnemyID =  EnemyID
        self.DropTemplate = DropTemplate
        self.DropPercent = DropPercent
        self.EnemyDrops = EnemyDrops

class ItemDrops():
    def __init__(self, *item):
        self.item = list(item)

    def add_item(self, item):
        self.item.append(item)

    def remove_item(self, item):
        self.item.remove(item)

    def get_item(self, index):
        if 0 <= index < len(self.item):
            return self.item[index]
        else:
            return None
        
class EnemyDrops():
    def __init__(self, *item):
        self.item = list(item)

    def add_item(self, item):
        self.item.append(item)

    def remove_item(self, item):
        self.item.remove(item)

    def get_item(self, index):
        if 0 <= index < len(self.item):
            return self.item[index]
        else:
            return None
        
class Drop():
    def __init__(self, ItemName, ItemID, ItemWeight):
        self.ItemName = ItemName
        self.ItemID = ItemID
        self.ItemWeight = ItemWeight

def get_itemPercent(name: str) -> int:
    drop = EnemyList[name]
    dropies = drop["Drop %"][game_region][game_revision]
    return int(dropies, drop["datatype"])

ItemHexValues = {}
for item in HexList:
    ItemHexValues[item.name] = item.hex

def get_hex_value(item_name):
    return ItemHexValues.get(item_name)

EnemyList = {
    '0':EnemyEntry (
        "Nothing",
        None,
        "Template 0",
        0.04,
        EnemyDrops (
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Honey Jar", hex_value = get_hex_value("Honey Jar"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 200),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '1':EnemyEntry (
        "Goomba",
        0x11A,
        "Template 1",
        0.04,
        EnemyDrops (
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Honey Jar", hex_value = get_hex_value("Honey Jar"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 200),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '2':EnemyEntry (
        "Goomba",
        0x11A,
        "Template 2",
        0.04,
        EnemyDrops (
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Honey Jar", hex_value = get_hex_value("Honey Jar"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 200),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '3':EnemyEntry (
        "Spiked Goomba",
        0x11B,
        "Template 3",
        0.03,
        EnemyDrops (
            Drop (item_name = "Power Steak", hex_value = get_hex_value("Power Steak"), weight = 100),
            Drop (item_name = "Fresh Pasta Bunch", hex_value = get_hex_value("Fresh Pasta Bunch"), weight = 100),
            Drop (item_name = "Hot Sauce", hex_value = get_hex_value("Hot Sauce"), weight = 100),
            Drop (item_name = "Smelly Herb", hex_value = get_hex_value("Smelly Herb"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 200),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '4':EnemyEntry (
        "Paragoomba",
        0x11D,
        "Template 4",
        0.03,
        EnemyDrops (
            Drop (item_name = "Peachy Peach", hex_value = get_hex_value("Peachy Peach"), weight = 100),
            Drop (item_name = "Keel Mango", hex_value = get_hex_value("Keel Mango"), weight = 100),
            Drop (item_name = "Fresh Veggie", hex_value = get_hex_value("Fresh Veggie"), weight = 100),
            Drop (item_name = "Horsetail", hex_value = get_hex_value("Horsetail"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 200),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '5':EnemyEntry (
        "Flip Goomba",
        0x11A,
        "Template 5",
        0.03,
        EnemyDrops (
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Honey Jar", hex_value = get_hex_value("Honey Jar"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 200),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '6':EnemyEntry (
        "Spiked Goomba",
        0x11B,
        "Template 6",
        0.03,
        EnemyDrops (
            Drop (item_name = "Power Steak", hex_value = get_hex_value("Power Steak"), weight = 100),
            Drop (item_name = "Fresh Pasta Bunch", hex_value = get_hex_value("Fresh Pasta Bunch"), weight = 100),
            Drop (item_name = "Hot Sauce", hex_value = get_hex_value("Hot Sauce"), weight = 100),
            Drop (item_name = "Smelly Herb", hex_value = get_hex_value("Smelly Herb"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 200),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '7':EnemyEntry (
        "Goomba",
        0x11A,
        "Template 7",
        0.04,
        EnemyDrops (
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Honey Jar", hex_value = get_hex_value("Honey Jar"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 200),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '8':EnemyEntry (
        "Green Koopa Troopa",
        0x123,
        "Template 8",
        0.09,
        EnemyDrops (
            Drop (item_name = "Turtley Leaf", hex_value = get_hex_value("Turtley Leaf"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    '9':EnemyEntry (
        "Red Koopa Troopa",
        0x123,
        "Template 9",
        0.09,
        EnemyDrops (
            Drop (item_name = "Turtley Leaf", hex_value = get_hex_value("Turtley Leaf"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    '10':EnemyEntry (
        "(Unused) Shady Koopa",
        None,
        "Template 10",
        0.04,
        EnemyDrops (
            None
        )
    ),
    '11':EnemyEntry (
        "Koopatrol",
        0x124,
        "Template 11",
        0.05,
        EnemyDrops (
            Drop (item_name = "Turtley Leaf", hex_value = get_hex_value("Turtley Leaf"), weight = 100),
            Drop (item_name = "Thunder Rage", hex_value = get_hex_value("Thunder Rage"), weight = 300),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 20),
        )
    ),
    '12':EnemyEntry (
        "Flip Red Koopa Troopa",
        0x123,
        "Template 12",
        0.09,
        EnemyDrops (
            Drop (item_name = "Turtley Leaf", hex_value = get_hex_value("Turtley Leaf"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    '13':EnemyEntry (
        "(Unused) Flip Shady Koopa",
        None,
        "Template 13",
        0.04,
        EnemyDrops (
            None
        )
    ),
    '14':EnemyEntry (
        "Green Paratroopa",
        0x128,
        "Template 14",
        0.03,
        EnemyDrops (
            Drop (item_name = "Turtley Leaf", hex_value = get_hex_value("Turtley Leaf"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    '15':EnemyEntry (
        "Red Paratroopa",
        0x128,
        "Template 15",
        0.03,
        EnemyDrops (
            Drop (item_name = "Turtley Leaf", hex_value = get_hex_value("Turtley Leaf"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    '16':EnemyEntry (
        "(Unused) Shady Paratroopa",
        None,
        "Template 16",
        0.04,
        EnemyDrops (
            None
        )
    ),
    '17':EnemyEntry (
        "Flip Red Paratroopa",
        0x128,
        "Template 17",
        0.03,
        EnemyDrops (
            Drop (item_name = "Turtley Leaf", hex_value = get_hex_value("Turtley Leaf"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    '18':EnemyEntry (
        "(Unused) Flip Shady Paratroopa",
        None,
        "Template 18",
        0.04,
        EnemyDrops (
            None
        )
    ),
    '19':EnemyEntry (
        "Clubba",
        0x143,
        "Template 19",
        0.03,
        EnemyDrops (
            Drop (item_name = "Power Steak", hex_value = get_hex_value("Power Steak"), weight = 100),
            Drop (item_name = "Fresh Pasta Bunch", hex_value = get_hex_value("Fresh Pasta Bunch"), weight = 100),
            Drop (item_name = "Hot Sauce", hex_value = get_hex_value("Hot Sauce"), weight = 100),
            Drop (item_name = "Smelly Herb", hex_value = get_hex_value("Smelly Herb"), weight = 100),
            Drop (item_name = "Fire Burst", hex_value = get_hex_value("Fire Burst"), weight = 800),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '20':EnemyEntry (
        "PatrolMeow",
        0x194,
        "Template 20",
        0,
        EnemyDrops (
            None
        )
    ),
    '21':EnemyEntry (
        "AirMeow",
        0x195,
        "Template 21",
        0,
        EnemyDrops (
            None
        )
    ),
    '22':EnemyEntry (
        "SurpriseMeow",
        0x196,
        "Template 22",
        0,
        EnemyDrops (
            None
        )
    ),
    '23':EnemyEntry (
        "MeowBomb (SurpriseMeow)",
        0x193,
        "Template 23",
        0,
        EnemyDrops (
            None
        )
    ),
    '24':EnemyEntry (
        "Hammer Bro.",
        0x137,
        "Template 24",
        0.05,
        EnemyDrops (
            Drop (item_name = "Super Shroom Shake", hex_value = get_hex_value("Super Shroom Shake"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Honey Jar", hex_value = get_hex_value("Honey Jar"), weight = 100),
            Drop (item_name = "Fire Burst", hex_value = get_hex_value("Fire Burst"), weight = 400),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '25':EnemyEntry (
        "Green Cheep Cheep",
        0x152,
        "Template 25",
        0.03,
        EnemyDrops (
            Drop (item_name = "Power Steak", hex_value = get_hex_value("Power Steak"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 100),
            Drop (item_name = "Hot Sauce", hex_value = get_hex_value("Hot Sauce"), weight = 100),
            Drop (item_name = "Smelly Herb", hex_value = get_hex_value("Smelly Herb"), weight = 100),
            Drop (item_name = "Volt Shroom", hex_value = get_hex_value("Volt Shroom"), weight = 800),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '26':EnemyEntry (
        "Blooper",
        0x153,
        "Template 26",
        0.15,
        EnemyDrops (
            Drop (item_name = "Inky Sauce", hex_value = get_hex_value("Inky Sauce"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    '27':EnemyEntry (
        "Thwomp",
        0x170,
        "Template 27",
        0,
        EnemyDrops (
            None
        )
    ),
    '28':EnemyEntry (
        "Lava Bubble",
        0x165,
        "Template 28",
        0.04,
        EnemyDrops (
            Drop (item_name = "Fire Burst", hex_value = get_hex_value("Fire Burst"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    '29':EnemyEntry (
        "Spiny Tromp",
        0x171,
        "Template 29",
        0,
        EnemyDrops (
            None
        )
    ),
    '30':EnemyEntry (
        "Goomba",
        0x11A,
        "Template 30",
        0.04,
        EnemyDrops (
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Honey Jar", hex_value = get_hex_value("Honey Jar"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 200),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '31':EnemyEntry (
        "Piranha Plant",
        0x145,
        "Template 31",
        0.1,
        EnemyDrops (
            Drop (item_name = "Peachy Peach", hex_value = get_hex_value("Peachy Peach"), weight = 100),
            Drop (item_name = "Keel Mango", hex_value = get_hex_value("Keel Mango"), weight = 100),
            Drop (item_name = "Fresh Veggie", hex_value = get_hex_value("Fresh Veggie"), weight = 100),
            Drop (item_name = "Horsetail", hex_value = get_hex_value("Horsetail"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 40),
        )
    ),
    '32':EnemyEntry (
        "Goomba",
        0x11A,
        "Template 32",
        0.04,
        EnemyDrops (
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Honey Jar", hex_value = get_hex_value("Honey Jar"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 200),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '33':EnemyEntry (
        "Goomba",
        0x11A,
        "Template 33",
        0.04,
        EnemyDrops (
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Honey Jar", hex_value = get_hex_value("Honey Jar"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 200),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '34':EnemyEntry (
        "Goomba",
        0x11A,
        "Template 34",
        0.04,
        EnemyDrops (
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Honey Jar", hex_value = get_hex_value("Honey Jar"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 200),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '35':EnemyEntry (
        "Goomba",
        0x11A,
        "Template 35",
        0.04,
        EnemyDrops (
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Honey Jar", hex_value = get_hex_value("Honey Jar"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 200),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '36':EnemyEntry (
        "Dry Bones",
        0x136,
        "Template 36",
        0.03,
        EnemyDrops (
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Honey Jar", hex_value = get_hex_value("Honey Jar"), weight = 100),
            Drop (item_name = "Ice Storm", hex_value = get_hex_value("Ice Storm"), weight = 800),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '37':EnemyEntry (
        "Rubee",
        None,
        "Template 37",
        0,
        EnemyDrops (
            None
        )
    ),
    '38':EnemyEntry (
        "Dull Bones",
        0x134,
        "Template 38",
        0.04,
        EnemyDrops (
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Honey Jar", hex_value = get_hex_value("Honey Jar"), weight = 100),
            Drop (item_name = "Ice Storm", hex_value = get_hex_value("Ice Storm"), weight = 800),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '39':EnemyEntry (
        "Boomerang Bro",
        0x138,
        "Template 39",
        0.05,
        EnemyDrops (
            Drop (item_name = "Super Shroom Shake", hex_value = get_hex_value("Super Shroom Shake"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Honey Jar", hex_value = get_hex_value("Honey Jar"), weight = 100),
            Drop (item_name = "Fire Burst", hex_value = get_hex_value("Fire Burst"), weight = 400),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '40':EnemyEntry (
        "Fire Bro",
        0x139,
        "Template 40",
        0.05,
        EnemyDrops (
            Drop (item_name = "Super Shroom Shake", hex_value = get_hex_value("Super Shroom Shake"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Honey Jar", hex_value = get_hex_value("Honey Jar"), weight = 100),
            Drop (item_name = "Fire Burst", hex_value = get_hex_value("Fire Burst"), weight = 800),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '41':EnemyEntry (
        "Goomba",
        0x11A,
        "Template 41",
        0.04,
        EnemyDrops (
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Honey Jar", hex_value = get_hex_value("Honey Jar"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 200),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '42':EnemyEntry (
        "Goomba",
        0x11A,
        "Template 42",
        0.04,
        EnemyDrops (
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Honey Jar", hex_value = get_hex_value("Honey Jar"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 200),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '43':EnemyEntry (
        "Fracktail",
        0x1C8,
        "Template 43",
        0,
        EnemyDrops (
            None
        )
    ),
    '44':EnemyEntry (
        "Wracktail",
        0x1C9,
        "Template 44",
        0,
        EnemyDrops (
            None
        )
    ),
    '45':EnemyEntry (
        "Flip Blooper",
        0x153,
        "Template 45",
        0.15,
        EnemyDrops (
            Drop (item_name = "Inky Sauce", hex_value = get_hex_value("Inky Sauce"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    '46':EnemyEntry (
        "Flip Hammer Bro.",
        0x137,
        "Template 46",
        0.05,
        EnemyDrops (
            Drop (item_name = "Super Shroom Shake", hex_value = get_hex_value("Super Shroom Shake"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Honey Jar", hex_value = get_hex_value("Honey Jar"), weight = 100),
            Drop (item_name = "Fire Burst", hex_value = get_hex_value("Fire Burst"), weight = 400),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '47':EnemyEntry (
        "Small Spiky Tromp",
        0x172,
        "Template 47",
        0,
        EnemyDrops (
            None
        )
    ),
    '48':EnemyEntry (
        "Nothing?",
        None,
        "Template 48",
        0.1,
        EnemyDrops (
            Drop (item_name = "Peachy Peach", hex_value = get_hex_value("Peachy Peach"), weight = 100),
            Drop (item_name = "Keel Mango", hex_value = get_hex_value("Keel Mango"), weight = 100),
            Drop (item_name = "Fresh Veggie", hex_value = get_hex_value("Fresh Veggie"), weight = 100),
            Drop (item_name = "Horsetail", hex_value = get_hex_value("Horsetail"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 40),
        )
    ),
    '49':EnemyEntry (
        "Putrid Piranha",
        0x146,
        "Template 49",
        1,
        EnemyDrops (
            Drop (item_name = "Peachy Peach", hex_value = get_hex_value("Peachy Peach"), weight = 100),
            Drop (item_name = "Keel Mango", hex_value = get_hex_value("Keel Mango"), weight = 200),
            Drop (item_name = "Fresh Veggie", hex_value = get_hex_value("Fresh Veggie"), weight = 100),
            Drop (item_name = "Horsetail", hex_value = get_hex_value("Horsetail"), weight = 600),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 40),
        )
    ),
    '50':EnemyEntry (
        "Nothing?",
        None,
        "Template 50",
        0.1,
        EnemyDrops (
            Drop (item_name = "Peachy Peach", hex_value = get_hex_value("Peachy Peach"), weight = 100),
            Drop (item_name = "Keel Mango", hex_value = get_hex_value("Keel Mango"), weight = 200),
            Drop (item_name = "Fresh Veggie", hex_value = get_hex_value("Fresh Veggie"), weight = 100),
            Drop (item_name = "Horsetail", hex_value = get_hex_value("Horsetail"), weight = 600),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 40),
        )
    ),
    '51':EnemyEntry (
        "Frost Piranha",
        0x147,
        "Template 51",
        0.1,
        EnemyDrops (
            Drop (item_name = "Ice Storm", hex_value = get_hex_value("Ice Storm"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    '52':EnemyEntry (
        "Nothing?",
        None,
        "Template 52",
        0.1,
        EnemyDrops (
            Drop (item_name = "Ice Storm", hex_value = get_hex_value("Ice Storm"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    '53':EnemyEntry (
        "Buzzy Beetle",
        0x12A,
        "Template 53",
        0.03,
        EnemyDrops (
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Honey Jar", hex_value = get_hex_value("Honey Jar"), weight = 100),
            Drop (item_name = "Courage Shell", hex_value = get_hex_value("Courage Shell"), weight = 800),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '54':EnemyEntry (
        "Nothing?",
        None,
        "Template 54",
        0.03,
        EnemyDrops (
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Honey Jar", hex_value = get_hex_value("Honey Jar"), weight = 100),
            Drop (item_name = "Courage Shell", hex_value = get_hex_value("Courage Shell"), weight = 800),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '55':EnemyEntry (
        "Flip Buzzy Beetle",
        0x12A,
        "Template 55",
        0.04,
        EnemyDrops (
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Honey Jar", hex_value = get_hex_value("Honey Jar"), weight = 100),
            Drop (item_name = "Courage Shell", hex_value = get_hex_value("Courage Shell"), weight = 800),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '56':EnemyEntry (
        "Spike Top",
        0x12B,
        "Template 56",
        0.03,
        EnemyDrops (
            Drop (item_name = "Power Steak", hex_value = get_hex_value("Power Steak"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Hot Sauce", hex_value = get_hex_value("Hot Sauce"), weight = 100),
            Drop (item_name = "Smelly Herb", hex_value = get_hex_value("Smelly Herb"), weight = 100),
            Drop (item_name = "Courage Shell", hex_value = get_hex_value("Courage Shell"), weight = 800),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '57':EnemyEntry (
        "Parabuzzy",
        0x12D,
        "Template 57",
        0.03,
        EnemyDrops (
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Honey Jar", hex_value = get_hex_value("Honey Jar"), weight = 100),
            Drop (item_name = "Courage Shell", hex_value = get_hex_value("Courage Shell"), weight = 800),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '58':EnemyEntry (
        "Spiky Parabuzzy",
        0x12E,
        "Template 58",
        0.03,
        EnemyDrops (
            Drop (item_name = "Power Steak", hex_value = get_hex_value("Power Steak"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Hot Sauce", hex_value = get_hex_value("Hot Sauce"), weight = 100),
            Drop (item_name = "Smelly Herb", hex_value = get_hex_value("Smelly Herb"), weight = 100),
            Drop (item_name = "Courage Shell", hex_value = get_hex_value("Courage Shell"), weight = 800),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '59':EnemyEntry (
        "Spiny",
        0x131,
        "Template 59",
        0.03,
        EnemyDrops (
            Drop (item_name = "Power Steak", hex_value = get_hex_value("Power Steak"), weight = 100),
            Drop (item_name = "Fresh Pasta Bunch", hex_value = get_hex_value("Fresh Pasta Bunch"), weight = 100),
            Drop (item_name = "Hot Sauce", hex_value = get_hex_value("Hot Sauce"), weight = 100),
            Drop (item_name = "Smelly Herb", hex_value = get_hex_value("Smelly Herb"), weight = 100),
            Drop (item_name = "Mighty Tonic", hex_value = get_hex_value("Mighty Tonic"), weight = 800),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '60':EnemyEntry (
        "(UNUSED?) Weird Spiny",
        0x131,
        "Template 60",
        0.04,
        EnemyDrops (
            Drop (item_name = "Power Steak", hex_value = get_hex_value("Power Steak"), weight = 100),
            Drop (item_name = "Fresh Pasta Bunch", hex_value = get_hex_value("Fresh Pasta Bunch"), weight = 100),
            Drop (item_name = "Hot Sauce", hex_value = get_hex_value("Hot Sauce"), weight = 100),
            Drop (item_name = "Smelly Herb", hex_value = get_hex_value("Smelly Herb"), weight = 100),
            Drop (item_name = "Mighty Tonic", hex_value = get_hex_value("Mighty Tonic"), weight = 800),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '61':EnemyEntry (
        "Lakitu",
        0x133,
        "Template 61",
        0.1,
        EnemyDrops (
            Drop (item_name = "Thunder Rage", hex_value = get_hex_value("Thunder Rage"), weight = 100),
            Drop (item_name = "Mystery Box", hex_value = get_hex_value("Mystery Box"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 30),
        )
    ),
    '62':EnemyEntry (
        "Flip Lakitu",
        None,
        "Template 62",
        0x133,
        EnemyDrops (
            Drop (item_name = "Thunder Rage", hex_value = get_hex_value("Thunder Rage"), weight = 100),
            Drop (item_name = "Mystery Box", hex_value = get_hex_value("Mystery Box"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 30),
        )
    ),
    '63':EnemyEntry (
        "Mega Koopa",
        0x127,
        "Template 63",
        0,
        EnemyDrops (
            None
        )
    ),
    '64':EnemyEntry (
        "Goomba",
        0x11A,
        "Template 64",
        0.04,
        EnemyDrops (
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Honey Jar", hex_value = get_hex_value("Honey Jar"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 200),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '65':EnemyEntry (
        "Chain Chomp",
        0x166,
        "Template 65",
        0.05,
        EnemyDrops (
            Drop (item_name = "Power Steak", hex_value = get_hex_value("Power Steak"), weight = 100),
            Drop (item_name = "Thunder Rage", hex_value = get_hex_value("Thunder Rage"), weight = 200),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 30),
        )
    ),
    '66':EnemyEntry (
        "Goomba",
        0x11A,
        "Template 66",
        0.04,
        EnemyDrops (
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Honey Jar", hex_value = get_hex_value("Honey Jar"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 200),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '67':EnemyEntry (
        "Red Cheep Cheep",
        0x152,
        "Template 67",
        0.03,
        EnemyDrops (
            Drop (item_name = "Power Steak", hex_value = get_hex_value("Power Steak"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 100),
            Drop (item_name = "Hot Sauce", hex_value = get_hex_value("Hot Sauce"), weight = 100),
            Drop (item_name = "Smelly Herb", hex_value = get_hex_value("Smelly Herb"), weight = 100),
            Drop (item_name = "Volt Shroom", hex_value = get_hex_value("Volt Shroom"), weight = 800),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '68':EnemyEntry (
        "Goomba",
        0x11A,
        "Template 68",
        0.04,
        EnemyDrops (
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Honey Jar", hex_value = get_hex_value("Honey Jar"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 200),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '69':EnemyEntry (
        "Flip Cheep Cheep",
        0x152,
        "Template 69",
        0.03,
        EnemyDrops (
            Drop (item_name = "Power Steak", hex_value = get_hex_value("Power Steak"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 100),
            Drop (item_name = "Hot Sauce", hex_value = get_hex_value("Hot Sauce"), weight = 100),
            Drop (item_name = "Smelly Herb", hex_value = get_hex_value("Smelly Herb"), weight = 100),
            Drop (item_name = "Volt Shroom", hex_value = get_hex_value("Volt Shroom"), weight = 800),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '70':EnemyEntry (
        "Swooper",
        0x151,
        "Template 70",
        0.03,
        EnemyDrops (
            Drop (item_name = "Peachy Peach", hex_value = get_hex_value("Peachy Peach"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 100),
            Drop (item_name = "Fresh Veggie", hex_value = get_hex_value("Fresh Veggie"), weight = 100),
            Drop (item_name = "Horsetail", hex_value = get_hex_value("Horsetail"), weight = 100),
            Drop (item_name = "Sleepy Sleep", hex_value = get_hex_value("Sleepy Sleep"), weight = 800),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '71':EnemyEntry (
        "Glitchy Dark Koopa",
        None,
        "Template 71",
        0.05,
        EnemyDrops (
            Drop (item_name = "Turtley Leaf", hex_value = get_hex_value("Turtley Leaf"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    '72':EnemyEntry (
        "Goomba",
        0x11A,
        "Template 72",
        0.04,
        EnemyDrops (
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Honey Jar", hex_value = get_hex_value("Honey Jar"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 200),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '73':EnemyEntry (
        "Glitchy Koopa",
        None,
        "Template 73",
        0.09,
        EnemyDrops (
            Drop (item_name = "Turtley Leaf", hex_value = get_hex_value("Turtley Leaf"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    '74':EnemyEntry (
        "(Unused) Spinia",
        None,
        "Template 74",
        0.04,
        EnemyDrops (
            None
        )
    ),
    '75':EnemyEntry (
        "Spania",
        0x157,
        "Template 75",
        0.03,
        EnemyDrops (
            Drop (item_name = "Long-Last Shake", hex_value = get_hex_value("Long-Last Shake"), weight = 100),
            Drop (item_name = "Keel Mango", hex_value = get_hex_value("Keel Mango"), weight = 100),
            Drop (item_name = "Fresh Veggie", hex_value = get_hex_value("Fresh Veggie"), weight = 100),
            Drop (item_name = "Horsetail", hex_value = get_hex_value("Horsetail"), weight = 100),
            Drop (item_name = "Mystery Box", hex_value = get_hex_value("Mystery Box"), weight = 800),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '76':EnemyEntry (
        "(Unused) Spunia",
        None,
        "Template 76",
        0.04,
        EnemyDrops (
            None
        )
    ),
    '77':EnemyEntry (
        "Bald Cleft",
        0x16A,
        "Template 77",
        0.04,
        EnemyDrops (
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Honey Jar", hex_value = get_hex_value("Honey Jar"), weight = 100),
            Drop (item_name = "Courage Shell", hex_value = get_hex_value("Courage Shell"), weight = 800),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '78':EnemyEntry (
        "Moon Cleft",
        0x16B,
        "Template 78",
        0.04,
        EnemyDrops (
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Honey Jar", hex_value = get_hex_value("Honey Jar"), weight = 100),
            Drop (item_name = "Courage Shell", hex_value = get_hex_value("Courage Shell"), weight = 800),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '79':EnemyEntry (
        "Goomba",
        0x11A,
        "Template 79",
        0.04,
        EnemyDrops (
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Honey Jar", hex_value = get_hex_value("Honey Jar"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 200),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '80':EnemyEntry (
        "Magikoopa",
        0x13D,
        "Template 80",
        0.05,
        EnemyDrops (
            Drop (item_name = "Turtley Leaf", hex_value = get_hex_value("Turtley Leaf"), weight = 100),
            Drop (item_name = "Fire Burst", hex_value = get_hex_value("Fire Burst"), weight = 100),
            Drop (item_name = "Ice Storm", hex_value = get_hex_value("Ice Storm"), weight = 100),
            Drop (item_name = "Thunder Rage", hex_value = get_hex_value("Thunder Rage"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 100),
        )
    ),
    '81':EnemyEntry (
        "Broom Magikoopa",
        0x13D,
        "Template 81",
        0.05,
        EnemyDrops (
            Drop (item_name = "Turtley Leaf", hex_value = get_hex_value("Turtley Leaf"), weight = 100),
            Drop (item_name = "Fire Burst", hex_value = get_hex_value("Fire Burst"), weight = 100),
            Drop (item_name = "Ice Storm", hex_value = get_hex_value("Ice Storm"), weight = 100),
            Drop (item_name = "Thunder Rage", hex_value = get_hex_value("Thunder Rage"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 100),
        )
    ),
    '82':EnemyEntry (
        "Nothing?",
        None,
        "Template 82",
        0,
        EnemyDrops (
            None
        )
    ),
    '83':EnemyEntry (
        "Goomba",
        0x11A,
        "Template 83",
        0.04,
        EnemyDrops (
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Honey Jar", hex_value = get_hex_value("Honey Jar"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 200),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '84':EnemyEntry (
        "Headbonk Goomba",
        0x120,
        "Template 84",
        0.03,
        EnemyDrops (
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Honey Jar", hex_value = get_hex_value("Honey Jar"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 200),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '85':EnemyEntry (
        "Goomba",
        0x11A,
        "Template 85",
        0.04,
        EnemyDrops (
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Honey Jar", hex_value = get_hex_value("Honey Jar"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 200),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '86':EnemyEntry (
        "Barribad",
        0x1A1,
        "Template 86",
        0.05,
        EnemyDrops (
            Drop (item_name = "Power Steak", hex_value = get_hex_value("Power Steak"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 100),
            Drop (item_name = "Hot Sauce", hex_value = get_hex_value("Hot Sauce"), weight = 100),
            Drop (item_name = "Block Block", hex_value = get_hex_value("Block Block"), weight = 1200),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '87':EnemyEntry (
        "Barribad Projectile?",
        None,
        "Template 87",
        0,
        EnemyDrops (
            None
        )
    ),
    '88':EnemyEntry (
        "Pigarithm",
        0x1A4,
        "Template 88",
        0.05,
        EnemyDrops (
            Drop (item_name = "Long-Last Shake", hex_value = get_hex_value("Long-Last Shake"), weight = 200),
            Drop (item_name = "Thunder Rage", hex_value = get_hex_value("Thunder Rage"), weight = 200),
            Drop (item_name = "Shell Shock", hex_value = get_hex_value("Shell Shock"), weight = 200),
            Drop (item_name = "Volt Shroom", hex_value = get_hex_value("Volt Shroom"), weight = 200),
            Drop (item_name = "Sleepy Sleep", hex_value = get_hex_value("Sleepy Sleep"), weight = 200),
            Drop (item_name = "Mystery Box", hex_value = get_hex_value("Mystery Box"), weight = 200),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '89':EnemyEntry (
        "Goomba",
        0x11A,
        "Template 89",
        0.04,
        EnemyDrops (
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Honey Jar", hex_value = get_hex_value("Honey Jar"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 200),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '90':EnemyEntry (
        "Goomba",
        0x11A,
        "Template 90",
        0.04,
        EnemyDrops (
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Honey Jar", hex_value = get_hex_value("Honey Jar"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 200),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '91':EnemyEntry (
        "Goomba",
        0x11A,
        "Template 91",
        0.04,
        EnemyDrops (
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Honey Jar", hex_value = get_hex_value("Honey Jar"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 200),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '92':EnemyEntry (
        "Goomba",
        0x11A,
        "Template 92",
        0.04,
        EnemyDrops (
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Honey Jar", hex_value = get_hex_value("Honey Jar"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 200),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '93':EnemyEntry (
        "Goomba",
        0x11A,
        "Template 93",
        0.04,
        EnemyDrops (
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Honey Jar", hex_value = get_hex_value("Honey Jar"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 200),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '94':EnemyEntry (
        "Zombie Shroom",
        0x1C3,
        "Template 94",
        0.05,
        EnemyDrops (
            Drop (item_name = "Poison Shroom", hex_value = get_hex_value("Poison Shroom"), weight = 200),
            Drop (item_name = "Ghost Shroom", hex_value = get_hex_value("Ghost Shroom"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 30),
        )
    ),
    '95':EnemyEntry (
        "Goomba",
        0x11A,
        "Template 95",
        0.04,
        EnemyDrops (
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Honey Jar", hex_value = get_hex_value("Honey Jar"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 200),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '96':EnemyEntry (
        "Stone Buzzy",
        0x12F,
        "Template 96",
        0.03,
        EnemyDrops (
            Drop (item_name = "Peachy Peach", hex_value = get_hex_value("Peachy Peach"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Hot Sauce", hex_value = get_hex_value("Hot Sauce"), weight = 100),
            Drop (item_name = "Horsetail", hex_value = get_hex_value("Horsetail"), weight = 100),
            Drop (item_name = "Courage Shell", hex_value = get_hex_value("Courage Shell"), weight = 800),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '97':EnemyEntry (
        "Longator",
        0x19E,
        "Template 97",
        0.03,
        EnemyDrops (
            Drop (item_name = "Peachy Peach", hex_value = get_hex_value("Peachy Peach"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 100),
            Drop (item_name = "Fresh Veggie", hex_value = get_hex_value("Fresh Veggie"), weight = 100),
            Drop (item_name = "Horsetail", hex_value = get_hex_value("Horsetail"), weight = 100),
            Drop (item_name = "Stop Watch", hex_value = get_hex_value("Stop Watch"), weight = 800),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '98':EnemyEntry (
        "Goomba",
        0x11A,
        "Template 98",
        0.04,
        EnemyDrops (
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Honey Jar", hex_value = get_hex_value("Honey Jar"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 200),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '99':EnemyEntry (
        "Flip Spiny",
        0x131,
        "Template 99",
        0.03,
        EnemyDrops (
            Drop (item_name = "Power Steak", hex_value = get_hex_value("Power Steak"), weight = 100),
            Drop (item_name = "Fresh Pasta Bunch", hex_value = get_hex_value("Fresh Pasta Bunch"), weight = 100),
            Drop (item_name = "Hot Sauce", hex_value = get_hex_value("Hot Sauce"), weight = 100),
            Drop (item_name = "Smelly Herb", hex_value = get_hex_value("Smelly Herb"), weight = 100),
            Drop (item_name = "Mighty Tonic", hex_value = get_hex_value("Mighty Tonic"), weight = 800),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '100':EnemyEntry (
        "Mister I",
        0x188,
        "Template 100",
        0.1,
        EnemyDrops (
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 100),
            Drop (item_name = "Sleepy Sleep", hex_value = get_hex_value("Sleepy Sleep"), weight = 800),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '101':EnemyEntry (
        "(Unused) Flip Spike Top",
        0x12B,
        "Template 101",
        0.04,
        EnemyDrops (
            Drop (item_name = "Power Steak", hex_value = get_hex_value("Power Steak"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Hot Sauce", hex_value = get_hex_value("Hot Sauce"), weight = 100),
            Drop (item_name = "Smelly Herb", hex_value = get_hex_value("Smelly Herb"), weight = 100),
            Drop (item_name = "Courage Shell", hex_value = get_hex_value("Courage Shell"), weight = 800),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '102':EnemyEntry (
        "Nothing?",
        None,
        "Template 102",
        0,
        EnemyDrops (
            None
        )
    ),
    '103':EnemyEntry (
        "Projectile?",
        None,
        "Template 103",
        0,
        EnemyDrops (
            None
        )
    ),
    '104':EnemyEntry (
        "Gnip / Howl",
        0x186,
        "Template 104",
        0,
        EnemyDrops (
            None
        )
    ),
    '105':EnemyEntry (
        "Gnaw / Growl",
        0x187,
        "Template 105",
        0,
        EnemyDrops (
            None
        )
    ),
    '106':EnemyEntry (
        "Bullet Bill",
        0x173,
        "Template 106",
        0,
        EnemyDrops (
            None
        )
    ),
    '107':EnemyEntry (
        "Bill Blaster",
        0x174,
        "Template 107",
        0,
        EnemyDrops (
            None
        )
    ),
    '108':EnemyEntry (
        "(Unused) Giant Bombshell Bill",
        None,
        "Template 108",
        0.04,
        EnemyDrops (
            None
        )
    ),
    '109':EnemyEntry (
        "(Unused) Giant Bombshell Bill Blaster",
        None,
        "Template 109",
        0,
        EnemyDrops (
            None
        )
    ),
    '110':EnemyEntry (
        "Boo",
        0x162,
        "Template 110",
        0.04,
        EnemyDrops (
            Drop (item_name = "Peachy Peach", hex_value = get_hex_value("Peachy Peach"), weight = 100),
            Drop (item_name = "Keel Mango", hex_value = get_hex_value("Keel Mango"), weight = 100),
            Drop (item_name = "Long-Last Shake", hex_value = get_hex_value("Long-Last Shake"), weight = 100),
            Drop (item_name = "Horsetail", hex_value = get_hex_value("Horsetail"), weight = 100),
            Drop (item_name = "Sleepy Sleep", hex_value = get_hex_value("Sleepy Sleep"), weight = 400),
            Drop (item_name = "Ghost Shroom", hex_value = get_hex_value("Ghost Shroom"), weight = 400),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '111':EnemyEntry (
        "Dark Boo",
        0x163,
        "Template 111",
        0.04,
        EnemyDrops (
            Drop (item_name = "Peachy Peach", hex_value = get_hex_value("Peachy Peach"), weight = 100),
            Drop (item_name = "Keel Mango", hex_value = get_hex_value("Keel Mango"), weight = 100),
            Drop (item_name = "Long-Last Shake", hex_value = get_hex_value("Long-Last Shake"), weight = 100),
            Drop (item_name = "Horsetail", hex_value = get_hex_value("Horsetail"), weight = 100),
            Drop (item_name = "Sleepy Sleep", hex_value = get_hex_value("Sleepy Sleep"), weight = 400),
            Drop (item_name = "Ghost Shroom", hex_value = get_hex_value("Ghost Shroom"), weight = 800),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '112':EnemyEntry (
        "Atomic Boo",
        0x20D,
        "Template 112",
        0.2,
        EnemyDrops (
            Drop (item_name = "Ghost Shroom", hex_value = get_hex_value("Ghost Shroom"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    '113':EnemyEntry (
        "(Unused) Dark Atomic Boo",
        None,
        "Template 113",
        0.1,
        EnemyDrops (
            Drop (item_name = "Ghost Shroom", hex_value = get_hex_value("Ghost Shroom"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    '114':EnemyEntry (
        "Goomba",
        0x11A,
        "Template 114",
        0.04,
        EnemyDrops (
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Honey Jar", hex_value = get_hex_value("Honey Jar"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 200),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '115':EnemyEntry (
        "Goomba",
        0x11A,
        "Template 115",
        0.04,
        EnemyDrops (
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Honey Jar", hex_value = get_hex_value("Honey Jar"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 200),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '116':EnemyEntry (
        "Goomba",
        0x11A,
        "Template 116",
        0.04,
        EnemyDrops (
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Honey Jar", hex_value = get_hex_value("Honey Jar"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 200),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '117':EnemyEntry (
        "Fuzzy",
        0x14B,
        "Template 117",
        0.03,
        EnemyDrops (
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Honey Jar", hex_value = get_hex_value("Honey Jar"), weight = 100),
            Drop (item_name = "Life Shroom", hex_value = get_hex_value("Life Shroom"), weight = 400),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '118':EnemyEntry (
        "Goomba",
        0x11A,
        "Template 118",
        0.04,
        EnemyDrops (
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Honey Jar", hex_value = get_hex_value("Honey Jar"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 200),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '119':EnemyEntry (
        "Goomba",
        0x11A,
        "Template 119",
        0.04,
        EnemyDrops (
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Honey Jar", hex_value = get_hex_value("Honey Jar"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 200),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '120':EnemyEntry (
        "Pink Fuzzy",
        0x14C,
        "Template 120",
        0.03,
        EnemyDrops (
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Honey Jar", hex_value = get_hex_value("Honey Jar"), weight = 100),
            Drop (item_name = "Life Shroom", hex_value = get_hex_value("Life Shroom"), weight = 400),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    '121':EnemyEntry (
        "Goomba",
        0x11A,
        "Template 121",
        0.04,
        EnemyDrops (
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Honey Jar", hex_value = get_hex_value("Honey Jar"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 200),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '122':EnemyEntry (
        "Goomba",
        0x11A,
        "Template 122",
        0.04,
        EnemyDrops (
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Honey Jar", hex_value = get_hex_value("Honey Jar"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 200),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '123':EnemyEntry (
        "Goomba",
        0x11A,
        "Template 123",
        0.04,
        EnemyDrops (
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Honey Jar", hex_value = get_hex_value("Honey Jar"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 200),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '124':EnemyEntry (
        "Goomba",
        0x11A,
        "Template 124",
        0.04,
        EnemyDrops (
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Honey Jar", hex_value = get_hex_value("Honey Jar"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 200),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '125':EnemyEntry (
        "Weak Ruff Puff",
        0x155,
        "Template 125",
        0.04,
        EnemyDrops (
            None
        )
    ),
    '126':EnemyEntry (
        "Pokey",
        0x14E,
        "Template 126",
        0.03,
        EnemyDrops (
            Drop (item_name = "Peachy Peach", hex_value = get_hex_value("Peachy Peach"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 100),
            Drop (item_name = "Fresh Veggie", hex_value = get_hex_value("Fresh Veggie"), weight = 100),
            Drop (item_name = "Horsetail", hex_value = get_hex_value("Horsetail"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 40),
        )
    ),
    '127':EnemyEntry (
        "Poison Pokey",
        0x14F,
        "Template 127",
        1,
        EnemyDrops (
            Drop (item_name = "Peachy Peach", hex_value = get_hex_value("Peachy Peach"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 100),
            Drop (item_name = "Fresh Veggie", hex_value = get_hex_value("Fresh Veggie"), weight = 100),
            Drop (item_name = "Horsetail", hex_value = get_hex_value("Horsetail"), weight = 100),
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 800),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '128':EnemyEntry (
        "Koopa Striker",
        0x13F,
        "Template 128",
        0.05,
        EnemyDrops (
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 100),
            Drop (item_name = "Turtley Leaf", hex_value = get_hex_value("Turtley Leaf"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 20),
        )
    ),
    '129':EnemyEntry (
        "Koopa Striker's Shell",
        None,
        "Template 129",
        0,
        EnemyDrops (
            None
        )
    ),
    '130':EnemyEntry (
        "Mimi",
        0x1C7,
        "Template 130",
        0,
        EnemyDrops (
            None
        )
    ),
    '131':EnemyEntry (
        "Chasing Mimi",
        0x1C7,
        "Template 131",
        0,
        EnemyDrops (
            None
        )
    ),
    '132':EnemyEntry (
        "Bowser",
        0x1CA,
        "Template 132",
        0,
        EnemyDrops (
            None
        )
    ),
    '133':EnemyEntry (
        "Bittacuda",
        0x154,
        "Template 133",
        0.07,
        EnemyDrops (
            Drop (item_name = "Power Steak", hex_value = get_hex_value("Power Steak"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 100),
            Drop (item_name = "Hot Sauce", hex_value = get_hex_value("Hot Sauce"), weight = 100),
            Drop (item_name = "Smelly Herb", hex_value = get_hex_value("Smelly Herb"), weight = 100),
            Drop (item_name = "Volt Shroom", hex_value = get_hex_value("Volt Shroom"), weight = 800),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '134':EnemyEntry (
        "Nothing?",
        None,
        "Template 134",
        0,
        EnemyDrops (
            None
        )
    ),
    '135':EnemyEntry (
        "MeowBomb (Francis)",
        0x193,
        "Template 135",
        0,
        EnemyDrops (
            None
        )
    ),
    '136':EnemyEntry (
        "Big Blooper",
        0x1CF,
        "Template 136",
        0,
        EnemyDrops (
            None
        )
    ),
    '137':EnemyEntry (
        "Mr. L",
        0x1D2,
        "Template 137",
        0,
        EnemyDrops (
            None
        )
    ),
    '138':EnemyEntry (
        "Brobot",
        0x1D3,
        "Template 138",
        0,
        EnemyDrops (
            None
        )
    ),
    '139':EnemyEntry (
        "Brobot Missile",
        None,
        "Template 139",
        0,
        EnemyDrops (
            None
        )
    ),
    '140':EnemyEntry (
        "Brobot Mustache",
        None,
        "Template 140",
        0,
        EnemyDrops (
            None
        )
    ),
    '141':EnemyEntry (
        "Jawbus",
        0x182,
        "Template 141",
        0.1,
        EnemyDrops (
            Drop (item_name = "Fire Burst", hex_value = get_hex_value("Fire Burst"), weight = 300),
            Drop (item_name = "Ice Storm", hex_value = get_hex_value("Ice Storm"), weight = 200),
            Drop (item_name = "Thunder Rage", hex_value = get_hex_value("Thunder Rage"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 30),
        )
    ),
    '142':EnemyEntry (
        "Dimentio",
        0x1C6,
        "Template 142",
        0,
        EnemyDrops (
            None
        )
    ),
    '143':EnemyEntry (
        "Dimentio Magic",
        None,
        "Template 143",
        0,
        EnemyDrops (
            None
        )
    ),
    '144':EnemyEntry (
        "Sproing-Oing",
        0x17A,
        "Template 144",
        0.05,
        EnemyDrops (
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Honey Jar", hex_value = get_hex_value("Honey Jar"), weight = 100),
            Drop (item_name = "Long-Last Shake", hex_value = get_hex_value("Long-Last Shake"), weight = 400),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '145':EnemyEntry (
        "Mini Sproing-Oing",
        0x17A,
        "Template 145",
        0.02,
        EnemyDrops (
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    '146':EnemyEntry (
        "Rubee",
        None,
        "Template 146",
        0,
        EnemyDrops (
            None
        )
    ),
    '147':EnemyEntry (
        "Shlurp",
        0x16D,
        "Template 147",
        0.03,
        EnemyDrops (
            Drop (item_name = "Power Steak", hex_value = get_hex_value("Power Steak"), weight = 100),
            Drop (item_name = "Fresh Pasta Bunch", hex_value = get_hex_value("Fresh Pasta Bunch"), weight = 100),
            Drop (item_name = "Hot Sauce", hex_value = get_hex_value("Hot Sauce"), weight = 100),
            Drop (item_name = "Smelly Herb", hex_value = get_hex_value("Smelly Herb"), weight = 100),
            Drop (item_name = "Fire Burst", hex_value = get_hex_value("Fire Burst"), weight = 400),
            Drop (item_name = "POW Block", hex_value = get_hex_value("POW Block"), weight = 400),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '148':EnemyEntry (
        "Squig",
        0x176,
        "Template 148",
        0.03,
        EnemyDrops (
            Drop (item_name = "Power Steak", hex_value = get_hex_value("Power Steak"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 100),
            Drop (item_name = "Hot Sauce", hex_value = get_hex_value("Hot Sauce"), weight = 100),
            Drop (item_name = "Smelly Herb", hex_value = get_hex_value("Smelly Herb"), weight = 100),
            Drop (item_name = "Ice Storm", hex_value = get_hex_value("Ice Storm"), weight = 400),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '149':EnemyEntry (
        "Nothing?",
        None,
        "Template 149",
        0,
        EnemyDrops (
            None
        )
    ),
    '150':EnemyEntry (
        "King Croacus",
        0x1D1,
        "Template 150",
        0,
        EnemyDrops (
            None
        )
    ),
    '151':EnemyEntry (
        "Slow Cursya",
        0x159,
        "Template 151",
        0.1,
        EnemyDrops (
            Drop (item_name = "Poison Shroom", hex_value = get_hex_value("Poison Shroom"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    '152':EnemyEntry (
        "Megabite",
        0x1BB,
        "Template 152",
        0.1,
        EnemyDrops (
            Drop (item_name = "Shooting Star", hex_value = get_hex_value("Shooting Star"), weight = 100),
            Drop (item_name = "Ghost Shroom", hex_value = get_hex_value("Ghost Shroom"), weight = 200),
            Drop (item_name = "Catch Card SP", hex_value = get_hex_value("Catch Card SP"), weight = 200),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 30),
        )
    ),
    '153':EnemyEntry (
        "Boomboxer",
        0x17E,
        "Template 153",
        0.03,
        EnemyDrops (
            Drop (item_name = "Peachy Peach", hex_value = get_hex_value("Peachy Peach"), weight = 100),
            Drop (item_name = "Keel Mango", hex_value = get_hex_value("Keel Mango"), weight = 100),
            Drop (item_name = "Fresh Veggie", hex_value = get_hex_value("Fresh Veggie"), weight = 100),
            Drop (item_name = "Horsetail", hex_value = get_hex_value("Horsetail"), weight = 100),
            Drop (item_name = "Volt Shroom", hex_value = get_hex_value("Volt Shroom"), weight = 400),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '154':EnemyEntry (
        "Choppa",
        0x1A7,
        "Template 154",
        0.03,
        EnemyDrops (
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Honey Jar", hex_value = get_hex_value("Honey Jar"), weight = 100),
            Drop (item_name = "Long-Last Shake", hex_value = get_hex_value("Long-Last Shake"), weight = 400),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '155':EnemyEntry (
        "Croacus Petal",
        None,
        "Template 155",
        0,
        EnemyDrops (
            None
        )
    ),
    '156':EnemyEntry (
        "Croacus Petal",
        None,
        "Template 156",
        0,
        EnemyDrops (
            None
        )
    ),
    '157':EnemyEntry (
        "Croacus Petal",
        None,
        "Template 157",
        0,
        EnemyDrops (
            None
        )
    ),
    '158':EnemyEntry (
        "Boomboxer Attack",
        None,
        "Template 158",
        0,
        EnemyDrops (
            None
        )
    ),
    '159':EnemyEntry (
        "Ruff Puff",
        0x155,
        "Template 159",
        0.03,
        EnemyDrops (
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Honey Jar", hex_value = get_hex_value("Honey Jar"), weight = 100),
            Drop (item_name = "Long-Last Shake", hex_value = get_hex_value("Long-Last Shake"), weight = 800),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '160':EnemyEntry (
        "Tileoid G",
        0x18E,
        "Template 160",
        0.03,
        EnemyDrops (
            Drop (item_name = "Peachy Peach", hex_value = get_hex_value("Peachy Peach"), weight = 100),
            Drop (item_name = "Keel Mango", hex_value = get_hex_value("Keel Mango"), weight = 100),
            Drop (item_name = "Fresh Veggie", hex_value = get_hex_value("Fresh Veggie"), weight = 100),
            Drop (item_name = "Horsetail", hex_value = get_hex_value("Horsetail"), weight = 100),
            Drop (item_name = "Block Block", hex_value = get_hex_value("Block Block"), weight = 400),
            Drop (item_name = "Stop Watch", hex_value = get_hex_value("Stop Watch"), weight = 800),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '161':EnemyEntry (
        "Tileoid B",
        0x18F,
        "Template 161",
        0.03,
        EnemyDrops (
            Drop (item_name = "Peachy Peach", hex_value = get_hex_value("Peachy Peach"), weight = 100),
            Drop (item_name = "Keel Mango", hex_value = get_hex_value("Keel Mango"), weight = 100),
            Drop (item_name = "Fresh Veggie", hex_value = get_hex_value("Fresh Veggie"), weight = 100),
            Drop (item_name = "Horsetail", hex_value = get_hex_value("Horsetail"), weight = 100),
            Drop (item_name = "Block Block", hex_value = get_hex_value("Block Block"), weight = 400),
            Drop (item_name = "Stop Watch", hex_value = get_hex_value("Stop Watch"), weight = 800),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '162':EnemyEntry (
        "Tileoid R",
        0x190,
        "Template 162",
        0.03,
        EnemyDrops (
            Drop (item_name = "Power Steak", hex_value = get_hex_value("Power Steak"), weight = 100),
            Drop (item_name = "Fresh Pasta Bunch", hex_value = get_hex_value("Fresh Pasta Bunch"), weight = 100),
            Drop (item_name = "Hot Sauce", hex_value = get_hex_value("Hot Sauce"), weight = 100),
            Drop (item_name = "Smelly Herb", hex_value = get_hex_value("Smelly Herb"), weight = 100),
            Drop (item_name = "Block Block", hex_value = get_hex_value("Block Block"), weight = 400),
            Drop (item_name = "Stop Watch", hex_value = get_hex_value("Stop Watch"), weight = 400),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '163':EnemyEntry (
        "Tileoid Y",
        0x191,
        "Template 163",
        0.03,
        EnemyDrops (
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 100),
            Drop (item_name = "Fresh Pasta Bunch", hex_value = get_hex_value("Fresh Pasta Bunch"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Honey Jar", hex_value = get_hex_value("Honey Jar"), weight = 100),
            Drop (item_name = "Block Block", hex_value = get_hex_value("Block Block"), weight = 400),
            Drop (item_name = "Stop Watch", hex_value = get_hex_value("Stop Watch"), weight = 400),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '164':EnemyEntry (
        "Growmeba",
        0x18A,
        "Template 164",
        0,
        EnemyDrops (
            None
        )
    ),
    '165':EnemyEntry (
        "Growmeba Part",
        None,
        "Template 165",
        0,
        EnemyDrops (
            None
        )
    ),
    '166':EnemyEntry (
        "Boomerang",
        None,
        "Template 166",
        0,
        EnemyDrops (
            None
        )
    ),
    '167':EnemyEntry (
        "Fire Bro Fireball",
        None,
        "Template 167",
        0,
        EnemyDrops (
            None
        )
    ),
    '168':EnemyEntry (
        "BigMeow",
        0x197,
        "Template 168",
        0,
        EnemyDrops (
            None
        )
    ),
    '169':EnemyEntry (
        "Eeligon",
        0x19B,
        "Template 169",
        0.05,
        EnemyDrops (
            Drop (item_name = "Power Steak", hex_value = get_hex_value("Power Steak"), weight = 100),
            Drop (item_name = "Fresh Pasta Bunch", hex_value = get_hex_value("Fresh Pasta Bunch"), weight = 100),
            Drop (item_name = "Hot Sauce", hex_value = get_hex_value("Hot Sauce"), weight = 100),
            Drop (item_name = "Long-Last Shake", hex_value = get_hex_value("Long-Last Shake"), weight = 100),
            Drop (item_name = "Block Block", hex_value = get_hex_value("Block Block"), weight = 800),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '170':EnemyEntry (
        "Jellien",
        0x198,
        "Template 170",
        0.02,
        EnemyDrops (
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Honey Jar", hex_value = get_hex_value("Honey Jar"), weight = 100),
            Drop (item_name = "Volt Shroom", hex_value = get_hex_value("Volt Shroom"), weight = 400),
            Drop (item_name = "Thunder Rage", hex_value = get_hex_value("Thunder Rage"), weight = 200),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '171':EnemyEntry (
        "Foton",
        0x199,
        "Template 171",
        0.02,
        EnemyDrops (
            Drop (item_name = "Peachy Peach", hex_value = get_hex_value("Peachy Peach"), weight = 100),
            Drop (item_name = "Shooting Star", hex_value = get_hex_value("Shooting Star"), weight = 50),
            Drop (item_name = "Fresh Veggie", hex_value = get_hex_value("Fresh Veggie"), weight = 100),
            Drop (item_name = "Horsetail", hex_value = get_hex_value("Horsetail"), weight = 100),
            Drop (item_name = "Stop Watch", hex_value = get_hex_value("Stop Watch"), weight = 800),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '172':EnemyEntry (
        "Warpid",
        0x19A,
        "Template 172",
        0.02,
        EnemyDrops (
            Drop (item_name = "Peachy Peach", hex_value = get_hex_value("Peachy Peach"), weight = 100),
            Drop (item_name = "Shooting Star", hex_value = get_hex_value("Shooting Star"), weight = 50),
            Drop (item_name = "Fresh Veggie", hex_value = get_hex_value("Fresh Veggie"), weight = 100),
            Drop (item_name = "Horsetail", hex_value = get_hex_value("Horsetail"), weight = 100),
            Drop (item_name = "Stop Watch", hex_value = get_hex_value("Stop Watch"), weight = 800),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '173':EnemyEntry (
        "Muth",
        0x1AA,
        "Template 173",
        0.2,
        EnemyDrops (
            Drop (item_name = "Bone-In Cut", hex_value = get_hex_value("Bone-In Cut"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    '174':EnemyEntry (
        "Veggiefied O'Chunks",
        0x1C5,
        "Template 174",
        0,
        EnemyDrops (
            None
        )
    ),
    '175':EnemyEntry (
        "Floro Cragnon (Round)",
        0x1AE,
        "Template 175",
        0.07,
        EnemyDrops (
            Drop (item_name = "Keel Mango", hex_value = get_hex_value("Keel Mango"), weight = 100),
            Drop (item_name = "Primordial Fruit", hex_value = get_hex_value("Primordial Fruit"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 20),
        )
    ),
    '176':EnemyEntry (
        "Floro Cragnon (Triangular)",
        0x1AE,
        "Template 176",
        0.07,
        EnemyDrops (
            Drop (item_name = "Keel Mango", hex_value = get_hex_value("Keel Mango"), weight = 100),
            Drop (item_name = "Primordial Fruit", hex_value = get_hex_value("Primordial Fruit"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 20),
        )
    ),
    '177':EnemyEntry (
        "Trap Gold Bar x3",
        None,
        "Template 177",
        0,
        EnemyDrops (
            None
        )
    ),
    '178':EnemyEntry (
        "Ninjoe",
        0x1AF,
        "Template 178",
        0.07,
        EnemyDrops (
            Drop (item_name = "Thunder Rage", hex_value = get_hex_value("Thunder Rage"), weight = 100),
            Drop (item_name = "Volt Shroom", hex_value = get_hex_value("Volt Shroom"), weight = 100),
            Drop (item_name = "Stop Watch", hex_value = get_hex_value("Stop Watch"), weight = 200),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 30),
        )
    ),
    '179':EnemyEntry (
        "Player Pinwheel",
        None,
        "Template 179",
        0,
        EnemyDrops (
            None
        )
    ),
    '180':EnemyEntry (
        "Projectile?",
        None,
        "Template 180",
        0,
        EnemyDrops (
            None
        )
    ),
    '181':EnemyEntry (
        "O'Chunks",
        0x1C5,
        "Template 181",
        0,
        EnemyDrops (
            None
        )
    ),
    '182':EnemyEntry (
        "O'Chunks",
        0x1C5,
        "Template 182",
        0,
        EnemyDrops (
            None
        )
    ),
    '183':EnemyEntry (
        "Giant O'Chunks",
        0x1C5,
        "Template 183",
        0,
        EnemyDrops (
            None
        )
    ),
    '184':EnemyEntry (
        "Small Dimentio Dimension Cube",
        None,
        "Template 184",
        0,
        EnemyDrops (
            None
        )
    ),
    '185':EnemyEntry (
        "Medium Dimentio Dimension Cube",
        None,
        "Template 185",
        0,
        EnemyDrops (
            None
        )
    ),
    '186':EnemyEntry (
        "Big Dimentio Dimension Cube",
        None,
        "Template 186",
        0,
        EnemyDrops (
            None
        )
    ),
    '187':EnemyEntry (
        "World 6 Mimi",
        0x1C7,
        "Template 187",
        0,
        EnemyDrops (
            None
        )
    ),
    '188':EnemyEntry (
        "Brobot L Type",
        0x1D4,
        "Template 188",
        0,
        EnemyDrops (
            None
        )
    ),
    '189':EnemyEntry (
        "Bonechill",
        0x1D5,
        "Template 189",
        0,
        EnemyDrops (
            None
        )
    ),
    '190':EnemyEntry (
        "Bonechill Projectile",
        None,
        "Template 190",
        0,
        EnemyDrops (
            None
        )
    ),
    '191':EnemyEntry (
        "Bonechill Icicle",
        None,
        "Template 191",
        0,
        EnemyDrops (
            None
        )
    ),
    '192':EnemyEntry (
        "Ninjoe Attack",
        None,
        "Template 192",
        0,
        EnemyDrops (
            None
        )
    ),
    '193':EnemyEntry (
        "FRY_BAKUDAN (Nothing?)",
        None,
        "Template 193",
        0,
        EnemyDrops (
            None
        )
    ),
    '194':EnemyEntry (
        "Skellobit",
        0x1B4,
        "Template 194",
        0.03,
        EnemyDrops (
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Power Steak", hex_value = get_hex_value("Power Steak"), weight = 100),
            Drop (item_name = "Peachy Peach", hex_value = get_hex_value("Peachy Peach"), weight = 100),
            Drop (item_name = "Ice Storm", hex_value = get_hex_value("Ice Storm"), weight = 300),
            Drop (item_name = "Ghost Shroom", hex_value = get_hex_value("Ghost Shroom"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '195':EnemyEntry (
        "Spiky Skellobit",
        0x1B5,
        "Template 195",
        0.05,
        EnemyDrops (
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Power Steak", hex_value = get_hex_value("Power Steak"), weight = 100),
            Drop (item_name = "Peachy Peach", hex_value = get_hex_value("Peachy Peach"), weight = 100),
            Drop (item_name = "POW Block", hex_value = get_hex_value("POW Block"), weight = 300),
            Drop (item_name = "Ghost Shroom", hex_value = get_hex_value("Ghost Shroom"), weight = 100),
            Drop (item_name = "Super Shroom Shake", hex_value = get_hex_value("Super Shroom Shake"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '196':EnemyEntry (
        "Count Bleck",
        0x1D6,
        "Template 196",
        0,
        EnemyDrops (
            None
        )
    ),
    '197':EnemyEntry (
        "Void",
        None,
        "Template 197",
        0,
        EnemyDrops (
            None
        )
    ),
    '198':EnemyEntry (
        "Big Void",
        None,
        "Template 198",
        0,
        EnemyDrops (
            None
        )
    ),
    '199':EnemyEntry (
        "Particle",
        None,
        "Template 199",
        0,
        EnemyDrops (
            None
        )
    ),
    '200':EnemyEntry (
        "Nastasia?",
        None,
        "Template 200",
        0,
        EnemyDrops (
            None
        )
    ),
    '201':EnemyEntry (
        "Disappearing Count Bleck",
        None,
        "Template 201",
        0,
        EnemyDrops (
            None
        )
    ),
    '202':EnemyEntry (
        "Boomerang",
        None,
        "Template 202",
        0,
        EnemyDrops (
            None
        )
    ),
    '203':EnemyEntry (
        "Fire Bro Fire",
        None,
        "Template 203",
        0,
        EnemyDrops (
            None
        )
    ),
    '204':EnemyEntry (
        "Pokey Part",
        None,
        "Template 204",
        0,
        EnemyDrops (
            None
        )
    ),
    '205':EnemyEntry (
        "Poison Pokey Part",
        None,
        "Template 205",
        0,
        EnemyDrops (
            None
        )
    ),
    '206':EnemyEntry (
        "Back Cursya",
        0x15A,
        "Template 206",
        0.1,
        EnemyDrops (
            Drop (item_name = "Poison Shroom", hex_value = get_hex_value("Poison Shroom"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    '207':EnemyEntry (
        "Tech Cursya",
        0x15B,
        "Template 207",
        0.1,
        EnemyDrops (
            Drop (item_name = "Poison Shroom", hex_value = get_hex_value("Poison Shroom"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    '208':EnemyEntry (
        "Heavy Cursya",
        0x15C,
        "Template 208",
        0.1,
        EnemyDrops (
            Drop (item_name = "Poison Shroom", hex_value = get_hex_value("Poison Shroom"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    '209':EnemyEntry (
        "Reversya Cursya",
        0x15D,
        "Template 209",
        0.1,
        EnemyDrops (
            Drop (item_name = "Poison Shroom", hex_value = get_hex_value("Poison Shroom"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    '210':EnemyEntry (
        "Hooligon",
        0x19C,
        "Template 210",
        0.05,
        EnemyDrops (
            Drop (item_name = "Power Steak", hex_value = get_hex_value("Power Steak"), weight = 100),
            Drop (item_name = "Fresh Pasta Bunch", hex_value = get_hex_value("Fresh Pasta Bunch"), weight = 100),
            Drop (item_name = "Hot Sauce", hex_value = get_hex_value("Hot Sauce"), weight = 100),
            Drop (item_name = "Long-Last Shake", hex_value = get_hex_value("Long-Last Shake"), weight = 100),
            Drop (item_name = "Block Block", hex_value = get_hex_value("Block Block"), weight = 800),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '211':EnemyEntry (
        "Eeligon Part",
        None,
        "Template 211",
        0,
        EnemyDrops (
            None
        )
    ),
    '212':EnemyEntry (
        "Hooligon Part",
        None,
        "Template 212",
        0,
        EnemyDrops (
            None
        )
    ),
    '213':EnemyEntry (
        "Overworld Underchomp (3)",
        None,
        "Template 213",
        0,
        EnemyDrops (
            None
        )
    ),
    '214':EnemyEntry (
        "Overworld Blue Underchomp",
        None,
        "Template 214",
        0,
        EnemyDrops (
            None
        )
    ),
    '215':EnemyEntry (
        "Overworld Yellow Underchomp",
        None,
        "Template 215",
        0,
        EnemyDrops (
            None
        )
    ),
    '216':EnemyEntry (
        "Overworld Red Underchomp",
        0x168,
        "Template 216",
        0.05,
        EnemyDrops (
            Drop (item_name = "Power Steak", hex_value = get_hex_value("Power Steak"), weight = 100),
            Drop (item_name = "POW Block", hex_value = get_hex_value("POW Block"), weight = 200),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 30),
        )
    ),
    '217':EnemyEntry (
        "Crazee Dayzee",
        0x148,
        "Template 217",
        0.15,
        EnemyDrops (
            Drop (item_name = "Dayzee Tear", hex_value = get_hex_value("Dayzee Tear"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    '218':EnemyEntry (
        "Dayzee Attack",
        None,
        "Template 218",
        0,
        EnemyDrops (
            None
        )
    ),
    '219':EnemyEntry (
        "Stench",
        None,
        "Template 219",
        0,
        EnemyDrops (
            None
        )
    ),
    '220':EnemyEntry (
        "Freeze",
        None,
        "Template 220",
        0,
        EnemyDrops (
            None
        )
    ),
    '221':EnemyEntry (
        "Skellobomber w/Skellobait",
        0x1B8,
        "Template 221",
        0.03,
        EnemyDrops (
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Power Steak", hex_value = get_hex_value("Power Steak"), weight = 100),
            Drop (item_name = "Peachy Peach", hex_value = get_hex_value("Peachy Peach"), weight = 100),
            Drop (item_name = "Ice Storm", hex_value = get_hex_value("Ice Storm"), weight = 300),
            Drop (item_name = "Ghost Shroom", hex_value = get_hex_value("Ghost Shroom"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '222':EnemyEntry (
        "Skellobomber",
        0x1B8,
        "Template 222",
        0.03,
        EnemyDrops (
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Power Steak", hex_value = get_hex_value("Power Steak"), weight = 100),
            Drop (item_name = "Peachy Peach", hex_value = get_hex_value("Peachy Peach"), weight = 100),
            Drop (item_name = "Ice Storm", hex_value = get_hex_value("Ice Storm"), weight = 300),
            Drop (item_name = "Ghost Shroom", hex_value = get_hex_value("Ghost Shroom"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '223':EnemyEntry (
        "Skellobait",
        0x1B9,
        "Template 223",
        0.02,
        EnemyDrops (
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Power Steak", hex_value = get_hex_value("Power Steak"), weight = 100),
            Drop (item_name = "Peachy Peach", hex_value = get_hex_value("Peachy Peach"), weight = 100),
            Drop (item_name = "Ice Storm", hex_value = get_hex_value("Ice Storm"), weight = 300),
            Drop (item_name = "Ghost Shroom", hex_value = get_hex_value("Ghost Shroom"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '224':EnemyEntry (
        "Spiky Skellobait",
        0x1BA,
        "Template 224",
        0.02,
        EnemyDrops (
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Power Steak", hex_value = get_hex_value("Power Steak"), weight = 100),
            Drop (item_name = "Peachy Peach", hex_value = get_hex_value("Peachy Peach"), weight = 100),
            Drop (item_name = "Ice Storm", hex_value = get_hex_value("Ice Storm"), weight = 300),
            Drop (item_name = "Ghost Shroom", hex_value = get_hex_value("Ghost Shroom"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '225':EnemyEntry (
        "Dimentio",
        0x1C6,
        "Template 225",
        0,
        EnemyDrops (
            None
        )
    ),
    '226':EnemyEntry (
        "Dimentio",
        0x1C6,
        "Template 226",
        0,
        EnemyDrops (
            None
        )
    ),
    '227':EnemyEntry (
        "Skellobomber Head",
        None,
        "Template 227",
        0,
        EnemyDrops (
            None
        )
    ),
    '228':EnemyEntry (
        "Nothing?",
        None,
        "Template 228",
        0,
        EnemyDrops (
            None
        )
    ),
    '229':EnemyEntry (
        "Red Magiblot",
        0x1BE,
        "Template 229",
        0.04,
        EnemyDrops (
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 300),
            Drop (item_name = "Catch Card SP", hex_value = get_hex_value("Catch Card SP"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 100),
        )
    ),
    '230':EnemyEntry (
        "Blue Magiblot",
        0x1BF,
        "Template 230",
        0.04,
        EnemyDrops (
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 200),
            Drop (item_name = "Catch Card SP", hex_value = get_hex_value("Catch Card SP"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 100),
        )
    ),
    '231':EnemyEntry (
        "Yellow Magiblot",
        0x1C0,
        "Template 231",
        0.04,
        EnemyDrops (
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 100),
            Drop (item_name = "Catch Card SP", hex_value = get_hex_value("Catch Card SP"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 100),
        )
    ),
    '232':EnemyEntry (
        "Nothing?",
        None,
        "Template 232",
        0,
        EnemyDrops (
            None
        )
    ),
    '233':EnemyEntry (
        "Nothing?",
        None,
        "Template 233",
        0,
        EnemyDrops (
            None
        )
    ),
    '234':EnemyEntry (
        "Nothing?",
        None,
        "Template 234",
        0,
        EnemyDrops (
            None
        )
    ),
    '235':EnemyEntry (
        "Gloomba",
        0x11F,
        "Template 235",
        0.03,
        EnemyDrops (
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Honey Jar", hex_value = get_hex_value("Honey Jar"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 200),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '236':EnemyEntry (
        "Bone",
        None,
        "Template 236",
        0,
        EnemyDrops (
            None
        )
    ),
    '237':EnemyEntry (
        "Glasses-less Koopa",
        0x123,
        "Template 237",
        0.09,
        EnemyDrops (
            Drop (item_name = "Turtley Leaf", hex_value = get_hex_value("Turtley Leaf"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    '238':EnemyEntry (
        "Glasses-less Paratroopa",
        0x128,
        "Template 238",
        0.03,
        EnemyDrops (
            Drop (item_name = "Turtley Leaf", hex_value = get_hex_value("Turtley Leaf"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    '239':EnemyEntry (
        "Floro Sapien",
        0x1AD,
        "Template 239",
        0.08,
        EnemyDrops (
            Drop (item_name = "Sap Soup", hex_value = get_hex_value("Sap Soup"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    '240':EnemyEntry (
        "Floro Sapien Head",
        None,
        "Template 240",
        0,
        EnemyDrops (
            None
        )
    ),
    '241':EnemyEntry (
        "8-Bit Shell",
        None,
        "Template 241",
        0,
        EnemyDrops (
            None
        )
    ),
    '242':EnemyEntry (
        "Small 8-Bit Shell",
        None,
        "Template 242",
        0,
        EnemyDrops (
            None
        )
    ),
    '243':EnemyEntry (
        "Purple Floro Sapien",
        0x1AD,
        "Template 243",
        0.08,
        EnemyDrops (
            Drop (item_name = "Sap Soup", hex_value = get_hex_value("Sap Soup"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    '244':EnemyEntry (
        "Purple Floro Sapien Head",
        None,
        "Template 244",
        0,
        EnemyDrops (
            None
        )
    ),
    '245':EnemyEntry (
        "Red Floro Sapien",
        0x1AD,
        "Template 245",
        0.08,
        EnemyDrops (
            Drop (item_name = "Sap Soup", hex_value = get_hex_value("Sap Soup"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    '246':EnemyEntry (
        "Red Floro Sapien Head",
        None,
        "Template 246",
        0,
        EnemyDrops (
            None
        )
    ),
    '247':EnemyEntry (
        "Free Underhand",
        0x1B3,
        "Template 247",
        0,
        EnemyDrops (
            None
        )
    ),
    '248':EnemyEntry (
        "Bound Underhand",
        0x1B3,
        "Template 248",
        0,
        EnemyDrops (
            None
        )
    ),
    '249':EnemyEntry (
        "Disappearing Bound Underhand",
        0x1B3,
        "Template 249",
        0,
        EnemyDrops (
            None
        )
    ),
    '250':EnemyEntry (
        "Squiglet",
        0x175,
        "Template 250",
        0.03,
        EnemyDrops (
            Drop (item_name = "Peachy Peach", hex_value = get_hex_value("Peachy Peach"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 100),
            Drop (item_name = "Fresh Veggie", hex_value = get_hex_value("Fresh Veggie"), weight = 100),
            Drop (item_name = "Horsetail", hex_value = get_hex_value("Horsetail"), weight = 100),
            Drop (item_name = "Fire Burst", hex_value = get_hex_value("Fire Burst"), weight = 400),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '251':EnemyEntry (
        "Squog",
        0x177,
        "Template 251",
        0.03,
        EnemyDrops (
            Drop (item_name = "Power Steak", hex_value = get_hex_value("Power Steak"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 100),
            Drop (item_name = "Hot Sauce", hex_value = get_hex_value("Hot Sauce"), weight = 100),
            Drop (item_name = "Smelly Herb", hex_value = get_hex_value("Smelly Herb"), weight = 100),
            Drop (item_name = "Thunder Rage", hex_value = get_hex_value("Thunder Rage"), weight = 400),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '252':EnemyEntry (
        "Nothing?",
        None,
        "Template 252",
        0,
        EnemyDrops (
            None
        )
    ),
    '253':EnemyEntry (
        "Spike Top",
        0x12B,
        "Template 253",
        0.03,
        EnemyDrops (
            Drop (item_name = "Power Steak", hex_value = get_hex_value("Power Steak"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Hot Sauce", hex_value = get_hex_value("Hot Sauce"), weight = 100),
            Drop (item_name = "Smelly Herb", hex_value = get_hex_value("Smelly Herb"), weight = 100),
            Drop (item_name = "Courage Shell", hex_value = get_hex_value("Courage Shell"), weight = 800),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '254':EnemyEntry (
        "Broken Flip Koopa Troopa",
        0x123,
        "Template 254",
        0.09,
        EnemyDrops (
            Drop (item_name = "Turtley Leaf", hex_value = get_hex_value("Turtley Leaf"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    '255':EnemyEntry (
        "Super Dimentio",
        0x1D8,
        "Template 255",
        0,
        EnemyDrops (
            None
        )
    ),
    '256':EnemyEntry (
        "Pal Pill Luigi",
        None,
        "Template 256",
        0,
        EnemyDrops (
            None
        )
    ),
    '257':EnemyEntry (
        "Gold Bar",
        0x047,
        "Template 257",
        0,
        EnemyDrops (
            None
        )
    ),
    '258':EnemyEntry (
        "Gold Bar x3",
        0x048,
        "Template 258",
        0,
        EnemyDrops (
            None
        )
    ),
    '259':EnemyEntry (
        "Ninjohn",
        0x1B0,
        "Template 259",
        0.08,
        EnemyDrops (
            Drop (item_name = "Thunder Rage", hex_value = get_hex_value("Thunder Rage"), weight = 100),
            Drop (item_name = "Volt Shroom", hex_value = get_hex_value("Volt Shroom"), weight = 200),
            Drop (item_name = "Stop Watch", hex_value = get_hex_value("Stop Watch"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 30),
        )
    ),
    '260':EnemyEntry (
        "Ninjohn Projectile",
        None,
        "Template 260",
        0,
        EnemyDrops (
            None
        )
    ),
    '261':EnemyEntry (
        "Nothing?",
        None,
        "Template 261",
        0,
        EnemyDrops (
            None
        )
    ),
    '262':EnemyEntry (
        "Ninjerry",
        0x1B1,
        "Template 262",
        0.09,
        EnemyDrops (
            Drop (item_name = "Thunder Rage", hex_value = get_hex_value("Thunder Rage"), weight = 200),
            Drop (item_name = "Volt Shroom", hex_value = get_hex_value("Volt Shroom"), weight = 100),
            Drop (item_name = "Stop Watch", hex_value = get_hex_value("Stop Watch"), weight = 100),
            Drop (item_name = "Super Shroom Shake", hex_value = get_hex_value("Super Shroom Shake"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 30),
        )
    ),
    '263':EnemyEntry (
        "Ninjerry Projectile",
        None,
        "Template 263",
        0,
        EnemyDrops (
            None
        )
    ),
    '264':EnemyEntry (
        "Nothing?",
        None,
        "Template 264",
        0,
        EnemyDrops (
            None
        )
    ),
    '265':EnemyEntry (
        "Gigabite",
        0x1BC,
        "Template 265",
        0.1,
        EnemyDrops (
            Drop (item_name = "POW Block", hex_value = get_hex_value("POW Block"), weight = 100),
            Drop (item_name = "Ghost Shroom", hex_value = get_hex_value("Ghost Shroom"), weight = 100),
            Drop (item_name = "Catch Card SP", hex_value = get_hex_value("Catch Card SP"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 30),
        )
    ),
    '266':EnemyEntry (
        "Blomeba",
        0x18B,
        "Template 266",
        0,
        EnemyDrops (
            None
        )
    ),
    '267':EnemyEntry (
        "Chromeba",
        0x18C,
        "Template 267",
        0,
        EnemyDrops (
            None
        )
    ),
    '268':EnemyEntry (
        "Flip Koopa Stiker",
        0x13F,
        "Template 268",
        0.05,
        EnemyDrops (
            Drop (item_name = "Super Shroom Shake", hex_value = get_hex_value("Super Shroom Shake"), weight = 100),
            Drop (item_name = "Turtley Leaf", hex_value = get_hex_value("Turtley Leaf"), weight = 200),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 20),
        )
    ),
    '269':EnemyEntry (
        "Flip Toopa Striker",
        0x140,
        "Template 269",
        0,
        EnemyDrops (
            None
        )
    ),
    '270':EnemyEntry (
        "Soopa Striker",
        0x141,
        "Template 270",
        0.05,
        EnemyDrops (
            Drop (item_name = "Super Shroom Shake", hex_value = get_hex_value("Super Shroom Shake"), weight = 100),
            Drop (item_name = "Turtley Leaf", hex_value = get_hex_value("Turtley Leaf"), weight = 200),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 20),
        )
    ),
    '271':EnemyEntry (
        "Soopa Striker's Shell",
        None,
        "Template 271",
        0,
        EnemyDrops (
            None
        )
    ),
    '272':EnemyEntry (
        "Ghoul Shroom",
        0x1C4,
        "Template 272",
        0.05,
        EnemyDrops (
            Drop (item_name = "Poison Shroom", hex_value = get_hex_value("Poison Shroom"), weight = 200),
            Drop (item_name = "Ghost Shroom", hex_value = get_hex_value("Ghost Shroom"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 30),
        )
    ),
    '273':EnemyEntry (
        "Longadile",
        0x19F,
        "Template 273",
        0.03,
        EnemyDrops (
            Drop (item_name = "Peachy Peach", hex_value = get_hex_value("Peachy Peach"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 100),
            Drop (item_name = "Fresh Veggie", hex_value = get_hex_value("Fresh Veggie"), weight = 100),
            Drop (item_name = "Horsetail", hex_value = get_hex_value("Horsetail"), weight = 100),
            Drop (item_name = "Stop Watch", hex_value = get_hex_value("Stop Watch"), weight = 800),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '274':EnemyEntry (
        "Beepboxer",
        0x17F,
        "Template 274",
        0.03,
        EnemyDrops (
            Drop (item_name = "Peachy Peach", hex_value = get_hex_value("Peachy Peach"), weight = 100),
            Drop (item_name = "Keel Mango", hex_value = get_hex_value("Keel Mango"), weight = 100),
            Drop (item_name = "Fresh Veggie", hex_value = get_hex_value("Fresh Veggie"), weight = 100),
            Drop (item_name = "Horsetail", hex_value = get_hex_value("Horsetail"), weight = 100),
            Drop (item_name = "Volt Shroom", hex_value = get_hex_value("Volt Shroom"), weight = 400),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '275':EnemyEntry (
        "Nothing?",
        None,
        "Template 275",
        0,
        EnemyDrops (
            None
        )
    ),
    '276':EnemyEntry (
        "(Unused) Boomboxer Recolor",
        None,
        "Template 276",
        0.04,
        EnemyDrops (
            None
        )
    ),
    '277':EnemyEntry (
        "Nothing?",
        None,
        "Template 277",
        0,
        EnemyDrops (
            None
        )
    ),
    '278':EnemyEntry (
        "Copta",
        0x1A8,
        "Template 278",
        0.03,
        EnemyDrops (
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Honey Jar", hex_value = get_hex_value("Honey Jar"), weight = 100),
            Drop (item_name = "Long-Last Shake", hex_value = get_hex_value("Long-Last Shake"), weight = 400),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '279':EnemyEntry (
        "(Unused) Muth Recolor",
        None,
        "Template 279",
        1,
        EnemyDrops (
            None
        )
    ),
    '280':EnemyEntry (
        "Red I",
        0x189,
        "Template 280",
        0.1,
        EnemyDrops (
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 100),
            Drop (item_name = "Sleepy Sleep", hex_value = get_hex_value("Sleepy Sleep"), weight = 800),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '281':EnemyEntry (
        "Nothing?",
        None,
        "Template 281",
        0,
        EnemyDrops (
            None
        )
    ),
    '282':EnemyEntry (
        "Nothing?",
        None,
        "Template 282",
        0,
        EnemyDrops (
            None
        )
    ),
    '283':EnemyEntry (
        "Squoinker",
        0x179,
        "Template 283",
        0.03,
        EnemyDrops (
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Honey Jar", hex_value = get_hex_value("Honey Jar"), weight = 100),
            Drop (item_name = "Shooting Star", hex_value = get_hex_value("Shooting Star"), weight = 400),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '284':EnemyEntry (
        "Nothing?",
        None,
        "Template 284",
        0,
        EnemyDrops (
            None
        )
    ),
    '285':EnemyEntry (
        "Dark Bowser",
        0x1CB,
        "Template 285",
        0,
        EnemyDrops (
            None
        )
    ),
    '286':EnemyEntry (
        "Dark Luigi",
        0x1CC,
        "Template 286",
        0,
        EnemyDrops (
            None
        )
    ),
    '287':EnemyEntry (
        "Dark Mario",
        0x1CD,
        "Template 287",
        0,
        EnemyDrops (
            None
        )
    ),
    '288':EnemyEntry (
        "Dark Peach",
        0x1CE,
        "Template 288",
        0,
        EnemyDrops (
            None
        )
    ),
    '289':EnemyEntry (
        "Boing-Oing",
        0x17B,
        "Template 289",
        0.05,
        EnemyDrops (
            Drop (item_name = "Peachy Peach", hex_value = get_hex_value("Peachy Peach"), weight = 100),
            Drop (item_name = "Keel Mango", hex_value = get_hex_value("Keel Mango"), weight = 100),
            Drop (item_name = "Fresh Veggie", hex_value = get_hex_value("Fresh Veggie"), weight = 100),
            Drop (item_name = "Horsetail", hex_value = get_hex_value("Horsetail"), weight = 100),
            Drop (item_name = "Long-Last Shake", hex_value = get_hex_value("Long-Last Shake"), weight = 400),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '290':EnemyEntry (
        "Mini Boing-Oing",
        0x17B,
        "Template 290",
        0.02,
        EnemyDrops (
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    '291':EnemyEntry (
        "Zoing-Oing",
        0x17C,
        "Template 291",
        0.05,
        EnemyDrops (
            Drop (item_name = "Peachy Peach", hex_value = get_hex_value("Peachy Peach"), weight = 100),
            Drop (item_name = "Keel Mango", hex_value = get_hex_value("Keel Mango"), weight = 100),
            Drop (item_name = "Fresh Veggie", hex_value = get_hex_value("Fresh Veggie"), weight = 100),
            Drop (item_name = "Horsetail", hex_value = get_hex_value("Horsetail"), weight = 100),
            Drop (item_name = "Long-Last Shake", hex_value = get_hex_value("Long-Last Shake"), weight = 400),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '292':EnemyEntry (
        "Mini Zoing-Oing",
        0x17C,
        "Template 292",
        0.02,
        EnemyDrops (
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    '293':EnemyEntry (
        "Mega Muth",
        0x1AC,
        "Template 293",
        0.2,
        EnemyDrops (
            Drop (item_name = "Bone-In Cut", hex_value = get_hex_value("Bone-In Cut"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    '294':EnemyEntry (
        "Blastboxer",
        0x181,
        "Template 294",
        0.03,
        EnemyDrops (
            Drop (item_name = "Peachy Peach", hex_value = get_hex_value("Peachy Peach"), weight = 100),
            Drop (item_name = "Keel Mango", hex_value = get_hex_value("Keel Mango"), weight = 100),
            Drop (item_name = "Fresh Veggie", hex_value = get_hex_value("Fresh Veggie"), weight = 100),
            Drop (item_name = "Horsetail", hex_value = get_hex_value("Horsetail"), weight = 100),
            Drop (item_name = "Volt Shroom", hex_value = get_hex_value("Volt Shroom"), weight = 400),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '295':EnemyEntry (
        "Nothing?",
        None,
        "Template 295",
        0,
        EnemyDrops (
            None
        )
    ),
    '296':EnemyEntry (
        "Rawbus",
        0x183,
        "Template 296",
        0.1,
        EnemyDrops (
            Drop (item_name = "Fire Burst", hex_value = get_hex_value("Fire Burst"), weight = 100),
            Drop (item_name = "Ice Storm", hex_value = get_hex_value("Ice Storm"), weight = 100),
            Drop (item_name = "Thunder Rage", hex_value = get_hex_value("Thunder Rage"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 30),
        )
    ),
    '297':EnemyEntry (
        "Gawbus",
        0x185,
        "Template 297",
        0.1,
        EnemyDrops (
            Drop (item_name = "Fire Burst", hex_value = get_hex_value("Fire Burst"), weight = 100),
            Drop (item_name = "Ice Storm", hex_value = get_hex_value("Ice Storm"), weight = 200),
            Drop (item_name = "Thunder Rage", hex_value = get_hex_value("Thunder Rage"), weight = 300),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 30),
        )
    ),
    '298':EnemyEntry (
        "Sobarribad",
        0x1A2,
        "Template 298",
        0.05,
        EnemyDrops (
            Drop (item_name = "Power Steak", hex_value = get_hex_value("Power Steak"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 100),
            Drop (item_name = "Hot Sauce", hex_value = get_hex_value("Hot Sauce"), weight = 100),
            Drop (item_name = "Block Block", hex_value = get_hex_value("Block Block"), weight = 1200),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '299':EnemyEntry (
        "Sobarribad Projectile",
        None,
        "Template 299",
        0,
        EnemyDrops (
            None
        )
    ),
    '300':EnemyEntry (
        "Hogarithm",
        0x1A5,
        "Template 300",
        0.05,
        EnemyDrops (
            Drop (item_name = "Long-Last Shake", hex_value = get_hex_value("Long-Last Shake"), weight = 200),
            Drop (item_name = "Shooting Star", hex_value = get_hex_value("Shooting Star"), weight = 200),
            Drop (item_name = "Block Block", hex_value = get_hex_value("Block Block"), weight = 200),
            Drop (item_name = "Ghost Shroom", hex_value = get_hex_value("Ghost Shroom"), weight = 200),
            Drop (item_name = "Stop Watch", hex_value = get_hex_value("Stop Watch"), weight = 200),
            Drop (item_name = "Mighty Tonic", hex_value = get_hex_value("Mighty Tonic"), weight = 200),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '301':EnemyEntry (
        "Shlorp",
        0x16E,
        "Template 301",
        0.03,
        EnemyDrops (
            Drop (item_name = "Power Steak", hex_value = get_hex_value("Power Steak"), weight = 100),
            Drop (item_name = "Fresh Pasta Bunch", hex_value = get_hex_value("Fresh Pasta Bunch"), weight = 100),
            Drop (item_name = "Hot Sauce", hex_value = get_hex_value("Hot Sauce"), weight = 100),
            Drop (item_name = "Smelly Herb", hex_value = get_hex_value("Smelly Herb"), weight = 100),
            Drop (item_name = "Fire Burst", hex_value = get_hex_value("Fire Burst"), weight = 400),
            Drop (item_name = "POW Block", hex_value = get_hex_value("POW Block"), weight = 800),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '302':EnemyEntry (
        "Amazee Dayzee",
        0x149,
        "Template 302",
        0.7,
        EnemyDrops (
            Drop (item_name = "Golden Leaf", hex_value = get_hex_value("Golden Leaf"), weight = 200),
            Drop (item_name = "Dayzee Tear", hex_value = get_hex_value("Dayzee Tear"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 20),
        )
    ),
    '303':EnemyEntry (
        "Nothing?",
        None,
        "Template 303",
        0,
        EnemyDrops (
            None
        )
    ),
    '304':EnemyEntry (
        "Flip Gloomba",
        0x11F,
        "Template 304",
        0.03,
        EnemyDrops (
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Honey Jar", hex_value = get_hex_value("Honey Jar"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 200),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '305':EnemyEntry (
        "Invincible Underchomp",
        None,
        "Template 305",
        0,
        EnemyDrops (
            None
        )
    ),
    '306':EnemyEntry (
        "Invincible Blue Underchomp",
        None,
        "Template 306",
        0,
        EnemyDrops (
            None
        )
    ),
    '307':EnemyEntry (
        "Invincible Yellow Underchomp",
        None,
        "Template 307",
        0,
        EnemyDrops (
            None
        )
    ),
    '308':EnemyEntry (
        "Invincible Red Underchomp",
        None,
        "Template 308",
        0,
        EnemyDrops (
            None
        )
    ),
    '309':EnemyEntry (
        "Nothing?",
        None,
        "Template 309",
        0,
        EnemyDrops (
            None
        )
    ),
    '310':EnemyEntry (
        "Flip Boomerang Bro",
        0x138,
        "Template 310",
        0.05,
        EnemyDrops (
            Drop (item_name = "Super Shroom Shake", hex_value = get_hex_value("Super Shroom Shake"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Honey Jar", hex_value = get_hex_value("Honey Jar"), weight = 100),
            Drop (item_name = "Fire Burst", hex_value = get_hex_value("Fire Burst"), weight = 400),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '311':EnemyEntry (
        "Flip Fire Bro",
        0x139,
        "Template 311",
        0.05,
        EnemyDrops (
            Drop (item_name = "Super Shroom Shake", hex_value = get_hex_value("Super Shroom Shake"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Honey Jar", hex_value = get_hex_value("Honey Jar"), weight = 100),
            Drop (item_name = "Fire Burst", hex_value = get_hex_value("Fire Burst"), weight = 800),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '312':EnemyEntry (
        "Flip Skellobit",
        0x1B4,
        "Template 312",
        0.03,
        EnemyDrops (
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Power Steak", hex_value = get_hex_value("Power Steak"), weight = 100),
            Drop (item_name = "Peachy Peach", hex_value = get_hex_value("Peachy Peach"), weight = 100),
            Drop (item_name = "Ice Storm", hex_value = get_hex_value("Ice Storm"), weight = 300),
            Drop (item_name = "Ghost Shroom", hex_value = get_hex_value("Ghost Shroom"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '313':EnemyEntry (
        "Flip Spiky Skellobit",
        0x1B5,
        "Template 313",
        0.05,
        EnemyDrops (
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Power Steak", hex_value = get_hex_value("Power Steak"), weight = 100),
            Drop (item_name = "Peachy Peach", hex_value = get_hex_value("Peachy Peach"), weight = 100),
            Drop (item_name = "POW Block", hex_value = get_hex_value("POW Block"), weight = 300),
            Drop (item_name = "Ghost Shroom", hex_value = get_hex_value("Ghost Shroom"), weight = 100),
            Drop (item_name = "Super Shroom Shake", hex_value = get_hex_value("Super Shroom Shake"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '314':EnemyEntry (
        "Flip Skellobomber w/Skellobait",
        0x1B8,
        "Template 314",
        0.03,
        EnemyDrops (
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Power Steak", hex_value = get_hex_value("Power Steak"), weight = 100),
            Drop (item_name = "Peachy Peach", hex_value = get_hex_value("Peachy Peach"), weight = 100),
            Drop (item_name = "Ice Storm", hex_value = get_hex_value("Ice Storm"), weight = 300),
            Drop (item_name = "Ghost Shroom", hex_value = get_hex_value("Ghost Shroom"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '315':EnemyEntry (
        "Flip Skellobomber",
        0x1B8,
        "Template 315",
        0.03,
        EnemyDrops (
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Power Steak", hex_value = get_hex_value("Power Steak"), weight = 100),
            Drop (item_name = "Peachy Peach", hex_value = get_hex_value("Peachy Peach"), weight = 100),
            Drop (item_name = "Ice Storm", hex_value = get_hex_value("Ice Storm"), weight = 300),
            Drop (item_name = "Ghost Shroom", hex_value = get_hex_value("Ghost Shroom"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '316':EnemyEntry (
        "(Unused) Green Magikoopa",
        None,
        "Template 316",
        0.04,
        EnemyDrops (
            None
        )
    ),
    '317':EnemyEntry (
        "(Unused) Broom Green Magikoopa",
        None,
        "Template 317",
        0.04,
        EnemyDrops (
            None
        )
    ),
    '318':EnemyEntry (
        "Nothing?",
        None,
        "Template 318",
        0,
        EnemyDrops (
            None
        )
    ),
    '319':EnemyEntry (
        "(Unused) White Magikoopa",
        None,
        "Template 319",
        0.04,
        EnemyDrops (
            None
        )
    ),
    '320':EnemyEntry (
        "(Unused) Broom White Magikoopa",
        None,
        "Template 320",
        0.04,
        EnemyDrops (
            None
        )
    ),
    '321':EnemyEntry (
        "Nothing?",
        None,
        "Template 321",
        0,
        EnemyDrops (
            None
        )
    ),
    '322':EnemyEntry (
        "(Unused) Red Magikoopa",
        None,
        "Template 322",
        0.04,
        EnemyDrops (
            None
        )
    ),
    '323':EnemyEntry (
        "(Unused) Broom Red Magikoopa",
        None,
        "Template 323",
        0.04,
        EnemyDrops (
            None
        )
    ),
    '324':EnemyEntry (
        "Nothing?",
        None,
        "Template 324",
        0,
        EnemyDrops (
            None
        )
    ),
    '325':EnemyEntry (
        "Nothing?",
        None,
        "Template 325",
        0,
        EnemyDrops (
            None
        )
    ),
    '326':EnemyEntry (
        "Nothing?",
        None,
        "Template 326",
        0,
        EnemyDrops (
            None
        )
    ),
    '327':EnemyEntry (
        "Dark Spiked Goomba",
        0x11C,
        "Template 327",
        0.04,
        EnemyDrops (
            Drop (item_name = "Power Steak", hex_value = get_hex_value("Power Steak"), weight = 100),
            Drop (item_name = "Fresh Pasta Bunch", hex_value = get_hex_value("Fresh Pasta Bunch"), weight = 100),
            Drop (item_name = "Hot Sauce", hex_value = get_hex_value("Hot Sauce"), weight = 100),
            Drop (item_name = "Smelly Herb", hex_value = get_hex_value("Smelly Herb"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 200),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '328':EnemyEntry (
        "Dark Paragoomba",
        0x11E,
        "Template 328",
        0.04,
        EnemyDrops (
            Drop (item_name = "Peachy Peach", hex_value = get_hex_value("Peachy Peach"), weight = 100),
            Drop (item_name = "Keel Mango", hex_value = get_hex_value("Keel Mango"), weight = 100),
            Drop (item_name = "Fresh Veggie", hex_value = get_hex_value("Fresh Veggie"), weight = 100),
            Drop (item_name = "Horsetail", hex_value = get_hex_value("Horsetail"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 200),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '329':EnemyEntry (
        "Dark Goomba",
        0x122,
        "Template 329",
        0.04,
        EnemyDrops (
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Honey Jar", hex_value = get_hex_value("Honey Jar"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 200),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '330':EnemyEntry (
        "Dark Headbonk Goomba",
        0x121,
        "Template 330",
        0.04,
        EnemyDrops (
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Honey Jar", hex_value = get_hex_value("Honey Jar"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 200),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '331':EnemyEntry (
        "Dark Koopatrol",
        0x125,
        "Template 331",
        0.07,
        EnemyDrops (
            Drop (item_name = "Turtley Leaf", hex_value = get_hex_value("Turtley Leaf"), weight = 100),
            Drop (item_name = "Thunder Rage", hex_value = get_hex_value("Thunder Rage"), weight = 300),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 20),
        )
    ),
    '332':EnemyEntry (
        "Dark Shady Koopa",
        None,
        "Template 332",
        0.04,
        EnemyDrops (
            None
        )
    ),
    '333':EnemyEntry (
        "Dark Paratroopa",
        0x129,
        "Template 333",
        0.05,
        EnemyDrops (
            Drop (item_name = "Turtley Leaf", hex_value = get_hex_value("Turtley Leaf"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    '334':EnemyEntry (
        "Dark Spike Top",
        0x12C,
        "Template 334",
        0.05,
        EnemyDrops (
            Drop (item_name = "Power Steak", hex_value = get_hex_value("Power Steak"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Hot Sauce", hex_value = get_hex_value("Hot Sauce"), weight = 100),
            Drop (item_name = "Smelly Herb", hex_value = get_hex_value("Smelly Herb"), weight = 100),
            Drop (item_name = "Courage Shell", hex_value = get_hex_value("Courage Shell"), weight = 800),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '335':EnemyEntry (
        "Dark Stone Buzzy",
        0x130,
        "Template 335",
        0.05,
        EnemyDrops (
            Drop (item_name = "Peachy Peach", hex_value = get_hex_value("Peachy Peach"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Hot Sauce", hex_value = get_hex_value("Hot Sauce"), weight = 100),
            Drop (item_name = "Horsetail", hex_value = get_hex_value("Horsetail"), weight = 100),
            Drop (item_name = "Courage Shell", hex_value = get_hex_value("Courage Shell"), weight = 800),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '336':EnemyEntry (
        "Dark Spiny",
        0x132,
        "Template 336",
        0.05,
        EnemyDrops (
            Drop (item_name = "Power Steak", hex_value = get_hex_value("Power Steak"), weight = 100),
            Drop (item_name = "Fresh Pasta Bunch", hex_value = get_hex_value("Fresh Pasta Bunch"), weight = 100),
            Drop (item_name = "Hot Sauce", hex_value = get_hex_value("Hot Sauce"), weight = 100),
            Drop (item_name = "Smelly Herb", hex_value = get_hex_value("Smelly Herb"), weight = 100),
            Drop (item_name = "Mighty Tonic", hex_value = get_hex_value("Mighty Tonic"), weight = 800),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '337':EnemyEntry (
        "Dark Dull Bones",
        0x135,
        "Template 337",
        0.04,
        EnemyDrops (
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Honey Jar", hex_value = get_hex_value("Honey Jar"), weight = 100),
            Drop (item_name = "Ice Storm", hex_value = get_hex_value("Ice Storm"), weight = 800),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '338':EnemyEntry (
        "Dark Bone",
        None,
        "Template 338",
        0,
        EnemyDrops (
            None
        )
    ),
    '339':EnemyEntry (
        "Dark Hammer Bro",
        0x13A,
        "Template 339",
        0.07,
        EnemyDrops (
            Drop (item_name = "Super Shroom Shake", hex_value = get_hex_value("Super Shroom Shake"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Honey Jar", hex_value = get_hex_value("Honey Jar"), weight = 100),
            Drop (item_name = "Fire Burst", hex_value = get_hex_value("Fire Burst"), weight = 400),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '340':EnemyEntry (
        "Dark Boomerang Bro",
        0x13B,
        "Template 340",
        0.07,
        EnemyDrops (
            Drop (item_name = "Super Shroom Shake", hex_value = get_hex_value("Super Shroom Shake"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Honey Jar", hex_value = get_hex_value("Honey Jar"), weight = 100),
            Drop (item_name = "Fire Burst", hex_value = get_hex_value("Fire Burst"), weight = 400),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '341':EnemyEntry (
        "Dark Fire Bro",
        0x13C,
        "Template 341",
        0.07,
        EnemyDrops (
            Drop (item_name = "Super Shroom Shake", hex_value = get_hex_value("Super Shroom Shake"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Honey Jar", hex_value = get_hex_value("Honey Jar"), weight = 100),
            Drop (item_name = "Fire Burst", hex_value = get_hex_value("Fire Burst"), weight = 800),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '342':EnemyEntry (
        "Dark Hammer",
        None,
        "Template 342",
        0,
        EnemyDrops (
            None
        )
    ),
    '343':EnemyEntry (
        "Dark Boomerang",
        None,
        "Template 343",
        0,
        EnemyDrops (
            None
        )
    ),
    '344':EnemyEntry (
        "Dark Fire Bro Fireball",
        None,
        "Template 344",
        0,
        EnemyDrops (
            None
        )
    ),
    '345':EnemyEntry (
        "Dark Magikoopa",
        0x13E,
        "Template 345",
        0.07,
        EnemyDrops (
            Drop (item_name = "Turtley Leaf", hex_value = get_hex_value("Turtley Leaf"), weight = 100),
            Drop (item_name = "Fire Burst", hex_value = get_hex_value("Fire Burst"), weight = 100),
            Drop (item_name = "Ice Storm", hex_value = get_hex_value("Ice Storm"), weight = 100),
            Drop (item_name = "Thunder Rage", hex_value = get_hex_value("Thunder Rage"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 100),
        )
    ),
    '346':EnemyEntry (
        "Broom Dark Magikoopa",
        0x13E,
        "Template 346",
        0.07,
        EnemyDrops (
            Drop (item_name = "Turtley Leaf", hex_value = get_hex_value("Turtley Leaf"), weight = 100),
            Drop (item_name = "Fire Burst", hex_value = get_hex_value("Fire Burst"), weight = 100),
            Drop (item_name = "Ice Storm", hex_value = get_hex_value("Ice Storm"), weight = 100),
            Drop (item_name = "Thunder Rage", hex_value = get_hex_value("Thunder Rage"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 100),
        )
    ),
    '347':EnemyEntry (
        "Nothing?",
        None,
        "Template 347",
        0,
        EnemyDrops (
            None
        )
    ),
    '348':EnemyEntry (
        "Dark Striker",
        0x142,
        "Template 348",
        0.07,
        EnemyDrops (
            Drop (item_name = "Super Shroom Shake", hex_value = get_hex_value("Super Shroom Shake"), weight = 100),
            Drop (item_name = "Turtley Leaf", hex_value = get_hex_value("Turtley Leaf"), weight = 200),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 20),
        )
    ),
    '349':EnemyEntry (
        "Dark Striker's Shell",
        None,
        "Template 349",
        0,
        EnemyDrops (
            None
        )
    ),
    '350':EnemyEntry (
        "Dark Clubba",
        0x144,
        "Template 350",
        0.05,
        EnemyDrops (
            Drop (item_name = "Power Steak", hex_value = get_hex_value("Power Steak"), weight = 100),
            Drop (item_name = "Fresh Pasta Bunch", hex_value = get_hex_value("Fresh Pasta Bunch"), weight = 100),
            Drop (item_name = "Hot Sauce", hex_value = get_hex_value("Hot Sauce"), weight = 100),
            Drop (item_name = "Smelly Herb", hex_value = get_hex_value("Smelly Herb"), weight = 100),
            Drop (item_name = "Fire Burst", hex_value = get_hex_value("Fire Burst"), weight = 800),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '351':EnemyEntry (
        "Dark Dayzee",
        0x14A,
        "Template 351",
        0.15,
        EnemyDrops (
            Drop (item_name = "Golden Leaf", hex_value = get_hex_value("Golden Leaf"), weight = 200),
            Drop (item_name = "Dayzee Tear", hex_value = get_hex_value("Dayzee Tear"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 20),
        )
    ),
    '352':EnemyEntry (
        "Nothing?",
        None,
        "Template 352",
        0,
        EnemyDrops (
            None
        )
    ),
    '353':EnemyEntry (
        "Goomba",
        0x11A,
        "Template 353",
        0.04,
        EnemyDrops (
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Honey Jar", hex_value = get_hex_value("Honey Jar"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 200),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '354':EnemyEntry (
        "Dark Fuzzy",
        0x14D,
        "Template 354",
        0.05,
        EnemyDrops (
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Honey Jar", hex_value = get_hex_value("Honey Jar"), weight = 100),
            Drop (item_name = "Life Shroom", hex_value = get_hex_value("Life Shroom"), weight = 400),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    '355':EnemyEntry (
        "Dark Pokey",
        0x150,
        "Template 355",
        0.5,
        EnemyDrops (
            Drop (item_name = "Peachy Peach", hex_value = get_hex_value("Peachy Peach"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 100),
            Drop (item_name = "Fresh Veggie", hex_value = get_hex_value("Fresh Veggie"), weight = 100),
            Drop (item_name = "Horsetail", hex_value = get_hex_value("Horsetail"), weight = 100),
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 800),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '356':EnemyEntry (
        "Dark Pokey Part",
        None,
        "Template 356",
        0,
        EnemyDrops (
            None
        )
    ),
    '357':EnemyEntry (
        "Dark Ruff Puff",
        0x156,
        "Template 357",
        0.04,
        EnemyDrops (
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Honey Jar", hex_value = get_hex_value("Honey Jar"), weight = 100),
            Drop (item_name = "Long-Last Shake", hex_value = get_hex_value("Long-Last Shake"), weight = 800),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '358':EnemyEntry (
        "Nothing?",
        None,
        "Template 358",
        0,
        EnemyDrops (
            None
        )
    ),
    '359':EnemyEntry (
        "Dark Spania",
        0x158,
        "Template 359",
        0.05,
        EnemyDrops (
            None
        )
    ),
    '360':EnemyEntry (
        "Dark Cursya",
        0x15E,
        "Template 360",
        0.15,
        EnemyDrops (
            Drop (item_name = "Poison Shroom", hex_value = get_hex_value("Poison Shroom"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    '361':EnemyEntry (
        "(Unused) Dark Back Cursya",
        None,
        "Template 361",
        0.1,
        EnemyDrops (
            Drop (item_name = "Poison Shroom", hex_value = get_hex_value("Poison Shroom"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    '362':EnemyEntry (
        "Dark Tech Cursya",
        0x15F,
        "Template 362",
        0.15,
        EnemyDrops (
            Drop (item_name = "Poison Shroom", hex_value = get_hex_value("Poison Shroom"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    '363':EnemyEntry (
        "Dark Heavy Cursya",
        0x160,
        "Template 363",
        0.15,
        EnemyDrops (
            Drop (item_name = "Poison Shroom", hex_value = get_hex_value("Poison Shroom"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    '364':EnemyEntry (
        "Dark Reversya Cursya",
        0x161,
        "Template 364",
        0.15,
        EnemyDrops (
            Drop (item_name = "Poison Shroom", hex_value = get_hex_value("Poison Shroom"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    '365':EnemyEntry (
        "Dark Chomp",
        0x167,
        "Template 365",
        0.07,
        EnemyDrops (
            Drop (item_name = "Power Steak", hex_value = get_hex_value("Power Steak"), weight = 100),
            Drop (item_name = "Thunder Rage", hex_value = get_hex_value("Thunder Rage"), weight = 200),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 30),
        )
    ),
    '366':EnemyEntry (
        "Dark Dark Boo",
        0x164,
        "Template 366",
        0.06,
        EnemyDrops (
            Drop (item_name = "Peachy Peach", hex_value = get_hex_value("Peachy Peach"), weight = 100),
            Drop (item_name = "Keel Mango", hex_value = get_hex_value("Keel Mango"), weight = 100),
            Drop (item_name = "Long-Last Shake", hex_value = get_hex_value("Long-Last Shake"), weight = 100),
            Drop (item_name = "Horsetail", hex_value = get_hex_value("Horsetail"), weight = 100),
            Drop (item_name = "Sleepy Sleep", hex_value = get_hex_value("Sleepy Sleep"), weight = 400),
            Drop (item_name = "Ghost Shroom", hex_value = get_hex_value("Ghost Shroom"), weight = 800),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '367':EnemyEntry (
        "Dark Cleft",
        0x16C,
        "Template 367",
        0.05,
        EnemyDrops (
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Honey Jar", hex_value = get_hex_value("Honey Jar"), weight = 100),
            Drop (item_name = "Courage Shell", hex_value = get_hex_value("Courage Shell"), weight = 800),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '368':EnemyEntry (
        "Dark Shlurp",
        0x16F,
        "Template 368",
        0.04,
        EnemyDrops (
            Drop (item_name = "Power Steak", hex_value = get_hex_value("Power Steak"), weight = 100),
            Drop (item_name = "Fresh Pasta Bunch", hex_value = get_hex_value("Fresh Pasta Bunch"), weight = 100),
            Drop (item_name = "Hot Sauce", hex_value = get_hex_value("Hot Sauce"), weight = 100),
            Drop (item_name = "Smelly Herb", hex_value = get_hex_value("Smelly Herb"), weight = 100),
            Drop (item_name = "Fire Burst", hex_value = get_hex_value("Fire Burst"), weight = 400),
            Drop (item_name = "POW Block", hex_value = get_hex_value("POW Block"), weight = 800),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '369':EnemyEntry (
        "Dark Squiglet",
        0x178,
        "Template 369",
        0.05,
        EnemyDrops (
            Drop (item_name = "Power Steak", hex_value = get_hex_value("Power Steak"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 100),
            Drop (item_name = "Hot Sauce", hex_value = get_hex_value("Hot Sauce"), weight = 100),
            Drop (item_name = "Smelly Herb", hex_value = get_hex_value("Smelly Herb"), weight = 100),
            Drop (item_name = "Thunder Rage", hex_value = get_hex_value("Thunder Rage"), weight = 400),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '370':EnemyEntry (
        "Nothing?",
        None,
        "Template 370",
        0,
        EnemyDrops (
            None
        )
    ),
    '371':EnemyEntry (
        "Dark Sproing-Oing",
        0x17D,
        "Template 371",
        0.07,
        EnemyDrops (
            Drop (item_name = "Peachy Peach", hex_value = get_hex_value("Peachy Peach"), weight = 100),
            Drop (item_name = "Keel Mango", hex_value = get_hex_value("Keel Mango"), weight = 100),
            Drop (item_name = "Fresh Veggie", hex_value = get_hex_value("Fresh Veggie"), weight = 100),
            Drop (item_name = "Horsetail", hex_value = get_hex_value("Horsetail"), weight = 100),
            Drop (item_name = "Long-Last Shake", hex_value = get_hex_value("Long-Last Shake"), weight = 400),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '372':EnemyEntry (
        "Mini Dark Sproing-Oing",
        0x17D,
        "Template 372",
        0.03,
        EnemyDrops (
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    '373':EnemyEntry (
        "Dark Boomboxer",
        0x180,
        "Template 373",
        0.05,
        EnemyDrops (
            Drop (item_name = "Peachy Peach", hex_value = get_hex_value("Peachy Peach"), weight = 100),
            Drop (item_name = "Keel Mango", hex_value = get_hex_value("Keel Mango"), weight = 100),
            Drop (item_name = "Fresh Veggie", hex_value = get_hex_value("Fresh Veggie"), weight = 100),
            Drop (item_name = "Horsetail", hex_value = get_hex_value("Horsetail"), weight = 100),
            Drop (item_name = "Volt Shroom", hex_value = get_hex_value("Volt Shroom"), weight = 400),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '374':EnemyEntry (
        "Nothing?",
        None,
        "Template 374",
        0,
        EnemyDrops (
            None
        )
    ),
    '375':EnemyEntry (
        "Dark Jawbus",
        0x184,
        "Template 375",
        0.15,
        EnemyDrops (
            Drop (item_name = "Fire Burst", hex_value = get_hex_value("Fire Burst"), weight = 100),
            Drop (item_name = "Ice Storm", hex_value = get_hex_value("Ice Storm"), weight = 200),
            Drop (item_name = "Thunder Rage", hex_value = get_hex_value("Thunder Rage"), weight = 300),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 30),
        )
    ),
    '376':EnemyEntry (
        "(Unused) Dark I",
        None,
        "Template 376",
        0.1,
        EnemyDrops (
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 100),
            Drop (item_name = "Sleepy Sleep", hex_value = get_hex_value("Sleepy Sleep"), weight = 800),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '377':EnemyEntry (
        "Nothing?",
        None,
        "Template 377",
        0,
        EnemyDrops (
            None
        )
    ),
    '378':EnemyEntry (
        "Dark Growmeba",
        0x18D,
        "Template 378",
        0,
        EnemyDrops (
            None
        )
    ),
    '379':EnemyEntry (
        "Dark Tileoid",
        0x192,
        "Template 379",
        0.05,
        EnemyDrops (
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 100),
            Drop (item_name = "Fresh Pasta Bunch", hex_value = get_hex_value("Fresh Pasta Bunch"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Honey Jar", hex_value = get_hex_value("Honey Jar"), weight = 100),
            Drop (item_name = "Block Block", hex_value = get_hex_value("Block Block"), weight = 400),
            Drop (item_name = "Stop Watch", hex_value = get_hex_value("Stop Watch"), weight = 400),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '380':EnemyEntry (
        "Dark Eeligon",
        0x19D,
        "Template 380",
        0.07,
        EnemyDrops (
            Drop (item_name = "Power Steak", hex_value = get_hex_value("Power Steak"), weight = 100),
            Drop (item_name = "Fresh Pasta Bunch", hex_value = get_hex_value("Fresh Pasta Bunch"), weight = 100),
            Drop (item_name = "Hot Sauce", hex_value = get_hex_value("Hot Sauce"), weight = 100),
            Drop (item_name = "Long-Last Shake", hex_value = get_hex_value("Long-Last Shake"), weight = 100),
            Drop (item_name = "Block Block", hex_value = get_hex_value("Block Block"), weight = 800),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '381':EnemyEntry (
        "Dark Eeligon Part",
        None,
        "Template 381",
        0,
        EnemyDrops (
            None
        )
    ),
    '382':EnemyEntry (
        "Dark Longator",
        0x1A0,
        "Template 382",
        0.05,
        EnemyDrops (
            Drop (item_name = "Peachy Peach", hex_value = get_hex_value("Peachy Peach"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 100),
            Drop (item_name = "Fresh Veggie", hex_value = get_hex_value("Fresh Veggie"), weight = 100),
            Drop (item_name = "Horsetail", hex_value = get_hex_value("Horsetail"), weight = 100),
            Drop (item_name = "Stop Watch", hex_value = get_hex_value("Stop Watch"), weight = 800),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '383':EnemyEntry (
        "Dark Barribad",
        0x1A3,
        "Template 383",
        0.07,
        EnemyDrops (
            Drop (item_name = "Power Steak", hex_value = get_hex_value("Power Steak"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 100),
            Drop (item_name = "Hot Sauce", hex_value = get_hex_value("Hot Sauce"), weight = 100),
            Drop (item_name = "Block Block", hex_value = get_hex_value("Block Block"), weight = 1200),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '384':EnemyEntry (
        "Dark Barribad Projectile",
        None,
        "Template 384",
        0,
        EnemyDrops (
            None
        )
    ),
    '385':EnemyEntry (
        "Dark Pigarithm",
        0x1A6,
        "Template 385",
        0.07,
        EnemyDrops (
            Drop (item_name = "Long-Last Shake", hex_value = get_hex_value("Long-Last Shake"), weight = 200),
            Drop (item_name = "Shooting Star", hex_value = get_hex_value("Shooting Star"), weight = 200),
            Drop (item_name = "Block Block", hex_value = get_hex_value("Block Block"), weight = 200),
            Drop (item_name = "Ghost Shroom", hex_value = get_hex_value("Ghost Shroom"), weight = 200),
            Drop (item_name = "Stop Watch", hex_value = get_hex_value("Stop Watch"), weight = 200),
            Drop (item_name = "Mighty Tonic", hex_value = get_hex_value("Mighty Tonic"), weight = 200),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '386':EnemyEntry (
        "Dark Choppa",
        0x1A9,
        "Template 386",
        0.05,
        EnemyDrops (
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 100),
            Drop (item_name = "Cake Mix", hex_value = get_hex_value("Cake Mix"), weight = 100),
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Honey Jar", hex_value = get_hex_value("Honey Jar"), weight = 100),
            Drop (item_name = "Long-Last Shake", hex_value = get_hex_value("Long-Last Shake"), weight = 400),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '387':EnemyEntry (
        "Dark Muth",
        0x1AB,
        "Template 387",
        0.25,
        EnemyDrops (
            Drop (item_name = "Bone-In Cut", hex_value = get_hex_value("Bone-In Cut"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    '388':EnemyEntry (
        "Dark Ninjoe",
        0x1AF,
        "Template 388",
        0.1,
        EnemyDrops (
            Drop (item_name = "Thunder Rage", hex_value = get_hex_value("Thunder Rage"), weight = 200),
            Drop (item_name = "Volt Shroom", hex_value = get_hex_value("Volt Shroom"), weight = 100),
            Drop (item_name = "Stop Watch", hex_value = get_hex_value("Stop Watch"), weight = 100),
            Drop (item_name = "Super Shroom Shake", hex_value = get_hex_value("Super Shroom Shake"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 30),
        )
    ),
    '389':EnemyEntry (
        "Dark Ninjoe Projectile",
        None,
        "Template 389",
        0,
        EnemyDrops (
            None
        )
    ),
    '390':EnemyEntry (
        "Nothing?",
        None,
        "Template 390",
        0,
        EnemyDrops (
            None
        )
    ),
    '391':EnemyEntry (
        "Dark Skellobit",
        0x1B6,
        "Template 391",
        0.05,
        EnemyDrops (
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Power Steak", hex_value = get_hex_value("Power Steak"), weight = 100),
            Drop (item_name = "Peachy Peach", hex_value = get_hex_value("Peachy Peach"), weight = 100),
            Drop (item_name = "Ice Storm", hex_value = get_hex_value("Ice Storm"), weight = 300),
            Drop (item_name = "Ghost Shroom", hex_value = get_hex_value("Ghost Shroom"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '392':EnemyEntry (
        "Dark Spiky Skellobit",
        0x1B7,
        "Template 392",
        0.07,
        EnemyDrops (
            Drop (item_name = "Big Egg", hex_value = get_hex_value("Big Egg"), weight = 100),
            Drop (item_name = "Power Steak", hex_value = get_hex_value("Power Steak"), weight = 100),
            Drop (item_name = "Peachy Peach", hex_value = get_hex_value("Peachy Peach"), weight = 100),
            Drop (item_name = "POW Block", hex_value = get_hex_value("POW Block"), weight = 300),
            Drop (item_name = "Ghost Shroom", hex_value = get_hex_value("Ghost Shroom"), weight = 100),
            Drop (item_name = "Super Shroom Shake", hex_value = get_hex_value("Super Shroom Shake"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    '393':EnemyEntry (
        "Dark Megabite",
        0x1BD,
        "Template 393",
        0.15,
        EnemyDrops (
            Drop (item_name = "POW Block", hex_value = get_hex_value("POW Block"), weight = 100),
            Drop (item_name = "Ghost Shroom", hex_value = get_hex_value("Ghost Shroom"), weight = 100),
            Drop (item_name = "Catch Card SP", hex_value = get_hex_value("Catch Card SP"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 30),
        )
    ),
    '394':EnemyEntry (
        "Dark Magiblot",
        0x1C1,
        "Template 394",
        0.06,
        EnemyDrops (
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 100),
            Drop (item_name = "Catch Card SP", hex_value = get_hex_value("Catch Card SP"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 100),
        )
    ),
    '395':EnemyEntry (
        "Nothing?",
        None,
        "Template 395",
        0,
        EnemyDrops (
            None
        )
    ),
    '396':EnemyEntry (
        "Brobot Fist",
        None,
        "Template 396",
        0,
        EnemyDrops (
            None
        )
    ),
    '397':EnemyEntry (
        "Mimi 2",
        0x1C7,
        "Template 397",
        0,
        EnemyDrops (
            None
        )
    ),
    '398':EnemyEntry (
        "Bowser 2",
        0x1CA,
        "Template 398",
        0,
        EnemyDrops (
            None
        )
    ),
    '399':EnemyEntry (
        "Dark Dimentio Cube",
        None,
        "Template 399",
        0,
        EnemyDrops (
            None
        )
    ),
    '400':EnemyEntry (
        "Big Dark Dimentio Cube",
        None,
        "Template 400",
        0,
        EnemyDrops (
            None
        )
    ),
    '401':EnemyEntry (
        "Giant Dark Dimentio Cube",
        None,
        "Template 401",
        0,
        EnemyDrops (
            None
        )
    ),
    '402':EnemyEntry (
        "Rubee",
        None,
        "Template 402",
        0,
        EnemyDrops (
            None
        )
    ),
    '403':EnemyEntry (
        "Nothing?",
        None,
        "Template 403",
        0,
        EnemyDrops (
            None
        )
    ),
    '404':EnemyEntry (
        "Dimentio Attack",
        None,
        "Template 404",
        0,
        EnemyDrops (
            None
        )
    ),
    '405':EnemyEntry (
        "Dimentio",
        0x1C6,
        "Template 405",
        0,
        EnemyDrops (
            None
        )
    ),
    '406':EnemyEntry (
        "Dimentio",
        0x1C6,
        "Template 406",
        0,
        EnemyDrops (
            None
        )
    ),
    '407':EnemyEntry (
        "Dimentio",
        0x1C6,
        "Template 407",
        0,
        EnemyDrops (
            None
        )
    ),
    '408':EnemyEntry (
        "Stench",
        None,
        "Template 408",
        0,
        EnemyDrops (
            None
        )
    ),
    '409':EnemyEntry (
        "Cherbil",
        0x210,
        "Template 409",
        0.04,
        EnemyDrops (
            Drop (item_name = "Peachy Peach", hex_value = get_hex_value("Peachy Peach"), weight = 100),
            Drop (item_name = "Sleepy Sleep", hex_value = get_hex_value("Sleepy Sleep"), weight = 100),
            Drop (item_name = "Long-Last Shake", hex_value = get_hex_value("Long-Last Shake"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 20),
        )
    ),
    '410':EnemyEntry (
        "Cherbil's Projectile",
        None,
        "Template 410",
        0,
        EnemyDrops (
            None
        )
    ),
    '411':EnemyEntry (
        "Poison Cherbil",
        0x212,
        "Template 411",
        1,
        EnemyDrops (
            Drop (item_name = "Peachy Peach", hex_value = get_hex_value("Peachy Peach"), weight = 100),
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 500),
            Drop (item_name = "Long-Last Shake", hex_value = get_hex_value("Long-Last Shake"), weight = 50),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 20),
        )
    ),
    '412':EnemyEntry (
        "Poison Cherbil's Projectile",
        None,
        "Template 412",
        0,
        EnemyDrops (
            None
        )
    ),
    '413':EnemyEntry (
        "Ice Cherbil",
        0x211,
        "Template 413",
        0.04,
        EnemyDrops (
            Drop (item_name = "Peachy Peach", hex_value = get_hex_value("Peachy Peach"), weight = 100),
            Drop (item_name = "Ice Storm", hex_value = get_hex_value("Ice Storm"), weight = 100),
            Drop (item_name = "Long-Last Shake", hex_value = get_hex_value("Long-Last Shake"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 20),
        )
    ),
    '414':EnemyEntry (
        "Ice Cherbil's Projectile",
        None,
        "Template 414",
        0,
        EnemyDrops (
            None
        )
    ),
    '415':EnemyEntry (
        "Dark Cherbil",
        0x217,
        "Template 415",
        0.5,
        EnemyDrops (
            Drop (item_name = "Peachy Peach", hex_value = get_hex_value("Peachy Peach"), weight = 100),
            Drop (item_name = "Sleepy Sleep", hex_value = get_hex_value("Sleepy Sleep"), weight = 100),
            Drop (item_name = "Long-Last Shake", hex_value = get_hex_value("Long-Last Shake"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 20),
        )
    ),
    '416':EnemyEntry (
        "Dark Cherbil's Projectile",
        None,
        "Template 416",
        0,
        EnemyDrops (
            None
        )
    ),
    '417':EnemyEntry (
        "Ice Dark Cherbil's Projectile",
        None,
        "Template 417",
        0,
        EnemyDrops (
            None
        )
    ),
    '418':EnemyEntry (
        "Poison Dark Cherbil's Projectile",
        None,
        "Template 418",
        0,
        EnemyDrops (
            None
        )
    ),
    '419':EnemyEntry (
        "Frackle",
        0x213,
        "Template 419",
        0,
        EnemyDrops (
            None
        )
    ),
    '420':EnemyEntry (
        "Wrackle",
        0x214,
        "Template 420",
        0,
        EnemyDrops (
            None
        )
    ),
    '421':EnemyEntry (
        "Nothing?",
        None,
        "Template 421",
        0,
        EnemyDrops (
            None
        )
    ),
    '422':EnemyEntry (
        "Enemy Mario",
        None,
        "Template 422",
        0,
        EnemyDrops (
            None
        )
    ),
    '423':EnemyEntry (
        "Glitchy Enemy Mario",
        None,
        "Template 423",
        0,
        EnemyDrops (
            None
        )
    ),
    '424':EnemyEntry (
        "Enemy Luigi?",
        None,
        "Template 424",
        0,
        EnemyDrops (
            None
        )
    ),
    '425':EnemyEntry (
        "Enemy Luigi?",
        None,
        "Template 425",
        0,
        EnemyDrops (
            None
        )
    ),
    '426':EnemyEntry (
        "Sammer Guy",
        None,
        "Template 426",
        0,
        EnemyDrops (
            None
        )
    ),
    '427':EnemyEntry (
        "Stationary Enemy Mario",
        None,
        "Template 427",
        0,
        EnemyDrops (
            None
        )
    ),
    '428':EnemyEntry (
        "Stationary Enemy Luigi",
        None,
        "Template 428",
        0,
        EnemyDrops (
            None
        )
    ),
    '429':EnemyEntry (
        "Stationary Enemy Peach",
        None,
        "Template 429",
        0,
        EnemyDrops (
            None
        )
    ),
    '430':EnemyEntry (
        "Stationary Enemy Bowser",
        None,
        "Template 430",
        0,
        EnemyDrops (
            None
        )
    ),
    '431':EnemyEntry (
        "Two Koopa Strikers at once",
        None,
        "Template 431",
        0,
        EnemyDrops (
            None
        )
    ),
    '432':EnemyEntry (
        "Giant Shell",
        None,
        "Template 432",
        0,
        EnemyDrops (
            None
        )
    ),
    '433':EnemyEntry (
        "(No name)",
        None,
        "Template 433",
        0,
        EnemyDrops (
            None
        )
    )
}