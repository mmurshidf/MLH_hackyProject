import pygame
import random

choice1 = ""
choice2 = ""
choice3 = ""

Img_h = 110
Img_w = 110
Cake = pygame.image.load('cake.png')
Presents = pygame.image.load('Gift.png')
Clown = pygame.image.load('clown.png')
Money = pygame.image.load('Money.png')
Candle = pygame.image.load('candle.png')
Friends = pygame.image.load('friends.png')
Cake_size = pygame.transform.scale(Cake, (Img_w, Img_h))
Presents_size = pygame.transform.scale(Presents, (Img_w, Img_h))
Clown_size = pygame.transform.scale(Clown, (Img_w, Img_h))
Money_size = pygame.transform.scale(Money, (Img_w, Img_h))
Candle_size = pygame.transform.scale(Candle, (Img_w, Img_h))
Friends_size = pygame.transform.scale(Friends, (Img_w, Img_h))
machine_symbols = ["Cake", "Presents", "Clown", "Money", "Candle", "Friends"]
x = ""
#when using GUI you can call variable names cake, present etc. define the variable to corresponding image and then put variable names in list

counter = 0


current_roll = "I want to roll"
push_leave = "game is open"
advice_msg = ""
credit = 1.0 #the amount of money they start with - it will change depending on score
points = str(credit)

def colour_change(): #in UI Could change spin colour of button if spin is pressed
    if current_roll == "I want to roll":
        #change colour of button?
        current_roll = "Another Go!" #prompt to re roll

def leave():
    if push_leave == "I want to leave": #can change somewhere in the game then pass the function through
        #kill the game
        push_leave = "leave"

def roll(choice1, choice2, choice3, credit, machine_symbols, points,counter, x, text4, textRect4, text5, textRect5, textRect6, text6):

    choice1 = random.choice(machine_symbols)
    choice2 = random.choice(machine_symbols)
    choice3 = random.choice(machine_symbols)
    
    if choice1 == choice2 == choice3: #all different combos for point change based on fruit machine rolls
        credit += 1
        if choice1 == "Presents":
            credit += 4
            print(all_lines[random.randint(0, len(all_lines))]) #advice appears when credit increases
            x = all_lines[random.randint(0, len(all_lines))]
        elif choice1 == "Friends":
            credit = 0
            
    elif choice1 == choice2:
        if choice1 != choice3:
            credit += 0.5
            print(all_lines[random.randint(0, len(all_lines))])
            x = all_lines[random.randint(0, len(all_lines))]
            if choice1 == "Friends":
                credit -= 1.5
                
    elif choice2 == choice3:
        if choice2 != choice1:
            credit += 0.5
            print(all_lines[random.randint(0, len(all_lines))])
            x = all_lines[random.randint(0, len(all_lines))]
            if choice2 == "Friends":
                credit -= 1.5
                
    elif choice1 == choice3:
        if choice1 != choice2:
            credit += 0.5
            print(all_lines[random.randint(0, len(all_lines))])
            x = all_lines[random.randint(0, len(all_lines))]
            if choice1 == "Friends":
                credit -= 1.5
                
    credit = round(credit, 2)

    print("You got", choice1, choice2, choice3, "Your credit so far is: ", credit)
    points = str(credit)
    print("this is", points, credit)
    while counter < 1500:
        if choice1 == "Presents":
            Screen.blit(Presents_size, (55,165))
        elif choice1 == "Cake":
            Screen.blit(Cake_size, (55,165))
        elif choice1 == "Money":
            Screen.blit(Money_size, (55,165))
        elif choice1 == "Candle":
            Screen.blit(Candle_size, (55,165))
        elif choice1 == "Friends":
            Screen.blit(Friends_size, (55,165))
        else:
            Screen.blit(Clown_size, (55,165))

        if choice2 == "Presents":
            Screen.blit(Presents_size, (190,165))
        elif choice2 == "Cake":
            Screen.blit(Cake_size, (190,165))
        elif choice2 == "Money":
            Screen.blit(Money_size, (190,165))
        elif choice2 == "Candle":
            Screen.blit(Candle_size, (190,165))
        elif choice2 == "Friends":
            Screen.blit(Friends_size, (190,165))
        else:
            Screen.blit(Clown_size, (190,165))

        if choice3 == "Presents":
            Screen.blit(Presents_size, (325,165))
        elif choice3 == "Cake":
            Screen.blit(Cake_size, (325,165))
        elif choice3 == "Money":
            Screen.blit(Money_size, (325,165))
        elif choice3 == "Candle":
            Screen.blit(Candle_size, (325,165))
        elif choice3 == "Friends":
            Screen.blit(Friends_size, (325,165))
        else:
            Screen.blit(Clown_size, (325,165))
        font2 = pygame.font.Font('Bubblegum.ttf', 18)
        text4 = font2.render(x, True, (0,0,0,0))
        textRect4 = text4.get_rect()
        textRect4.center = (250, 550)
        Screen.blit(text4, textRect4)

        font = pygame.font.Font('Bubblegum.ttf', 30)
        text5 = font.render(points, True, (0,0,0,0))
        textRect5 = text5.get_rect()
        textRect5.center = (400,75)
        Screen.blit(text5, textRect5)

        text6 = font2.render("Out of Money - GoodBye!", True, (0,0,0,0))
        textRect6 = text6.get_rect()
        textRect6.center = ((180, 600))
        if credit == 0.0 or credit < 0.0:
            Screen.blit(text6, textRect6)
        pygame.display.update()
        counter += 1
    if credit == 0.0 or credit < 0.0:
        pygame.quit()

advice_text = open("advice.txt", "r")
all_lines = advice_text.readlines()
all_lines[random.randint(0, len(all_lines))]


    
#end game here this is because credit is greater than 0

#-------------------------------------------------------------------------
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
    font2 = pygame.font.Font('Bubblegum.ttf', 18)
    text = font.render('SPIN', True, (255,255,255,255))
    textRect = text.get_rect()
    textRect.center = (250,390)
    text3 = font.render('SPIN', True, (0,0,0,0))
    textRect3 = text3.get_rect()
    textRect3.center = (250,390)
    text2 = font.render('Advice', True, (0,0,0,0))
    textRect2 = text2.get_rect()
    textRect2.center = (240, 475)
    text4 = font2.render(x, True, (0,0,0,0))
    textRect4 = text4.get_rect()
    textRect4.center = (250, 550)
    text5 = font.render(points, True, (0,0,0,0))
    textRect5 = text5.get_rect()
    textRect5.center = (400,75)
    text6 = font2.render("Out of Money - GoodBye!", True, (0,0,0,0))
    textRect6 = text6.get_rect()
    textRect6.center = ((180, 600))
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            mousee = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                run = False
            if (event.type == pygame.MOUSEBUTTONDOWN):
                if (290 > mousee[0] > 190) and (450 > mousee[1] > 350):
                    roll(choice1, choice2, choice3, credit, machine_symbols, points,counter,x,text4, textRect4, text5, textRect5, text6, textRect6)

        display(text, textRect, text2, textRect2, text3, textRect3)
    pygame.quit()

if __name__ == "__main__":
    main()
