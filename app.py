#test
#battle ships
import pygame

# Initialize pygame
pygame.init()

# Set up the screen
Black = (0,0,0)
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill((255, 255, 255))

#Load The images
imp = pygame.image.load("CRUZ.png")
imp = pygame.transform.scale(imp, (100,100))
imp2 = pygame.image.load("Nought.png")
imp2 = pygame.transform.scale(imp2, (100,100))

#initilize the font
font = pygame.font.SysFont("Arial", 32)

def RedrawGameWindow():

  screen.fill((255, 255, 255))
  
  global G00
  global G01
  global G02
  global G10
  global G11
  global G12
  global G20
  global G21
  global G22
  
  G00 =pygame.draw.rect(screen, Black, (250, 150, 100, 100), 1)

  G01 = pygame.draw.rect(screen, Black, (350, 150, 100, 100), 1)

  G02 = pygame.draw.rect(screen, Black, (450, 150, 100, 100), 1)  

  G10 = pygame.draw.rect(screen, Black, (250, 250, 100, 100), 1)
    
  G11 = pygame.draw.rect(screen, Black, (350, 250, 100, 100), 1)

  G12 =pygame.draw.rect(screen, Black, (450, 250, 100, 100), 1)

  G20 =pygame.draw.rect(screen, Black, (250, 350, 100, 100), 1)

  G21 = pygame.draw.rect(screen, Black, (350, 350, 100, 100), 1)

  G22 = pygame.draw.rect(screen, Black, (450, 350, 100, 100), 1)

  grid = [[" "," "," "],[" "," "," "],[" "," "," "]]
  
  pygame.display.flip()

def displayGrid(grid):
  print(" " + grid[0][0] + " | " + grid[0][1] + " | " + grid[0][2])
  print("-----------")
  print(" " + grid[1][0] + " | " + grid[1][1] + " | " + grid[1][2])
  print("-----------")
  print(" " + grid[2][0] + " | " + grid[2][1] + " | " + grid[2][2])

def checkGridX(grid):
  global RowMsg
  #Checks The Rows
  
  if grid[0][0]=="X" and grid[0][1]=="X" and grid[0][2]=="X":
    RowMsg = "Three Xs in a row."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print(RowMsg)
    #winner = True
      
    screen.blit(text2, text_rect2)
    text3 = font.render("Press R to restart", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)
      
  if grid[1][0]=="X" and grid[1][1]=="X" and grid[1][2]=="X":
    RowMsg = "Three Xs in a row."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print(RowMsg)
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Press R to restart", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)

  if grid[2][0]=="X" and grid[2][1]=="X" and grid[2][2]=="X":
    RowMsg = "Three Xs in a row."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Three Xs in a row.")
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Press R to restart", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)
  #Checks The Collums

  if grid[0][0]=="X" and grid[1][0]=="X" and grid[2][0]=="X":
    RowMsg = "Three Xs in a Collum."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Three Xs in a Collum.")
    screen.blit(text2, text_rect2)
    text3 = font.render("Press R to restart", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)
  
  if grid[0][1]=="X" and grid[1][1]=="X" and grid[2][1]=="X":
    RowMsg = "Three Xs in a Collum."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Three Xs in a Collum.")
    screen.blit(text2, text_rect2)
    text3 = font.render("Press R to restart", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)
  
  if grid[0][2]=="X" and grid[1][2]=="X" and grid[2][2]=="X":
    RowMsg = "Three Xs in a Collum."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Three Xs in a Collum.")
    screen.blit(text2, text_rect2)
    text3 = font.render("Press R to restart", True, (0, 0, 0))  
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)

  if grid[2][0]=="X" and grid[1][1]=="X" and grid[0][2]=="X":
    RowMsg = "Three Xs in a Diagonal."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Three Xs in a Diagonal.")
    screen.blit(text2, text_rect2)
    text3 = font.render("Press R to restart", True, (0, 0, 0))  
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)
  
  if grid[0][0]=="X" and grid[1][1]=="X" and grid[2][2]=="X":
    RowMsg = "Three Xs in a Diagonal."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Three Xs in a diagonal.")    
    screen.blit(text2, text_rect2)
    text3 = font.render("Press R to restart", True, (0, 0, 0))  
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)

