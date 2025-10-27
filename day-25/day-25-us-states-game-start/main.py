import turtle
import pandas as pd


screen = turtle.Screen()
screen.title("U.S. states game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)


data= pd.read_csv('50_states.csv')
ans_list = []
while len(ans_list)<2:
    answer_text = screen.textinput(title="Guess the state", prompt=" whats another states name")
    answer_text= answer_text.title()
    if answer_text in data['state'].values:
        ans_list.append(answer_text)
        print(f"x cord  {data[data.state == answer_text]['x'].item()}")
        print(f"y cord {data[data.state == answer_text]['y'].item()}")
        print(ans_list)

print(data[data.state== 'Ohio']['y'])
print(ans_list)



turtle.mainloop()

