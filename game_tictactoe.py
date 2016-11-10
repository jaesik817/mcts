from pymcts.uct import UCTNode
from pymcts.game.tic_tac_toe import TicTacToeState

s = TicTacToeState()
user=input("Which one do you want to play?(X:Black,O:White) :")
if(user=="O"):
  root=UCTNode(s)
  for _ in range(100):
    root.mc_round()
  s.do_move(root.best_move())
print("Game Start!!")  
print(repr(s))
while(1):
  move=input("Move Your Point (e.g. (0,0), (1,2)):")
  s.do_move((int(move[1]),int(move[3])))
  print(repr(s))
  if(s.result!=None):
    break
  print("His Turn...")
  root=UCTNode(s)
  for _ in range(100):
    root.mc_round()
  s.do_move(root.best_move())
  print(repr(s))
  if(s.result!=None):
    break
if(s.result[1]==0.5):
  print("The Result is TIE!!")
if(user=="O"):
  if(s.result[1]==1.0):
    print("Computer Win!!")
  if(s.result[2]==1.0):
    print("You Win!!")
if(user=="X"):
  if(s.result[2]==1.0):
    print("Computer Win!!")
  if(s.result[1]==1.0):
    print("You Win!!")
  
