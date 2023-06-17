from tkinter import *
import random
board=[["NA","NA","NA"],["NA","NA","NA"],["NA","NA","NA"]]

def empty_cell_deactivator():
    global board,button_list
    empty_cell_list= empty_cell_finder()
    for (x,y) in empty_cell_list:
        button_list[x][y].config(bg="pink", state=DISABLED)
def brain():
    global board
    empty_cell_list = empty_cell_finder()
    for (x, y) in empty_cell_list:
        if (green_flag_detector(x,y) == "True"):
            board[x][y]="o"
            return
    for (x, y) in empty_cell_list:
        if (red_flag_detector(x,y) == "True"):
            board[x][y] = "o"
            return
    for (x, y) in empty_cell_list:
        if semi_green_flag_detector(x, y) == "True":
            board[x][y] = "o"
            return
    semi_red_count=0
    for (x, y) in empty_cell_list:
        if semi_red_flag_detector(x, y) == "True":
            semi_red_count += 1
    if semi_red_count==1:
        for (x, y) in empty_cell_list:
            if semi_red_flag_detector(x, y) == "True":
                board[x][y]="o"
                return
    for (x, y) in empty_cell_list:
        if green_flag_generator(x, y) == "True":
            board[x][y] = "o"
            return

    else:
        last_option = random.randint(0, len(empty_cell_list)-1)
        if (last_option%2!=0):
            if (board[1][1] == "NA"):
                board[1][1] = "o"
                return
            else:
                board[empty_cell_list[last_option][0]][empty_cell_list[last_option][1]] = "o"
        else:
            board[empty_cell_list[last_option][0]][empty_cell_list[last_option][1]] = "o"
            return
    return
def empty_cell_finder():
    global board
    result = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == "NA":
                result.append([i, j])
    return result

def green_flag_detector(x, y):
    global board
    diag1 = [[0, 0], [1, 1], [2, 2]]
    diag1value = [board[0][0], board[1][1], board[2][2]]
    diag2 = [[0, 2], [1, 1], [2, 0]]
    diag2value = [board[0][2], board[1][1], board[2][0]]
    if board[x].count("o") == 2:
        return "True"
    elif [board[j][y] for j in range(3)].count("o") == 2:
        return "True"
    elif [x, y] in diag1:
        if diag1value.count("o") == 2:
            return "True"
    elif [x, y] in diag2:
        if diag2value.count("o") == 2:
            return "True"
    else:
        return "False"
def red_flag_detector(x, y):
    global board
    diag1 = [[0, 0], [1, 1], [2, 2]]
    diag1value = [board[0][0], board[1][1], board[2][2]]
    diag2 = [[0, 2], [1, 1], [2, 0]]
    diag2value = [board[0][2], board[1][1], board[2][0]]
    if board[x].count("x") == 2:
        return "True"
    elif [board[j][y] for j in range(3)].count("x") == 2:
        return "True"
    elif [x, y] in diag1:
        if diag1value.count("x") == 2:
            return "True"
    elif [x, y] in diag2:
        if diag2value.count("x") == 2:
            return "True"
    else:
        return "False"

def semi_green_flag_detector(x, y):
    global board
    diag1 = [[0, 0], [1, 1], [2, 2]]
    diag1value = [board[0][0], board[1][1], board[2][2]]

    diag2 = [[0, 2], [1, 1], [2, 0]]
    diag2value = [board[0][2], board[1][1], board[2][0]]

    rr = (board[x].count("o") == 1) and (board[x].count("x") == 0)

    cc = ([board[j][y] for j in range(3)].count("o") == 1) and ([board[j][y] for j in range(3)].count("x") == 0)

    dd1 = (diag1value.count("o") == 1) and (diag1value.count("x") == 0)

    dd2 = (diag2value.count("o") == 1) and (diag1value.count("x") == 0)

    if rr == True and cc == True:
        return "True"
    elif ([x, y] in diag1):
        if rr == True and dd1 == True:
            return "True"
        elif cc == True and dd1 == True:
            return "True"
    elif [x, y] in diag2:
        if rr == True and dd2 == True:
            return "True"
        elif cc == True and dd2 == True:
            return "True"
    else:
        return "False"

def semi_red_flag_detector(x, y):
    global board
    diag1 = [[0, 0], [1, 1], [2, 2]]
    diag1value = [board[0][0], board[1][1], board[2][2]]

    diag2 = [[0, 2], [1, 1], [2, 0]]
    diag2value = [board[0][2], board[1][1], board[2][0]]

    rr = (board[x].count("x") == 1) and (board[x].count("o") == 0)

    cc = ([board[j][y] for j in range(3)].count("x") == 1) and ([board[j][y] for j in range(3)].count("o") == 0)

    dd1 = (diag1value.count("x") == 1) and (diag1value.count("o") == 0)

    dd2 = (diag2value.count("x") == 1) and (diag1value.count("o") == 0)

    if rr == True and cc == True:
        return "True"
    elif ([x, y] in diag1):
        if rr == True and dd1 == True:
            return "True"
        elif cc == True and dd1 == True:
            return "True"
    elif [x, y] in diag2:
        if rr == True and dd2 == True:
            return "True"
        elif cc == True and dd2 == True:
            return "True"
    else:
        return "False"

