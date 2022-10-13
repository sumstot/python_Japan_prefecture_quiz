import turtle
import pandas

FONT = ("Arial", 12)
screen = turtle.Screen()
image = "japan.gif"
screen.addshape(image)
turtle.shape(image)
turtle.speed("fastest")


data = pandas.read_csv('japan-quiz.csv')
all_prefecture_list_en = data.PrefectureEN.tolist()
all_prefecture_list_jp = data.PrefectureJP.tolist()
SCORE = 0

guessed_prefectures = []


# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)

LANGUAGE = screen.textinput(title='Language choice', prompt='Please choose English or　日本語').title()

while len(guessed_prefectures) < 47:
    if LANGUAGE == "English":
        if SCORE == 0:
            answer_prefecture = screen.textinput(title="Guess a prefecture", prompt="Guess a prefecture").title()
        else:
            answer_prefecture = screen.textinput(title=f"{SCORE}/47 Prefectures", prompt="Guess another prefecture").title()
        if answer_prefecture == 'Exit':
            missing_prefectures = []
            for prefecture in all_prefecture_list_en:
                if prefecture not in guessed_prefectures:
                    missing_prefectures.append(prefecture)
            print(missing_prefectures)
            break
        if answer_prefecture in all_prefecture_list_en:
            guessed_prefectures.append(answer_prefecture)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            prefecture_data = data[data.PrefectureEN == answer_prefecture]
            print(prefecture_data)
            t.goto(int(prefecture_data.X), int(prefecture_data.Y))
            t.write(answer_prefecture, font=FONT)
            SCORE += 1

    if LANGUAGE == "日本語":
        if SCORE == 0:
            answer_prefecture = screen.textinput(title="都道府県を当たれますか？", prompt="都道府県を入力ください")
        else:
            answer_prefecture = screen.textinput(title=f"{SCORE}/47 都道府県", prompt="Guess another prefecture").title()
        if answer_prefecture == 'Exit':
            missing_prefectures = []
            for prefecture in all_prefecture_list_jp:
                if prefecture not in guessed_prefectures:
                    missing_prefectures.append(prefecture)
            print(missing_prefectures)
    if answer_prefecture in all_prefecture_list_jp:
        guessed_prefectures.append(answer_prefecture)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        prefecture_data = data[data.PrefectureJP == answer_prefecture]
        print(prefecture_data)
        t.goto(int(prefecture_data.X), int(prefecture_data.Y))
        t.write(answer_prefecture, font=FONT)
        SCORE += 1


turtle.mainloop()