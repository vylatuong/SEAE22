import sys

# Comment for checking that commit works.

# This is the main function for controlling the flow of the
# implementation.
def main():
    limits = parse_limits()
    sensor_data = []

    if len(limits) > 0 and check_limits(limits):
        sensor_data = read_sensors()
        # This is a mockup code that prints the sensor readings
        # to console. To be replaced with actual implementation
        # (whatever that might be according to the low level design,
        # for example).
        for row in sensor_data:
            print (row)
    else:
        print("Error: Incorrect command line arguments.")

# This is the parse_limits function for getting the temperature
# limits from the command line parameters. Returns an array
# that has the limits (limits[0] has min. temperature limit and
# limits[1] has max. temperature limit). If there is an exception
# reading the command line paratmeters, the limits array is empty.
def parse_limits():
    limits = []

    try:
        limits = [int(sys.argv[1]), int(sys.argv[2])]
    except Exception:
        pass
    
    return limits

# This is the check_limits function that gets an array containing the
# limits as a parameter and checks that the lower limit is smaller
# than the higher limit. If this is the case, the function returns
# True. Otherwise, it returns False.
def check_limits(limits):
    if limits[0] < limits[1]:
        return True
    else:
        return False

# This is a stub implementation for function read_sensors
# returning a fixed sensor readings (four sensors, five readings per
# sensor) for development and testing. To be replaced with an actual
# implementation.
def read_sensors():
    return [
            [21.2, 18.2, 18.2, 22.2],
            [-5.0, -4.2, -3.9, -4.5],
            [1.2, 0.0, 0.5, -0.8, -1.0],
            [25.0, -4.2, -13.9, 4.5]]

# Other parts of the implementation such as printing the information
# for the operator are also missing and to be implemented.

main()