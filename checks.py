def calculated(current, voltage, time):
    '''
    This function demonstrates how more than one output quantities can be returned.

    INPUTS:
    current: Electric current
    voltage: Electric voltage
    time: The length of time the circuit was on

    OUTPUT:
    powers: Electrical power
    energys: Electrical energy
    '''
    powers = current * voltage
    energys = current * voltage * time
    return powers, energys
