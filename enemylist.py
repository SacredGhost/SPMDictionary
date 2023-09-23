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
        0x11A,
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
    EnemyEntry (
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
    EnemyEntry (
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
    EnemyEntry (
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
    EnemyEntry (
        "3D Goomba",
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
}
    