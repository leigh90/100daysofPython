import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 10
SHORT_BREAK_MIN = 10
LONG_BREAK_MIN = 10
cycle = 0
main_timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    mywindow.after_cancel(main_timer)
    canvas.itemconfig(timer_txt,text="00:00")
    timer_label.config(text="START")
    checkmarks.config(text=" ")
    global cycle
    cycle = 0



# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global cycle
    cycle += 1
    if cycle == 8:
        countdown(LONG_BREAK_MIN)
        timer_label.config(text="LONG BREAK" ,bg=RED, font=(FONT_NAME, 16, "normal"))
    elif cycle % 2 == 0:
        countdown(SHORT_BREAK_MIN)
        timer_label.config(text="SHORT BREAK", bg=PINK, font=(FONT_NAME, 16, "normal"))
    else:
        countdown(WORK_MIN)
        timer_label.config(text="WERK", bg=GREEN, font=(FONT_NAME, 16, "normal"))




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    count_sec_new = "0"
    if count_sec < 10:
        count_sec = count_sec_new + str(count_sec)
        # or
        # count_sec = f'0{count_sec}'
    canvas.itemconfig(timer_txt, text=f'{count_min}:{count_sec}')
    # print(count)
    global main_timer
    if count > 0:
        main_timer = mywindow.after(1000, countdown, count-1)
    else:
        start_timer()
        if cycle % 2 == 0:
            checkmarks.config(text=f'{cycle// 2 * "✔"}')
# ---------------------------- UI SETUP ------------------------------- #
# todo create a tkinter window
mywindow = Tk()
mywindow.title('Pomodoro')
mywindow.config(padx=100, pady=100, bg=YELLOW)

# todo Create a canvas
canvas = Canvas(width=200, height=224,bg=YELLOW, highlightthickness=0)
# direct tkinter to the image file
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_txt = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=2, row=2)

# TODO LABELS
# # todo Timer Label
timer_label = Label(text='Timer',bg=YELLOW, font=(FONT_NAME, 16, "normal"))
timer_label.grid(column=2, row=1)

# # todo checkmark label
checkmarks = Label(text='',bg=YELLOW, font=(FONT_NAME, 16, "normal"))
checkmarks.grid(column=2, row=3)
#
# todo start_button button
start_button = Button(text="START",highlightthickness=0, command=start_timer, )
start_button.grid(column=1, row=3)

# todo reset button
reset_button = Button(text="RESET",highlightthickness=0, command=reset)
reset_button.grid(column=3, row=3)

mywindow.mainloop()