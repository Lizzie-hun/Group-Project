import globals
import arcade
# Constants
SCREEN_WIDTH = globals.SCREEN_WIDTH
SCREEN_HEIGHT = globals.SCREEN_HEIGHT
SCREEN_TITLE = "Dino Run"
TILE_SCALING = 0.5


# Map name
map1_name = "Map/map1..tmj"
map2_name = "Map/Map2.tmj"
map_list = [map1_name, map2_name]

# Layer Names from our TileMap
LAYER_NAME_PLATFORMS = "Platforms"
LAYER_NAME_FLOOR = "Floor"
LAYER_NAME_CHECKPOINT = "Checkpoint"

LAYER_NAME_FOREGROUND = "Foreground"
LAYER_NAME_BACKGROUND = "Background"


class Map(arcade.TileMap):
    
    def __init__(self):

    # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.tile_map = None
        self.scene = None
    
    def setup(self):

        # Layer Specific Options for the Tilemap
        layer_options = {
            LAYER_NAME_PLATFORMS: {
                "use_spatial_hash": True,
            },
            LAYER_NAME_FLOOR: {
                "use_spatial_hash": True,
            },
            LAYER_NAME_CHECKPOINT: {
                "use_spatial_hash": True,
            },
        }

        # Load in TileMap
        self.tile_map = arcade.load_tilemap(map1_name, TILE_SCALING, layer_options)

        # # Initiate New Scene with our TileMap, this will automatically add all layers
        # # from the map as SpriteLists in the scene in the proper order.

        self.scene = arcade.Scene.from_tilemap(self.tile_map)

    def layering_options():
        layer_options = {
            LAYER_NAME_PLATFORMS: {
                "use_spatial_hash": True,
            },
            LAYER_NAME_FLOOR: {
                "use_spatial_hash": True,
            },
            LAYER_NAME_CHECKPOINT: {
                "use_spatial_hash": True,
            },
        }
        return layer_options