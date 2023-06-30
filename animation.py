import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


class Animator:
    def __init__(self, bezier_path, mecanum_drivetrain):
        self.bezier_path = bezier_path
        self.mecanum_drivetrain = mecanum_drivetrain

        self.figure, self.ax = plt.subplots()
        self.animation = None

        self.setup()

    def setup(self):
        # Set up your animation parameters and initialization here
        pass

    def update(self, frame):
        # Update the animation frame
        # Implement your animation logic here
        pass

    def start_animation(self):
        self.animation = FuncAnimation(self.figure, self.update, interval=50)
        plt.show()
