from enum import Enum

class ListType(Enum):
    DEBUG = 0
    ITEM = 1
    PARTY = 2
    CARD = 3
    MAP = 4

class ItemType(Enum):
    NONE = 0
    IMPORTANT = 1
    KEY = 2
    COOKINGDISK = 3
    CONSUMABLE = 4
    RECIPE = 5

class CardType(Enum):
    NONE = 0
    GROUND = 1
    SHOP = 2

class RecipeType(Enum):
    NONE = 0
    GROUND = 1
    GROUNDSINGLE = 2
    SINGLE = 3
    DOUBLEV = 4
    DOUBLE = 5

class MysteryBox(Enum):
    NONE = 0
    NO = 1
    YES = 2

class TMapType(Enum):
    NONE = 0
    ITEM = 1
    CARD = 2

class HexList:
    def __init__(self, name, hex, ListType, ItemType, CardType, RecipeType, MysteryBox, TMapType, BuyPrices, SellPrices):
        self.name = name
        self.hex = hex
        self.ListType = ListType
        self.ItemType = ItemType
        self.CardType = CardType
        self.RecipeType = RecipeType
        self.MysteryBox = MysteryBox
        self.TMapType = TMapType
        self.BuyPrices = BuyPrices
        self.SellPrices = SellPrices

class BuyPrice:
    def __init__(self, home_buy, yold_buy, crag_buy, space_buy, flip_itty, flop_itty, dot_itty, crag_itty, over_itty):
        self.home_buy = home_buy
        self.yold_buy = yold_buy
        self.crag_buy = crag_buy
        self.space_buy = space_buy
        self.flip_itty = flip_itty
        self.flop_itty = flop_itty
        self.dot_itty = dot_itty
        self.crag_itty = crag_itty
        self.over_itty = over_itty

class SellPrice:
    def __init__(self, home_sell, yold_sell, crag_sell):
        self.home_sell = home_sell
        self.yold_sell = yold_sell
        self.crag_sell = crag_sell

