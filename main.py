from ursina import *
# from classs import Block
from ursina.shaders import lit_with_shadows_shader, unlit_shader, basic_lighting_shader
from numpy import floor
import os

sprint = False # global boolean
stels = False

app = Ursina()

from models import Block
from obj import player

def update():
    player.gravity = 0.5
    global sprint
    global stels

    if held_keys['control'] and held_keys['w']:
        sprint = True
        player.speed = 7
        player.scale = 0.85

    elif held_keys['shift']:
        stels = True
        player.speed = 2
        player.scale = 0.75


    else: # check for button pressed while sprinting.
        sprint = False
        stels = True
        player.speed = 4.5
        player.scale = 0.85
        
Block.id = 0

window.fullscreen = True
app.run()