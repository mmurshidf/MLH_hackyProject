import pygame
import random

choice1 = ""
choice2 = ""
choice3 = ""

Cake = pygame.image.load('cake.png')
machine_symbols = ["Cake", "Presents", "Clown", "Money", "Candle", "Friends"]
#when using GUI you can call variable names cake, present etc. define the variable to corresponding image and then put variable names in list

current_roll = "I want to roll"
push_leave = "game is open"
advice_msg = ""
credit = float(1) #the amount of money they start with - it will change depending on score


def colour_change(): #in UI Could change spin colour of button if spin is pressed
    if current_roll == "I want to roll":
        #change colour of button?
        current_roll = "Another Go!" #prompt to re roll

def leave():
    if push_leave == "I want to leave": #can change somewhere in the game then pass the function through
        #kill the game
        push_leave = "leave"

def roll(choice1, choice2, choice3, credit, machine_symbols):

    choice1 = random.choice(machine_symbols)
    choice2 = random.choice(machine_symbols)
    choice3 = random.choice(machine_symbols)

    if choice1 == choice2 == choice3: #all different combos for point change based on fruit machine rolls
        credit += 1
        if choice1 == "Presents":
            credit += 4
            print(all_lines[random.randint(0, len(all_lines))]) #advice appears when credit increases
        elif choice1 == "Friends":
            credit = 0
            
    if choice1 == choice2:
        if choice1 != choice3:
            credit += 0.5
            print(all_lines[random.randint(0, len(all_lines))])
            if choice1 == "Friends":
                credit -= 1.5
                
    if choice2 == choice3:
        if choice2 != choice1:
            credit += 0.5
            print(all_lines[random.randint(0, len(all_lines))])
            if choice2 == "Friends":
                credit -= 1.5
                
    if choice1 == choice3:
        if choice1 != choice2:
            credit += 0.5
            print(x)
            if choice1 == "Friends":
                credit -= 1.5
                
    credit = round(credit, 2)
    
    print("You got", choice1, choice2, choice3, "Your credit so far is: ", credit)

advice_text = open("advice.txt", "r")
all_lines = advice_text.readlines()
x = all_lines[random.randint(0, len(all_lines))]


while credit > float(0): #checking all money is not gone
    play_ans = input("Would you like to roll?")
    if play_ans == "y":
        credit -= 0.2 #spend to make a roll
        machine_play = roll(choice1, choice2, choice3, credit, machine_symbols)
    else:
        print("Ok bye")
        break
    
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
points = str(credit)

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

def display(text,textRect,text2,textRect2,text3,textRect3, text4, textRect4,count):
    Screen.fill((Background))
    pygame.draw.rect(Screen, Rect2, pygame.Rect(30,30,440,80),0,4)
    pygame.draw.rect(Screen, Border1,(30,120,440,200),0,4)
    pygame.draw.rect(Screen, Rect2, pygame.Rect(55,135,115,170),0,10)
    pygame.draw.rect(Screen, Rect2, pygame.Rect(190,135,115,170),0,10)
    pygame.draw.rect(Screen, Rect2, pygame.Rect(325,135,115,170),0,10)
    button(text, textRect, text3, textRect3)
    pygame.draw.rect(Screen, Rect2, pygame.Rect(30,450,440,200),0,4)
    Screen.blit(text2, textRect2)
    if count == 1:
        Screen.blit(text4, textRect4)
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    font = pygame.font.Font('Bubblegum.ttf', 30)
    font2 = pygame.font.Font('Bubblegum.ttf', 20)
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
    count = 0
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            mousee = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                run = False
            if (event.type == pygame.MOUSEBUTTONDOWN):
                if (290 > mousee[0] > 190) and (450 > mousee[1] > 350):
                    roll(choice1, choice2, choice3, credit, machine_symbols)
                    print(credit)
                    print("Hello")
                    print(choice1)
                    count += 1
        display(text, textRect, text2, textRect2, text3, textRect3, text4, textRect4, count)
    pygame.quit()

if __name__ == "__main__":
    main()
