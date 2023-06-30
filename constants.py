import pygame, math

class Constants:
    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0 , 0)
    
    def inchesToPygame(val):
        return val * 375/72 + 375

    def pygameToInches(val):
        return (val - 375) * (72/375)

    def formatControlPoints(control_points):
        for i in range(len(control_points)):
            control_points[i] = (int(Constants.inchesToPygame(control_points[i][0])), int(Constants.inchesToPygame(control_points[i][1])))
        
        return control_points
    
    def formatCurvePoints(curve_points):
        # print(f"BEFORE: {curve_points}")
        # Curve point inches to pygame units for graphing
        for i, point in enumerate(curve_points):
            curve_points[i] = (int(Constants.inchesToPygame(point[0])), int(Constants.inchesToPygame(-point[1])))
        
        # print(f"AFTER: {curve_points}")
        
        return curve_points

class Vector:
    def __init__(self, theta, pow):
        self.theta = theta
        self.pow = pow
    
    def getXComponent(self):
        return math.cos(self.theta) * self.pow
    
    def getYComponent(self):
        return math.sin(self.theta) * self.pow