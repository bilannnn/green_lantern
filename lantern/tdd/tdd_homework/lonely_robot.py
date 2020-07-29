

class Asteroid:
    def __init__(self, x, y, obstacles_x, obstacles_y):
        self.x = x
        self.y = y
        self.obstacles_x = obstacles_x
        self.obstacles_y = obstacles_y
        if self.obstacles_x > self.x:
            raise ObstaclesValueError()
        if self.obstacles_y > self.y:
            raise ObstaclesValueError()


class Robot:
    def __init__(self, x, y, asteroid, direction):
        step = 1
        self.x = x
        self.y = y
        self.direction = direction
        self.asteroid = asteroid
        self.step = step
        if self.x > self.asteroid.x:
            raise MissAsteroidError()
        if self.y > self.asteroid.y:
            raise MissAsteroidError()
        if self.step <= 0:
            raise StepValueError()

    def turn_left(self):
        turns = {"E": "N",
                 "N": "W",
                 "W": "S",
                 "S": "E"
                 }
        self.direction = turns[self.direction]

    def turn_right(self):
        turns = {"N": "E",
                 "E": "S",
                 "W": "N",
                 "S": "W"
                 }
        self.direction = turns[self.direction]

    # def limitation_x(self):
    #     # pass
    #     if self.x + self.step <= self.asteroid.x:
    #         return True
    #     raise StopObstaclesError()
    #
    # def limitation_y(self):
    #     # pass
    #     if self.y + self.step <= self.asteroid.y:
    #         return True
    #     raise StopObstaclesError()

    # def obstacles_move_x(self):
    #     if self.x + self.step != self.asteroid.obstacles_x:
    #         return True
    #     raise StopObstaclesError()
    #
    # def obstacles_move_y(self):
    #     if self.y + self.step != self.asteroid.obstacles_y:
    #         return True
    #     raise StopObstaclesError()

    def move_forward(self):
        if self.direction == "N" and self.y + self.step <= self.asteroid.y and self.y + self.step != self.asteroid.obstacles_y:
            self.y += self.step
        elif self.direction == "S" and self.y - self.step >= 0 and self.y - self.step != self.asteroid.obstacles_y:
            self.y -= self.step
        elif self.direction == "E" and self.x + self.step <= self.asteroid.x and self.x + self.step != self.asteroid.obstacles_x:
            self.x += self.step
        elif self.direction == "W" and self.x - self.step >= 0 and self.x - self.step != self.asteroid.obstacles_x:
            self.x -= self.step
        else:
            raise StopObstaclesError()

    def move_backward(self):
        if self.direction == "N" and self.y - self.step >= 0 and self.y - self.step != self.asteroid.obstacles_y:
            self.y -= self.step
        elif self.direction == "S" and self.y + self.step <= self.asteroid.y and self.y + self.step != self.asteroid.obstacles_y:
            self.y += self.step
        elif self.direction == "E" and self.x - self.step >= 0 and self.x - self.step != self.asteroid.obstacles_x:
            self.x -= self.step
        elif self.direction == "W" and self.x + self.step <= self.asteroid.x and self.x + self.step != self.asteroid.obstacles_x:
            self.x += self.step
        else:
            raise StopObstaclesError()


class MissAsteroidError(Exception):
    pass


class StepValueError(Exception):
    pass


class ObstaclesValueError(Exception):
    pass


class StopObstaclesError(Exception):
    pass


# ast_1 = Asteroid(20, 25, 8, 22)
# rob_1 = Robot(16, 24, ast_1, "S")
# print(rob_1.move_backward())

# print(rob_1.move_forward())