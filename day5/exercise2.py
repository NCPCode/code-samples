import pygame


class Player:
  def __init__(self, color, coords, size, speed):
    self.color = color
    self.initial_coords = list(coords)
    self.coords = coords
    self.size = size
    self.speed = speed

  def move(self, direction):
    if direction == 'up':
      self.coords[1] -= self.speed
    elif direction == 'down':
      self.coords[1] += self.speed
    elif direction == 'left':
      self.coords[0] -= self.speed
    else:
      self.coords[0] += self.speed

  def draw(self, window):
    pygame.draw.rect(window, self.color, (self.coords, self.size))

  def check_boundaries(self, screen_size):
    for i in [0, 1]:
      if (self.coords[i] < 0):
        self.coords[i] = 0
      elif (self.coords[i] >= screen_size[i] - self.size[i]):
        self.coords[i] = screen_size[i] - self.size[i]

  def has_collided(self, player):
    return ((self.coords[0] < player.coords[0] + player.size[0]) and
            (player.coords[0] < self.coords[0] + self.size[0]) and
            (self.coords[1] < player.coords[1] + player.size[1]) and
            (player.coords[1] < self.coords[1] + self.size[1]))

  def reset(self):
    self.coords = list(self.initial_coords)

WINDOW_SIZE = [100, 100]
PLAYER_SIZE = [10, 10]

player1 = Player(
  pygame.Color('red'),
  [0, 0],
  PLAYER_SIZE,
  5
)
player2 = Player(
  pygame.Color('blue'),
  [WINDOW_SIZE[0] - PLAYER_SIZE[0], WINDOW_SIZE[1] - PLAYER_SIZE[1]],
  PLAYER_SIZE,
  2
)

window = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()


while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      exit()

  keys = pygame.key.get_pressed()
  if keys[pygame.K_RIGHT]:
    player1.move('right')
  elif keys[pygame.K_LEFT]:
    player1.move('left')
  if keys[pygame.K_UP]:
    player1.move('up')
  elif keys[pygame.K_DOWN]:
    player1.move('down')

  if keys[pygame.K_d]:
    player2.move('right')
  elif keys[pygame.K_a]:
    player2.move('left')
  if keys[pygame.K_w]:
    player2.move('up')
  elif keys[pygame.K_s]:
    player2.move('down')

  player1.check_boundaries(WINDOW_SIZE)
  player2.check_boundaries(WINDOW_SIZE)

  if player1.has_collided(player2):
    player1.reset()
    player2.reset()

  window.fill(pygame.Color('white'))

  player1.draw(window)
  player2.draw(window)

  pygame.display.update()
  clock.tick(60)
