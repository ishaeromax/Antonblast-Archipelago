from BaseClasses import Item, ItemClassification

# I use dataclasses here so i import it too.
from dataclasses import dataclass

# I am going to use enums here so i will import it.
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
}

class AntonblastAPItem(Item):
    game = "ANTONBLAST"

    