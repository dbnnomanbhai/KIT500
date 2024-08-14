__author__ = "Najmul Uddin"

def distance(velocity: float, reaction_time: float) -> float:
    """
    Calculate the stopping distance of a vehicle.
    """
    FRICTION = 0.7  # Coefficient of friction
    GRAVITY = 9.81  # Acceleration due to gravity  
    
    distance = (velocity * reaction_time) + (velocity ** 2) / (2 * FRICTION * GRAVITY)
    return distance

def main():
    # Distance calculations with values
    print("Distance to stop 1:", distance(22.22, 1.75), "m")
    print("Distance to stop 2:", distance(8.33, 3.1), "m")
    
    # User input for calculation 
    velocity = float(input("Input initial velocity (m/s): "))
    reaction_time = float(input("Input reaction time (seconds): "))
    
    print("\n Calculating...")
    end_distance = distance(velocity, reaction_time)
    print(f"Distance to stop: {end_distance:.2f} m")

if __name__ == "__main__":
    main()
