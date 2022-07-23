import pygame
pygame.init()
Width = 500
Height = 700
Screen = pygame.display.set_mode((Width, Height))
Background = (111,28,28)
Border1 = (255,215,0)
Rect2 = (255,255,237)
White = (255,255,255)
Button = (255,57,57)
pygame.display.set_caption("MLH HACKY Birthday Slot Machine!")
FPS = 60

def button(text,textRect,text3,textRect3):
    mouse = pygame.mouse.get_pos()
    if (290 > mouse[0] > 190) and (450 > mouse[1] > 350):
        pygame.draw.ellipse(Screen,(255,204,203), (190,350,120,80))
        pygame.draw.ellipse(Screen, (0,0,0,0), (190, 350, 120, 80), 4)
        Screen.blit(text3,textRect3)
    else:
        pygame.draw.ellipse(Screen, Button, (190,350,120,80))
        pygame.draw.ellipse(Screen, (0,0,0,0), (190, 350, 120, 80), 4)
        Screen.blit(text, textRect)

def display(text,textRect,text2,textRect2,text3,textRect3):
    Screen.fill((Background))
    pygame.draw.rect(Screen, Rect2, pygame.Rect(30,30,440,80),0,4)
    pygame.draw.rect(Screen, Border1,(30,120,440,200),0,4)
    pygame.draw.rect(Screen, Rect2, pygame.Rect(55,135,115,170),0,10)
    pygame.draw.rect(Screen, Rect2, pygame.Rect(190,135,115,170),0,10)
    pygame.draw.rect(Screen, Rect2, pygame.Rect(325,135,115,170),0,10)
    button(text, textRect, text3, textRect3)
    pygame.draw.rect(Screen, Rect2, pygame.Rect(30,450,440,200),0,4)
    Screen.blit(text2, textRect2)
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    font = pygame.font.Font('Bubblegum.ttf', 30)
    text = font.render('SPIN', True, (255,255,255,255))
    textRect = text.get_rect()
    textRect.center = (250,390)
    text3 = font.render('SPIN', True, (0,0,0,0))
    textRect3 = text3.get_rect()
    textRect3.center = (250,390)
    text2 = font.render('Advice', True, (0,0,0,0))
    textRect2 = text2.get_rect()
    textRect2.center = (240, 475)
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            mousee = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                run = False
            if (event.type == pygame.MOUSEBUTTONDOWN):
                if (290 > mousee[0] > 190) and (450 > mousee[1] > 350):
                    print("Hello")
        display(text, textRect, text2, textRect2, text3, textRect3)
    pygame.quit()

if __name__ == "__main__":
    main()
