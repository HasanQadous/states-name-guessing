from turtle import Screen, Turtle
import pandas
data = pandas.read_csv("50_states.csv")
screen = Screen()
turtle = Turtle()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
SCORE = 0
all_states = data.state.to_list()
correct_answers = []
missing_states = []
while SCORE < 50:
    user_answer = screen.textinput(title=f"{SCORE}/50 States Correct"
                                   , prompt="Give another State Name").title()
    if user_answer == "Exit":
        missing_states = [state for state in all_states if state not in correct_answers]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if user_answer in all_states:
        writing_turtle = Turtle()
        writing_turtle.hideturtle()
        writing_turtle.penup()
        state_data = data[data.state == user_answer]
        writing_turtle.goto(x=int(state_data.x), y=int(state_data.y))
        writing_turtle.write(user_answer)
        correct_answers.append(user_answer)
        SCORE += 1

print(correct_answers)






