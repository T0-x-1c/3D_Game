from ursina import *
from ursina.prefabs.first_person_controller import *
from ursina.shaders import lit_with_shadows_shader, unlit_shader, basic_lighting_shader
from setting import *
from models import Block, WorldEdit

player = FirstPersonController() # type: ignore
player.y += 25

# snowman = Entity(model='models_compressed/snowman/scene.gltf', parent=player)  # Прив'язуємо до гравця
# snowman.rotation = Vec3(0, 90, 0)  # Повертаємо модель на 90 градусів
# snowman.visible = False

# player.collider = 'box'
player.scale = 0.85
player.speed = 4.5
player.jump_height = 1.5
player.gravity = 0.5

camera.fov=origFOV=110
# camera.position = (0, 0.8, 0)  # Камера на рівні голови
# camera.parent = player  # Прив'язуємо камеру до гравця


donat = Entity(model='assets/donat/donat_nodel.glb', scale=1,)
donat.position = (1,1,0)

sword = Entity(model='assets/sword/scene.gltf', scale=0.1, collider='box')
sword.position = (5,0,5)

sky = Sky(texture = 'sky_sunset')
sun = DirectionalLight(shadows=True)
sun.look_at(Vec3(1, -1, 1))

world = WorldEdit()
world.generate_world()