BigList = [
  HexList (
      "NULL",
      0x0,
      ListType.DEBUG,
      ItemType.NONE,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None)
  ),
  HexList (
      "undefined 0x1",
      0x1,
      ListType.DEBUG,
      ItemType.NONE,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None)
  ),
  HexList (
      "undefined 0x2",
      0x2,
      ListType.DEBUG,
      ItemType.NONE,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None)
  ),
  HexList (
      "undefined 0x3",
      0x3,
      ListType.DEBUG,
      ItemType.NONE,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None)
  ),
  HexList (
      "undefined 0x4",
      0x4,
      ListType.DEBUG,
      ItemType.NONE,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None)
  ),
  HexList (
      "undefined 0x5",
      0x5,
      ListType.DEBUG,
      ItemType.NONE,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None)
  ),
  HexList (
      "undefined 0x6",
      0x6,
      ListType.DEBUG,
      ItemType.NONE,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None)
  ),
  HexList (
      "undefined 0x7",
      0x7,
      ListType.DEBUG,
      ItemType.NONE,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None)
  ),
  HexList (
      "undefined 0x8",
      0x8,
      ListType.DEBUG,
      ItemType.NONE,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None)
  ),
  HexList (
      "undefined 0x9",
      0x9,
      ListType.DEBUG,
      ItemType.NONE,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None)
  ),
  HexList (
      "undefined 0xA",
      0xA,
      ListType.DEBUG,
      ItemType.NONE,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None)
  ),
  HexList (
      "undefined 0xC",
      0xB,
      ListType.DEBUG,
      ItemType.NONE,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None)
  ),
  HexList (
      "undefined 0xC",
      0xC,
      ListType.DEBUG,
      ItemType.NONE,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None)
  ),
  HexList (
      "undefined 0xD",
      0xD,
      ListType.DEBUG,
      ItemType.NONE,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None)
  ),
  HexList (
      "undefined 0xE",
      0xE,
      ListType.DEBUG,
      ItemType.NONE,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None)
  ),
  HexList (
      "undefined 0xF",
      0xF,
      ListType.DEBUG,
      ItemType.NONE,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None)
  ),
  HexList (
      "Ruins Key",
      0x10,
      ListType.ITEM,
      ItemType.KEY,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None)
  ),
  HexList (
      "Door Key",
      0x11,
      ListType.ITEM,
      ItemType.KEY,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None)
  ),
  HexList (
      "House Key",
      0x12,
      ListType.ITEM,
      ItemType.KEY,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None)
  ),
  HexList (
      "Fort Key",
      0x13,
      ListType.ITEM,
      ItemType.KEY,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None)
  ),
  HexList (
      "Fort Key",
      0x14,
      ListType.ITEM,
      ItemType.KEY,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None)
  ),
  HexList (
      "Fort Key",
      0x15,
      ListType.ITEM,
      ItemType.KEY,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None)
  ),
  HexList (
      "Goldfish Bowl",
      0x16,
      ListType.ITEM,
      ItemType.IMPORTANT,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None)
  ),
  HexList (
      "Goldfish Bowl", # Unused in game
      0x17,
      ListType.DEBUG,
      ItemType.IMPORTANT,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None)
  ),
  HexList (
      "Helmet",
      0x18,
      ListType.ITEM,
      ItemType.IMPORTANT,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None)
  ),
  HexList (
      "Ancient Clue",
      0x19,
      ListType.ITEM,
      ItemType.IMPORTANT,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None)
  ),
  HexList (
      "Door Key",
      0x1A,
      ListType.ITEM,
      ItemType.KEY,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None)
  ),
  HexList (
      "Dimension Key",
      0x1B,
      ListType.ITEM,
      ItemType.KEY,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None)
  ),
  HexList (
      "Dimension Key",
      0x1C,
      ListType.ITEM,
      ItemType.KEY,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None)
  ),
  HexList (
      "Dimension Key",
      0x1D,
      ListType.ITEM,
      ItemType.KEY,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None)
  ),
  HexList (
      "Water Tablet",
      0x1E,
      ListType.ITEM,
      ItemType.IMPORTANT,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None)
  ),
  HexList (
      "Stone Tablet",
      0x1F,
      ListType.ITEM,
      ItemType.IMPORTANT,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None)
  ),
  HexList (
      "Fire Tablet",
      0x20,
      ListType.ITEM,
      ItemType.IMPORTANT,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None)
  ),
  HexList (
      "Cave Key",
      0x21,
      ListType.ITEM,
      ItemType.KEY,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None)
  ),
  HexList (
      "Cave Key",
      0x22,
      ListType.ITEM,
      ItemType.KEY,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None)
  ),
  HexList (
      "Card Key",
      0x23,
      ListType.ITEM,
      ItemType.IMPORTANT,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None)
  ),
  HexList (
      "Floro Sprout",
      0x24,
      ListType.ITEM,
      ItemType.IMPORTANT,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None)
  ),
  HexList (
      "Door Key",
      0x25,
      ListType.ITEM,
      ItemType.KEY,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None)
  ),
  HexList (
      "Door Key",
      0x26,
      ListType.ITEM,
      ItemType.KEY,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None)
  ),
  HexList (
      "Diet Book",
      0x27,
      ListType.ITEM,
      ItemType.IMPORTANT,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None)
  ),
  HexList (
      "Door Key",
      0x28,
      ListType.ITEM,
      ItemType.KEY,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None)
  ),
  HexList (
      "Blue Orb",
      0x29,
      ListType.ITEM,
      ItemType.IMPORTANT,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None)
  ),
  HexList (
      "Yellow Orb",
      0x2A,
      ListType.ITEM,
      ItemType.IMPORTANT,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None)
  ),
  HexList (
      "Red Orb",
      0x2B,
      ListType.ITEM,
      ItemType.IMPORTANT,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None)
  ),
  HexList (
      "Pit Key",
      0x2C,
      ListType.ITEM,
      ItemType.KEY,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None)
  ),
  HexList (
      "undefined 0x2D",
      0x2D,
      ListType.DEBUG,
      ItemType.NONE,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None)
  ),
  HexList (
      "Castle Bleck Key",
      0x2E,
      ListType.ITEM,
      ItemType.KEY,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None)
  ),
  HexList (
      "Old Key",
      0x2F,
      ListType.ITEM,
      ItemType.KEY,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None)
  ),
  HexList (
      "Pit Key",
      0x30,
      ListType.ITEM,
      ItemType.KEY,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None)
  ),
  HexList (
      "Door Key",
      0x31,
      ListType.ITEM,
      ItemType.KEY,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None)
  ),
  HexList (
      "Return Pipe",
      0x32,
      ListType.ITEM,
      ItemType.IMPORTANT,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None)
  ),
  HexList (
      "Crystal Ball",
      0x33,
      ListType.ITEM,
      ItemType.IMPORTANT,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None)
  ),
  HexList (
      "Training Machine",
      0x34,
      ListType.ITEM,
      ItemType.IMPORTANT,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None)
  ),
  HexList (
      "You-Know-What",
      0x35,
      ListType.ITEM,
      ItemType.IMPORTANT,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None)
  ),
  HexList (
      "Paper",
      0x36,
      ListType.ITEM,
      ItemType.IMPORTANT,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None)
  ),
  HexList (
      "Autograph",
      0x37,
      ListType.ITEM,
      ItemType.IMPORTANT,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None)
  ),
  HexList (
      "Random House Key",
      0x38,
      ListType.ITEM,
      ItemType.KEY,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None)
  ),
  HexList (
      "Cooking Disk R",
      0x39,
      ListType.ITEM,
      ItemType.COOKINGDISK,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None)
  ),
  HexList (
      "Cooking Disk W",
      0x3A,
      ListType.ITEM,
      ItemType.COOKINGDISK,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None)
  ),
  HexList (
      "Cooking Disk Y",
      0x3B,
      ListType.ITEM,
      ItemType.COOKINGDISK,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None)
  ),
  HexList (
      "Cooking Disk B",
      0x3C,
      ListType.ITEM,
      ItemType.COOKINGDISK,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None)
  ),
  HexList (
      "Cooking Disk G",
      0x3D,
      ListType.ITEM,
      ItemType.COOKINGDISK,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None)
  ),
  HexList (
      "Cooking Disk PU",
      0x3E,
      ListType.ITEM,
      ItemType.COOKINGDISK,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None)
  ),
  HexList (
      "Cooking Disk PI", # Unused in game
      0x3F,
      ListType.DEBUG,
      ItemType.COOKINGDISK,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None)
  ),
  HexList (
      "Golden Card",
      0x40,
      ListType.ITEM,
      ItemType.IMPORTANT,
      CardType.NONE,
      RecipeType.NONE,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None),
      SellPrice(None, None, None)
  ),
  HexList (
      "Fire Burst",
      0x41,
      ListType.ITEM,
      ItemType.CONSUMABLE,
      CardType.NONE,
      RecipeType.GROUND,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(20, 7, 15, None, None, None, None, None, None),
      SellPrice(10, 4, 8)
  ),
  HexList (
      "Ice Storm",
      0x42,
      ListType.ITEM,
      ItemType.CONSUMABLE,
      CardType.NONE,
      RecipeType.GROUND,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(40, None, 25, None, None, None, None, None, None),
      SellPrice(20, 30, 13)
  ),
  HexList (
      "Thunder Rage",
      0x43,
      ListType.ITEM,
      ItemType.CONSUMABLE,
      CardType.NONE,
      RecipeType.GROUND,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(80, None, None, None, None, None, None, None, None),
      SellPrice(40, 100, 40)
  ),
  HexList (
      "Shooting Star",
      0x44,
      ListType.ITEM,
      ItemType.CONSUMABLE,
      CardType.NONE,
      RecipeType.GROUND,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None),
      SellPrice(80, 150, 80)
  ),
  HexList (
      "POW Block",
      0x45,
      ListType.ITEM,
      ItemType.CONSUMABLE,
      CardType.NONE,
      RecipeType.GROUND,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None),
      SellPrice(80, 150, 80)
  ),
  HexList (
      "Shell Shock",
      0x46,
      ListType.ITEM,
      ItemType.CONSUMABLE,
      CardType.NONE,
      RecipeType.GROUND,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(20, 8, None, None, None, None, None, None, None),
      SellPrice(10, 4, 10)
  ),
  HexList (
      "Gold Bar",
      0x47,
      ListType.ITEM,
      ItemType.CONSUMABLE,
      CardType.NONE,
      RecipeType.GROUND,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(100, None, None, None, None, None, None, None, None),
      SellPrice(90, 120, 115)
  ),
  HexList (
      "Gold Bar x3",
      0x48,
      ListType.ITEM,
      ItemType.CONSUMABLE,
      CardType.NONE,
      RecipeType.GROUND,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(300, None, None, None, None, None, None, None, None),
      SellPrice(300, 375, 350)
  ),
  HexList (
      "Block Block",
      0x49,
      ListType.ITEM,
      ItemType.CONSUMABLE,
      CardType.NONE,
      RecipeType.GROUND,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(50, None, None, None, None, None, None, None, None),
      SellPrice(25, 25, 25)
  ),
  HexList (
      "Courage Shell",
      0x4A,
      ListType.ITEM,
      ItemType.CONSUMABLE,
      CardType.NONE,
      RecipeType.GROUND,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(10, None, None, None, None, None, None, None, None),
      SellPrice(5, 13, 4)
  ),
  HexList (
      "Mighty Tonic",
      0x4B,
      ListType.ITEM,
      ItemType.CONSUMABLE,
      CardType.NONE,
      RecipeType.GROUND,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(70, None, None, None, None, None, None, None, None),
      SellPrice(35, 25, 35)
  ),
  HexList (
      "Volt Shroom",
      0x4C,
      ListType.ITEM,
      ItemType.CONSUMABLE,
      CardType.NONE,
      RecipeType.GROUND,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(30, None, None, None, None, None, None, None, None),
      SellPrice(15, 10, 15)
  ),
  HexList (
      "Ghost Shroom",
      0x4D,
      ListType.ITEM,
      ItemType.CONSUMABLE,
      CardType.NONE,
      RecipeType.GROUND,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(88, None, None, None, None, None, None, None, None),
      SellPrice(44, 44, 44)
  ),
  HexList (
      "Sleepy Sheep",
      0x4E,
      ListType.ITEM,
      ItemType.CONSUMABLE,
      CardType.NONE,
      RecipeType.GROUND,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(88, None, None, None, None, None, None, None, None),
      SellPrice(44, 44, 44)
  ),
  HexList (
      "Stop Watch",
      0x4F,
      ListType.ITEM,
      ItemType.CONSUMABLE,
      CardType.NONE,
      RecipeType.GROUND,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(50, None, None, None, None, None, None, None, None),
      SellPrice(25, 25, 25)
  ),
  HexList (
      "Shroom Shake",
      0x50,
      ListType.ITEM,
      ItemType.CONSUMABLE,
      CardType.NONE,
      RecipeType.GROUND,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(30, 11, 25, None, None, None, None, None, None),
      SellPrice(15, 11, 13)
  ),
  HexList (
      "Super Shroom Shake",
      0x51,
      ListType.ITEM,
      ItemType.CONSUMABLE,
      CardType.NONE,
      RecipeType.GROUND,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(80, None, 100, None, None, None, None, None, None),
      SellPrice(40, 40, 50)
  ),
  HexList (
      "Ultra Shroom Shake",
      0x52,
      ListType.ITEM,
      ItemType.CONSUMABLE,
      CardType.NONE,
      RecipeType.GROUND,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(300, None, None, None, None, None, None, None, None),
      SellPrice(150, 150, 150)
  ),
  HexList (
      "Dried Shroom",
      0x53,
      ListType.ITEM,
      ItemType.CONSUMABLE,
      CardType.NONE,
      RecipeType.GROUND,
      MysteryBox.NONE,
      TMapType.NONE,
      BuyPrice(None, None, None, None, None, None, None, None, None),
      SellPrice(1, 1, 1)
  ),
]

