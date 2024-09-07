from ursina import *
from ursina.prefabs.first_person_controller import *
# from classs import Block
from ursina.shaders import lit_with_shadows_shader
from numpy import floor
from perlin_noise import PerlinNoise
import os

app = Ursina()

MAPSIZE = 10
BASE_DIR = os.getcwd()
IMG_DIR = os.path.join(BASE_DIR, 'assets/block_texture')

block_textures = []

file_list = os.listdir(IMG_DIR)
for image in file_list:
    texture = load_texture('assets/block_texture' + os.sep + image)
    block_textures.append(texture)

print(block_textures)

class Block(Button):
    id = 0 

    def __init__(self, pos, **kwargs):
        super().__init__(
            parent = scene,
            model = 'cube',
            texture=block_textures[Block.id],
            scale=1,
            collider='box',
            position=pos,
            color=color.color(0,0, random.uniform(0.95, 1)),
            origin_y=2.5,
            shader = lit_with_shadows_shader,
            **kwargs)
        
    def input(self, key):
        if self.hovered:
            d = distance(player, self)
            if key == 'left mouse down' and d < 9:
                destroy(self)

            if key == 'right mouse down' and d < 9:
                block = Block(self.position + mouse.normal)
            

            if key == 'scroll up':
                Block.id += 1  
                if len(block_textures) <= Block.id:
                    Block.id = 0          
            if key == 'scroll down':
                Block.id -= 1
                if Block.id < 0:
                    Block.id = len(block_textures)-1 

sky = Sky(texture = 'sky_sunset')
sun = DirectionalLight(shadows=True)
sun.look_at((Vec3(1,-1,1)))


player = FirstPersonController() # type: ignore

torch = Entity(model='assets/torch/scene.gltf', scale=0.1, collider='box')
torch.position = (0,0,0)

donat = Entity(model='assets/donat/donat_nodel.glb', scale=1,)
donat.position = (1,0.5,0)

sword = Entity(model='assets/sword/scene.gltf', scale=0.1, collider='box')
sword.position = (5,0,5)

noise = PerlinNoise(octaves=1, seed=2222)

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