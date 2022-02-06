import turtle
import pandas
from states import AddState
from scoreboard import Scoreboard


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
add_state = AddState()
my_scoreboard = Scoreboard()
data = pandas.read_csv("50_states.csv")
end_of_game = False
correct_guesses = []
unique_correct_guesses = 0
while not end_of_game:
    answer_state = (screen.textinput(title="Guess the State", prompt="What's another state's name?")).title()
    if answer_state in data.values:
        print("Match exists!")
        matched_state = data[data.state == answer_state]
        add_state.set_location(x=int(matched_state.x), y=int(matched_state.y))
        add_state.write_state(answer_state)
        correct_guesses.append(answer_state)
        unique_correct_guesses = len(sorted(set(correct_guesses)))
        my_scoreboard.update_scoreboard(unique_correct_guesses)
        if unique_correct_guesses == 50:
            my_scoreboard.you_win()
            end_of_game = True
    else:
        print("Sorry, not a state!")
        my_scoreboard.wrong_guess()
        my_scoreboard.update_scoreboard(unique_correct_guesses)
screen.exitonclick()