def searchList(name_or_id):
    try:
        input_as_int = int(name_or_id, 16)
    except ValueError:
        input_as_int = None

    matching_items = []
    for item in BigList:
        if item.name.lower() == name_or_id.lower() or (isinstance(item.hex, int) and item.hex == input_as_int):
            matching_items.append(item)

    return matching_items

with open ("bighexlist.py", "w") as f:
    f.write("bigList = " + repr(BigList))

while True:
    searchInput = input("Enter the item name or hex value: ").lower()
    results = searchList(searchInput)

    if not results:
        print("Item not found")
    else:
        if len(results) == 1:
            result = results[0]
        else:
            print("Multiple items found:")
            for i, item in enumerate(results):
                print(f"{i + 1}: {item.name}, 0x{item.hex:03X}")
            choice = input("Enter the number of the item you want: ")
            try:
                choice = int(choice)
                if choice < 1 or choice > len(results):
                    print("Invalid choice")
                    continue
                result = results[choice - 1]
            except ValueError:
                print("Invalid choice")
                continue

        print(f"Name: {result.name}")
        print(f"Hex: 0x{result.hex:03X}")
        print(f"ListType: {result.ListType.name}")
        print(f"ItemType: {result.ItemType.name}")
        print(f"CardType: {result.CardType.name}")
        print(f"RecipeType: {result.RecipeType.name}")
        print(f"MysteryBox: {result.MysteryBox.name}")
        print(f"TMapType: {result.TMapType.name}")
        print(f"BuyPrices: Home: {result.BuyPrices.home_buy}, Yold: {result.BuyPrices.yold_buy}, Crag: {result.BuyPrices.crag_buy}")
        print(f"SellPrices: Home: {result.SellPrices.home_sell}, Yold: {result.SellPrices.yold_sell}, Crag: {result.SellPrices.crag_sell}")
