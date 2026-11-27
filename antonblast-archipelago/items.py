from BaseClasses import Item, ItemClassification

# I will keep imports simple tbh
from dataclasses import dataclass
from enum import Enum

# Enumerator of the items groups, you can add more groups here.
class AntonblastItemGroup(Enum):
    SPIRITS = "Spirits"
    LEVEL_KEYS = "Level Keys"
    TRASH = "Trash"
    VINYLS = "Vinyls"
    SPRAYS = "Sprays"
    POWER_UPS = "Power Ups"
    CHIPS = "Chips"

# Enumerator of the Item Classifications so i have alias for them so its more simple. (i guess)
class AntonblastItemClassification(Enum):
    FILLER = ItemClassification.filler
    USEFUL = ItemClassification.useful
    PROGRESSION = ItemClassification.progression
    TRAP = ItemClassification.trap

# A dataclass for the item data for the items in Antonblast.
@dataclass(frozen=True)
class AntonblastItemData:
    itemName: str
    itemID: int
    itemGroup: AntonblastItemGroup
    itemClassification: AntonblastItemClassification

# Here you can set the antonblast items with AntonblastItemData.
ANTONBLAST_ITEMS = {
    AntonblastItemData("500 Chips", 1, AntonblastItemGroup.CHIPS, AntonblastItemClassification.FILLER),
    AntonblastItemData("1000 Chips", 2, AntonblastItemGroup.CHIPS, AntonblastItemClassification.FILLER),
    AntonblastItemData("1500 Chips", 3, AntonblastItemGroup.CHIPS, AntonblastItemClassification.FILLER),
}

# This dictionary gets all the item names with their respective IDs.
ANTONBLAST_ITEMS_NAME_TO_ID: dict[str, int] = {}

# This dictionary gets all the classifications of the items.
ANTONBLAST_ITEMS_CLASSIFICATIONS: dict[str, ItemClassification] = {}

# This dictionary gets the group name with their respective items names.
ANTONBLAST_ITEMS_GROUPS: dict[str, set[str]] = {}

# Do a for in the items of ANTONBLAST_ITEMS so we can assign to the
# dictionaries their respective values from the AntonblastItemData.
for item in ANTONBLAST_ITEMS:
    # Set the items names with their itemID to ANTONBLAST_ITEMS_NAME_TO_ID. 
    ANTONBLAST_ITEMS_NAME_TO_ID[item.itemName] = item.itemID

    # Set the items names with their itemClassification.value 
    # (So we get the ItemClassification value instead of the enum) to ANTONBLAST_ITEMS_CLASSIFICATIONS
    ANTONBLAST_ITEMS_CLASSIFICATIONS[item.itemName] = item.itemClassification.value

    # Checks if the group is on the ANTONBLAST_ITEMS_GROUPS, if not we set the group on the ANTONBLAST_ITEMS_GROUPS.
    if item.itemGroup.value not in ANTONBLAST_ITEMS_GROUPS:
        ANTONBLAST_ITEMS_GROUPS[item.itemGroup.value] = set()

    # Add the item to the already existing group in ANTONBLAST_ITEMS_GROUPS.
    ANTONBLAST_ITEMS_GROUPS[item.itemGroup.value].add(item.itemName)

class AntonblastAPItem(Item):
    game = "ANTONBLAST"

    