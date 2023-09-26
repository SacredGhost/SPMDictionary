from enum import Enum

from bighexlist import ListType, ItemType
from enemylist import EnemyList

class Map():
    def __init__(self, MapName, MapArea, MapType, MapEnemies, MapItems, ShopItems, MapEntrance):
        self.MapName = MapName
        self.MapArea = MapArea
        self.MapType = MapType
        self.MapEnemies = MapEnemies
        self.MapItems = MapItems
        self.ShopItems = ShopItems
        self.MapEntrance = MapEntrance

class MapEntrance():
    def __init__(self, *entrances):
        self.entrances = list(entrances)

    def add_entrance(self, entrance):
        self.entrances.append(entrance)

    def remove_entrance(self, entrance):
        self.entrances.remove(entrance)

    def get_entrance(self, index):
        if 0 <= index < len(self.entrances):
            return self.entrances[index]
        else:
            return None

class EntranceDest():
    def __init__(self, curMap, destinations):
        self.curMap = curMap
        self.destinations = destinations

    def add_destination(self, destMap, destEntrance, MinSequence):
        self.destinations.append((destMap, destEntrance, MinSequence))

    def remove_destination(self, destMap, destEntrance, MinSequence):
        self.destinations.remove((destMap, destEntrance, MinSequence))
        
class Entrance():
    def __init__(self, EntranceName, EntranceType, EntranceLocation, EntranceDest, EntranceValid):
        self.EntranceName = EntranceName
        self.EntranceType = EntranceType
        self.EntranceLocation = EntranceLocation
        self.EntranceDest = EntranceDest
        self.EntranceValid = EntranceValid


class Location():
    def __init__(self, xpos, ypos, zpos):
        self.xpos = xpos
        self.ypos = ypos
        self.zpos = zpos

class ItemPos():
    def __init__(self, ItemState, xpos, ypos, zpos):
        self.ItemState = ItemState
        self.xpos = xpos
        self.ypos = ypos
        self.zpos = zpos

class ItemState(Enum):
    GROUND = 0
    GROUND3D = 1
    CHEST = 2
    ENEMY = 3
    MAP = 4

class MapType(Enum):
    INVALID = 0
    MAIN = 1
    USELESS = 2

class EntranceType(Enum):
    DEFAULT = 0
    DOOR = 1
    PIPE = 2
    ELEVATOR = 3
    RETURNPIPE = 4
    CHAPTERDOOR = 5
    BACKPIPE = 6

class EntranceValid(Enum):
    WELDERBERG = 1
    BOOMER = 2

class MapItems():
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
        
class Item():
    def __init__(self, ItemName, ItemHex, ListType, ItemType, ItemLocation):
        self.ItemName = ItemName
        self.ItemHex = ItemHex
        self.ListType = ListType
        self.ItemType = ItemType
        self.ItemLocation = ItemLocation

class MapEnemies():
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
        
class Enemy():
    def __init__(self, EnemyName, TemplateID, EnemyLocation):
        self.EnemyName = EnemyName
        self.TemplateID = TemplateID
        self.EnemyLocation = EnemyLocation

class EnemyLocation():
    def __init__(self, EnemyState, xpos, ypos, zpos):
        self.EnemyState = EnemyState
        self.xpos = xpos
        self.ypos = ypos
        self.zpos = zpos

class EnemyState(Enum):
    IN2D = 0
    IN3D = 1

class MapShop():
    def __init__(self, ShopID, ShopLocation):
        self.ShopID = ShopID
        self.ShopLocation = ShopLocation

