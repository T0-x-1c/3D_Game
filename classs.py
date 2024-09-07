from ursina import *
from ursina import Default, camera
from ursina.prefabs.first_person_controller import *

class Block(Button):
    def __init__(self, pos, **kwargs):
        super().__init__(
            parent = scene,
            model = 'cube',
            texture='assets\\block_texture\\Gold_Ore_29_JE7_BE4.png',
            scale=1,
            collider='box',
            position=pos,
            color=color.white,
            **kwargs)