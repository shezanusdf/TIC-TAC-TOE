positions = [[' ',' ',' '],
             [' ',' ',' '],
             [' ',' ',' ']]

count = 0

def main():
        drawBoard()
        while True:
                moves("X")
                drawBoard()
                if checkWin():
                        break
                if checkdraw():
                        break
                moves("O")
                drawBoard()
                if checkWin():
                        break
                
# Draw Board
def drawBoard():
        count = 0
        for i in positions:
                print(" | ".join(i))
                count += 1
                if count <= 2:
                        print('---------')
def moves(symbol):
        while True:
                try:
                        pos = int(input("Enter Position for {} (1-9): ".format(symbol)))
                except ValueError: 
                        print("Enter integer value!")
                        continue
                if 1 <= pos <= 9:
                        row = (pos - 1) // 3
                        col = (pos - 1) % 3
                        if positions[row][col] == " ":
                                positions[row][col] = symbol
                                break
                else:
                        print("Enter valid value!")
                        continue

def checkWin():
        for i in positions:
                result = "".join(i)
                if result == "XXX":
                        print("X Wins thru a straight row!")
                        return True
                elif result == "OOO":
                        print("O wins!")
                        return True

        for i in range(3):
                if positions[0][i] == positions[1][i] == positions[2][i] == "X":
                        print("X wins thru a column!")
                        return True
                elif positions[0][i] == positions[1][i] == positions[2][i] == "O":
                        print("O wins!")
                        return True
                if positions[0][0] == positions[1][1] == positions[2][2]:
                        if positions[0][0] == "X":
                                print("X wins DIAGONALLY!")
                                return True
                        elif positions[0][0] == "O":
                                print("O wins !")
                                return True
                elif positions[0][2] == positions[1][1] == positions[2][0] != " ":
                        if positions[1][1] == "X":
                                print("X wins!")
                                return True
                        elif positions[1][1] == "O":
                                print("O wins!")
                                return True
                
def checkdraw():
        count = 0   
        for i in positions:
                for x in range(3):
                        if i[x] == " ":
                                count += 1
        if count == 0:
                return True
        





if __name__ == "__main__":
        main()