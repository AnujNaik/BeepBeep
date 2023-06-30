'''
# Create an instance of BezierPath
bezier_path = BezierPath()

# Create an instance of MecanumDrivetrain
mecanum_drivetrain = MecanumDrivetrain()

# Create an instance of PathFollower
path_follower = PathFollower(bezier_path, mecanum_drivetrain)

# Create an instance of Animator
animator = Animator(bezier_path, mecanum_drivetrain)

# Generate the bezier path
bezier_path.generate_path()

# Perform path following
path_follower.follow_path()

# Start the animation
animator.start_animation()
'''

from mecanum_drivetrain import MecanumDrivetrain
from animation import Animator
from path_following import PathFollower
from bezier_path import BezierPath
from field import Field
from constants import Constants
from bezier_points import BPoint
from simulation import Simulation

# Define paths
#                           start       interpolation points    end
# start = BezierPath(BPoint(  (-35, 68), (-40, 20), (-25, 5),  (-68, 11)))
mid = BezierPath(BPoint(    (-35, -68),  (-40, 5), (-25, -10),  (-68, -11)))

paths = [mid]

# for i in start.generate_path()[0]:
#     print(i)

print(mid.retrieveVectorVelocities())

# Begin simulation
simulation = Simulation(paths)
simulation.start()