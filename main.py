from ursina import *
from ursina.prefabs.first_person_controller import *
# from classs import Block
from ursina.shaders import lit_with_shadows_shader, unlit_shader
from numpy import floor
from perlin_noise import PerlinNoise
import os

sprint = False # global boolean

def update():
    global sprint

    if held_keys['control'] and held_keys['w']:
        sprint = True
        player.speed = 7

    if sprint and not held_keys['w']: # check for button pressed while sprinting.
        sprint = False
        player.speed = 4.5

app = Ursina()

MAPSIZE = 12
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
                    
                mini_block.texture=block_textures[Block.id]   

            if key == 'scroll down':
                Block.id -= 1
                if Block.id < 0:
                    Block.id = len(block_textures)-1 

                mini_block.texture=block_textures[Block.id]

sky = Sky(texture = 'sky_sunset')
sun = DirectionalLight(shadows=True)
sun.look_at(Vec3(1, -1, 1))

player = FirstPersonController() # type: ignore
player.y += 15
camera.fov=origFOV=110

# player.model = load_model("assets/steve/stay.gltf.glb")
# player.model.z -= 5
# player.collider = 'box'
player.scale_y = .9
player.scale_x = .9	
player.speed = 4.5

mini_block = Entity(parent = camera,
                    model = 'cube',
                    color=color.color(0,0, 1),
                    texture=block_textures[Block.id],
                    scale = 0.11,
                    position=(0.25, -0.13, 0.25),
                    rotation = Vec3(3, -32, 3),
                    shader = unlit_shader)

donat = Entity(model='assets/donat/donat_nodel.glb', scale=1,)
donat.position = (1,0.5,0)

sword = Entity(model='assets/sword/scene.gltf', scale=0.1, collider='box')
sword.position = (5,0,5)

noise = PerlinNoise(octaves=1, seed=random.uniform(1000, 10000))

def createmap(layers):
    for i in range(layers):
        print(i)
        if i >= 1:
            Block.id = 4
        for x in range(-MAPSIZE, MAPSIZE):
            for z in range(-MAPSIZE, MAPSIZE):
                y = floor(noise([x/24, z/24])*6)-i
                block = Block((x,y,z))

createmap(layers=1)

# ground = Entity(model='quad', texture = 'grass', scale = 64, texture_scale=(128,128),
#                 rotation = 90, position=(0,0,0), collider='box')


# EditorCamera()  # add camera controls for orbiting and moving the camera

# def input(key):
#     if key == "left mouse down":
#         cube.x += 1

window.fullscreen = True
app.run()