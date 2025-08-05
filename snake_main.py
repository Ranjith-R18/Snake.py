from turtle import Turtle,Screen,textinput 
import time
from snake import Snake
from food import Food
from score import Scoreboard

screen=Screen()
scoreboard = Scoreboard()
textinput(None,None)
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake  Game")
screen.tracer(0)

snake=Snake()
food=Food()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")
   
is_on=True
while is_on:
    screen.update()
    time.sleep(0.1)
    
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        
    if snake.head.xcor()<-280 or snake.head.xcor()>280 or snake.head.ycor()<-280 or snake.head.ycor()>280:
        is_on=False
        scoreboard.game_over()
        break
        
    for segment in snake.segments:
        if segment == snake.head:
            continue 
        elif snake.head.distance(segment.pos())<15:
            is_on=False
            scoreboard.game_over()
    
    
    snake.move()    
screen.exitonclick()
    