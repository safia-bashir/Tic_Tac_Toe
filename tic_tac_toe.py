
import random 
class Tic_Tac_Toe:
    def __init__ (self):
        self.board=[]
        
    def creata_board(self):
        
        for i in range(3):
            row=[]
            for j in range(3):
                row.append("-")
            self.board.append(row)
        return self.board
    
    
    
    def first_player(self):
        return random.randint(0,1)
    
    def swap_players(self,player):
        
        return "X" if player=="O" else "O"
    
    def fix_spot(self,row,column,player):
        self.board[row][column]=player
    
    
    
    def is_player_win(self,player):
        n=len(self.board)
        
        # checking rows
        for i in range(n):
            
            if all([self.board[i][j]==player for j in range(n)]):
                return True
        
        # checking columns:
        for i in range(n):
            if all([self.board[j][i]==player for j in range(n)]):
                return True 
        # checking digonal
        
        if all(self.board[i][i]==player for i in range(n)):
            
            return True 
        
        if all(self.board[i][n-1-i]==player for i in range(n)):
            return True
    
        return False
    
    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item=="-":
                    return False
        return True 
    def show_board(self):
        for row in self.board:
            for item in row:
                print(item,end="")
            print()
    
    

    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()
            
            
    def start_game(self):
        
        self.creata_board()
                
        player="X" if self.first_player()==1 else "O"
        while True:
            print(f"Player {player} turn")
            self.show_board()
            # asking the player for input 
            row,column=list(map(int,input("Enter row and column numbers to fix spot: ").split()))
            print()
            # fixing the spot 
            self.fix_spot(row-1, column-1, player)
            
            # checking if he won or not 
            if self.is_player_win(player):
                print(f"player{player} wins this game")
                break
            # checking if game is dran 
            if self.is_board_filled():
                print("Match Draw!")
                break
            # swap player 
            player=self.swap_players(player)
        # showing the final view of board
        print()
        self.show_board()
x=Tic_Tac_Toe()
x.start_game()



