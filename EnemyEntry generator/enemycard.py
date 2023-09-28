from enum import Enum
import os

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define the relative path to 'enemycard.txt' based on the new working directory
file_name = 'enemycard.txt'

# Change the working directory to the "EnemyEntry generator" folder
os.chdir(script_dir)

# Now, the working directory is set to the "EnemyEntry generator" folder
print("Current Working Directory:", os.getcwd())

# Read the text file and parse item entries
item_entries = []

with open(file_name, 'r') as file:
    lines = file.readlines()

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
    VANILLA = 4
    RECIPE = 5
    CARD = 6

class CardType(Enum):
    NONE = 0
    GROUND = 1
    SHOP = 2

class RecipeType(Enum):
    NONE = 0
    USELESS = 1
    GROUND = 2
    SINGLE = 3
    DOUBLE = 4

class MysteryBox(Enum):
    NO = 0
    YES = 1

class TMapType(Enum):
    NONE = 0
    ITEM = 1
    CARD = 2

class ItemEntry:
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

    def __repr__(self):
        return f'ItemEntry (\n' \
               f'    "{self.name} Card",\n' \
               f'    {self.hex},\n' \
               f'    ListType.{self.ListType.name},\n' \
               f'    ItemType.{self.ItemType.name},\n' \
               f'    CardType.{self.CardType.name},\n' \
               f'    RecipeType.{self.RecipeType.name},\n' \
               f'    MysteryBox.{self.MysteryBox.name},\n' \
               f'    TMapType.{self.TMapType.name},\n' \
               f'    BuyPrice(None, None, None, None, None, None, None, None, None, None, None, {self.BuyPrices.card_shop}, None),\n' \
               f'    SellPrice(None, None, None, {self.SellPrices.card_sell})\n' \
               f'),'

class BuyPrice:
    def __init__(self, flip_buy, flop_buy, yold_buy, crag_buy, space_buy, flip_itty, flop_itty, dot_itty, crag_itty, over_itty, cardbag_shop, card_shop, map_shop):
        self.flip_buy = flip_buy
        self.flop_buy = flop_buy
        self.yold_buy = yold_buy
        self.crag_buy = crag_buy
        self.space_buy = space_buy
        self.flip_itty = flip_itty
        self.flop_itty = flop_itty
        self.dot_itty = dot_itty
        self.crag_itty = crag_itty
        self.over_itty = over_itty
        self.cardbag_shop = cardbag_shop
        self.card_shop = card_shop
        self.map_shop = map_shop

class SellPrice:
    def __init__(self, home_sell, yold_sell, crag_sell, card_sell):
        self.home_sell = home_sell
        self.yold_sell = yold_sell
        self.crag_sell = crag_sell
        self.card_sell = card_sell

item_data = {}
item_number = None

for line in lines:
    line = line.strip()
    if line.startswith("Item "):
        if item_data:
            name_message = item_data.get("Name Message", "")
            name = name_message.split('(')[-1].strip()[:-1]
            hex_value = f"0x{item_number:X}" if item_number is not None else "0x0"
            buy_price = int(item_data.get("Buy Price", "0").split()[-1])
            sell_price = int(item_data.get("Sell Price", "0").split()[-1])
            buy_prices = BuyPrice(None, None, None, None, None, None, None, None, None, None, None, buy_price, None)
            sell_prices = SellPrice(None, None, None, sell_price)
            item_entry = ItemEntry(
                name,
                hex_value,
                ListType.CARD,
                ItemType.CARD,
                CardType.NONE,
                RecipeType.NONE,
                MysteryBox.NO,
                TMapType.NONE,
                buy_prices,
                sell_prices
            )
            item_entries.append(item_entry)
        item_data = {}  # Reset item_data for the next item
        item_number = int(line.split()[-1].rstrip(":"))
    else:
        key, value = map(str.strip, line.split(":", 1))
        item_data[key] = value

print("Results:")
output_file_name = "Card_Output.txt"

with open(output_file_name, 'w') as output_file:
    for item_entry in item_entries:
        output_file.write(repr(item_entry) + '\n')

print(f'Item entries exported to {output_file_name}')