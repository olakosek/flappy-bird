import arcade
import pyglet
from scores import load_scores
from game import Game
from buttons import QuitButton, StartButton, SwitchViewButton, AvatarButton
pyglet.font.add_file("Kenney_Blocks.ttf")
pyglet.font.add_file("Kenney_Rocket_Square.ttf")
font_name = "Kenney Blocks"
style = {
            "normal": {"font_name": font_name,"font_size": 18,"font_color": arcade.color.FUCHSIA,"bg_color": arcade.color.DEEP_PINK,"border_color": arcade.color.WHITE,"border_width": 2,}, 
            "hover":{"font_name": font_name,"bg_color": arcade.color.LIGHT_PINK, "border_color": arcade.color.WHITE,},
            "press":{"font_name": font_name, "bg_color": arcade.color.PINK_LAVENDER ,"border_color": arcade.color.WHITE,}}
class Start(arcade.View):
    def on_show_view(self):
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        super().on_show_view()
        self.font_name = "Kenney Blocks"

        self.v_box = arcade.gui.UIBoxLayout()
        quit_button = QuitButton(text="EXIT", width=200, style = style)
        quit_button.style = style
        self.v_box.add(quit_button)

        start_button = StartButton(text="Click to Start", width=200, style = style, view=self)
        self.v_box.add(start_button)

        instruction_button = SwitchViewButton(text="HOW TO PLAY?", width=200, style = style, view=self, target_view=InstructionView)
        self.v_box.add(instruction_button)

        author_button = SwitchViewButton(text="ABOUT THE AUTHOR", width=200, style = style, view=self, target_view=AuthorView)
        self.v_box.add(author_button)

        scores_button = SwitchViewButton(text="BEST SCORES", width=200, style = style, view=self, target_view=ScoresView)
        self.v_box.add(scores_button)

        avatar_button = SwitchViewButton(text="CHOOSE AVATAR", width=200, style = style, view=self, target_view=AvatarView)
        self.v_box.add(avatar_button)

        self.window.set_mouse_visible(True)
        self.background_color = arcade.csscolor.FUCHSIA
        self.anchor_layout = arcade.gui.UIAnchorLayout()
        self.manager.add(self.anchor_layout)
        self.anchor_layout.add(child=self.v_box, anchor_x="center_x", anchor_y="center_y")
    def on_draw(self):
        self.clear()
        arcade.draw_lrbt_rectangle_filled(0.97*(self.window.width // 4), (self.window.width // 4)*3, self.window.height // 4.6, self.window.height // 1.2, arcade.color.DEEP_PINK)
        self.manager.draw()
    def on_hide_view(self):
        self.manager.disable()
        super().on_hide_view()

class InstructionView(arcade.View):
    def __init__(self):
        super().__init__()
        self.font_name = "Kenney Blocks"
        self.next_font = "Kenney Rocket Square"
        self.background_color = arcade.color.LIGHT_DEEP_PINK
        self.head_text = arcade.Text("HOW TO PLAY?",640,630,arcade.color.FUCHSIA,font_size=50,anchor_x="center", font_name = self.font_name)
        instructions = ("1. Press space to start. \n"
                        "2. Avoid hitting the pipes, while collecting coins. \n"
                        "3. Remember that you cannot touch the ground or the top of the screen. \n"
                        "4. If you do the game starts from the beginning. \n")
        self.instructions_text = arcade.Text(instructions,640,500,arcade.color.PINK_PEARL,font_size=24,anchor_x="center", anchor_y="top", font_name = self.next_font, width=1050, align="left", multiline=True)
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.v_box = arcade.gui.UIBoxLayout()
        start_button = SwitchViewButton(text="go back",width = 300, style = style, view=self, target_view=Start)
        self.v_box.add(start_button)
        self.anchor_layout = arcade.gui.UIAnchorLayout()
        self.manager.add(self.anchor_layout)
        self.anchor_layout.add(child=self.v_box, anchor_x="left", anchor_y="top")

    def on_show_view(self):
        self.manager.enable()
    def on_draw(self):
        self.clear()
        arcade.draw_lrbt_rectangle_filled(self.window.width // 12, self.window.width // 1.1, self.window.height // 4.6, self.window.height // 1.2, arcade.color.DEEP_PINK)
        self.head_text.draw()
        self.instructions_text.draw()
        self.manager.draw()

class AuthorView(arcade.View):
    def on_show_view(self):
        self.font_name = "Kenney Blocks"
        self.next_font = "Kenney Rocket Square"
        self.background_color = arcade.color.LIGHT_DEEP_PINK
        self.head_text = arcade.Text("ABOUT THE AUTHOR",640,630,arcade.color.FUCHSIA,font_size=40,anchor_x="center", font_name = self.font_name)
        author = ("Aleksandra Kosek is an aspiring applied mathematics student who is entering the world of programming with her first game — a personal version of the popular 'Flappy Bird'.")
        self.author_text = arcade.Text(author, 640,500,arcade.color.PINK_PEARL,font_size=24,anchor_x="center", anchor_y="top", font_name = self.next_font, width=1050, align="left", multiline=True)
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.v_box = arcade.gui.UIBoxLayout()
        start_button = SwitchViewButton(text="go back",width = 300, style = style, view=self, target_view=Start)
        self.v_box.add(start_button)
        self.anchor_layout = arcade.gui.UIAnchorLayout()
        self.manager.add(self.anchor_layout)
        self.anchor_layout.add(child=self.v_box, anchor_x="left", anchor_y="top")
    def on_draw(self):
        self.clear()
        arcade.draw_lrbt_rectangle_filled(self.window.width // 12, self.window.width // 1.1, self.window.height // 4.6, self.window.height // 1.2, arcade.color.DEEP_PINK)
        self.head_text.draw()
        self.author_text.draw()  
        self.manager.draw()    

class ScoresView(arcade.View):
    def on_show_view(self):
        self.font_name = "Kenney Blocks"
        self.next_font = "Kenney Rocket Square"
        self.background_color = arcade.color.LIGHT_DEEP_PINK
        self.head_text = arcade.Text("BEST SCORES!",640,630,arcade.color.FUCHSIA,font_size=50,anchor_x="center", font_name = self.font_name)
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.v_box = arcade.gui.UIBoxLayout()
        start_button = SwitchViewButton(text="go back",width = 300, style = style, view=self, target_view=Start)
        self.v_box.add(start_button)

        self.anchor_layout = arcade.gui.UIAnchorLayout()
        self.manager.add(self.anchor_layout)
        self.anchor_layout.add(child=self.v_box, anchor_x="left", anchor_y="top")
    def on_draw(self):
        self.clear()
        self.head_text.draw()
        self.manager.draw()
        arcade.draw_lrbt_rectangle_filled(0.97*(self.window.width // 4), (self.window.width // 4)*3, self.window.height // 4.6, self.window.height // 1.2, arcade.color.DEEP_PINK)
        i=0
        for score in load_scores():
            self.score_text = arcade.Text(f'{i+1}. {score}', 640,580-30*i,arcade.color.PINK_PEARL,font_size=24,anchor_x="center", anchor_y="top", font_name = self.next_font, align="left")
            i+= 1
            self.score_text.draw()
            
class AvatarView(arcade.View):
    def __init__(self):
        self.points = sum(load_scores())
        super().__init__()
        self.font_name = "Kenney Blocks"
        self.head_text = None
        self.error3 = False
        self.error4 = False
        self.error_message = ""
        self.error_timer = 0

        self.manager = arcade.gui.UIManager()
        self.manager1 = arcade.gui.UIManager()

        self.v_box = arcade.gui.UIBoxLayout()
        self.anchor_layout = arcade.gui.UIAnchorLayout()

        self.v_box2 = arcade.gui.UIBoxLayout()
        self.anchor_layout1 = arcade.gui.UIAnchorLayout()


    def on_show_view(self):
        i = 1
        self.background_color = arcade.color.LIGHT_DEEP_PINK
        self.head_text = arcade.Text("CHOSE YOUR AVATAR",640,630,arcade.color.FUCHSIA,font_size=40,anchor_x="center", font_name = self.font_name)
        self.manager.enable()
        self.v_box = arcade.gui.UIBoxLayout()

        for avatar_path in ["flappy.png", "flappy2.png", "flappy3.png", "flappy4.png"]:
            if i<3:
                button = AvatarButton(image=avatar_path, on_select=lambda path=avatar_path: self.start_game(path))
            elif i == 3:
                if self.points >=100:
                    button = AvatarButton(image=avatar_path, on_select=lambda path=avatar_path: self.start_game(path))
                else:
                    button = AvatarButton(image=avatar_path, on_select=lambda path=avatar_path: self.show_error(100))
            else:
                if self.points >=200:
                    button = AvatarButton(image=avatar_path, on_select=lambda path=avatar_path: self.start_game(path))
                else:
                    button = AvatarButton(image=avatar_path,on_select=lambda path=avatar_path: self.show_error(200))
            self.v_box.add(button)
            i+=1

        self.anchor_layout = arcade.gui.UIAnchorLayout()
        self.manager.add(self.anchor_layout)
        self.anchor_layout.add(child=self.v_box, anchor_x="center_x", anchor_y="center_y")
        
        self.manager1.enable()
        self.v_box2 = arcade.gui.UIBoxLayout()
        start_button = SwitchViewButton(text="go back",width = 300, style = style, view=self, target_view=Start)
        self.v_box2.add(start_button)

        self.anchor_layout1 = arcade.gui.UIAnchorLayout()
        self.manager1.add(self.anchor_layout1)
        self.anchor_layout1.add(child=self.v_box2, anchor_x="left", anchor_y="top")

    def start_game(self, avatar_path):
        game_view = Game(selected_avatar = avatar_path)
        game_view.setup()
        self.window.show_view(game_view)

    def show_error(self, required_points):
        if required_points == 100:
            self.error3 = True
        elif required_points == 200:
            self.error4 = True
        self.error_timer = 180
    
    def on_draw(self):
        self.clear()
        arcade.draw_lrbt_rectangle_filled(0.97*(self.window.width // 4), (self.window.width // 4)*3, self.window.height // 4.6, self.window.height // 1.2, arcade.color.DEEP_PINK)
        if self.head_text:
            self.head_text.draw()  
        self.manager.draw()  
        if self.points<100:
            arcade.draw_text("🔒", 645, 313, arcade.color.WHITE, 24, anchor_x="center", anchor_y="center")
        if self.points<200:
            arcade.draw_text("🔒", 645, 213, arcade.color.WHITE, 24, anchor_x="center", anchor_y="center")
        self.manager1.draw() 
        arcade.draw_lrbt_rectangle_filled(1100, 1280, 650, 720, arcade.color.YANKEES_BLUE)
        text_points = arcade.Text(f"YOUR POINTS: {self.points}", 1140, 680, color = arcade.color.FUCHSIA, font_size = 10, font_name = font_name)
        text_points.draw()
        if self.error3 or self.error4:
            arcade.draw_lrbt_rectangle_filled(300, 970, 300, 500, arcade.color.RED_BROWN)
            arcade.draw_text("AVATAR UNAVAILABLE!", self.window.width // 2, self.window.height // 2 + 40, arcade.color.RED_DEVIL, 37, anchor_x="center", font_name=font_name)
            if self.error3:
                arcade.draw_text(f"You need to gain: {100-self.points} POINT", self.window.width // 2 , self.window.height // 2 , arcade.color.WHITE_SMOKE, 20, anchor_x="center", font_name=self.font_name)
            else:
                arcade.draw_text(f"You need to gain: {200-self.points} POINTS", self.window.width // 2 , self.window.height // 2 , arcade.color.WHITE_SMOKE, 20, anchor_x="center", font_name=self.font_name)
    def on_update(self, delta_time):
        if self.error3 or self.error4:
            self.error_timer -= 1
            if self.error_timer <= 0:
                self.error3 = False
                self.error4 = False

