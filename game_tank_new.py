from random import randint

class Tank:
    def __init__(self,
                 position = (5, 5),
                 movement = None,
                 target = None,
                 tank_direction = '<',
                 tank_coordinates = None,
                 tank_count_shoots = None,
                 tank_shoots_left = None,
                 tank_shoots_right = None,
                 tank_shoots_north = None,
                 tank_shoots_south = None):
        self.position = position
        self.movement = movement
        self.target = target
        self.tank_direction = tank_direction
        self.tank_coordinates = tank_coordinates
        self.tank_count_shoots = tank_count_shoots
        self.tank_shoots_left = tank_shoots_left
        self.tank_shoots_right = tank_shoots_right
        self.tank_shoots_north = tank_shoots_north
        self.tank_shoots_south = tank_shoots_south

    def generate_target(self):
       while True:
           self.target = (randint(6,9), randint(1,4))
           break

    def draw_table(self, bullet = None):
       for i in range(10):
           for y in range(10):
               if i == self.position[0] and y == self.position[1]:
                   print(self.tank_direction, end='')
               elif bullet and i == bullet[0] and y == bullet[1]:
                   print('*', end='')
               elif self.target and i == self.target[0] and y == self.target[1]:
                   print('0', end='')
               else:
                   print('_', end='')
           print()

    def move_tank(self, direction):
        if direction == '<' and self.position[1] > 0:
            self.position = (self.position[0], self.position[1] - 1)
            self.tank_direction = '<'
        elif direction == '>' and self.position[1] < 9:
            self.position = (self.position[0], self.position[1] + 1)
            self.tank_direction = '>'
        elif direction == '^' and self.position[1] > 0:
            self.position = (self.position[0] - 1, self.position[1])
            self.tank_direction = '^'
        elif direction == 'v' and self.position[1] < 9:
            self.position = (self.position[0] + 1, self.position[1])
            self.tank_direction = 'v'

    def shoot(self):
        bullet = None
        if self.tank_direction == '>':
            bullet = (self.position[0], self.position[1] + 1)
        elif self.tank_direction == '<':
            bullet = (self.position[0], self.position[1] - 1)
        elif self.tank_direction == '^':
            bullet = (self.position[0] - 1, self.position[1])
        elif self.tank_direction == 'v':
            bullet = (self.position[0] + 1, self.position[1])

        if bullet:
            self.draw_table(bullet)


tank = Tank()
tank.generate_target()
tank.draw_table()

while True:
    value = input('Enter Tank direction ( > , < , ^ , v ) or shoot (s): ')
    if value in '><^v':
        tank.move_tank(value)
    elif value == 's':
        tank.shoot()
    tank.draw_table()


