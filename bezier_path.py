import math
from constants import Constants

class BezierPath:
    def __init__(self, bPoint):
        self.control_points = bPoint.getControlPoints()
        # self.control_points = Constants.formatControlPoints(self.pure_control_points)
        self.t = 0.0
        self.t_step = 0.01
        
        # # Draw control points
        # for point in self.control_points:
        #     pygame.draw.circle(screen, BLACK, point, 5)
        
        # Draw Bezier curve
        self.curve_points = []
        while self.t <= 1.0:
            x = math.pow(1 - self.t, 3) * self.control_points[0][0] + \
                3 * self.t * math.pow(1 - self.t, 2) * self.control_points[1][0] + \
                3 * math.pow(self.t, 2) * (1 - self.t) * self.control_points[2][0] + \
                math.pow(self.t, 3) * self.control_points[3][0]

            y = math.pow(1 - self.t, 3) * self.control_points[0][1] + \
                3 * self.t * math.pow(1 - self.t, 2) * self.control_points[1][1] + \
                3 * math.pow(self.t, 2) * (1 - self.t) * self.control_points[2][1] + \
                math.pow(self.t, 3) * self.control_points[3][1]

            self.curve_points.append(((x), (y)))

            self.t += self.t_step

        self.t = 0.0

    def retrievePath(self):
        return self.curve_points, self.control_points
    
    def retrieveVectorVelocities(self):
        print(self.control_points)
        for i, point in enumerate(self.curve_points):
            try:
                dy = self.curve_points[(i+1)][1] - self.curve_points[i][1]
                dx = self.curve_points[(i+1)][0] - self.curve_points[i][0]
                
                x_coor = round((point[0]), 2)
                y_coor = round((point[1]), 2)
                
                print(f"REGULAR ({x_coor}, {y_coor}) : {round(dy / dx, 2)}")
                # print(f"DERIVATIVE: ({x_coor}, {y_coor}) : {(self.getDerivative((i/100) + 0.01), 2)}")
                print(f"DERIVATIVE: {self.getDerivative(i/100)}")
                print(i/100)
                print()
                
                # print(f"({x_coor}, {y_coor}) : {math.degrees(math.atan2(dx, dy)) + 90}")
            except:
                print("ERROR")
                
    def getDerivative(self, t):
        print(f"GET DERIVATIVE CONTROL POINT: {self.control_points}")
        ax = self.control_points[0][0]
        ay = self.control_points[0][1]

        bx = self.control_points[1][0]
        by = self.control_points[1][1]

        cx = self.control_points[2][0]
        cy = self.control_points[2][1]

        dx = self.control_points[3][0]
        dy = self.control_points[3][1]

        # -3c_{1}\left(1-t\right)^{2}+3c_{2}\left(3t^{2}-4t+1\right)+3c_{3}\left(2t-3t^{2}\right)+3c_{4}t^{2}\ \left\{0<t<1\right\}

        dx_dt = -3 * ax * math.pow(1 - t, 2) + \
            3 * bx * (3 * math.pow(t, 2) - 4 * t + 1) + \
            3 * cx * (2 * t - 3 * math.pow(t, 2)) + \
            3 * dx * math.pow(t, 2)

        dy_dt = -3 * ay * math.pow(1 - t, 2) + \
                3 * by * (3 * math.pow(t, 2) - 4 * t + 1) + \
                3 * cy * (2 * t - 3 * math.pow(t, 2)) + \
                3 * dy * math.pow(t, 2)
                
        return (dy_dt, dx_dt)
        
