# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 21:51 2019

@author: Icarpio
"""
import pgzrun


WIDTH = 1280
HEIGHT = 720

main_box = Rect(0, 0, 820, 240)
timer_box = Rect(0, 0, 240, 240)

answer_box1 = Rect(0, 0 ,495, 165)
answer_box2 = Rect(0, 0 ,495, 165)
answer_box3 = Rect(0, 0 ,495, 165)
answer_box4 = Rect(0, 0 ,495, 165)

main_box.move_ip(50,40)
timer_box.move_ip(990, 40)
answer_box1.move_ip(50, 358)
answer_box2.move_ip(735, 358)
answer_box3.move_ip(50, 538)
answer_box4.move_ip(735, 538)
answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]

score = 0
time_left = 10

question1 = ["What is the capital of Spain?", "London", "Madrid", "Berlin", "Paris", 2]
question2 = ["What is 5 + 7?", "12","10","14","11", 1]
question3 = ["What is the seventh month of the year?", "April","May","July","June", 3]
question4 = ["Which planet is closest to the Sun?", "Saturn","Neptune","Mercury","Venus", 3]
question5 = ["Where are the pyramids?", "India","Egypt","Morocco","Canada", 2]

questions = [question1, question2, question3, question4, question5]
question = questions.pop(0)

def draw():
    screen.fill("dim grey")
    screen.draw.filled_rect(main_box, "sky blue")
    screen.draw.filled_rect(timer_box, "sky blue")
    for box in answer_boxes:
        screen.draw.filled_rect(box, "orange")
    screen.draw.textbox(str(time_left), timer_box, color=("black"))
    screen.draw.textbox(question[0], main_box, color=("black"))
    
    index = 1
    for box in answer_boxes:
        screen.draw.textbox(question[index], box, color=("black"))
        index = index + 1
        
def game_over():
    global question, time_left
    message = "Game Over. You got %s questions correct" % str(score)
    question = [message, "-","-","-","-",5]
    time_left = 0
    
def correct_answer():
    global question, score, time_left
    score = score + 1
    if questions:
        question = questions.pop(0)
        time_left = 10
    else:
        print("End of questions")
        game_over()
        
def on_mouse_down(pos):
    index =  1
    for box in answer_boxes:
        if box.collidepoint(pos):
            print("Clicked on answer" + str(index))
            if index == question[5]:
                print("You got it correct!")
                correct_answer()
            else:
                game_over()
        index = index + 1
        
def update_time_left():
    global time_left
    
    if time_left:
        time_left = time_left - 1
    else:
        game_over()

clock.schedule_interval(update_time_left, 1.0)
pgzrun.go()
    


