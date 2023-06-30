class PathFollower:
    def __init__(self, bezier_path, mecanum_drivetrain):
        self.bezier_path = bezier_path
        self.mecanum_drivetrain = mecanum_drivetrain

        self.current_point = None

    def follow_path(self):
        # Implement your path following logic here
        pass

    def get_next_target_point(self):
        # Implement your logic to get the next target point on the path
        pass