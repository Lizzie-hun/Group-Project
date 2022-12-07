# Find/Use Mouse Position in Pygame
import pygame
import main
import arcade
from director import Director
import globals
 
pygame.init()
 
WIDTH = 500
HEIGHT = 500
fps = 60
timer = pygame.time.Clock()
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Dino Run Menu')
main_menu = False
font = pygame.font.Font('freesansbold.ttf', 24)
menu_command = 0
 
class Button:
    def __init__(self, txt, pos):
        self.text = txt
        self.pos = pos
        self.button = pygame.rect.Rect((self.pos[0], self.pos[1]), (260, 40))
 
    def draw(self):
        pygame.draw.rect(screen, 'light gray', self.button, 0, 5)
        pygame.draw.rect(screen, 'dark gray', [self.pos[0], self.pos[1], 260, 40], 5, 5)
        text2 = font.render(self.text, True, 'black')
        screen.blit(text2, (self.pos[0] + 15, self.pos[1] + 7))
 
    def check_clicked(self):
        if self.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            return True
        else:
            return False
 
def draw_menu():
    command = -1
    pygame.draw.rect(screen, 'black', [100, 100, 300, 300])
    pygame.draw.rect(screen, 'green', [100, 100, 300, 300], 5)
    pygame.draw.rect(screen, 'white', [120, 120, 260, 40], 0, 5)
    pygame.draw.rect(screen, 'gray', [120, 120, 260, 40], 5, 5)
    txt = font.render('Welcome!', True, 'black')
    screen.blit(txt, (135, 127))
    # menu exit button
    menu = Button('Exit Menu', (120, 350))
    menu.draw()
    button1 = Button('Start', (120, 180))
    button1.draw()
    button2 = Button('Select Character', (120, 240))
    button2.draw()
    button3 = Button('Setting', (120, 300))
    button3.draw()
    if menu.check_clicked():
        command = 0
    if button1.check_clicked():
        command = 1
    if button2.check_clicked():
        command = 2
    if button3.check_clicked():
        command = 3
    return command
 
def draw_game():
    menu_btn = Button('Main Menu', (230, 450))
    menu_btn.draw()
    menu = menu_btn.check_clicked()
    return menu
 
run = True
while run:
    screen.fill('light blue')
    timer.tick(fps)
    if main_menu:
        menu_command = draw_menu()
        if menu_command != -1:
            main_menu = False
    else:
        main_menu = draw_game()
        if menu_command == 1:
            window = arcade.Window(globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT, globals.SCREEN_TITLE)
            start_game = Director()
            window.show_view(start_game)
            start_game.setup(dino_color="red")
            arcade.run()
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
 
    pygame.display.flip()
pygame.quit()