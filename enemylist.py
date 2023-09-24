import dolphin_memory_engine as dme
from bighexlist import BigList

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

game_region = chr(dme.read_byte(0x80000003))
game_revision = dme.read_byte(0x80000007)

def get_itemPercent(name: str) -> int:
    drop = EnemyList[name]
    dropies = drop["Drop %"][game_region][game_revision]
    return int(dropies, drop["datatype"])

ItemHexValues = {}
for item in BigList:
    ItemHexValues[item.name] = item.hex

def get_hex_value(item_name):
    return ItemHexValues.get(item_name)

EnemyList = {
    EnemyEntry (
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
    EnemyEntry (
        "Goomba",
        None,
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
    EnemyEntry (
        "Goomba",
        None,
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
    EnemyEntry (
        "Spiked Goomba",
        None,
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
    EnemyEntry (
        "Paragoomba",
        None,
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
    EnemyEntry (
        "Flip Goomba",
        None,
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
    EnemyEntry (
        "Spiked Goomba",
        None,
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
    EnemyEntry (
        "Goomba",
        None,
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
    EnemyEntry (
        "Green Koopa Troopa",
        None,
        "Template 8",
        0.09,
        EnemyDrops (
            Drop (item_name = "Turtley Leaf", hex_value = get_hex_value("Turtley Leaf"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    EnemyEntry (
        "Red Koopa Troopa",
        None,
        "Template 9",
        0.09,
        EnemyDrops (
            Drop (item_name = "Turtley Leaf", hex_value = get_hex_value("Turtley Leaf"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    EnemyEntry (
        "(Unused) Shady Koopa",
        None,
        "Template 10",
        0.04,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Koopatrol",
        None,
        "Template 11",
        0.05,
        EnemyDrops (
            Drop (item_name = "Turtley Leaf", hex_value = get_hex_value("Turtley Leaf"), weight = 100),
            Drop (item_name = "Thunder Rage", hex_value = get_hex_value("Thunder Rage"), weight = 300),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 20),
        )
    ),
    EnemyEntry (
        "Flip Red Koopa Troopa",
        None,
        "Template 12",
        0.09,
        EnemyDrops (
            Drop (item_name = "Turtley Leaf", hex_value = get_hex_value("Turtley Leaf"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    EnemyEntry (
        "(Unused) Flip Shady Koopa",
        None,
        "Template 13",
        0.04,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Green Paratroopa",
        None,
        "Template 14",
        0.03,
        EnemyDrops (
            Drop (item_name = "Turtley Leaf", hex_value = get_hex_value("Turtley Leaf"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    EnemyEntry (
        "Red Paratroopa",
        None,
        "Template 15",
        0.03,
        EnemyDrops (
            Drop (item_name = "Turtley Leaf", hex_value = get_hex_value("Turtley Leaf"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    EnemyEntry (
        "(Unused) Shady Paratroopa",
        None,
        "Template 16",
        0.04,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Flip Red Paratroopa",
        None,
        "Template 17",
        0.03,
        EnemyDrops (
            Drop (item_name = "Turtley Leaf", hex_value = get_hex_value("Turtley Leaf"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    EnemyEntry (
        "(Unused) Flip Shady Paratroopa",
        None,
        "Template 18",
        0.04,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Clubba",
        None,
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
    EnemyEntry (
        "PatrolMeow",
        None,
        "Template 20",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "AirMeow",
        None,
        "Template 21",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "SurpriseMeow",
        None,
        "Template 22",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "MeowBomb",
        None,
        "Template 23",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Hammer Bro.",
        None,
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
    EnemyEntry (
        "Green Cheep Cheep",
        None,
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
    EnemyEntry (
        "Blooper",
        None,
        "Template 26",
        0.15,
        EnemyDrops (
            Drop (item_name = "Inky Sauce", hex_value = get_hex_value("Inky Sauce"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    EnemyEntry (
        "Thwomp",
        None,
        "Template 27",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Lava Bubble",
        None,
        "Template 28",
        0.04,
        EnemyDrops (
            Drop (item_name = "Fire Burst", hex_value = get_hex_value("Fire Burst"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    EnemyEntry (
        "Spiny Tromp",
        None,
        "Template 29",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Goomba",
        None,
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
    EnemyEntry (
        "Piranha Plant",
        None,
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
    EnemyEntry (
        "Goomba",
        None,
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
    EnemyEntry (
        "Goomba",
        None,
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
    EnemyEntry (
        "Goomba",
        None,
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
    EnemyEntry (
        "Goomba",
        None,
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
    EnemyEntry (
        "Dry Bones",
        None,
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
    EnemyEntry (
        "Rubee",
        None,
        "Template 37",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Dull Bones",
        None,
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
    EnemyEntry (
        "Boomerang Bro",
        None,
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
    EnemyEntry (
        "Fire Bro",
        None,
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
    EnemyEntry (
        "Goomba",
        None,
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
    EnemyEntry (
        "Goomba",
        None,
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
    EnemyEntry (
        "Fracktail",
        None,
        "Template 43",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Wracktail",
        None,
        "Template 44",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Flip Blooper",
        None,
        "Template 45",
        0.15,
        EnemyDrops (
            Drop (item_name = "Inky Sauce", hex_value = get_hex_value("Inky Sauce"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    EnemyEntry (
        "Flip Hammer Bro.",
        None,
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
    EnemyEntry (
        "Small Spiky Tromp",
        None,
        "Template 47",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
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
    EnemyEntry (
        "Putrid Piranha",
        None,
        "Template 49",
        1.0,
        EnemyDrops (
            Drop (item_name = "Peachy Peach", hex_value = get_hex_value("Peachy Peach"), weight = 100),
            Drop (item_name = "Keel Mango", hex_value = get_hex_value("Keel Mango"), weight = 200),
            Drop (item_name = "Fresh Veggie", hex_value = get_hex_value("Fresh Veggie"), weight = 100),
            Drop (item_name = "Horsetail", hex_value = get_hex_value("Horsetail"), weight = 600),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 40),
        )
    ),
    EnemyEntry (
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
    EnemyEntry (
        "Frost Piranha",
        None,
        "Template 51",
        0.1,
        EnemyDrops (
            Drop (item_name = "Ice Storm", hex_value = get_hex_value("Ice Storm"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    EnemyEntry (
        "Nothing?",
        None,
        "Template 52",
        0.1,
        EnemyDrops (
            Drop (item_name = "Ice Storm", hex_value = get_hex_value("Ice Storm"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    EnemyEntry (
        "Buzzy Beetle",
        None,
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
    EnemyEntry (
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
    EnemyEntry (
        "Flip Buzzy Beetle",
        None,
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
    EnemyEntry (
        "Spike Top",
        None,
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
    EnemyEntry (
        "Parabuzzy",
        None,
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
    EnemyEntry (
        "Spiky Parabuzzy",
        None,
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
    EnemyEntry (
        "Spiny",
        None,
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
    EnemyEntry (
        "(UNUSED?) Weird Spiny",
        None,
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
    EnemyEntry (
        "Lakitu",
        None,
        "Template 61",
        0.1,
        EnemyDrops (
            Drop (item_name = "Thunder Rage", hex_value = get_hex_value("Thunder Rage"), weight = 100),
            Drop (item_name = "Mystery Box", hex_value = get_hex_value("Mystery Box"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 30),
        )
    ),
    EnemyEntry (
        "Flip Lakitu",
        None,
        "Template 62",
        0.1,
        EnemyDrops (
            Drop (item_name = "Thunder Rage", hex_value = get_hex_value("Thunder Rage"), weight = 100),
            Drop (item_name = "Mystery Box", hex_value = get_hex_value("Mystery Box"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 30),
        )
    ),
    EnemyEntry (
        "Mega Koopa",
        None,
        "Template 63",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Goomba",
        None,
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
    EnemyEntry (
        "Chain Chomp",
        None,
        "Template 65",
        0.05,
        EnemyDrops (
            Drop (item_name = "Power Steak", hex_value = get_hex_value("Power Steak"), weight = 100),
            Drop (item_name = "Thunder Rage", hex_value = get_hex_value("Thunder Rage"), weight = 200),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 30),
        )
    ),
    EnemyEntry (
        "Goomba",
        None,
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
    EnemyEntry (
        "Red Cheep Cheep",
        None,
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
    EnemyEntry (
        "Goomba",
        None,
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
    EnemyEntry (
        "Flip Cheep Cheep",
        None,
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
    EnemyEntry (
        "Swooper",
        None,
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
    EnemyEntry (
        "Glitchy Dark Koopa",
        None,
        "Template 71",
        0.05,
        EnemyDrops (
            Drop (item_name = "Turtley Leaf", hex_value = get_hex_value("Turtley Leaf"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    EnemyEntry (
        "Goomba",
        None,
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
    EnemyEntry (
        "Glitchy Koopa",
        None,
        "Template 73",
        0.09,
        EnemyDrops (
            Drop (item_name = "Turtley Leaf", hex_value = get_hex_value("Turtley Leaf"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    EnemyEntry (
        "Spinia",
        None,
        "Template 74",
        0.04,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Spania",
        None,
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
    EnemyEntry (
        "Spunia",
        None,
        "Template 76",
        0.04,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Bald Cleft",
        None,
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
    EnemyEntry (
        "Moon Cleft",
        None,
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
    EnemyEntry (
        "Goomba",
        None,
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
    EnemyEntry (
        "Magikoopa",
        None,
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
    EnemyEntry (
        "Broom Magikoopa",
        None,
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
    EnemyEntry (
        "Nothing?",
        None,
        "Template 82",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Goomba",
        None,
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
    EnemyEntry (
        "Headbonk Goomba",
        None,
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
    EnemyEntry (
        "Goomba",
        None,
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
    EnemyEntry (
        "Barribad",
        None,
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
    EnemyEntry (
        "Barribad Projectile?",
        None,
        "Template 87",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Pigarithm",
        None,
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
    EnemyEntry (
        "Goomba",
        None,
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
    EnemyEntry (
        "Goomba",
        None,
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
    EnemyEntry (
        "Goomba",
        None,
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
    EnemyEntry (
        "Goomba",
        None,
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
    EnemyEntry (
        "Goomba",
        None,
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
    EnemyEntry (
        "Zombie Shroom",
        None,
        "Template 94",
        0.05,
        EnemyDrops (
            Drop (item_name = "Poison Shroom", hex_value = get_hex_value("Poison Shroom"), weight = 200),
            Drop (item_name = "Ghost Shroom", hex_value = get_hex_value("Ghost Shroom"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 30),
        )
    ),
    EnemyEntry (
        "Goomba",
        None,
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
    EnemyEntry (
        "Stone Buzzy",
        None,
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
    EnemyEntry (
        "Longator",
        None,
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
    EnemyEntry (
        "Goomba",
        None,
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
    EnemyEntry (
        "Flip Spiny",
        None,
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
    EnemyEntry (
        "Mister I",
        None,
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
    EnemyEntry (
        "(Unused) Flip Spike Top",
        None,
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
    EnemyEntry (
        "Nothing?",
        None,
        "Template 102",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Projectile?",
        None,
        "Template 103",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Howl",
        None,
        "Template 104",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Growl",
        None,
        "Template 105",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Bullet Bill",
        None,
        "Template 106",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Bill Blaster",
        None,
        "Template 107",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "(Unused) Giant Bombshell Bill",
        None,
        "Template 108",
        0.04,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "(Unused) Giant Bombshell Bill Blaster",
        None,
        "Template 109",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Boo",
        None,
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
    EnemyEntry (
        "Dark Boo",
        None,
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
    EnemyEntry (
        "Atomic Boo",
        None,
        "Template 112",
        0.2,
        EnemyDrops (
            Drop (item_name = "Ghost Shroom", hex_value = get_hex_value("Ghost Shroom"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    EnemyEntry (
        "(Unused) Dark Atomic Boo",
        None,
        "Template 113",
        0.1,
        EnemyDrops (
            Drop (item_name = "Ghost Shroom", hex_value = get_hex_value("Ghost Shroom"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    EnemyEntry (
        "Goomba",
        None,
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
    EnemyEntry (
        "Goomba",
        None,
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
    EnemyEntry (
        "Goomba",
        None,
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
    EnemyEntry (
        "Fuzzy",
        None,
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
    EnemyEntry (
        "Goomba",
        None,
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
    EnemyEntry (
        "Goomba",
        None,
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
    EnemyEntry (
        "Pink Fuzzy",
        None,
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
    EnemyEntry (
        "Goomba",
        None,
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
    EnemyEntry (
        "Goomba",
        None,
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
    EnemyEntry (
        "Goomba",
        None,
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
    EnemyEntry (
        "Goomba",
        None,
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
    EnemyEntry (
        "Weak Ruff Puff",
        None,
        "Template 125",
        0.04,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Pokey",
        None,
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
    EnemyEntry (
        "Poison Pokey",
        None,
        "Template 127",
        1.0,
        EnemyDrops (
            Drop (item_name = "Peachy Peach", hex_value = get_hex_value("Peachy Peach"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 100),
            Drop (item_name = "Fresh Veggie", hex_value = get_hex_value("Fresh Veggie"), weight = 100),
            Drop (item_name = "Horsetail", hex_value = get_hex_value("Horsetail"), weight = 100),
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 800),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 50),
        )
    ),
    EnemyEntry (
        "Koopa Striker",
        None,
        "Template 128",
        0.05,
        EnemyDrops (
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 100),
            Drop (item_name = "Turtley Leaf", hex_value = get_hex_value("Turtley Leaf"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 20),
        )
    ),
    EnemyEntry (
        "Koopa Striker's Shell",
        None,
        "Template 129",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Mimi",
        None,
        "Template 130",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Chasing Mimi",
        None,
        "Template 131",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Bowser",
        None,
        "Template 132",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Bittacuda",
        None,
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
    EnemyEntry (
        "Nothing?",
        None,
        "Template 134",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "BombMeow",
        None,
        "Template 135",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Big Blooper",
        None,
        "Template 136",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Mr. L",
        None,
        "Template 137",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Brobot",
        None,
        "Template 138",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Brobot Missile",
        None,
        "Template 139",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Brobot Mustache",
        None,
        "Template 140",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Jawbus",
        None,
        "Template 141",
        0.1,
        EnemyDrops (
            Drop (item_name = "Fire Burst", hex_value = get_hex_value("Fire Burst"), weight = 300),
            Drop (item_name = "Ice Storm", hex_value = get_hex_value("Ice Storm"), weight = 200),
            Drop (item_name = "Thunder Rage", hex_value = get_hex_value("Thunder Rage"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 30),
        )
    ),
    EnemyEntry (
        "Dimentio",
        None,
        "Template 142",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Dimentio Magic",
        None,
        "Template 143",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Sproing-Oing",
        None,
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
    EnemyEntry (
        "Mini Sproing-Oing",
        None,
        "Template 145",
        0.02,
        EnemyDrops (
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    EnemyEntry (
        "Rubee",
        None,
        "Template 146",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Shlurp",
        None,
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
    EnemyEntry (
        "Squig",
        None,
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
    EnemyEntry (
        "Nothing?",
        None,
        "Template 149",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "King Croacus",
        None,
        "Template 150",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Slow Cursya",
        None,
        "Template 151",
        0.1,
        EnemyDrops (
            Drop (item_name = "Poison Shroom", hex_value = get_hex_value("Poison Shroom"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    EnemyEntry (
        "Megabite",
        None,
        "Template 152",
        0.1,
        EnemyDrops (
            Drop (item_name = "Shooting Star", hex_value = get_hex_value("Shooting Star"), weight = 100),
            Drop (item_name = "Ghost Shroom", hex_value = get_hex_value("Ghost Shroom"), weight = 200),
            Drop (item_name = "Catch Card SP", hex_value = get_hex_value("Catch Card SP"), weight = 200),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 30),
        )
    ),
    EnemyEntry (
        "Boomboxer",
        None,
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
    EnemyEntry (
        "Choppa",
        None,
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
    EnemyEntry (
        "Croacus Petal",
        None,
        "Template 155",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Croacus Petal",
        None,
        "Template 156",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Croacus Petal",
        None,
        "Template 157",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Boomboxer Attack",
        None,
        "Template 158",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Ruff Puff",
        None,
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
    EnemyEntry (
        "Tileoid G",
        None,
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
    EnemyEntry (
        "Tileoid B",
        None,
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
    EnemyEntry (
        "Tileoid R",
        None,
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
    EnemyEntry (
        "Tileoid Y",
        None,
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
    EnemyEntry (
        "Growmeba",
        None,
        "Template 164",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Growmeba Part",
        None,
        "Template 165",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Boomerang",
        None,
        "Template 166",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Fire Bro Fireball",
        None,
        "Template 167",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "BigMeow",
        None,
        "Template 168",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Eeligon",
        None,
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
    EnemyEntry (
        "Jellien",
        None,
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
    EnemyEntry (
        "Foton",
        None,
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
    EnemyEntry (
        "Warpid",
        None,
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
    EnemyEntry (
        "Muth",
        None,
        "Template 173",
        0.2,
        EnemyDrops (
            Drop (item_name = "Bone-In Cut", hex_value = get_hex_value("Bone-In Cut"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    EnemyEntry (
        "Veggiefied O'Chunks",
        None,
        "Template 174",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Floro Cragnon (Round)",
        None,
        "Template 175",
        0.07,
        EnemyDrops (
            Drop (item_name = "Keel Mango", hex_value = get_hex_value("Keel Mango"), weight = 100),
            Drop (item_name = "Primordial Fruit", hex_value = get_hex_value("Primordial Fruit"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 20),
        )
    ),
    EnemyEntry (
        "Floro Cragnon (Triangular)",
        None,
        "Template 176",
        0.07,
        EnemyDrops (
            Drop (item_name = "Keel Mango", hex_value = get_hex_value("Keel Mango"), weight = 100),
            Drop (item_name = "Primordial Fruit", hex_value = get_hex_value("Primordial Fruit"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 20),
        )
    ),
    EnemyEntry (
        "Trap Gold Bar x3",
        None,
        "Template 177",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Ninjoe",
        None,
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
    EnemyEntry (
        "Player Pinwheel",
        None,
        "Template 179",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Projectile?",
        None,
        "Template 180",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "O'Chunks",
        None,
        "Template 181",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "O'Chunks",
        None,
        "Template 182",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Giant O'Chunks",
        None,
        "Template 183",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Small Dimentio Dimension Cube",
        None,
        "Template 184",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Medium Dimentio Dimension Cube",
        None,
        "Template 185",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Big Dimentio Dimension Cube",
        None,
        "Template 186",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "World 6 Mimi",
        None,
        "Template 187",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Brobot L Type",
        None,
        "Template 188",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Bonechill",
        None,
        "Template 189",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Bonechill Projectile",
        None,
        "Template 190",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Bonechill Icicle",
        None,
        "Template 191",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Ninjoe Attack",
        None,
        "Template 192",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "FRY_BAKUDAN (Nothing?)",
        None,
        "Template 193",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Skellobit",
        None,
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
    EnemyEntry (
        "Spiky Skellobit",
        None,
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
    EnemyEntry (
        "Count Bleck",
        None,
        "Template 196",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Void",
        None,
        "Template 197",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Big Void",
        None,
        "Template 198",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Particle",
        None,
        "Template 199",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Nastasia?",
        None,
        "Template 200",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Disappearing Count Bleck",
        None,
        "Template 201",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Boomerang",
        None,
        "Template 202",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Fire Bro Fire",
        None,
        "Template 203",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Pokey Part",
        None,
        "Template 204",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Poison Pokey Part",
        None,
        "Template 205",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Back Cursya",
        None,
        "Template 206",
        0.1,
        EnemyDrops (
            Drop (item_name = "Poison Shroom", hex_value = get_hex_value("Poison Shroom"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    EnemyEntry (
        "Tech Cursya",
        None,
        "Template 207",
        0.1,
        EnemyDrops (
            Drop (item_name = "Poison Shroom", hex_value = get_hex_value("Poison Shroom"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    EnemyEntry (
        "Heavy Cursya",
        None,
        "Template 208",
        0.1,
        EnemyDrops (
            Drop (item_name = "Poison Shroom", hex_value = get_hex_value("Poison Shroom"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    EnemyEntry (
        "Reversya Cursya",
        None,
        "Template 209",
        0.1,
        EnemyDrops (
            Drop (item_name = "Poison Shroom", hex_value = get_hex_value("Poison Shroom"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    EnemyEntry (
        "Hooligon",
        None,
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
    EnemyEntry (
        "Eeligon Part",
        None,
        "Template 211",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Hooligon Part",
        None,
        "Template 212",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Overworld Underchomp (3)",
        None,
        "Template 213",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Overworld Blue Underchomp",
        None,
        "Template 214",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Overworld Yellow Underchomp",
        None,
        "Template 215",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Overworld Red Underchomp",
        None,
        "Template 216",
        0.05,
        EnemyDrops (
            Drop (item_name = "Power Steak", hex_value = get_hex_value("Power Steak"), weight = 100),
            Drop (item_name = "POW Block", hex_value = get_hex_value("POW Block"), weight = 200),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 30),
        )
    ),
    EnemyEntry (
        "Crazee Dayzee",
        None,
        "Template 217",
        0.15,
        EnemyDrops (
            Drop (item_name = "Dayzee Tear", hex_value = get_hex_value("Dayzee Tear"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    EnemyEntry (
        "Dayzee Attack",
        None,
        "Template 218",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Stench",
        None,
        "Template 219",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Freeze",
        None,
        "Template 220",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Skellobomber w/Skellobait",
        None,
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
    EnemyEntry (
        "Skellobomber",
        None,
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
    EnemyEntry (
        "Skellobait",
        None,
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
    EnemyEntry (
        "Spiky Skellobait",
        None,
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
    EnemyEntry (
        "Dimentio",
        None,
        "Template 225",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Dimentio",
        None,
        "Template 226",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Skellobomber Head",
        None,
        "Template 227",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Nothing?",
        None,
        "Template 228",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Red Magiblot",
        None,
        "Template 229",
        0.04,
        EnemyDrops (
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 300),
            Drop (item_name = "Catch Card SP", hex_value = get_hex_value("Catch Card SP"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 100),
        )
    ),
    EnemyEntry (
        "Blue Magiblot",
        None,
        "Template 230",
        0.04,
        EnemyDrops (
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 200),
            Drop (item_name = "Catch Card SP", hex_value = get_hex_value("Catch Card SP"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 100),
        )
    ),
    EnemyEntry (
        "Yellow Magiblot",
        None,
        "Template 231",
        0.04,
        EnemyDrops (
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 100),
            Drop (item_name = "Catch Card SP", hex_value = get_hex_value("Catch Card SP"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 100),
        )
    ),
    EnemyEntry (
        "Nothing?",
        None,
        "Template 232",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Nothing?",
        None,
        "Template 233",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Nothing?",
        None,
        "Template 234",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Gloomba",
        None,
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
    EnemyEntry (
        "Bone",
        None,
        "Template 236",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Glasses-less Koopa",
        None,
        "Template 237",
        0.09,
        EnemyDrops (
            Drop (item_name = "Turtley Leaf", hex_value = get_hex_value("Turtley Leaf"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    EnemyEntry (
        "Glasses-less Paratroopa",
        None,
        "Template 238",
        0.03,
        EnemyDrops (
            Drop (item_name = "Turtley Leaf", hex_value = get_hex_value("Turtley Leaf"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    EnemyEntry (
        "Floro Sapien",
        None,
        "Template 239",
        0.08,
        EnemyDrops (
            Drop (item_name = "Sap Soup", hex_value = get_hex_value("Sap Soup"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    EnemyEntry (
        "Floro Sapien Head",
        None,
        "Template 240",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "8-Bit Shell",
        None,
        "Template 241",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Small 8-Bit Shell",
        None,
        "Template 242",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Purple Floro Sapien",
        None,
        "Template 243",
        0.08,
        EnemyDrops (
            Drop (item_name = "Sap Soup", hex_value = get_hex_value("Sap Soup"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    EnemyEntry (
        "Purple Floro Sapien Head",
        None,
        "Template 244",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Red Floro Sapien",
        None,
        "Template 245",
        0.08,
        EnemyDrops (
            Drop (item_name = "Sap Soup", hex_value = get_hex_value("Sap Soup"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    EnemyEntry (
        "Red Floro Sapien Head",
        None,
        "Template 246",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Free Underhand",
        None,
        "Template 247",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Bound Underhand",
        None,
        "Template 248",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Disappearing Bound Underhand",
        None,
        "Template 249",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Squiglet",
        None,
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
    EnemyEntry (
        "Squog",
        None,
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
    EnemyEntry (
        "Nothing?",
        None,
        "Template 252",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Spike Top",
        None,
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
    EnemyEntry (
        "Broken Flip Koopa Troopa",
        None,
        "Template 254",
        0.09,
        EnemyDrops (
            Drop (item_name = "Turtley Leaf", hex_value = get_hex_value("Turtley Leaf"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    EnemyEntry (
        "Super Dimentio",
        None,
        "Template 255",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Pal Pill Luigi",
        None,
        "Template 256",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Gold Bar",
        None,
        "Template 257",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Gold Bar x3",
        None,
        "Template 258",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Ninjohn",
        None,
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
    EnemyEntry (
        "Ninjohn Projectile",
        None,
        "Template 260",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Nothing?",
        None,
        "Template 261",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Ninjerry",
        None,
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
    EnemyEntry (
        "Ninjerry Projectile",
        None,
        "Template 263",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Nothing?",
        None,
        "Template 264",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Gigabite",
        None,
        "Template 265",
        0.1,
        EnemyDrops (
            Drop (item_name = "POW Block", hex_value = get_hex_value("POW Block"), weight = 100),
            Drop (item_name = "Ghost Shroom", hex_value = get_hex_value("Ghost Shroom"), weight = 100),
            Drop (item_name = "Catch Card SP", hex_value = get_hex_value("Catch Card SP"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 30),
        )
    ),
    EnemyEntry (
        "Blomeba",
        None,
        "Template 266",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Chromeba",
        None,
        "Template 267",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Flip Koopa Stiker",
        None,
        "Template 268",
        0.05,
        EnemyDrops (
            Drop (item_name = "Super Shroom Shake", hex_value = get_hex_value("Super Shroom Shake"), weight = 100),
            Drop (item_name = "Turtley Leaf", hex_value = get_hex_value("Turtley Leaf"), weight = 200),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 20),
        )
    ),
    EnemyEntry (
        "Flip Toopa Striker",
        None,
        "Template 269",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Soopa Striker",
        None,
        "Template 270",
        0.05,
        EnemyDrops (
            Drop (item_name = "Super Shroom Shake", hex_value = get_hex_value("Super Shroom Shake"), weight = 100),
            Drop (item_name = "Turtley Leaf", hex_value = get_hex_value("Turtley Leaf"), weight = 200),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 20),
        )
    ),
    EnemyEntry (
        "Soopa Striker's Shell",
        None,
        "Template 271",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Ghoul Shroom",
        None,
        "Template 272",
        0.05,
        EnemyDrops (
            Drop (item_name = "Poison Shroom", hex_value = get_hex_value("Poison Shroom"), weight = 200),
            Drop (item_name = "Ghost Shroom", hex_value = get_hex_value("Ghost Shroom"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 30),
        )
    ),
    EnemyEntry (
        "Longadile",
        None,
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
    EnemyEntry (
        "Beepboxer",
        None,
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
    EnemyEntry (
        "Nothing?",
        None,
        "Template 275",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "(Unused) Boomboxer Recolor",
        None,
        "Template 276",
        0.04,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Nothing?",
        None,
        "Template 277",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Copta",
        None,
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
    EnemyEntry (
        "(Unused) Muth Recolor",
        None,
        "Template 279",
        1.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Red I",
        None,
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
    EnemyEntry (
        "Nothing?",
        None,
        "Template 281",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Nothing?",
        None,
        "Template 282",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Squoinker",
        None,
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
    EnemyEntry (
        "Nothing?",
        None,
        "Template 284",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Dark Bowser",
        None,
        "Template 285",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Dark Luigi",
        None,
        "Template 286",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Dark Mario",
        None,
        "Template 287",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Dark Peach",
        None,
        "Template 288",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Boing-Oing",
        None,
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
    EnemyEntry (
        "Mini Boing-Oing",
        None,
        "Template 290",
        0.02,
        EnemyDrops (
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    EnemyEntry (
        "Zoing-Oing",
        None,
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
    EnemyEntry (
        "Mini Zoing-Oing",
        None,
        "Template 292",
        0.02,
        EnemyDrops (
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    EnemyEntry (
        "Mega Muth",
        None,
        "Template 293",
        0.2,
        EnemyDrops (
            Drop (item_name = "Bone-In Cut", hex_value = get_hex_value("Bone-In Cut"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    EnemyEntry (
        "Blastboxer",
        None,
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
    EnemyEntry (
        "Nothing?",
        None,
        "Template 295",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Rawbus",
        None,
        "Template 296",
        0.1,
        EnemyDrops (
            Drop (item_name = "Fire Burst", hex_value = get_hex_value("Fire Burst"), weight = 100),
            Drop (item_name = "Ice Storm", hex_value = get_hex_value("Ice Storm"), weight = 100),
            Drop (item_name = "Thunder Rage", hex_value = get_hex_value("Thunder Rage"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 30),
        )
    ),
    EnemyEntry (
        "Gawbus",
        None,
        "Template 297",
        0.1,
        EnemyDrops (
            Drop (item_name = "Fire Burst", hex_value = get_hex_value("Fire Burst"), weight = 100),
            Drop (item_name = "Ice Storm", hex_value = get_hex_value("Ice Storm"), weight = 200),
            Drop (item_name = "Thunder Rage", hex_value = get_hex_value("Thunder Rage"), weight = 300),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 30),
        )
    ),
    EnemyEntry (
        "Sobarribad",
        None,
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
    EnemyEntry (
        "Sobarribad Projectile",
        None,
        "Template 299",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Hogarithm",
        None,
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
    EnemyEntry (
        "Shlorp",
        None,
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
    EnemyEntry (
        "Amazee Dayzee",
        None,
        "Template 302",
        0.7,
        EnemyDrops (
            Drop (item_name = "Golden Leaf", hex_value = get_hex_value("Golden Leaf"), weight = 200),
            Drop (item_name = "Dayzee Tear", hex_value = get_hex_value("Dayzee Tear"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 20),
        )
    ),
    EnemyEntry (
        "Nothing?",
        None,
        "Template 303",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Flip Gloomba",
        None,
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
    EnemyEntry (
        "Invincible Underchomp",
        None,
        "Template 305",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Invincible Blue Underchomp",
        None,
        "Template 306",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Invincible Yellow Underchomp",
        None,
        "Template 307",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Invincible Red Underchomp",
        None,
        "Template 308",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Nothing?",
        None,
        "Template 309",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Flip Boomerang Bro",
        None,
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
    EnemyEntry (
        "Flip Fire Bro",
        None,
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
    EnemyEntry (
        "Flip Skellobit",
        None,
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
    EnemyEntry (
        "Flip Spiky Skellobit",
        None,
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
    EnemyEntry (
        "Flip Skellobomber w/Skellobait",
        None,
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
    EnemyEntry (
        "Flip Skellobomber",
        None,
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
    EnemyEntry (
        "(Unused) Green Magikoopa",
        None,
        "Template 316",
        0.04,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "(Unused) Broom Green Magikoopa",
        None,
        "Template 317",
        0.04,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Nothing?",
        None,
        "Template 318",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "(Unused) White Magikoopa",
        None,
        "Template 319",
        0.04,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "(Unused) Broom White Magikoopa",
        None,
        "Template 320",
        0.04,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Nothing?",
        None,
        "Template 321",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "(Unused) Red Magikoopa",
        None,
        "Template 322",
        0.04,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "(Unused) Broom Red Magikoopa",
        None,
        "Template 323",
        0.04,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Nothing?",
        None,
        "Template 324",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Nothing?",
        None,
        "Template 325",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Nothing?",
        None,
        "Template 326",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Dark Spiked Goomba",
        None,
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
    EnemyEntry (
        "Dark Paragoomba",
        None,
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
    EnemyEntry (
        "Dark Goomba",
        None,
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
    EnemyEntry (
        "Dark Headbonk Goomba",
        None,
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
    EnemyEntry (
        "Dark Koopatrol",
        None,
        "Template 331",
        0.07,
        EnemyDrops (
            Drop (item_name = "Turtley Leaf", hex_value = get_hex_value("Turtley Leaf"), weight = 100),
            Drop (item_name = "Thunder Rage", hex_value = get_hex_value("Thunder Rage"), weight = 300),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 20),
        )
    ),
    EnemyEntry (
        "Dark Shady Koopa",
        None,
        "Template 332",
        0.04,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Dark Paratroopa",
        None,
        "Template 333",
        0.05,
        EnemyDrops (
            Drop (item_name = "Turtley Leaf", hex_value = get_hex_value("Turtley Leaf"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    EnemyEntry (
        "Dark Spike Top",
        None,
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
    EnemyEntry (
        "Dark Stone Buzzy",
        None,
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
    EnemyEntry (
        "Dark Spiny",
        None,
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
    EnemyEntry (
        "Dark Dull Bones",
        None,
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
    EnemyEntry (
        "Dark Bone",
        None,
        "Template 338",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Dark Hammer Bro",
        None,
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
    EnemyEntry (
        "Dark Boomerang Bro",
        None,
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
    EnemyEntry (
        "Dark Fire Bro",
        None,
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
    EnemyEntry (
        "Dark Hammer",
        None,
        "Template 342",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Dark Boomerang",
        None,
        "Template 343",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Dark Fire Bro Fireball",
        None,
        "Template 344",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Dark Magikoopa",
        None,
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
    EnemyEntry (
        "Broom Dark Magikoopa",
        None,
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
    EnemyEntry (
        "Nothing?",
        None,
        "Template 347",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Dark Striker",
        None,
        "Template 348",
        0.07,
        EnemyDrops (
            Drop (item_name = "Super Shroom Shake", hex_value = get_hex_value("Super Shroom Shake"), weight = 100),
            Drop (item_name = "Turtley Leaf", hex_value = get_hex_value("Turtley Leaf"), weight = 200),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 20),
        )
    ),
    EnemyEntry (
        "Dark Striker's Shell",
        None,
        "Template 349",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Dark Clubba",
        None,
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
    EnemyEntry (
        "Dark Dayzee",
        None,
        "Template 351",
        0.15,
        EnemyDrops (
            Drop (item_name = "Golden Leaf", hex_value = get_hex_value("Golden Leaf"), weight = 200),
            Drop (item_name = "Dayzee Tear", hex_value = get_hex_value("Dayzee Tear"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 20),
        )
    ),
    EnemyEntry (
        "Nothing?",
        None,
        "Template 352",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Goomba",
        None,
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
    EnemyEntry (
        "Dark Fuzzy",
        None,
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
    EnemyEntry (
        "Dark Pokey",
        None,
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
    EnemyEntry (
        "Dark Pokey Part",
        None,
        "Template 356",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Dark Ruff Puff",
        None,
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
    EnemyEntry (
        "Nothing?",
        None,
        "Template 358",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Dark Spania",
        None,
        "Template 359",
        0.05,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Dark Cursya",
        None,
        "Template 360",
        0.15,
        EnemyDrops (
            Drop (item_name = "Poison Shroom", hex_value = get_hex_value("Poison Shroom"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    EnemyEntry (
        "(Unused) Dark Back Cursya",
        None,
        "Template 361",
        0.1,
        EnemyDrops (
            Drop (item_name = "Poison Shroom", hex_value = get_hex_value("Poison Shroom"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    EnemyEntry (
        "Dark Tech Cursya",
        None,
        "Template 362",
        0.15,
        EnemyDrops (
            Drop (item_name = "Poison Shroom", hex_value = get_hex_value("Poison Shroom"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    EnemyEntry (
        "Dark Heavy Cursya",
        None,
        "Template 363",
        0.15,
        EnemyDrops (
            Drop (item_name = "Poison Shroom", hex_value = get_hex_value("Poison Shroom"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    EnemyEntry (
        "Dark Reversya Cursya",
        None,
        "Template 364",
        0.15,
        EnemyDrops (
            Drop (item_name = "Poison Shroom", hex_value = get_hex_value("Poison Shroom"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    EnemyEntry (
        "Dark Chomp",
        None,
        "Template 365",
        0.07,
        EnemyDrops (
            Drop (item_name = "Power Steak", hex_value = get_hex_value("Power Steak"), weight = 100),
            Drop (item_name = "Thunder Rage", hex_value = get_hex_value("Thunder Rage"), weight = 200),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 30),
        )
    ),
    EnemyEntry (
        "Dark Dark Boo",
        None,
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
    EnemyEntry (
        "Dark Cleft",
        None,
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
    EnemyEntry (
        "Dark Shlurp",
        None,
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
    EnemyEntry (
        "Dark Squiglet",
        None,
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
    EnemyEntry (
        "Nothing?",
        None,
        "Template 370",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Dark Sproing-Oing",
        None,
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
    EnemyEntry (
        "Mini Dark Sproing-Oing",
        None,
        "Template 372",
        0.03,
        EnemyDrops (
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    EnemyEntry (
        "Dark Boomboxer",
        None,
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
    EnemyEntry (
        "Nothing?",
        None,
        "Template 374",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Dark Jawbus",
        None,
        "Template 375",
        0.15,
        EnemyDrops (
            Drop (item_name = "Fire Burst", hex_value = get_hex_value("Fire Burst"), weight = 100),
            Drop (item_name = "Ice Storm", hex_value = get_hex_value("Ice Storm"), weight = 200),
            Drop (item_name = "Thunder Rage", hex_value = get_hex_value("Thunder Rage"), weight = 300),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 30),
        )
    ),
    EnemyEntry (
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
    EnemyEntry (
        "Nothing?",
        None,
        "Template 377",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Dark Growmeba",
        None,
        "Template 378",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Dark Tileoid",
        None,
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
    EnemyEntry (
        "Dark Eeligon",
        None,
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
    EnemyEntry (
        "Dark Eeligon Part",
        None,
        "Template 381",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Dark Longator",
        None,
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
    EnemyEntry (
        "Dark Barribad",
        None,
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
    EnemyEntry (
        "Dark Barribad Projectile",
        None,
        "Template 384",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Dark Pigarithm",
        None,
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
    EnemyEntry (
        "Dark Choppa",
        None,
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
    EnemyEntry (
        "Dark Muth",
        None,
        "Template 387",
        0.25,
        EnemyDrops (
            Drop (item_name = "Bone-In Cut", hex_value = get_hex_value("Bone-In Cut"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 10),
        )
    ),
    EnemyEntry (
        "Dark Ninjoe",
        None,
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
    EnemyEntry (
        "Dark Ninjoe Projectile",
        None,
        "Template 389",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Nothing?",
        None,
        "Template 390",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Dark Skellobit",
        None,
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
    EnemyEntry (
        "Dark Spiky Skellobit",
        None,
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
    EnemyEntry (
        "Dark Megabite",
        None,
        "Template 393",
        0.15,
        EnemyDrops (
            Drop (item_name = "POW Block", hex_value = get_hex_value("POW Block"), weight = 100),
            Drop (item_name = "Ghost Shroom", hex_value = get_hex_value("Ghost Shroom"), weight = 100),
            Drop (item_name = "Catch Card SP", hex_value = get_hex_value("Catch Card SP"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 30),
        )
    ),
    EnemyEntry (
        "Dark Magiblot",
        None,
        "Template 394",
        0.06,
        EnemyDrops (
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 100),
            Drop (item_name = "Catch Card SP", hex_value = get_hex_value("Catch Card SP"), weight = 100),
            Drop (item_name = "Shroom Shake", hex_value = get_hex_value("Shroom Shake"), weight = 100),
        )
    ),
    EnemyEntry (
        "Nothing?",
        None,
        "Template 395",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Brobot Fist",
        None,
        "Template 396",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Mimi 2",
        None,
        "Template 397",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Bowser 2",
        None,
        "Template 398",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Dark Dimentio Cube",
        None,
        "Template 399",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Big Dark Dimentio Cube",
        None,
        "Template 400",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Giant Dark Dimentio Cube",
        None,
        "Template 401",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Rubee",
        None,
        "Template 402",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Nothing?",
        None,
        "Template 403",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Dimentio Attack",
        None,
        "Template 404",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Dimentio",
        None,
        "Template 405",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Dimentio",
        None,
        "Template 406",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Dimentio",
        None,
        "Template 407",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Stench",
        None,
        "Template 408",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Cherbil",
        None,
        "Template 409",
        0.04,
        EnemyDrops (
            Drop (item_name = "Peachy Peach", hex_value = get_hex_value("Peachy Peach"), weight = 100),
            Drop (item_name = "Sleepy Sleep", hex_value = get_hex_value("Sleepy Sleep"), weight = 100),
            Drop (item_name = "Long-Last Shake", hex_value = get_hex_value("Long-Last Shake"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 20),
        )
    ),
    EnemyEntry (
        "Cherbil's Projectile",
        None,
        "Template 410",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Poison Cherbil",
        None,
        "Template 411",
        1.0,
        EnemyDrops (
            Drop (item_name = "Peachy Peach", hex_value = get_hex_value("Peachy Peach"), weight = 100),
            Drop (item_name = "Dried Shroom", hex_value = get_hex_value("Dried Shroom"), weight = 500),
            Drop (item_name = "Long-Last Shake", hex_value = get_hex_value("Long-Last Shake"), weight = 50),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 20),
        )
    ),
    EnemyEntry (
        "Poison Cherbil's Projectile",
        None,
        "Template 412",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Ice Cherbil",
        None,
        "Template 413",
        0.04,
        EnemyDrops (
            Drop (item_name = "Peachy Peach", hex_value = get_hex_value("Peachy Peach"), weight = 100),
            Drop (item_name = "Ice Storm", hex_value = get_hex_value("Ice Storm"), weight = 100),
            Drop (item_name = "Long-Last Shake", hex_value = get_hex_value("Long-Last Shake"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 20),
        )
    ),
    EnemyEntry (
        "Ice Cherbil's Projectile",
        None,
        "Template 414",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Dark Cherbil",
        None,
        "Template 415",
        0.5,
        EnemyDrops (
            Drop (item_name = "Peachy Peach", hex_value = get_hex_value("Peachy Peach"), weight = 100),
            Drop (item_name = "Sleepy Sleep", hex_value = get_hex_value("Sleepy Sleep"), weight = 100),
            Drop (item_name = "Long-Last Shake", hex_value = get_hex_value("Long-Last Shake"), weight = 100),
            Drop (item_name = "Catch Card", hex_value = get_hex_value("Catch Card"), weight = 20),
        )
    ),
    EnemyEntry (
        "Dark Cherbil's Projectile",
        None,
        "Template 416",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Ice Dark Cherbil's Projectile",
        None,
        "Template 417",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Poison Dark Cherbil's Projectile",
        None,
        "Template 418",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Frackle",
        None,
        "Template 419",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Wrackle",
        None,
        "Template 420",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Nothing?",
        None,
        "Template 421",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Enemy Mario",
        None,
        "Template 422",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Glitchy Enemy Mario",
        None,
        "Template 423",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Enemy Luigi?",
        None,
        "Template 424",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Enemy Luigi?",
        None,
        "Template 425",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Sammer Guy",
        None,
        "Template 426",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Stationary Enemy Mario",
        None,
        "Template 427",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Stationary Enemy Luigi",
        None,
        "Template 428",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Stationary Enemy Peach",
        None,
        "Template 429",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Stationary Enemy Bowser",
        None,
        "Template 430",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Two Koopa Strikers at once",
        None,
        "Template 431",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "Giant Shell",
        None,
        "Template 432",
        0.0,
        EnemyDrops (
            
        )
    ),
    EnemyEntry (
        "(No name)",
        None,
        "Template 433",
        0.0,
        EnemyDrops (
            
        )
    )
}
    