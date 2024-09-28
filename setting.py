import os
from ursina import load_texture 
from ursina.shaders import lit_with_shadows_shader, unlit_shader, basic_lighting_shader


CHUNKSIZE = 4
WORLDSIZE = 30
DATAILDISTANCE = 20
BASE_DIR = os.getcwd()
IMG_DIR = os.path.join(BASE_DIR, 'assets/block_texture')
SHADER = basic_lighting_shader

block_textures = []

file_list = os.listdir(IMG_DIR)
for image in file_list:
    texture = load_texture('assets/block_texture' + os.sep + image)
    block_textures.append(texture)