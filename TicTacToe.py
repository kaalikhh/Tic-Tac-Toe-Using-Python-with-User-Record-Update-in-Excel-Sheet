#Tic Tac Toe Game using Python
#Tic-tac-toe (American English), noughts and crosses (British English), or Xs and Os
#is a paper-and-pencil game for two players, X and O, who take turns marking the spaces in a 3×3 grid.
#The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins the game.

import pandas as pd

def check(player):
    for ind in df.index:

        if(df['1_Player'][ind]==player):
            return ind

    return -1

file_path = '/home/saurabhyadav789/141642.xlsx'

df = pd.read_excel(file_path)
rd = pd.DataFrame({'1_Player':[],'2_Age':[],'3_Total':[],'4_Wins':[],'5_Lose':[],'6_WinP':[]})

#if not os.path.exists('ud.xlsx'):
    #df = pd.DataFrame({'Player1':[],'Age1':[],'Player2':[],'Age2':[],'Win_1':[],'Win_2':[],'Total':[], 'Win_1 %':[],'Win_2 %':[]})
    #df.to_excel('ud.xlsx',index=False)

#taking user inputs

print("Enter Player 1 Name: ")
player1 = input()
print("Enter Player 2 Name: ")
player2 = input()
print(("Enter Age of %s: ")%player1)
age1 = input()
print(("Enter Age of %s: ")%player2)
age2 = input()
win_1=0
win_2=0
total=0

def tic_tac_toe():

    file_path = '/home/saurabhyadav789/141642.xlsx'
    global player1, player2, age1, age2
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    end = False
    win_commbinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

#drawing board for the game play
    def draw():
        print(board[0], board[1], board[2])
        print(board[3], board[4], board[5])
        print(board[6], board[7], board[8])
        print()

#player 1 choice for putting cross
    def p1():
        n = choose_number()
        if board[n] == "X" or board[n] == "O":
            print("\nYou can't go there. Try again")
            p1()
        else:
            board[n] = "X"
#player 2 choice for putting nought
    def p2():
        n = choose_number()
        if board[n] == "X" or board[n] == "O":
            print("\nYou can't go there. Try again")
            p2()
        else:
            board[n] = "O"

#function for taking number from 1 to 9

    def choose_number():
        while True:
            while True:
                a = input()
                try:
                    a  = int(a)
                    a -= 1
                    if a in range(0, 9):
                        return a

                    else:
                        print("\nThat's not on the board. Try again")
                        continue

                except ValueError:
                   print("\nThat's not a number. Try again")
                   continue

#function for monitoring win
    def check_win():
        global total, win_1p, win_2p,win_1,win_2
        count = 0
        for a in win_commbinations:
            if board[a[0]] == board[a[1]] == board[a[2]] == "X":
                print(("%s Wins!\n")%player1)
                print("Congratulations!\n")
                win_1 += 1
                total+=1
                return True

            if board[a[0]] == board[a[1]] == board[a[2]] == "O":
                print(("%s Wins!\n")%player2)
                print("Congratulations!\n")
                win_2 += 1
                total+=1
                return True

        for a in range(9):
            if board[a] == "X" or board[a] == "O":
                count += 1

            if count == 9:
                print("The game ends in a Tie\n")
                total+=1
                return True

    while not end:
        draw()
        end = check_win()
        if end == True:
            break
        print(("%s, choose where to place a cross")%player1)
        p1()
        print()
        draw()
        end = check_win()
        if end == True:
            break
        print(("%s, choose where to place a nought")%player2)
        p2()
        print()

    if input("Play again (y/n)\n") == "y":
        tic_tac_toe()
    else:
        if win_1>win_2:
            w1 = 1
            w2 = 0
            l1 = 0
            l2 = 1
        elif win_1<win_2:
            w2 =1
            w1 = 0
            l1 = 1
            l2 = 0
        else:
            w1=1
            w2=1
            l1 = 0
            l2 = 0

        ind1 = check(player1)
        ind2 = check(player2)

        win_1p = (w1/(w1+l1))*100
        win_1p = ("%.2f" % win_1p)
        win_2p = (w2/(w1+l1))*100
        win_2p = ("%.2f" % win_2p)
        df = pd.read_excel(file_path)

        if ind1==-1 and ind2==-1:
#If Both players are new
            qd = pd.DataFrame({'1_Player':player1,'2_Age': age1, '3_Total':1,'4_Wins':w1,'5_Lose':l1,'6_WinP':win_1p},index=[1])

            rd = pd.DataFrame({'1_Player':player2,'2_Age':age2,'3_Total':1,'4_Wins':w2,'5_Lose':l2,'6_WinP':win_2p},index=[1])
            df= pd.concat([df,qd] ,sort='True', ignore_index = 'True')
            df= pd.concat([df,rd] ,sort='True', ignore_index = 'True')

            df.sort_values('4_Wins',ascending=False,inplace=True)
            df.reset_index(drop=True,inplace = True)
            df.to_excel(file_path)

        elif ind1>(-1) and ind2==-1:
#If only player2 is new            
            df.at[ind1,'3_Total']+=1
            if win_1>win_2:
                df.at[ind1,'4_Wins']+=1
            else:
                df.at[ind1,'5_Lose']+=1
            df.at[ind1,'6_WinP'] = win_1p

            rd = pd.DataFrame({'1_Player':player2,'2_Age':age2,'3_Total':1, '4_Wins':w2,'5_Lose':l2,'6_WinP':win_2p},index=[1])
            df= pd.concat([df,rd] , ignore_index = 'True',sort= 'True')

            df.sort_values('4_Wins',ascending=False,inplace=True)
            df.reset_index(drop=True,inplace = True)

            df.to_excel(file_path)

        elif ind2>(-1) and ind1==-1:
#If only player1 is new
            df.at[ind2,'3_Total']+=1
            if win_2>win_1:
                df.at[ind2,'4_Wins']+=1
            else:
                df.at[ind2,'5_Lose']+=1

            df.at[ind2,'6_WinP'] = win_2p

            rd = pd.DataFrame({'1_Player':player1,'2_Age':age1,'3_Total':1, '4_Wins':w1,'5_Lose':l1,'6_WinP':win_1p},index=[1])
            df= pd.concat([df,rd] , ignore_index = 'True',sort='True')

            df.sort_values('4_Wins',ascending=False,inplace=True)
            df.reset_index(drop=True,inplace = True)
            df.to_excel(file_path)
        else:            
#if Both are pre-existing Players defined in data base
            df.at[ind1,'3_Total']+=1
            if win_1>=win_2:
                df.at[ind1,'4_Wins']+=1
            else:
                df.at[ind1,'5_Lose']+=1
            df.at[ind1,'6_WinP'] = win_1p

            if win_2>=win_1:
                df.at[ind2,'4_Wins']+=1
            else:
                df.at[ind2,'5_Lose']+=1
            df.at[ind2,'6_WinP'] = win_2p

            df.sort_values('4_Wins',ascending=False,inplace=True)
            df.reset_index(drop=True,inplace = True)
            df.to_excel(file_path)

        print(df)

#main function
if __name__ == '__main__':
                         tic_tac_toe()
