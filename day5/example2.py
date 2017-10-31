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

  def move(self, keys):
    speed = self.speed
    if ((keys[self.controls['up']] or keys[self.controls['down']]) and
        (keys[self.controls['left']] or keys[self.controls['right']])):
      speed = self.speed * 2 ** .5

    if keys[self.controls['up']]:
      self.rect.coords[1] -= speed
    if keys[self.controls['down']]:
      self.rect.coords[1] += speed
    if keys[self.controls['left']]:
      self.rect.coords[0] -= speed
    if keys[self.controls['right']]:
      self.rect.coords[0] += speed

  def draw(self, window):
    pygame.draw.rect(window, self.color, self.rect.format())

  def check_boundaries(self, screen_size):
    for i in [0, 1]:
      if (self.rect.coords[i] < 0):
        self.rect.coords[i] = 0
      elif (self.rect.coords[i] >= screen_size[i] - self.rect.size[i]):
        self.rect.coords[i] = screen_size[i] - self.rect.size[i]

  def collided(self, rect):
    return self.rect.collided(rect)

  def reset(self):
    self.rect.coords = list(self.initial_coords)

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
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      exit()

  keys = pygame.key.get_pressed()
  for player in players:
    player.move(keys)
    player.check_boundaries(WINDOW_SIZE)

  if Rect.collided_list(list(map(lambda player: player.rect, players))):
    for player in players:
      player.reset()

  window.fill(pygame.Color('white'))

  for player in players:
    player.draw(window)

  pygame.display.update()
  clock.tick(60)
