# File: CS112_A1_T6_Game2_20230333
# Purpose: tic tac toe by numbers
# Author: Muhammed khalid hamed EL_Mekawy
# ID : 20230333
pp=['1','2']
rr=1
while rr==1:
    print("1) play")
    print("2) exit")
    pl_no = input()
    if pl_no in pp:
        if pl_no=='1':
            board = ("""
                  0 | 1 | 2     
                 ---|---|---
                  3 | 4 | 5
                 ---|---|---
                  6 | 7 | 8""")#to understand the board
            print(board)
            dig = [''] * 9 #list of digits
            played_n_time = 0
            def the_board(): # the input fun
                c_board = f"""
                  {dig[0]:^3} | {dig[1]:^3} | {dig[2]:^3}      0 | 1 | 2 
                 -----|-----|-----    ---|---|---
                  {dig[3]:^3} | {dig[4]:^3} | {dig[5]:^3}      3 | 4 | 5
                 -----|-----|-----    ---|---|---
                  {dig[6]:^3} | {dig[7]:^3} | {dig[8]:^3}      6 | 7 | 8
                  """
                print(c_board)
                return dig
            def win (the_winner): # wining conditions
                if (dig[0]!= '' and dig[1]!= '' and dig[2] != ''):
                    if (int(dig[0]) + int(dig[1]) + int(dig[2]) == 15):
                        print('** you win ', the_winner,' **')
                        return True
                if (dig[3]!= '' and dig[4]!= '' and dig[5] != ''):
                    if (int(dig[3]) + int(dig[4]) + int(dig[5]) == 15):
                        print('** you win ', the_winner,' **')
                        return True
                if (dig[6]!= '' and dig[7]!= '' and dig[8] != ''):
                    if (int(dig[6]) + int(dig[7]) + int(dig[8]) == 15):
                        print('** you win ', the_winner,' **')
                        return True
                if (dig[0]!= '' and dig[3]!= '' and dig[6] != ''):
                    if (int(dig[3]) + int(dig[0]) + int(dig[6]) == 15):
                        print('** you win ', the_winner,' **')
                        return True
                if (dig[4]!= '' and dig[1]!= '' and dig[7] != ''):
                    if (int(dig[4]) + int(dig[1]) + int(dig[7]) == 15):
                        print('** you win ', the_winner,' **')
                        return True
                if (dig[8]!= '' and dig[5]!= '' and dig[2] != ''):
                    if (int(dig[8]) + int(dig[5]) + int(dig[2]) == 15):
                        print('** you win ', the_winner,' **')
                        return True
                if (dig[4]!='' and dig[6]!='' and dig[2] != ''):
                    if (int(dig[4]) + int(dig[6]) + int(dig[2]) == 15):
                        print('** you win ', the_winner,' **')
                        return True
                if (dig[0]!='' and dig[4]!='' and dig[8] != ''):
                    if (int(dig[0]) + int(dig[4]) + int(dig[8]) == 15):
                        print('** you win ', the_winner,' **')
                        return True
            plyer1_list = ['1', '3', '5', '7', '9'] # where player 1 can play
            player2_list = ['0', '2', '4', '6', '8'] # where player 2 can play
            game_d = ['0', '1', '2', '3', '4', '5', '6', '7', '8'] # the board digits
            while played_n_time <= 9: # game loop
                if(played_n_time%2==0): # to switch between players
                        print('take from ', plyer1_list)
                        place_index1 = input('where player1):') #the index of digit
                        plyer1_index = input('what player1):') # the numer will p1 take
                        if(place_index1 in game_d and plyer1_index  in plyer1_list): # check
                            dig[int(place_index1)] = int(plyer1_index) # using the input
                            played_n_time += 1
                            plyer1_list.remove(plyer1_index) # remove what we used
                            game_d.remove(place_index1) # remove what we used
                            the_board()
                            player1__= "player1"
                            if (win(player1__) == True):# wining
                                break
                        else:
                            print('enter valid input player1') # invalid input
                            continue
                elif(played_n_time % 2 == 1 and played_n_time != 9): # p2 round
                        print('take from ', player2_list)
                        place_index2 = input('where player2):') # digit index
                        player_index2 = input('what player2):') # the num
                        if(place_index2 in game_d and player_index2 in player2_list): # check
                            dig[int(place_index2)] = int(player_index2)
                            played_n_time += 1
                            player2_list.remove(player_index2)
                            game_d.remove(place_index2)
                            the_board()
                            player2__= "player2"
                            if (win(player2__) == True):
                                break
                        else:
                            print('enter valid input player2')
                            continue
                elif(played_n_time == 9): # board filled without winner
                    print('draw')
                    played_n_time += 1
        while pl_no=='2':
          rr=0
          break
    elif (pl_no not in pp):
        print("enter valid input")
