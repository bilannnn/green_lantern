
import pytest
from lonely_robot import Robot, Asteroid, MissAsteroidError, ObstaclesValueError


class TestRobotCreationAndAsteroid:
    def test_parameters(self):
        x, y = 10, 15
        obstacles_x, obstacles_y = 15, 15
        ast_x, ast_y = 20, 20
        asteroid = Asteroid(ast_x, ast_y, obstacles_x, obstacles_y)
        direction = "E"
        robot = Robot(x, y, asteroid, direction)
        assert robot.x == 10
        assert robot.y == 15
        assert robot.direction == direction
        assert robot.asteroid == asteroid


    @pytest.mark.parametrize(
        "asteroid_size,robot_coordinates",
        (
            ((15, 25), (26, 30)),
            ((15, 25), (26, 24)),
            ((15, 25), (15, 27)),
        )
    )
    def test_check_if_robot_on_asteroid(self, asteroid_size, robot_coordinates):
        with pytest.raises(MissAsteroidError):
             asteroid = Asteroid(*asteroid_size, 15, 15)
             robot = Robot(*robot_coordinates, asteroid, "W")

    @pytest.mark.parametrize(
        "asteroid_size,obstacles_coordinates",
        (
                ((15, 25), (26, 30)),
                ((15, 25), (26, 24)),
                ((15, 25), (15, 27)),
        )
    )
    def test_check_if_obstacles_on_asteroid(self, asteroid_size, obstacles_coordinates):
        with pytest.raises(ObstaclesValueError):
            asteroid = Asteroid(*asteroid_size, *obstacles_coordinates)

class TestMovingRobot:

    def setup(self):
        self.direction = "W"
        x, y = 10, 15
        self.x = x
        self.y = y
        self.asteroid = Asteroid(self.x + 10, self.y + 10, self.x + 3, self.y + 3)
        self.step = 1

    @pytest.mark.parametrize(
        "current_direction,expected_direction",
        (
                ("N", "W"),
                ("W", "S"),
                ("S", "E"),
                ("E", "N")
        )
    )
    def test_turn_left(self, current_direction, expected_direction):
        robot = Robot(self.x, self.y, self.asteroid, current_direction)
        robot.turn_left()
        assert robot.direction == expected_direction

    @pytest.mark.parametrize(
        "current_direction,expected_direction",
        (
                ("N", "E"),
                ("E", "S"),
                ("S", "W"),
                ("W", "N")
        )
    )
    def test_turn_right(self, current_direction, expected_direction):
        robot = Robot(self.x, self.y, self.asteroid, current_direction)
        robot.turn_right()
        assert robot.direction == expected_direction

    @pytest.mark.parametrize(
        "current_direction,coordinate",
        (
                ("N", 16),
                ("E", 11),
                ("S", 14),
                ("W", 9)
                # ("R", 12)
        )
    )
    def test_move_forward(self, current_direction, coordinate):
        robot = Robot(self.x, self.y, self.asteroid, current_direction)
        robot.move_forward()
        assert robot.y == coordinate or robot.x == coordinate

    @pytest.mark.parametrize(
        "current_direction,coordinate",
        (
                ("N", 14),
                ("E", 9),
                ("S", 16),
                ("W", 11)
        )
    )
    def test_move_backward(self, current_direction, coordinate):
        robot = Robot(self.x, self.y, self.asteroid, current_direction)
        robot.move_backward()
        assert robot.y == coordinate or robot.x == coordinate

    # @pytest.mark.parametrize(
    #     "robot_coordinate,asteroid_coordinate",
    #     (
    #             (11, True),
    #
    #     )
    # )
    # def test_limitation_x(self, robot_coordinate, asteroid_coordinate):
    #     self.asteroid.x = 15
    #     robot = Robot(robot_coordinate, self.y, self.asteroid, self.direction)
    #     assert robot.limitation_x() == asteroid_coordinate
    #
    # @pytest.mark.parametrize(
    #     "robot_coordinate,asteroid_coordinate",
    #     (
    #             (11, True),
    #
    #
    #     )
    # )
    # def test_limitation_y(self, robot_coordinate, asteroid_coordinate):
    #     self.asteroid.y = 15
    #     robot = Robot(self.x, robot_coordinate, self.asteroid, self.direction)
    #     assert robot.limitation_y() == asteroid_coordinate
