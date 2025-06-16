import arcade
from views import Start
window_width =1280
window_height= 720
window_title="game"
def main():
    window = arcade.Window(window_width, window_height, window_title)
    start_view = Start()
    window.show_view(start_view)
    arcade.run()
if __name__=="__main__":
    main()