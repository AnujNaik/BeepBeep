import math

# Function to calculate motor powers for mecanum drivetrain
def calculate_motor_powers(vector):
    # Extract x and y components from the vector
    x = vector[0]
    y = vector[1]
    
    # Calculate the desired motion components
    drive = y
    strafe = x
    rotate = 0  # No rotation in this example
    
    # Calculate motor powers using inverse kinematics
    front_left = drive + strafe + rotate
    front_right = drive - strafe - rotate
    rear_left = drive - strafe + rotate
    rear_right = drive + strafe - rotate
    
    # Normalize motor powers if necessary
    powers = [front_left, front_right, rear_left, rear_right]
    max_power = max(map(abs, powers))
    if max_power > 1.0:
        powers = [p / max_power for p in powers]
    
    # Return the motor powers
    return powers

# Example usage
vector = [1.0, 0.5]  # Example vector [x, y]
motor_powers = calculate_motor_powers(vector)
print("Motors: FL FR RL RR")
print("Motor Powers:", motor_powers)
