class BPoint:
    def __init__(self, A, B, C, D):
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        self.control_points = [A, B, C, D]
    
    def getStart(self):
        return self.A
    
    def getEnd(self):
        return self.B
    
    def getInterpolation(self):
        return self.C, self.D
    
    def getControlPoints(self):
        return self.control_points