def checkGrid0(grid):
  
  if grid[0][0]=="O" and grid[0][1]=="O" and grid[0][2]=="O":
    RowMsg = "Three 0s in a row."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Three 0s in a row.")
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Press R to restart", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)
  
  if grid[1][0]=="O" and grid[1][1]=="O" and grid[1][2]=="O":
    RowMsg = "Three 0s in a row."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Three 0s in a row.")
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Press R to restart", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)

  if grid[2][0]=="O" and grid[2][1]=="O" and grid[2][2]=="O":
    RowMsg = "Three 0s in a row."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Three 0s in a row.")
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Press R to restart", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)

  #Checks The Collums

  if grid[0][0]=="O" and grid[1][0]=="O" and grid[2][0]=="O":
    RowMsg = "Three 0s in a Collum."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Three 0s in a Collum.")
    #winner = Truez
    screen.blit(text2, text_rect2)
    text3 = font.render("Press R to restart", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)

  if grid[0][1]=="O" and grid[1][1]=="O" and grid[2][1]=="O":
    RowMsg = "Three 0s in a Collum."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Three 0s in a Collum.")
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Press R to restart", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)

  if grid[0][2]=="O" and grid[1][2]=="O" and grid[2][2]=="O":
    RowMsg = "Three 0s in a Collum."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Three 0s in a Collum.")
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Press R to restart", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)

  #Checks Diagonals

  if grid[2][0]=="O" and grid[1][1]=="O" and grid[0][2]=="O":
    RowMsg = "Three 0s in a diagonal."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Three Os in a Diagonal.")
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Press R to restart", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)
  
  if grid[0][0]=="O" and grid[1][1]=="O" and grid[2][2]=="O":
    RowMsg = "Three 0s in a diagonal."
    text2 = font.render(RowMsg, True, (0, 0, 0))
    print("Three Os in a diagonal.")
    #winner = True
    screen.blit(text2, text_rect2)
    text3 = font.render("Press R to restart", True, (0, 0, 0))  # Render the text
    text_rect3 = text.get_rect(center=(screen_width/2, 700))
    screen.blit(text3, text_rect3)

#Intializing More varibles
grid = [[" "," "," "],[" "," "," "],[" "," "," "]] #creates the Consle Reperezentaio of the Grid
Turn = True # Deterumins wether its X or Os turn
#winner = False

#Creates the Grid In Pygame


displayGrid(grid)
RedrawGameWindow()
# Set up the game loop
running = True
while running:
    # Handle events
  
    for event in pygame.event.get():
      
      #Mouse Detection
      #Checks For mouse clicking within each aquare
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_r:
          RedrawGameWindow()
          grid = [[" "," "," "],[" "," "," "],[" "," "," "]]
          Turn = True

      if event.type == pygame.MOUSEBUTTONDOWN:
          
          if G00.collidepoint(pygame.mouse.get_pos()):
            print ('CLICKED!')
            row = 0
            col = 0
            if "X" in grid[0][0] or "O" in grid[0][0]: # Checks wether the grid is empty
              print("stop")
            else:
              if Turn == True:
                grid[row][col] = "X"
                Turn = False
                screen.blit(imp, (250,150))
              else:
                screen.blit(imp2, (250, 150))
                grid[row][col] = "O"
                Turn = True
                checkGrid0(grid)
              
              
            
              displayGrid(grid)
            
              pygame.display.flip()
              checkGridX(grid)
          if G01.collidepoint(pygame.mouse.get_pos()):
            print ('CLICKED!')
            row = 0
            col = 1
            if "X" in grid[0][1] or "O" in grid[0][1]:
              print("Stop")
            else:
              if Turn == True:
                grid[row][col] = "X"
                Turn = False
                screen.blit(imp, (350,150))
              else:
                screen.blit(imp2, (350,150))
                grid[row][col] = "O"
                Turn = True
                checkGrid0(grid)
              displayGrid(grid)

              pygame.display.flip()
              checkGridX(grid)
              
          if G02.collidepoint(pygame.mouse.get_pos()):
            print ('CLICKED!')
            row = 0
            col = 2
            if "X" in grid[0][2] or "O" in grid[0][2]:
              print("Stop")
            else:
              if Turn == True:
                grid[row][col] = "X"
                Turn = False
                screen.blit(imp, (450,150))
              else:
                screen.blit(imp2, (450,150))
                grid[row][col] = "O"
                Turn = True
                checkGrid0(grid)
                displayGrid(grid)
              
              pygame.display.flip()
              checkGridX(grid)
          if G10.collidepoint(pygame.mouse.get_pos()):
            print ('CLICKED!')
            row = 1
            col = 0
            if "X" in grid[1][0] or "O" in grid[1][0]:
              print("Stop")
            else:
              if Turn == True:
                screen.blit(imp, (250,250))
                grid[row][col] = "X"
                Turn = False
              else:
                screen.blit(imp2, (250,250))
                grid[row][col] = "O"
                Turn = True
                checkGrid0(grid)
              displayGrid(grid)
            
              pygame.display.flip()
              checkGridX(grid)
          if G11.collidepoint(pygame.mouse.get_pos()):
            print ('CLICKED!')
            row = 1
            col = 1
            if "X" in grid[1][1] or "O" in grid[1][1]:
              print("Stop")
            else:
              if Turn == True:
                screen.blit(imp, (350,250))
                grid[row][col] = "X"
                Turn = False
              else:
                screen.blit(imp2, (350,250))
                grid[row][col] = "O"
                Turn = True
                checkGrid0(grid)
              displayGrid(grid)
            
              pygame.display.flip()
              checkGridX(grid)
          if G12.collidepoint(pygame.mouse.get_pos()):
            print ('CLICKED!')
            row = 1
            col = 2
            if "X" in grid[1][2] or "O" in grid[1][2]:
              print("Stop")
            else:
              if Turn == True:
                screen.blit(imp, (450,250))
                grid[row][col] = "X"
                Turn = False
              else:
                screen.blit(imp2, (450,250))
                grid[row][col] = "O"
                Turn = True
                checkGrid0(grid)
              displayGrid(grid)
              
              pygame.display.flip()
              checkGridX(grid)
          if G20.collidepoint(pygame.mouse.get_pos()):
            print ('CLICKED!')
            row = 2
            col = 0
            if "X" in grid[2][0] or "O" in grid[2][0]:
              print("Stop")
            else:
              if Turn == True:
                screen.blit(imp, (250,350))
                grid[row][col] = "X"
                Turn = False
              else:
                screen.blit(imp2, (250,350))
                grid[row][col] = "O"
                Turn = True
                checkGrid0(grid)
              displayGrid(grid)
              
              pygame.display.flip()
              checkGridX(grid)
          if G21.collidepoint(pygame.mouse.get_pos()):
            print ('CLICKED!')
            row = 2
            col = 1
            if "X" in grid[2][1] or "O" in grid[2][1]:
              print("Stop")
            else:
              if Turn == True:
                screen.blit(imp, (350,350))
                grid[row][col] = "X"
                Turn = False
                
              else:
                screen.blit(imp2, (350,350))
                grid[row][col] = "O"
                Turn = True
                checkGrid0(grid)
              displayGrid(grid)
              
              pygame.display.flip()
              checkGridX(grid)
          if G22.collidepoint(pygame.mouse.get_pos()):
            print ('CLICKED!')
            row = 2
            col = 2
            if "X" in grid[2][2] or "O" in grid[2][2]:
              print("Stop")
            else:
              if Turn == True:
                screen.blit(imp, (450,350))
                grid[row][col] = "X"
                Turn = False
                checkGridX(grid)
              else:
                screen.blit(imp2, (450,350))
                
                grid[row][col] = "O"
                Turn = True
                checkGrid0(grid)
                
              displayGrid(grid)
              
              pygame.display.flip()
              checkGridX(grid)

      if event.type == pygame.QUIT: #Checks whether you pressed the X button
        running = False
    
    text = font.render("Tic Tac toe ", True, (0, 0, 0))  # Render the text
    text_rect = text.get_rect(center=(screen_width/2, 100))  # Get the rectangle for the text
    
    #text2 = font.render(RowMsg, True, (0, 0, 0))  # Render the text
    text_rect2 = text.get_rect(center=(350, 500))
    
    screen.blit(text, text_rect)
