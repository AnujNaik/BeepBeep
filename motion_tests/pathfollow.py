import pygame
import math

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mecanum Drivetrain - Bezier Curve Path")

# Mecanum Drivetrain Constants
WHEEL_RADIUS = 20
ROBOT_WIDTH = 2 * WHEEL_RADIUS
ROBOT_LENGTH = 3 * WHEEL_RADIUS
MOTOR_POWER_SCALE = 0.5

# Bezier Curve Control Points
control_points = [(100, 400), (300, 100), (500, 500), (700, 200)]

# Initialize Robot Position and Orientation
robot_x = control_points[0][0]
robot_y = control_points[0][1]
robot_angle = 0

# Initialize Motor Powers
motor_powers = [0, 0, 0, 0]  # Front Left, Front Right, Rear Left, Rear Right

# Calculate Bezier Curve Points
num_points = 100
curve_points = []
for i in range(num_points):
    t = i / (num_points - 1)
    x = (1 - t) ** 3 * control_points[0][0] + 3 * (1 - t) ** 2 * t * control_points[1][0] + \
        3 * (1 - t) * t ** 2 * control_points[2][0] + t ** 3 * control_points[3][0]
    y = (1 - t) ** 3 * control_points[0][1] + 3 * (1 - t) ** 2 * t * control_points[1][1] + \
        3 * (1 - t) * t ** 2 * control_points[2][1] + t ** 3 * control_points[3][1]
    curve_points.append((x, y))


def update_robot():
    global robot_x, robot_y, robot_angle, current_point_index

    # Update Robot Position
    robot_x = curve_points[current_point_index][0]
    robot_y = curve_points[current_point_index][1]

    # Update Robot Orientation
    if current_point_index < num_points - 1:
        dx = curve_points[current_point_index + 1][0] - robot_x
        dy = curve_points[current_point_index + 1][1] - robot_y
        desired_angle = math.atan2(dy, dx)

        # Gradually rotate the robot towards the desired angle
        max_rotation_speed = math.radians(2)  # Adjust the rotation speed as needed
        angle_diff = desired_angle - robot_angle
        if angle_diff > math.pi:
            angle_diff -= 2 * math.pi
        elif angle_diff < -math.pi:
            angle_diff += 2 * math.pi
        if angle_diff > max_rotation_speed:
            angle_diff = max_rotation_speed
        elif angle_diff < -max_rotation_speed:
            angle_diff = -max_rotation_speed

        robot_angle += angle_diff

    # Increment Current Point Index
    current_point_index += 1


def calculate_motor_powers():
    global motor_powers

    # Calculate Robot Velocity
    dx = curve_points[current_point_index][0] - robot_x
    dy = curve_points[current_point_index][1] - robot_y
    distance = math.sqrt(dx ** 2 + dy ** 2)

    # Calculate Robot Angular Velocity
    desired_angle = math.atan2(dy, dx)
    angle_diff = desired_angle - robot_angle

    # Calculate Centripetal Acceleration
    curvature = abs(angle_diff) / distance if distance > 0 else 0
    centripetal_acceleration = (curvature ** 2) * distance  # Adjust the scaling factor as per your requirements

    # Calculate Motor Powers
    velocity = distance * centripetal_acceleration * 0.1  # Adjust the scaling factor as per your requirements

    motor_powers[0] = int((velocity - angle_diff * ROBOT_WIDTH) * MOTOR_POWER_SCALE)
    motor_powers[1] = int((velocity + angle_diff * ROBOT_WIDTH) * MOTOR_POWER_SCALE)
    motor_powers[2] = int((velocity - angle_diff * ROBOT_WIDTH) * MOTOR_POWER_SCALE)
    motor_powers[3] = int((velocity + angle_diff * ROBOT_WIDTH) * MOTOR_POWER_SCALE)


# Game Loop
running = True
clock = pygame.time.Clock()
current_point_index = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    # Update Robot and Motor Powers
    if current_point_index < num_points:
        update_robot()
        calculate_motor_powers()

    # Draw Robot
    rotated_image = pygame.Surface((ROBOT_WIDTH, ROBOT_LENGTH))
    rotated_image.fill(RED)
    rotated_image = pygame.transform.rotate(rotated_image, math.degrees(robot_angle))
    rotated_rect = rotated_image.get_rect(center=(robot_x, robot_y))
    screen.blit(rotated_image, rotated_rect)

    # Draw Bezier Curve
    if len(curve_points) > 1:
        pygame.draw.lines(screen, WHITE, False, curve_points[:current_point_index + 1], 3)

    # Draw Motor Powers
    for i, power in enumerate(motor_powers):
        pygame.draw.rect(screen, GREEN, (10 + i * 30, SCREEN_HEIGHT - 50, 20, -power))

    pygame.display.flip()
    clock.tick(60)

# Quit the game
pygame.quit()