MapList = [
    Map (
        "aa1_01",
        "aa1",
        MapType.INVALID,
        None,
        None,
        None,
        None
    ),
    Map (
        "aa1_02",
        "aa1",
        MapType.INVALID,
        None,
        None,
        None,
        None
    ),
    Map (
        "aa2_01",
        "aa2",
        MapType.INVALID,
        None,
        None,
        None,
        None
    ),
    Map (
        "aa2_02",
        "aa2",
        MapType.INVALID,
        None,
        None,
        None,
        None
    ),
    Map (
        "aa3_01",
        "aa3",
        MapType.INVALID,
        None,
        None,
        None,
        None
    ),
    Map (
        "aa4_01",
        "aa4",
        MapType.INVALID,
        None,
        None,
        None,
        None
    ),
    Map (
        "an1_01",
        "an1",
        MapType.MAIN,
        None,
        None,
        None,
        MapEntrance (
            Entrance ("default", EntranceType.DEFAULT, Location (-590, 0, 0), None, False),
            Entrance ("doa1_l", EntranceType.DOOR, Location (625, 0, 0), EntranceDest ("an1_01" [("an1_02", "doa1_l", 0)]), True),
            Entrance ("doa7_l", EntranceType.DOOR, Location (-570, 0, 0), None, False)
        )
    ),
    Map (
        "an1_02",
        "an1",
        MapType.MAIN,
        MapEnemies (
            Enemy ("Dry Bones", EnemyList["36"], EnemyLocation (EnemyState.IN2D, -362, 0, 137)),
            Enemy ("Dry Bones", EnemyList["36"], EnemyLocation (EnemyState.IN2D, -813, 0, -125)),
            Enemy ("Dry Bones", EnemyList["36"], EnemyLocation (EnemyState.IN2D, -675, 275, 125)),
            Enemy ("Dry Bones", EnemyList["36"], EnemyLocation (EnemyState.IN2D, -550, 275, -125)),
            Enemy ("Frost Piranha", EnemyList["51"], EnemyLocation (EnemyState.IN2D, -750, 450, 0)),
            Enemy ("Frost Piranha", EnemyList["51"], EnemyLocation (EnemyState.IN2D, 250, 450, 0)),
            Enemy ("Lava Bubble", EnemyList["28"], EnemyLocation (EnemyState.IN2D, 75, -100, 0)),
            Enemy ("Lava Bubble", EnemyList["28"], EnemyLocation (EnemyState.IN2D, -125, -100, 0)),
            Enemy ("Dry Bones", EnemyList["36"], EnemyLocation (EnemyState.IN3D, -837, 275, 0)),
            Enemy ("Dry Bones", EnemyList["36"], EnemyLocation (EnemyState.IN3D, -837, 0, 0)),
            Enemy ("Dry Bones", EnemyList["36"], EnemyLocation (EnemyState.IN3D, 950, 275, 0)),
            Enemy ("Lava Bubble", EnemyList["28"], EnemyLocation (EnemyState.IN2D, -500, -100, 0)),
            Enemy ("Frost Piranha", EnemyList["51"], EnemyLocation (EnemyState.IN2D, -250, 450, 0)),
            Enemy ("Poison Cherbil", EnemyList["411"], EnemyLocation (EnemyState.IN2D, 125, 275, 125))
        ),
        MapItems (
            Item ("Super Shroom Shake", 0x51, ListType.ITEM, ItemType.VANILLA, ItemPos (ItemState.GROUND, 1225, 150, 0))
        ),
        None,
        MapEntrance (
            Entrance ("default", EntranceType.DEFAULT, Location (-1069, 0, 0), None, False),
            Entrance ("dokan_01", EntranceType.PIPE, Location (-1225, 225, 4), EntranceDest ("an1_02", [("an1_10", "dokan_01", 0)]), True),
            Entrance ("dokan_10", EntranceType.PIPE, Location (750, 450, 4), EntranceDest ("an1_02", [("an1_02", "h_dokan_4", 0)]), True),
            Entrance ("h_dokan_1", EntranceType.BACKPIPE, Location (343, 64, -160), EntranceDest ("an1_02", [("an1_02", "h_dokan_3", 0)]), True),
            Entrance ("h_dokan_2", EntranceType.BACKPIPE, Location (563, 80, -160),  EntranceDest ("an1_02", [("an1_11", "dokan_01", 0)]), True),
            Entrance ("h_dokan_3", EntranceType.BACKPIPE, Location (323, 352, -160), EntranceDest ("an1_02)", [("an1_02", "h_dokan_1", 0)]), True),
            Entrance ("h_dokan_4", EntranceType.BACKPIPE, Location (664, 347, -160), EntranceDest ("an1_02", [("an1_02", "dokan_10", 0)]), True),
            Entrance ("doa1_l", EntranceType.DOOR, Location (-1050, 0, 0), EntranceDest ("an1_02", [("an1_01",  "doa1_l", 0)]), True),
            Entrance ("doa2_l", EntranceType.DOOR, Location (1100, 0, 0), EntranceDest ("an1_02", [("an1_03", "doa1_l", 0)]), True),
            Entrance ("doa3_l", EntranceType.DOOR, Location (1100, 275, 0), EntranceDest  ("an1_02" [("an1_08", "doa1_l", 0)]), True)
        )
    ),
    Map (
        "an1_03",
        "an1",
        MapType.MAIN,
        None,
        None,
        None,
        MapEntrance (
            Entrance ("default", EntranceType.DEFAULT, Location (-1168, 2000, -150), None, False),
        )
    ),
    Map (
        "mac_02",
        "mac",
        MapType.MAIN,
        None,
        None,
        None,
        MapEntrance (
            Entrance ("default", EntranceType.DEFAULT, Location (0, 1500, 0), None, False),
            Entrance ("dokan_1", EntranceType.PIPE, Location (835, 125, 250), EntranceDest ("mac_02", [("mac_01", "dokan_1", 64)]), EntranceValid.BOOMER),
            Entrance ("dokan_2", EntranceType.PIPE, Location (750, 30, 1550), EntranceDest ("mac_02", [("mac_06", "dokan_1", 64)]), True),
            Entrance ("dokan_3", EntranceType.RETURNPIPE, Location (600, 1500, -150), None, False),
            Entrance ("aodokan_1", EntranceType.PIPE, Location (-1100, 30, -100), EntranceDest ("mac_02", [("mac_05", "aodokan_1", 65)]), EntranceValid.WELDERBERG),
            Entrance ("aodokan_2", EntranceType.PIPE, Location (1100, 30, -100), EntranceDest ("mac_02", [("mac_12", "aodokan_1", 176)]), EntranceValid.WELDERBERG),
            Entrance ("doa6_l", EntranceType.CHAPTERDOOR, Location (-450, 1500, -200), EntranceDest ("mac_02", [("he1_01", "doa1_l", 9), ("he2_01", "default", 58), ("he3_01", "default", 58), ("he4_01", "default", 58)]), True),
            Entrance ("doa8_l", EntranceType.CHAPTERDOOR, Location (-300, 1500, -200), EntranceDest ("mac_02", [("mi1_01", "doa2_l", 65), ("mi2_01", "default", 99), ("mi3_01", "default", 99), ("mi4_01", "default", 99)]), True),
            Entrance ("doa9_l", EntranceType.CHAPTERDOOR, Location (-150, 1500, -200), EntranceDest ("mac_02", [("ta1_01", "doa3_l", 100), ("ta2_01", "default", 127), ("ta3_01", "default", 127), ("ta4_01", "default", 127)]), True),
            Entrance ("doa10_l", EntranceType.CHAPTERDOOR, Location (0, 1500, -200), EntranceDest ("mac_02", [("sp1_01", "doa4_l", 134), ("sp2_01", "default", 175), ("sp3_01", "default", 175), ("sp4_01", "default", 175)]), True),
            Entrance ("doa11_l", EntranceType.CHAPTERDOOR, Location (150, 1500, -200), EntranceDest ("mac_02", [("gn1_01", "doa5_l", 177), ("gn2_01", "default", 222), ("gn3_01", "default", 222), ("gn4_01", "default", 222)]), True),
            Entrance ("doa12_l", EntranceType.CHAPTERDOOR, Location (300, 1500, -200), EntranceDest ("mac_02", [("wa1_01", "doa5_l", 222), ("wa1_27", "doa5_l", 281)]), True), # doa5_l is not a typo, also sequence is 224, but 222 is for people that do MCS
            Entrance ("doa11_l", EntranceType.CHAPTERDOOR, Location (150, 1500, -200), EntranceDest ("mac_02", [("an1_01", "doa7_l", 303), ("an2_01", "default", 355), ("an3_01", "default", 355), ("an4_01", "default", 355)]), True),
            Entrance ("elv1", EntranceType.ELEVATOR, Location (-700, 0, -250), EntranceDest ("mac_02", [("mac_09", "elv1", 53)]), True),
            Entrance ("elv2", EntranceType.ELEVATOR, Location (700, 0, -250), EntranceDest ("mac_02", [("mac_01", "elv1", 0)]), True),
            Entrance ("dearu_ie", EntranceType.DEFAULT, Location (0, 0, 0), None, False)
        )
    ),
]