def imprimir_tablero(tablero):
    for fila in tablero:
        print(" | ".join(fila))
        print("-" * 5)

def imprimir_tablero(tablero):
    for fila in tablero:
        print(" | ".join(fila))
        print("-" * 5)

def verificar_ganador(tablero):
    # Verificar filas y columnas
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != ' ':
            return tablero[i][0]
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != ' ':
            return tablero[0][i]

    # Verificar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != ' ':
        return tablero[0][0]
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != ' ':
        return tablero[0][2]

    return None

def jugar():
    tablero = [[' ' for _ in range(3)] for _ in range(3)]
    jugador = 'X'
    puntaje_x = 0
    puntaje_o = 0

    while True:
        imprimir_tablero(tablero)

        fila = int(input(f"Ingrese la fila (0, 1, 2) para {jugador}: "))
        columna = int(input(f"Ingrese la columna (0, 1, 2) para {jugador}: "))

        if tablero[fila][columna] == ' ':
            tablero[fila][columna] = jugador
        else:
            print("¡Esa casilla ya está ocupada! Inténtelo de nuevo.")
            continue

        ganador = verificar_ganador(tablero)

        if ganador:
            imprimir_tablero(tablero)
            print(f"¡El jugador {ganador} ha ganado!")
            if ganador == 'X':
                puntaje_x += 1
            else:
                puntaje_o += 1
            print(f"Puntaje - X: {puntaje_x}, O: {puntaje_o}")
            seguir_jugando = input("¿Quieres jugar otra vez? (s/n): ")
            if seguir_jugando.lower() != 's':
                break
            else:
                tablero = [[' ' for _ in range(3)] for _ in range(3)]
                continue

        if all(tablero[i][j] != ' ' for i in range(3) for j in range(3)):
            imprimir_tablero(tablero)
            print("¡Empate!")
            seguir_jugando = input("¿Quieres jugar otra vez? (s/n): ")
            if seguir_jugando.lower() != 's':
                break
            else:
                tablero = [[' ' for _ in range(3)] for _ in range(3)]
                continue

        jugador = 'O' if jugador == 'X' else 'X'

if __name__ == "__main__":
    jugar()
