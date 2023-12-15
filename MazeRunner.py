import pygame

class MazeGame:
     def __init__(self):
          pygame.init()
          self.cell_size = 30
          self.total_time = 500
          self.time_left = self.total_time
          self.grid = [
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 1, 1, 1, 0, 2, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0],
               [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
               [0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0],
               [0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0],
               [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0],
               [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
               [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
               [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
               [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
               [0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0],
               [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0],
               [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
               [0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
               [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
               [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
               [0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
               [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
               [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0],
               [0, 0, -2, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
          self.grid_width = len(self.grid[0])
          self.grid_height = len(self.grid)
          self.screen_width = self.cell_size * self.grid_width
          self.screen_height = self.cell_size * self.grid_height
          self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
          pygame.display.set_caption("Maze Runner")
          self.bar_width = self.screen_width
          self.running = True
          self.fps = 11
          self.maze_surface = pygame.Surface((self.screen_width, self.screen_height))
          self.maze_surface.fill((255, 255, 255))
          self.draw_maze()
          self.screen.blit(self.maze_surface, (0, 0))
          self.player = Player(self)
          self.clock = pygame.time.Clock()

     def draw_maze(self):
          color_set = {1: (255, 255, 255), 0: (0, 0, 0), -2: (0, 0, 255), 2: (0, 255, 0)}
          for row in range(self.grid_height):
               for col in range(self.grid_width):
                    pygame.draw.rect(self.maze_surface, color_set.get(self.grid[row][col]), (col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size))

     def game_over_screen(self):
          game_over_surface = pygame.Surface((self.screen_width, self.screen_height), pygame.SRCALPHA)
          pygame.draw.rect(game_over_surface, (255, 0, 0, 128), (0, 0, self.screen_width, self.screen_height))
          font = pygame.font.Font(None, 36)
          font.set_bold(True)
          text = font.render("Game Over", True, (255, 255, 255))
          text_rect = text.get_rect(center=(self.screen_width // 2, self.screen_height // 2))
          game_over_surface.blit(text, text_rect)
          self.screen.blit(game_over_surface, (0, 0))
          pygame.display.flip()

     def run(self):
          while self.running:
               for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                         self.running = False
                         pygame.quit()
                         return

               self.time_left -= 1
               bar_width = self.screen_width * self.time_left / self.total_time
               pygame.draw.rect(self.screen, (255, 255, 255), (0, 10, self.screen_width, 7))
               pygame.draw.rect(self.screen, (255, 0, 0), (0, 10, bar_width, 7))
               pygame.display.flip()

               if self.time_left == 0:
                    print("Game Over: Timeout")
                    self.game_over_screen()
                    self.running = False
                    break

               if self.player.check_win():
                    print("Game Over: player won")
                    self.game_over_screen()
                    self.running = False
                    break

               self.player.handle_input()
               self.clock.tick(self.fps)

class Player:
     def __init__(self, game):
          self.game = game
          self.row, self.col = self.find_player_position()
          self.calc_pos()

     def find_player_position(self):
          for row_idx, row in enumerate(self.game.grid):
               if -2 in row:
                    return row_idx, row.index(-2)
          return 0, 0

     def calc_pos(self):
          self.y = self.game.cell_size * self.row + 5
          self.x = self.game.cell_size * self.col + 5

     def move(self, direction):
          if self.check_valid_move(direction):
               if direction == "UP":
                    self.row -= 1
               elif direction == "DOWN":
                    self.row += 1
               elif direction == "RIGHT":
                    self.col += 1
               else:
                    self.col -= 1
               self.calc_pos()
               self.game.screen.blit(self.game.maze_surface, (0, 0))
               self.draw()
               pygame.display.flip()

     def draw(self):
          pygame.draw.rect(self.game.screen, (255, 0, 0), (self.x, self.y, 20, 20))

     def check_valid_move(self, direction):
          if direction == "UP":
               return bool(self.game.grid[self.row - 1][self.col])
          elif direction == "DOWN":
               return bool(self.game.grid[self.row + 1][self.col])
          elif direction == "RIGHT":
               return bool(self.game.grid[self.row][self.col + 1])
          else:
               return bool(self.game.grid[self.row][self.col - 1])

     def check_win(self):
          return self.game.grid[self.row][self.col] == 2

     def handle_input(self):
          keys = pygame.key.get_pressed()
          if keys[pygame.K_LEFT]:
               self.move("LEFT")
          if keys[pygame.K_RIGHT]:
               self.move("RIGHT")
          if keys[pygame.K_UP]:
               self.move("UP")
          if keys[pygame.K_DOWN]:
               self.move("DOWN")



if __name__ == "__main__":
     game = MazeGame()
     game.run()
     Quit = False
     while not Quit:
          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    pygame.quit()
                    Quit = True
