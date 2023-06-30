import pygame
from mecanum_drivetrain import MecanumDrivetrain
from animation import Animator
from path_following import PathFollower
from bezier_path import BezierPath
from field import Field
from constants import Constants

# control_points = [(100, 300), (300, 100), (500, 500), (700, 300)]

class Simulation:
    
    def __init__(self, paths):
        pygame.init()
        size = (750, 750)
        self.win = pygame.display.set_mode(size)
        pygame.display.set_caption('BeepBeep')
        self.clock = pygame.time.Clock()
        
        self.field = Field(self.win, size)
        self.paths = paths
        # control_points = [(-30, -30), (-10, 35), (10, 5), (30, 30)]
        # control_points = Constants.formatControlPoints(control_points)
        # bezierPath = BezierPath(control_points)

    def start(self):
        RUN = True
        FONT = pygame.font.SysFont("comicsans", 18)
        
        for path in self.paths:
            curve_points, control_points = path.retrievePath()
            curve_points = Constants.formatCurvePoints(curve_points)

        while RUN:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    RUN = False

            self.field.updateField()

            # print(field.getPos())
            
            self.field.updatePos(self.win, FONT)
            
            for path in self.paths:
                _, control_points = path.retrievePath()
                pygame.draw.lines(self.win, Constants.WHITE, False, curve_points, 5)
                
                for point in control_points:
                    pygame.draw.circle(self.win, Constants.WHITE, point, 5)
            
            pygame.display.update()
            self.clock.tick(60)
            
        pygame.quit()
        
if __name__ == "__main__":
    simulation = Simulation()