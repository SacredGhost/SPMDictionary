from enum import Enum

from bighexlist import HexList
from enemylist import EnemyList

class Map():
    def __init__(self, MapType, MapEnemies, MapItems, ShopItems, MapEntrance):
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

class EntranceKey():
    def __init__(self, enterable, locked, keyID):
        self.enterable = enterable
        self.locked = locked
        self.keyID = keyID

class Location():
    def __init__(self, xpos, ypos, zpos):
        self.xpos = xpos
        self.ypos = ypos
        self.zpos = zpos

class HexPos():
    def __init__(self, ItemState, xpos, ypos, zpos):
        self.ItemState = ItemState
        self.xpos = xpos
        self.ypos = ypos
        self.zpos = zpos

class ItemState(Enum):
    GROUND = 0
    GROUND3D = 1
    CHEST = 2
    CHEST3D = 3
    ENEMY = 4
    MAP = 5
    NPC = 6

class MapMatch():
    def __init__(self, MapName, MapHexID):
        self.MapName = MapName
        self.MapHexID = MapHexID

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
    STARBLOCK = 7

class WelderBergPipe1(Enum):
    NOTEXIST = 0
    EXIST = 1

class WelderBergPipe2(Enum):
    NOTEXIST = 0
    EXIST = 1

class WelderBergPipe3(Enum):
    NOTEXIST = 0
    EXIST = 1

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
    def __init__(self, ItemEntry, ItemLocation, MinSequence):
        self.ItemEntry = ItemEntry
        self.ItemLocation = ItemLocation
        self.MinSequence = MinSequence

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

