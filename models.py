from ursina import *
from ursina.shaders import lit_with_shadows_shader, unlit_shader, basic_lighting_shader
from setting import *
from perlin_noise import PerlinNoise
from random import randint

class Tree(Entity):
    def __init__(self, pos, parent_world, **kwargs):
        super().__init__(
            parent = parent_world,
            model = 'assets\\tree\\scene',
            scale=6,
            collider='box',
            position=pos,
            origin_y=1,
            shader = SHADER,
            **kwargs)
        

class Block(Button):
    id = 0 

    def __init__(self, pos, parent_world, **kwargs):
        super().__init__(
            parent = parent_world,
            model = 'cube',
            texture=block_textures[Block.id],
            scale=1,
            collider='box',
            position=pos,
            color=color.color(0,0, random.uniform(0.95, 1)),
            origin_y=2.5,
            shader = SHADER,
            **kwargs)
        

class Chunk(Entity):
    def __init__(self, chunk_pos, **kwargs):
        super().__init__(**kwargs, model = None, collider = None, shader = SHADER)
        self.chunk_pos = chunk_pos
        self.blocks = {}
        self.noise = PerlinNoise(octaves=1, seed=3504)
        self.layers = 3
        self.generate_chunk()

    def generate_chunk(self):
        Block.id = 0
        cx, cz = self.chunk_pos
        for i in range(self.layers):
            print(i)
            if i >= 2:
                Block.id = 4
            for x in range(CHUNKSIZE):
                for z in range(CHUNKSIZE):
                    block_x = cx * CHUNKSIZE + x
                    block_z = cz * CHUNKSIZE + z

                    y = floor(self.noise([block_x/24, block_z/24])*6)-i
                    block = Block((block_x,y,block_z), self)
                    self.blocks[(block_x,y,block_z)] = block

                    rand_num = randint(1,140)
                    if rand_num == 52:
                        tree = Tree((block_x,y+1,block_z), self)



class WorldEdit(Entity):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.chunks = {}
        self.current_chunk = None

    def generate_world(self):
            for x in range(WORLDSIZE):
                for z in range(WORLDSIZE):
                    chunk_pos = (x,z)
                    if chunk_pos not in self.chunks:
                        chunk = Chunk(chunk_pos)
                        self.chunks[chunk_pos] = chunk

    def input(self, key):
        if key == 'right mouse down':
            hit_info = raycast(camera.world_position, camera.forward, distance=10)
            if hit_info.hit:
                block = Block(hit_info.entity.position + hit_info.normal, self)
        if key == 'left mouse down' and mouse.hovered_entity:
            hit_info = raycast(camera.world_position, camera.forward, distance=10)
            if hit_info.hit:
                destroy(mouse.hovered_entity)

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


mini_block = Entity(parent = camera,
                    model = 'cube',
                    color=color.color(0,0, 1),
                    texture=block_textures[Block.id],
                    scale = 0.11,
                    position=(0.25, -0.13, 0.25),
                    rotation = Vec3(3, -32, 3),
                    shader = unlit_shader)