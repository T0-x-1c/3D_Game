from ursina import *
from ursina.prefabs.first_person_controller import *
# from classs import Block

from numpy import floor
from perlin_noise import PerlinNoise

app = Ursina()

MAPSIZE = 30

class Block(Button):
    def __init__(self, pos, **kwargs):
        super().__init__(
            parent = scene,
            model = 'cube',
            texture='assets\\block_texture\\Gold_Ore_29_JE7_BE4.png',
            scale=1,
            collider='box',
            position=pos,
            color=color.color(0,0, random.uniform(0.8, 1)),
            origin_y=2.5,
            **kwargs)

sky = Sky(texture = 'sky_sunset')
player = FirstPersonController() # type: ignore

torch = Entity(model='assets/torch/scene.gltf', scale=0.1, collider='box')
torch.position = (0,0,0)

donat = Entity(model='assets/donat/donat_nodel.glb', scale=1,)
donat.position = (1,0.5,0)

sword = Entity(model='assets/sword/scene.gltf', scale=0.1, collider='box')
sword.position = (5,0,5)

noise = PerlinNoise(octaves=2, seed=random.uniform(1000,10000))

for x in range(-MAPSIZE, MAPSIZE):
    for z in range(-MAPSIZE, MAPSIZE):
        y = floor(noise([x/24, z/24])*6)
        block = Block((x,y,z))


# ground = Entity(model='quad', texture = 'grass', scale = 64, texture_scale=(128,128),
#                 rotation = 90, position=(0,0,0), collider='box')


# EditorCamera()  # add camera controls for orbiting and moving the camera

# def input(key):
#     if key == "left mouse down":
#         cube.x += 1

window.fullscreen = True
app.run()