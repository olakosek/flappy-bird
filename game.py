import arcade
import random
from scores import add_score
font_name = "Kenney Blocks"
PLAYER_MOVEMENT_SPEED = 5
GRAVITY = 1
PLAYER_JUMP = 20
class Game(arcade.View):
    
    def __init__(self, selected_avatar="flappy.png"):
        super().__init__()
        self.selected_avatar = selected_avatar
        self.game_started = False
        self.game_over = False
        self.player_texture = None
        self.scene = None
        self.camera = None
        self.gui_camera = None
        self.score_text = None
        self.score = 0
        self.level = 1
        self.collect_coin_sound = arcade.load_sound(":resources:sounds/coin5.wav")
        self.jump_sound = arcade.load_sound(":resources:sounds/jump2.wav")
        self.game_over_sound = arcade.load_sound(":resources:sounds/gameover2.wav")
    
    def setup(self):
        self.game_started = False
        self.game_over = False
        self.scene = arcade.Scene()
        self.background_color = arcade.csscolor.HOTPINK
        self.score_text = arcade.Text(f"Score: {self.score}",5,700)
        self.player_sprite = arcade.Sprite(self.selected_avatar, scale=0.1)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 360
        self.scene.add_sprite("Player", self.player_sprite)
        self.scene.add_sprite_list("Walls", use_spatial_hash=True)
        self.scene.add_sprite_list("Coins", use_spatial_hash=True)
        self.scene.add_sprite_list("Pipes", use_spatial_hash=True)
        sign= arcade.Sprite(":resources:images/tiles/signRight.png")
        sign.position=[300,160]
        self.scene.add_sprite("Walls",sign)
        for i in range(0, 1400,128):
            wall=arcade.Sprite(":resources:images/tiles/grassMid.png",)
            wall.center_x = i
            wall.center_y = 32
            self.scene.add_sprite("Walls", wall)
        for i in range(0,920,50):
            wall = arcade.Sprite(":resources:images/tiles/grass_sprout.png",scale=0.8)
            wall.position = [i,147]
            self.scene.add_sprite("Walls", wall)
            if i%100:
                size=random.randint(1,10)*0.1
                grass = arcade.Sprite(":resources:images/tiles/mushroomRed.png",scale=size)
                grass.position = [i,160-67*(1-size)]
                self.scene.add_sprite("Walls", grass)
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite, walls=self.scene["Walls"], gravity_constant=GRAVITY)
        self.camera = arcade.Camera2D()
        self.camera.position=(576,350)
        self.gui_camera = arcade.Camera2D()
        self.score = 0
        self.last_pipe_x = 1000
        self.pipe_spacing = 400
        for i in range(5):
            self.create_pipe_pair(self.last_pipe_x)
            self.last_pipe_x += self.pipe_spacing
    
    def create_grass(self,x_position):
        wall = arcade.Sprite(":resources:images/tiles/grassMid.png")
        wall.center_x = x_position + 700
        wall.center_y = 32
        self.scene.add_sprite("Walls", wall)

    def create_pipe_pair(self, x_position):
        step=64
        gap_y = random.randint(100,600) #wysokoc przerwy
        if self.last_pipe_x>10000:
            self.pipe_gap_size = random.randint(150,400)
        else:
            self.pipe_gap_size = random.randint(300,500)
        while gap_y+self.pipe_gap_size//2>680 and gap_y-self.pipe_gap_size//2<50:
            gap_y = random.randint(200,600)
        y = gap_y + self.pipe_gap_size // 2 + step
        coin = arcade.Sprite(":resources:images/items/coinGold.png", scale=0.7)
        coin.position=(x_position,gap_y)
        self.scene.add_sprite("Coins", coin)
        while y < 848:  # or your screen height
            pipe = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", scale=0.5)
            pipe.center_x = x_position
            pipe.center_y = y
            self.scene.add_sprite("Pipes", pipe)
            y += step
        y = gap_y - self.pipe_gap_size // 2 - step
        while y >= 128:
            pipe = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", scale=0.5)
            pipe.center_x = x_position
            pipe.center_y = y
            self.scene.add_sprite("Pipes", pipe)
            y -= step
            if y<160:
                pipe = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", scale=0.5)
                pipe.center_x = x_position
                pipe.center_y = 128
                self.scene.add_sprite("Pipes", pipe)

    def on_draw(self):
        self.clear()
        self.camera.use()
        self.scene.draw()
        self.gui_camera.use()
        self.score_text.draw()
        if self.game_over:
            arcade.draw_lrbt_rectangle_filled(self.window.width // 4, 3*(self.window.width // 4), self.window.height // 4, 3*(self.window.height // 4), arcade.color.DEEP_PINK)
            arcade.draw_text("GAME OVER!", self.window.width // 2, self.window.height // 2 + 40, arcade.color.RED_DEVIL, 37, anchor_x="center", font_name=font_name)
            arcade.draw_text(f"FINAL SCORE: {self.score}", self.window.width // 2 , self.window.height // 2 , arcade.color.RED_DEVIL, 30, anchor_x="center", font_name=font_name)
            arcade.draw_text("Press SPACE to restart or press ESCAPE to go to menu", self.window.width//2,self.window.height//2 - 40, arcade.color.RED_DEVIL, 10, anchor_x="center", font_name=font_name)
    
    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            if self.game_over:
                self.setup()
            elif not self.game_started:
                self.game_started  = True
            self.player_sprite.change_y = PLAYER_JUMP
            arcade.play_sound(self.jump_sound, volume=0.5)
    
    def on_key_release(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            from views import Start
            self.window.show_view(Start())
    
    def on_update(self, delta_time):
        if self.game_started and self.game_over == False:
            self.physics_engine.update()
            if self.player_sprite.center_x<5000:
                self.player_sprite.center_x+=4
            else:
                self.player_sprite.center_x+=6
            if self.player_sprite.position[0] < 600:
                pass
            else:
                self.camera.position = (self.player_sprite.position[0], 350)
            coin_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.scene["Coins"])
            for coin in coin_hit_list:
                coin.remove_from_sprite_lists()
                arcade.play_sound(self.collect_coin_sound)
                self.score += 1
                self.score_text.text = f"Score: {self.score}"
            if arcade.check_for_collision_with_list(self.player_sprite,self.scene["Pipes"]) or self.player_sprite.center_y<126.1 or self.player_sprite.center_y >700:
                self.game_over = True
                arcade.play_sound(self.game_over_sound)
                final_score = self.score
                add_score(final_score)
            if self.player_sprite.center_x + 800 > self.last_pipe_x:
                self.create_pipe_pair(self.last_pipe_x)
                self.last_pipe_x += self.pipe_spacing
            if self.player_sprite.center_x%128==0 and self.player_sprite.center_x>600:
                self.create_grass(self.player_sprite.center_x)
        elif self.game_over:
            return