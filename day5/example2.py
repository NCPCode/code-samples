import pygame

class Rect:
  def __init__(self, coords, size):
    self.coords = coords
    self.size = size

  def collided(self, rect):
    return ((self.coords[0] < rect.coords[0] + rect.size[0]) and
            (rect.coords[0] < self.coords[0] + self.size[0]) and
            (self.coords[1] < rect.coords[1] + rect.size[1]) and
            (rect.coords[1] < self.coords[1] + self.size[1]))

  def format(self):
    return (self.coords, self.size)

  @staticmethod
  def collided_list(rect_list):
    for i, rect in enumerate(rect_list):
      for rect2 in rect_list[i + 1:]:
        if rect.collided(rect2):
          return True
    return False


class Player:
  def __init__(self, color, coords, size, speed, controls):
    self.color = color
    self.initial_coords = list(coords)
    self.rect = Rect(coords, size)
    self.speed = speed
    self.controls = controls
    self.reset()

  def process_key_change(self, key, value):
    for direction in self.controls:
      if self.controls[direction] == key:
        self.directions[direction] = value

  def move(self):
    speed = self.speed
    if ((self.controls['up'] or self.controls['down']) and
        (self.controls['left'] or self.controls['right'])):
      speed = self.speed * 2 ** .5

    if self.directions['up']:
      self.rect.coords[1] -= speed
    elif self.directions['down']:
      self.rect.coords[1] += speed
    if self.directions['left']:
      self.rect.coords[0] -= speed
    elif self.directions['right']:
      self.rect.coords[0] += speed

  def draw(self, window):
    pygame.draw.rect(window, self.color, self.rect.format())

  def check_boundaries(self, screen_size):
    for i in [0, 1]:
      if (self.rect.coords[i] < 0):
        self.rect.coords[i] = 0
      elif (self.rect.coords[i] >= screen_size[i] - self.rect.size[i]):
        self.rect.coords[i] = screen_size[i] - self.rect.size[i]

  def reset(self):
    self.rect.coords = list(self.initial_coords)
    self.directions = {'right': False, 'left': False, 'up': False, 'down': False}


WINDOW_SIZE = [100, 100]
PLAYER_SIZE = [10, 10]

players = [
  Player(
    pygame.Color('red'),
    [0, 0],
    PLAYER_SIZE,
    2,
    {
      'right': pygame.K_d,
      'left': pygame.K_a,
      'up': pygame.K_w,
      'down': pygame.K_s
    }
  ),
  Player(
    pygame.Color('blue'),
    [WINDOW_SIZE[0] - PLAYER_SIZE[0], WINDOW_SIZE[1] - PLAYER_SIZE[1]],
    PLAYER_SIZE,
    5,
    {
      'right': pygame.K_RIGHT,
      'left': pygame.K_LEFT,
      'up': pygame.K_UP,
      'down': pygame.K_DOWN
    }
  )
]

window = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()


while True:
  # INPUT
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      exit()

    if event.type == pygame.KEYDOWN:
      for player in players:
        player.process_key_change(event.key, True)

    elif event.type == pygame.KEYUP:
      for player in players:
        player.process_key_change(event.key, False)

  # PROCESSING
  for player in players:
    player.move()
    player.check_boundaries(WINDOW_SIZE)

  if Rect.collided_list(list(map(lambda player: player.rect, players))):
    for player in players:
      player.reset()

  # DISPLAY
  window.fill(pygame.Color('white'))

  for player in players:
    player.draw(window)

  pygame.display.update()
  clock.tick(60)