MapList = {
    'aa1_01':Map (
        MapType.INVALID,
        None,
        None,
        None,
        None
    ),
    'aa1_02':Map (
        MapType.INVALID,
        None,
        None,
        None,
        None
    ),
    'aa2_01':Map (
        MapType.INVALID,
        None,
        None,
        None,
        None
    ),
    'aa2_02':Map (
        MapType.INVALID,
        None,
        None,
        None,
        None
    ),
    'aa3_01':Map (
        MapType.INVALID,
        None,
        None,
        None,
        None
    ),
    'aa4_01':Map (
        MapType.INVALID,
        None,
        None,
        None,
        None
    ),
    'an1_01':Map (
        MapType.MAIN,
        None,
        MapItems(
            Item(HexList["Jaydes Card"], HexPos (ItemState.MAP, 0, 100, 0), 359)
        ),
        None,
        MapEntrance (
            Entrance ("default", EntranceType.DEFAULT, Location (-590, 0, 0), None, EntranceKey (False, False, None)),
            Entrance ("doa1_l", EntranceType.DOOR, Location (625, 0, 0), EntranceDest ("an1_01" [("an1_02", "doa1_l", 0)]), EntranceKey (True, False, None)),
            Entrance ("doa7_l", EntranceType.DOOR, Location (-570, 0, 0), None, EntranceKey (True, False, None))
        )
    ),
    'an1_02':Map (
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
            Item (HexList["Super Shroom Shake"], HexPos (ItemState.GROUND, 1225, 150, 0), 0)
        ),
        None,
        MapEntrance (
            Entrance ("default", EntranceType.DEFAULT, Location (-1069, 0, 0), None, EntranceKey (False, False, None)),
            Entrance ("dokan_01", EntranceType.PIPE, Location (-1225, 225, 4), EntranceDest ("an1_02", [("an1_10", "dokan_01", 0)]), EntranceKey (True, False, None)),
            Entrance ("dokan_10", EntranceType.PIPE, Location (750, 450, 4), EntranceDest ("an1_02", [("an1_02", "h_dokan_4", 0)]), EntranceKey (True, False, None)),
            Entrance ("h_dokan_1", EntranceType.BACKPIPE, Location (343, 64, -160), EntranceDest ("an1_02", [("an1_02", "h_dokan_3", 0)]), EntranceKey (True, False, None)),
            Entrance ("h_dokan_2", EntranceType.BACKPIPE, Location (563, 80, -160),  EntranceDest ("an1_02", [("an1_11", "dokan_01", 0)]), EntranceKey (True, False, None)),
            Entrance ("h_dokan_3", EntranceType.BACKPIPE, Location (323, 352, -160), EntranceDest ("an1_02)", [("an1_02", "h_dokan_1", 0)]), EntranceKey (True, False, None)),
            Entrance ("h_dokan_4", EntranceType.BACKPIPE, Location (664, 347, -160), EntranceDest ("an1_02", [("an1_02", "dokan_10", 0)]), EntranceKey (True, False, None)),
            Entrance ("doa1_l", EntranceType.DOOR, Location (-1050, 0, 0), EntranceDest ("an1_02", [("an1_01",  "doa1_l", 0)]), EntranceKey (True, False, None)),
            Entrance ("doa2_l", EntranceType.DOOR, Location (1100, 0, 0), EntranceDest ("an1_02", [("an1_03", "doa1_l", 0)]), EntranceKey (True, False, None)),
            Entrance ("doa3_l", EntranceType.DOOR, Location (1100, 275, 0), EntranceDest  ("an1_02" [("an1_08", "doa1_l", 297)]), EntranceKey (True, False, None))
        )
    ),
    'an1_03':Map (
        MapType.MAIN,
        MapEnemies (
            Enemy ("Underhand", EnemyList["248"], EnemyLocation (EnemyState.IN2D, -775, 500, 25)),
            Enemy ("Underhand", EnemyList["248"], EnemyLocation (EnemyState.IN2D, -550, 500, 175)),
            Enemy ("Underhand", EnemyList["248"], EnemyLocation (EnemyState.IN2D, -88, 500, -125)),
            Enemy ("Underhand", EnemyList["248"], EnemyLocation (EnemyState.IN2D, -413, 500, 50)),
            Enemy ("Underhand", EnemyList["248"], EnemyLocation (EnemyState.IN2D, 775, 500, -75)),
            Enemy ("Underhand", EnemyList["247"], EnemyLocation (EnemyState.IN2D, 337, 712, -50)),
            Enemy ("Underhand", EnemyList["247"], EnemyLocation (EnemyState.IN2D, 563, 863, 175)),
            Enemy ("Underhand", EnemyList["247"], EnemyLocation (EnemyState.IN2D, -263, 825, -100)),
            Enemy ("Underhand", EnemyList["247"], EnemyLocation (EnemyState.IN2D, -588, 913, 0)),
            Enemy ("Underhand", EnemyList["247"], EnemyLocation (EnemyState.IN2D, -513, 1713, -75)),
            Enemy ("Underhand", EnemyList["247"], EnemyLocation (EnemyState.IN2D, -175, 1613, 25)),
            Enemy ("Underhand", EnemyList["247"], EnemyLocation (EnemyState.IN2D, -688, 1525, 50)),
            Enemy ("Underhand", EnemyList["247"], EnemyLocation (EnemyState.IN2D, -100, 1188, -150)),
            Enemy ("Underhand", EnemyList["247"], EnemyLocation (EnemyState.IN2D, 213, 1313, -25)),
            Enemy ("Underhand", EnemyList["247"], EnemyLocation (EnemyState.IN2D, 563, 1300, -125)),
            Enemy ("Underhand", EnemyList["247"], EnemyLocation (EnemyState.IN2D, -450, 1238, 125)),
            Enemy ("Underhand", EnemyList["247"], EnemyLocation (EnemyState.IN2D, 250, 1638, 150)),
            Enemy ("Underhand", EnemyList["247"], EnemyLocation (EnemyState.IN2D, 688, 1613, 100)),
            Enemy ("Underhand", EnemyList["247"], EnemyLocation (EnemyState.IN2D, 63, 975, 75))
        ),
        None,
        None,
        MapEntrance (
            Entrance ("default", EntranceType.DEFAULT, Location (-1168, 2000, -150), None, EntranceKey (False, False, None)),
            Entrance ("doa1_l", EntranceType.DOOR, Location (-1150, 2000, 0), EntranceDest ("an1_03", [("an1_02", "doa2_l", 0)]), EntranceKey (True, False, None)),
            Entrance ("doa2_l", EntranceType.DOOR, Location (1150, 2000, 0), EntranceDest ("an1_03", [("an1_04", "doa1_l", 0)]), EntranceKey (True, False, None)),
            Entrance ("doa3_l", EntranceType.DOOR, Location (0, 0, 0), EntranceDest ("an1_03", [("an1_06", "doa1_l", 295)]), EntranceKey (True, True, HexList["Door Key 0x31"])),
        )
    ),
    'an1_04':Map (
        MapType.MAIN,
        None,
        MapItems (
            Item (HexList["Door Key 0x31"], HexPos (ItemState.NPC, 850, 100, 20), 0)
        ),
        None,
        MapEntrance (
            Entrance ("default", EntranceType.DEFAULT, Location (-868, 0, 0), None, EntranceKey (False, False, None)),
            Entrance ("doa1_l", EntranceType.DOOR, Location (-850, 0, 0), EntranceDest ("an1_04", [("an1_03", "doa2_l", 0)]), EntranceKey (True, False, None)),
            Entrance ("doa2_l", EntranceType.DOOR, Location (850, 100, 20), EntranceDest ("an1_04", [("an1_05", "doa1_l", 305)]), EntranceKey (True, False, None))
        )
    ),
    'an1_05':Map (
        MapType.MAIN,
        None,
        None,
        None,
        MapEntrance (
            Entrance ("default", EntranceType.DEFAULT, Location (-211, 0, 0), None, EntranceKey (False, False, None)),
            Entrance ("doa1_l", EntranceType.DOOR, Location (-200, 0, 0), EntranceDest ("an1_05", [("an1_04", "doa2_l", 0)]), EntranceKey (True, False, None)),
            Entrance ("Star Block", EntranceType.STARBLOCK, Location (193, 0, 0), EntranceDest ("an1_05", [("an2_01", "default", 0)]), EntranceKey (True, False, None))
        )
    ),
    'aa1_06':Map (
        MapType.MAIN,
        MapEnemies (
            Enemy ("Underhand", EnemyList["248"], EnemyLocation (EnemyState.IN2D, -1075, 0, -487)),
            Enemy ("Underhand", EnemyList["248"], EnemyLocation (EnemyState.IN3D, 50, 0, 100)),
            Enemy ("Underhand", EnemyList["248"], EnemyLocation (EnemyState.IN3D, 100, 0, 100)),
            Enemy ("Underhand", EnemyList["248"], EnemyLocation (EnemyState.IN3D, 75, 0, 100)),
            Enemy ("Underhand", EnemyList["248"], EnemyLocation (EnemyState.IN3D, 125, 0, 100)),
            Enemy ("Underhand", EnemyList["248"], EnemyLocation (EnemyState.IN3D, 150, 0, 100)),
            Enemy ("Underhand", EnemyList["248"], EnemyLocation (EnemyState.IN2D, 100, 0, -50))
        ),
        None,
        None,
        MapEntrance (
            Entrance ("default", EntranceType.DEFAULT, Location (-1575, 0, -498), None, EntranceKey (False, False, None)),
            Entrance ("dokan_05", EntranceType.PIPE, Location (275, 50, 460), EntranceDest ("an1_06", [("an1_09", "dokan_01", 0)]), EntranceKey (True, False, None)),
            Entrance ("doa1_l", EntranceType.DOOR, Location (-1550, 0, -550), EntranceDest ("an1_06", [("an1_04", "doa3_l", 0)]), EntranceKey (True, False, None)),
            Entrance ("doa2_l", EntranceType.DOOR, Location (450, 0, 460), EntranceDest ("an1_06", [("an1_07", "doa1_l", 0)]), EntranceKey (True, False, None))
        )
    ),
    'an1_07':Map (
        MapType.MAIN,
        None,
        MapItems (
            Item (HexList["Dry Bones Card"], HexPos (ItemState.CHEST, -730, 0, 90), 0),
            Item (HexList["Long-Last Shake"], HexPos (ItemState.GROUND3D, 605, 200, 100)),
            Item (HexList["Luigi"], HexPos (ItemState.GROUND, 400, 200, 0))
        ),
        None,
        MapEntrance (
            Entrance ("default", EntranceType.DEFAULT, Location (-725, 200, 0), None, EntranceKey (False, False, None)),
            Entrance ("doa1_l", EntranceType.DOOR, Location (-200, 0, 0), EntranceDest ("an1_07", [("an1_06", "doa2_l", 0)]), EntranceKey (True, False, None)),
        )
    ),
    'an1_08':Map (
        MapType.MAIN,
        MapEnemies (
            Enemy ("Frost Piranha", EnemyList["51"], EnemyLocation (EnemyState.IN2D, -125, 50, 125)),
            Enemy ("Frost Piranha", EnemyList["51"], EnemyLocation (EnemyState.IN2D, 75, 75, 125)),
            Enemy ("Frost Piranha", EnemyList["51"], EnemyLocation (EnemyState.IN2D, -225, 150, 125)),
            Enemy ("Frost Piranha", EnemyList["51"], EnemyLocation (EnemyState.IN2D, -25, 100, 125)),
            Enemy ("Frost Piranha", EnemyList["51"], EnemyLocation (EnemyState.IN2D, 175, 150, 125)),
            Enemy ("Frost Piranha", EnemyList["51"], EnemyLocation (EnemyState.IN3D, -225, 150, -75)),
            Enemy ("Frost Piranha", EnemyList["51"], EnemyLocation (EnemyState.IN3D, -125, 50, -75)),
            Enemy ("Frost Piranha", EnemyList["51"], EnemyLocation (EnemyState.IN3D, -25, 100, -75)),
            Enemy ("Frost Piranha", EnemyList["51"], EnemyLocation (EnemyState.IN3D, 75, 75, -75)),
            Enemy ("Frost Piranha", EnemyList["51"], EnemyLocation (EnemyState.IN3D, 175, 150, -75)),
        ),
        None,
        None,
        MapEntrance (
            Entrance ("default", EntranceType.DEFAULT, Location (-418, 0, 0), None, EntranceKey (False, False, None)),
            Entrance ("doa1_1", EntranceType.DOOR, Location (-400, 0, 0), EntranceDest ("an1_08", [("an1_02", "doa3_l")]), EntranceKey (True, False, None))
        )
    ),
    'an1_09':Map (
        MapType.USELESS,
        None,
        None,
        None,
        MapEntrance (
            Entrance ("default", EntranceType.DEFAULT, Location (-254, 40, 0), None, EntranceKey (False, False, None)),
            Entrance ("dokan_01", EntranceType.PIPE, Location (-214, 0, -85), EntranceDest ("an1_09", [("an1_06", "dokan_05")]), EntranceKey (True, False, None))
        )
    ),
    'an1_10':Map (
        MapType.USELESS,
        None,
        None,
        None,
        MapEntrance (
            Entrance ("default", EntranceType.DEFAULT, Location (-254, 215, 0), None, EntranceKey (False, False, None)),
            Entrance ("dokan_01", EntranceType.PIPE, Location (-214, 0, -80), EntranceDest ("an1_10", [("an1_02", "dokan_01")]), EntranceKey (True, False, None))
        )
    ),
    'an1_11':Map (
        MapType.USELESS,
        MapEnemies (
            Enemy ("Gigabite", EnemyList["265"], EnemyLocation (EnemyState.IN2D, 100, 50, 0))
        ),
        MapItems (
            Item (HexList["Peach (3) Card"], HexPos (ItemState.CHEST, 0, 0, 0))
        ),
        None,
        MapEntrance (
            Entrance ("default", EntranceType.DEFAULT, Location (-254, 40, 0), None, EntranceKey (False, False, None)),
            Entrance ("dokan_01", EntranceType.PIPE, Location (-214, 0, -80), EntranceDest ("an1_10", [("an1_02", "dokan_01")]), EntranceKey (True, False, None))
        )
    ),
    'mac_02':Map (
        MapType.MAIN,
        None,
        None,
        None,
        MapEntrance (
            Entrance ("default", EntranceType.DEFAULT, Location (0, 1500, 0), None, EntranceKey (False, False, None)),
            Entrance ("dokan_1", EntranceType.PIPE, Location (835, 125, 250), EntranceDest ("mac_02", [("mac_01", "dokan_1", 64)]), EntranceKey (True, True, HexList["Boomer"])),
            Entrance ("dokan_2", EntranceType.PIPE, Location (750, 30, 1550), EntranceDest ("mac_02", [("mac_06", "dokan_1", 64)]), EntranceKey (True, False, None)),
            Entrance ("dokan_3", EntranceType.RETURNPIPE, Location (600, 1500, -150), None, EntranceKey (False, False, None)),
            Entrance ("aodokan_1", EntranceType.PIPE, Location (-1100, 30, -100), EntranceDest ("mac_02", [("mac_05", "aodokan_1", 65)]), EntranceKey (True, True, WelderBergPipe2.EXIST)),
            Entrance ("aodokan_2", EntranceType.PIPE, Location (1100, 30, -100), EntranceDest ("mac_02", [("mac_12", "aodokan_1", 176)]), EntranceKey (True, True, WelderBergPipe1.EXIST)),
            Entrance ("doa6_l", EntranceType.CHAPTERDOOR, Location (-450, 1500, -200), EntranceDest ("mac_02", [("he1_01", "doa1_l", 9), ("he2_01", "default", 58), ("he3_01", "default", 58), ("he4_01", "default", 58)]), EntranceKey (True, False, None)),
            Entrance ("doa8_l", EntranceType.CHAPTERDOOR, Location (-300, 1500, -200), EntranceDest ("mac_02", [("mi1_01", "doa2_l", 65), ("mi2_01", "default", 99), ("mi3_01", "default", 99), ("mi4_01", "default", 99)]), EntranceKey (True, False, None)),
            Entrance ("doa9_l", EntranceType.CHAPTERDOOR, Location (-150, 1500, -200), EntranceDest ("mac_02", [("ta1_01", "doa3_l", 100), ("ta2_01", "default", 127), ("ta3_01", "default", 127), ("ta4_01", "default", 127)]), EntranceKey (True, False, None)),
            Entrance ("doa10_l", EntranceType.CHAPTERDOOR, Location (0, 1500, -200), EntranceDest ("mac_02", [("sp1_01", "doa4_l", 134), ("sp2_01", "default", 175), ("sp3_01", "default", 175), ("sp4_01", "default", 175)]), EntranceKey (True, False, None)),
            Entrance ("doa11_l", EntranceType.CHAPTERDOOR, Location (150, 1500, -200), EntranceDest ("mac_02", [("gn1_01", "doa5_l", 177), ("gn2_01", "default", 222), ("gn3_01", "default", 222), ("gn4_01", "default", 222)]), EntranceKey (True, False, None)),
            Entrance ("doa12_l", EntranceType.CHAPTERDOOR, Location (300, 1500, -200), EntranceDest ("mac_02", [("wa1_01", "doa5_l", 222), ("wa1_27", "doa5_l", 281)]), EntranceKey (True, False, None)), # doa5_l is not a typo, also sequence is 224, but 222 is for people that do MCS
            Entrance ("doa11_l", EntranceType.CHAPTERDOOR, Location (150, 1500, -200), EntranceDest ("mac_02", [("an1_01", "doa7_l", 303), ("an2_01", "default", 355), ("an3_01", "default", 355), ("an4_01", "default", 355)]), EntranceKey (True, False, None)),
            Entrance ("elv1", EntranceType.ELEVATOR, Location (-700, 0, -250), EntranceDest ("mac_02", [("mac_09", "elv1", 53)]), EntranceKey (True, False, None)),
            Entrance ("elv2", EntranceType.ELEVATOR, Location (700, 0, -250), EntranceDest ("mac_02", [("mac_01", "elv1", 0)]), EntranceKey (True, False, None)),
            Entrance ("dearu_ie", EntranceType.DEFAULT, Location (0, 0, 0), None, EntranceKey (False, False, None))
        )
    ),
}