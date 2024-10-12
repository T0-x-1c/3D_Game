from ursina import *
from ursina import Default, camera

Text.default_font = 'assets/F77MinecraftRegular-0VYv.ttf'

class Menu_Button(Button):
    def __init__(self, text, action, x, y, parent, **kwargs):
        super().__init__(text, on_click=action, x=x, y=y, parent=parent,
                        scale = (0.6, 0.1),
                        texture='assets\\block_texture\\5.png', 
                        origin = (0,0), ignore_paused = True,
                        color=color.color(0,0, random.uniform(0.9, 1)),
                        highlight_color=color.gray,
                        highlight_scale=1.05,
                        **kwargs)


class Menu(Entity):
    def __init__(self, game, **kwargs):
        super().__init__(parent = camera.ui, ignore_paused = True,**kwargs)

        self.bg = Sprite(texture='assets\\background.png', z=1, color=color.white, scale = 1.3)
        self.title = Text(text="UrsinaCruft", scale = 4, parent=self, origin = (0,0), x = 0, y = 0.35)

        background_music = Audio('bg_music.mp3', volume=0.3, loop=True, autoplay=True)

        Menu_Button("Quit", application.quit, 0, -0.26, self)
        Menu_Button("New Game", application.quit, 0, -0.13, self)
        Menu_Button("Load Game", application.quit, 0, 0, self)
        Menu_Button("Save Game", application.quit, 0, 0.13, self)


if __name__ == "__main__":
    app = Ursina()
    menu = Menu(app)
    app.run()