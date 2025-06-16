import arcade
import arcade.gui
from game import Game

class QuitButton(arcade.gui.UIFlatButton):
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        arcade.exit()

class StartButton(arcade.gui.UIFlatButton):
    def __init__(self, *, view, **kwargs):
        super().__init__(**kwargs)
        self.view = view
    def on_click(self,event: arcade.gui.UIOnClickEvent):
        game_view = Game()
        game_view.setup()
        self.view.window.show_view(game_view)

class SwitchViewButton(arcade.gui.UIFlatButton):
    def __init__(self, *, view, target_view, **kwargs):
        super().__init__(**kwargs)
        self.view = view
        self.target_view = target_view
    def on_click(self,event: arcade.gui.UIOnClickEvent):
        new_view = self.target_view()
        self.view.window.show_view(new_view)

class AvatarButton(arcade.gui.UITextureButton):
    def __init__(self, image, on_select = None, width=100, height=100, text=""):
        self.image_path = image
        self.on_select = on_select
        self.image = arcade.load_texture(image)
        super().__init__(texture=self.image, width=width, height=height)
    def on_click(self,event: arcade.gui.UIOnClickEvent):
        if self.on_select:
            self.on_select(self.image_path)
        