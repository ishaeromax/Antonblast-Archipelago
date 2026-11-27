from worlds.AutoWorld import World

# TODO: locations not yet done
from . import items, locations

class AntonblastAPWorld(World):
    # Haero TODO: Change this later when we have a proper good description for the APWORLD class.
    """
    ANTONBLAST is a fast-paced explosive action platformer that's all about destruction.
    Play as the enraged Dynamite Anton (or his cranked-out coworker Annie) 
    and use your Mighty n Hammer to demolish bizarre worlds, tussle with 
    screen-filling bosses, and steal your Spirits back from Satan!
    """

    # Name of the game.
    game = "ANTONBLAST"

    # Set item_name_to_id to the ANTONBLAST_ITEMS_NAME_TO_ID that we have in items. 
    item_name_to_id = items.ANTONBLAST_ITEMS_NAME_TO_ID

    # Set item_name_groups to the ANTONBLAST_ITEMS_GROUPS that we have in items.
    item_name_groups = items.ANTONBLAST_ITEMS_GROUPS

    # TODO: locations not yet done
    # Empty for now.
    location_name_to_id = {}