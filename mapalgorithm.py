from enum import Enum

from bighexlist import ListType, ItemType

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

    def add_destination(self, destMap, destEntrance):
        self.destinations.append((destMap, destEntrance))

    def remove_destination(self, destMap, destEntrance):
        self.destinations.remove((destMap, destEntrance))
        
class Entrance():
    def __init__(self, EntranceName, EntranceType, EntranceLocation, EntranceDest, EntranceValid, MinSeqence):
        self.EntranceName = EntranceName
        self.EntranceType = EntranceType
        self.EntranceLocation = EntranceLocation
        self.EntranceDest = EntranceDest
        self.EntranceValid = EntranceValid
        self.MinSeqence = MinSeqence


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
            Entrance ("default", EntranceType.DEFAULT, Location (-590, 0, 0), None, False, 0),
            Entrance ("doa1_l", EntranceType.DOOR, Location (625, 0, 0), EntranceDest ("an1_01" [("an1_02", "doa1_l")]), True, 0),
            Entrance ("doa7_l", EntranceType.DOOR, Location (-570, 0, 0), None, False, 0)
        )
    ),
    Map (
        "an1_02",
        "an1",
        MapType.MAIN,
        None,
        MapItems (
            Item ("Super Shroom Shake", 0x51, ListType.ITEM, ItemType.CONSUMABLE, ItemPos (ItemState.GROUND, 1225, 150, 0))
        ),
        None,
        MapEntrance (
            Entrance ("default", EntranceType.DEFAULT, Location (-1069, 0, 0), None, False, 0),
            Entrance ("dokan_01", EntranceType.PIPE, Location (-1225, 225, 4), EntranceDest ("an1_02", [("an1_10", "dokan_01")]), True, 0),
            Entrance ("dokan_10", EntranceType.PIPE, Location (750, 450, 4), EntranceDest ("an1_02", [("an1_02", "h_dokan_4")]), True, 0),
            Entrance ("h_dokan_1", EntranceType.BACKPIPE, Location (343, 64, -160), EntranceDest ("an1_02", [("an1_02", "h_dokan_3")]), True, 0),
            Entrance ("h_dokan_2", EntranceType.BACKPIPE, Location (563, 80, -160),  EntranceDest ("an1_02", [("an1_11", "dokan_01")]), True, 0),
            Entrance ("h_dokan_3", EntranceType.BACKPIPE, Location (323, 352, -160), EntranceDest ("an1_02)", [("an1_02", "h_dokan_1")]), True, 0),
            Entrance ("h_dokan_4", EntranceType.BACKPIPE, Location (664, 347, -160), EntranceDest ("an1_02", [("an1_02", "dokan_10")]), True, 0),
            Entrance ("doa1_l", EntranceType.DOOR, Location (-1050, 0, 0), EntranceDest ("an1_02", [("an1_01",  "doa1_l")]), True, 0),
            Entrance ("doa2_l", EntranceType.DOOR, Location (1100, 0, 0), EntranceDest ("an1_02", [("an1_03", "doa1_l")]), True, 0),
            Entrance ("doa3_l", EntranceType.DOOR, Location (1100, 275, 0), EntranceDest  ("an1_02" [("an1_08", "doa1_l")]), True, 0)
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
            Entrance ("default", EntranceType.DEFAULT, Location (-1168, 2000, -150), None, False, 0),
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
            Entrance ("default", EntranceType.DEFAULT, Location (0, 1500, 0), None, False, 0),
            Entrance ("dokan_1", EntranceType.PIPE, Location (835, 125, 250), EntranceDest ("mac_02", [("mac_01", "dokan_1")]), EntranceValid.BOOMER, 64),
            Entrance ("dokan_2", EntranceType.PIPE, Location (750, 30, 1550), EntranceDest ("mac_02", [("mac_06", "dokan_1")]), True, 64),
            Entrance ("dokan_3", EntranceType.RETURNPIPE, Location (600, 1500, -150), None, False, 0),
            Entrance ("aodokan_1", EntranceType.PIPE, Location (-1100, 30, -100), EntranceDest ("mac_02", [("mac_05", "aodokan_1")]), EntranceValid.WELDERBERG, 65),
            Entrance ("aodokan_2", EntranceType.PIPE, Location (1100, 30, -100), EntranceDest ("mac_02", [("mac_12", "aodokan_1")]), EntranceValid.WELDERBERG, 176),
            Entrance ("doa6_l", EntranceType.CHAPTERDOOR, Location (-450, 1500, -200), EntranceDest ("mac_02", [("he1_01", "doa1_l"), ("he2_01", "default"), ("he3_01", "default"), ("he4_01", "default")]), True, 9),
            Entrance ("doa8_l", EntranceType.CHAPTERDOOR, Location (-300, 1500, -200), EntranceDest ("mac_02", [("mi1_01", "doa2_l"), ("mi2_01", "default"), ("mi3_01", "default"), ("mi4_01", "default")]), True, 65),
            Entrance ("doa9_l", EntranceType.CHAPTERDOOR, Location (-150, 1500, -200), EntranceDest ("mac_02", [("ta1_01", "doa3_l"), ("ta2_01", "default"), ("ta3_01", "default"), ("ta4_01", "default")]), True, 100),
            Entrance ("doa10_l", EntranceType.CHAPTERDOOR, Location (0, 1500, -200), EntranceDest ("mac_02", [("sp1_01", "doa4_l"), ("sp2_01", "default"), ("sp3_01", "default"), ("sp4_01", "default")]), True, 134),
            Entrance ("doa11_l", EntranceType.CHAPTERDOOR, Location (150, 1500, -200), EntranceDest ("mac_02", [("gn1_01", "doa5_l"), ("gn2_01", "default"), ("gn3_01", "default"), ("gn4_01", "default")]), True, 177),
            Entrance ("doa12_l", EntranceType.CHAPTERDOOR, Location (300, 1500, -200), EntranceDest ("mac_02", [("wa1_01", "doa5_l"), ("wa1_27", "doa5_l")]), True, 222), # doa5_l is not a typo
            Entrance ("doa11_l", EntranceType.CHAPTERDOOR, Location (150, 1500, -200), EntranceDest ("mac_02", [("an1_01", "doa7_l"), ("an2_01", "default"), ("an3_01", "default"), ("an4_01", "default")]), True, 303),
            Entrance ("elv1", EntranceType.ELEVATOR, Location (-700, 0, -250), EntranceDest ("mac_02", [("mac_09", "elv1")]), True, 53),
            Entrance ("elv2", EntranceType.ELEVATOR, Location (700, 0, -250), EntranceDest ("mac_02", [("mac_01", "elv1")]), True, 0),
            Entrance ("dearu_ie", EntranceType.DEFAULT, Location (0, 0, 0), None, False, 0)
        )
    ),
]