def green_flag_generator(x,y):
    global board
    diag1 = [[0, 0], [1, 1], [2, 2]]
    diag1value = [board[0][0], board[1][1], board[2][2]]

    diag2 = [[0, 2], [1, 1], [2, 0]]
    diag2value = [board[0][2], board[1][1], board[2][0]]

    rr = (board[x].count("o") == 1) and (board[x].count("NA") == 2)
    cc = ([board[j][y] for j in range(3)].count("o") == 1) and ([board[j][y] for j in range(3)].count("NA") == 2)
    dd1 = (diag1value.count("o") == 1) and (diag1value.count("NA") == 2)
    dd2 = (diag2value.count("o") == 1) and (diag1value.count("NA") == 2)

    if rr == True:
        return "True"
    elif cc == True:
        return "True"
    elif ([x, y] in diag1):
        if dd1 == True:
            return "True"
    elif [x, y] in diag2:
        if dd2 == True:
            return "True"
    else:
        return "False"

def game_status(board):
    tboard=[[board[0][0],board[1][0],board[2][0]],[board[0][1],board[1][1],board[2][1]],[board[0][2],board[1][2],board[2][2]]]
    diag1=[board[0][0],board[1][1],board[2][2]]
    diag2=[board[0][2],board[1][1],board[2][0]]

    if ((board[0].count("x")==3) or (board[1].count("x")==3) or (board[2].count("x")==3) or (tboard[0].count("x")==3) or (tboard[1].count("x")==3) or (tboard[2].count("x")==3) or (diag1.count("x")==3) or (diag2.count("x")==3)):
        return "Player Won"
    elif ((board[0].count("o")==3) or (board[1].count("o")==3) or (board[2].count("o")==3) or (tboard[0].count("o")==3) or (tboard[1].count("o")==3) or (tboard[2].count("o")==3) or (diag1.count("o")==3) or (diag2.count("o")==3)):
        return "Computer Won"
    elif (("NA" in board[0]) or ("NA" in board[1]) or ("NA" in board[2])):
        return "To Be Continued"
    else:
        return "Match Draw"

def update_board():
    global board, button_list
    for i in range(3):
        for j in range(3):
            if (board[i][j] == "NA"):
                button_list[i][j].config(text="", bg="white")
            elif (board[i][j] == "x"):
                button_list[i][j].config(text="x", bg="green")
            elif (board[i][j] == "o"):
                button_list[i][j].config(text="o", bg="red")

def my_click(x,y):
    if(board[x][y]=="NA"):
        board[x][y]="x"
        update_board()
        nnn=game_status(board)
        if(nnn=="Player Won"):
            Footer.config(text="Player has Won")
            empty_cell_deactivator()
            return
        elif(nnn=="Computer Won"):
            Footer.config(text="Computer has Won")
            empty_cell_deactivator()
            return
        elif (nnn=="Match Draw"):
            Footer.config(text="Match is Draw")
            empty_cell_deactivator()
            return
        elif (nnn=="To Be Continued"):
            brain()
            update_board()
            mmm=game_status(board)
            if (mmm == "Player Won"):
                Footer.config(text="Player has Won")
                empty_cell_deactivator()
                return
            elif (mmm == "Computer Won"):
                Footer.config(text="Computer has Won")
                empty_cell_deactivator()
                return
            elif (mmm == "Match Draw"):
                Footer.config(text="Match is Draw")
                empty_cell_deactivator()
                return
            elif (mmm=="To Be Continued"):
                return
    return

root=Tk()
root.title("TIC TAC TOE")
root.geometry("750x550")
root.resizable(width=False,height=False)
root["bg"]="yellow"
Heading1=Label(root,text="Welcome to TIC TAC TOE game",font="Arial 20",bg="yellow")
Heading1.pack()
Heading2=Label(root,text="Mode: Player vs Computer",font="Arial 14",bg="yellow")
Heading2.pack()
Heading2=Label(root,text="""Presets: Player takes symbol "x" and make the first move
""",font="Arial 14",bg="yellow")
Heading2.pack()
BoardFrame=LabelFrame(root, width=570, height=570,padx=5,pady=5)
BoardFrame.pack()
Button00=Button(BoardFrame,text="",width=23, height=6, border=2, font="2",  command=lambda: my_click(0,0))
Button00.grid(row=0,column=0)
Button01=Button(BoardFrame,text="",width=23, height=6, border=2, font="2", command=lambda: my_click(0,1))
Button01.grid(row=0,column=1)
Button02=Button(BoardFrame,text="",width=23, height=6, border=2, font="2", command=lambda: my_click(0,2))
Button02.grid(row=0,column=2)
Button10=Button(BoardFrame,text="",width=23, height=6, border=2, font="2", command=lambda: my_click(1,0))
Button10.grid(row=1,column=0)
Button11=Button(BoardFrame,text="",width=23, height=6, border=2, font="2", command=lambda: my_click(1,1))
Button11.grid(row=1,column=1)
Button12=Button(BoardFrame,text="",width=23, height=6, border=2, font="2", command=lambda: my_click(1,2))
Button12.grid(row=1,column=2)
Button20=Button(BoardFrame,text="",width=23, height=6, border=2, font="2", command=lambda: my_click(2,0))
Button20.grid(row=2,column=0)
Button21=Button(BoardFrame,text="",width=23, height=6, border=2, font="2", command=lambda: my_click(2,1))
Button21.grid(row=2,column=1)
Button22=Button(BoardFrame,text="",width=23, height=6, border=2, font="2", command=lambda: my_click(2,2))
Button22.grid(row=2,column=2)
button_list=[[Button00, Button01,Button02],[Button10,Button11,Button12],[Button20,Button21,Button22]]
Footer=Label(root,text="",font="Arial 20",bg="yellow")
Footer.pack()
root.mainloop()