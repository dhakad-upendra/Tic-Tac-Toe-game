import random


# this function is for generating game board
def display_board(board):
    print("+------" *3, "+", sep="")
    for row in range(3):
        print("|      " * 3,"|", sep="")
        for colmn in range(3):
            print(f"|  {str(board[row][colmn])}   ", end="" )
            
        print("|")
        print("|      " * 3,"|", sep="")
        print("+------" *3, "+", sep="")
        


def row_column_detect(n,board):
    # this fnctn detects the position of item in the list 
    row_num = n //3
    colmn_num = n%3
    board[row_num][colmn_num]
    return  board[row_num][colmn_num], row_num, colmn_num

 
             
def check_free(board,row_column_detect,n,sign ):
    avail = False
    # this fnctn is checking the box if filled or not and to fill the box
    free_box = []
    for i in range(3):
        for j in range(3):
            if board[i][j] not in ["X","0"]:
                free_box.append(board[i][j])
    
    move_board_item, move_row, move_col = row_column_detect(n,board)
    if board[move_row][move_col] in free_box:
              avail = True  
              board[move_row][move_col] = sign
    return  avail 


    
  # This functn checks who is winner 
def victor(board):
    winner = None
    victory = False
    for i in range(3):
       if board[i][0] == board[i][1] == board[i][2]:
           victory = True
           if board[i][0] == '0' :
               winner = 'You'
           else:
               winner = 'Computer'    
        
           break
     
    
    if not victory:
        for i in range(3):
             if board[0][i] == board[1][i] == board[2][i]:
                 victory = True
                 if board[0][i] == '0' :
                     winner = 'You'
                 else:
                     winner = 'Computer'    
        
                 break
        
    if not victory:
        if board[0][0] == board[1][1] == board[2][2]:
                 victory = True
                 if board[0][0] == '0' :
                     winner = 'You'
                 else:
                     winner = 'Computer' 
    
    if not victory:
        if board[0][2] == board[1][1] == board[2][0]:
                 victory = True
                 if board[2][0] == '0' :
                     winner = 'You'
                 else:
                     winner = 'Computer'               
        
                     
    return winner, victory



#the main program starts from here
                   
board = [ [3 * j + i + 1 for i in range(3)] for j in range(3) ] 
victory = False 

while not victory:
    display_board(board) 
    okay = True
    while  okay:
        n = int(input("Enter the number: "))
        if n < 0 or n >= 9:
             print(''' 
                              -----------Bad input--------------
                                Please enter the number again.
                              The number should be between 1-9.
                                 Please repeat your input
                          
                        ''')
            
             okay = True
        else:
            okay = False
    
        n = n-1  # this is for making row and column calculation easy
        sign = '0'                                      
        if not check_free(board,row_column_detect,n,sign):
            print(''' 
                              -----------Bad input--------------
                                Please enter the number again.
                                The place is already occupied.
                                 Please repeat your input
                          
                        ''')
            okay = True 
        else: 
            okay = False
    
    
    
    comp_turn = True
    while comp_turn:
        n = random.randint(1,9)
        n = n - 1 
        sign = 'X'
        if not check_free(board,row_column_detect,n,sign):
            comp_turn = True 
        else: 
            comp_turn = False
        
    
    
    
    
    winner, victory = victor(board)
    if victory:
        print(f'''
                   The winner of the game is {winner} 
                   
                   \n''')
        display_board(board) 
                    

      
    
        

          
  





       
           