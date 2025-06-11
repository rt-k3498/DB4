def PID_temp(input):
    """
    input needs to be an array type with all data points
    The Kp, Ki, and Kd values are set to 0.1, 0.01, and 0.05 respectively, have to be tested and optimised
    """
    time_interval = 0.1  # Time interval in seconds
    Kp = 0.1  # Proportional gain
    Ki = 0.01  # Integral gain
    Kd = 0.05  # Derivative gain
    integral = input[-1:-10:-1] * time_interval  # Integral of the last 10 inputs
    derivative = input[-2]/time_interval if len(input) > 1 else 0
    P = input * Kp
    I = integral * Ki
    D = derivative * Kd
    output = P + I + D
    return output

def PID_OD(input):
    """
    input needs to be an array type with all data points
    The Kp, Ki, and Kd values are set to 0.1, 0.01, and 0.05 respectively, have to be tested and optimised
    """
    time_interval = 0.1  # Time interval in seconds
    Kp = 0.1  # Proportional gain
    Ki = 0.01  # Integral gain
    Kd = 0.05  # Derivative gain
    integral = 0
    derivative = 0
    previous_input = 0
    for i in range(len(input)):
        integral += input[i] * time_interval
        derivative = (input[i] - previous_input) / time_interval
        P = input[i] * Kp
        I = integral * Ki
        D = derivative * Kd
        output = P + I + D
        previous_input = input[i]
    return output