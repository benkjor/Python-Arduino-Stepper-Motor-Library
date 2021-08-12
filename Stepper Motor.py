from time import sleep
import pyfirmata
import StepperLib

#'COM3' is the USB port mine was plugged into
board = pyfirmata.Arduino('COM3') # remember to go to arduino ide, examples, firmata, standard firmata
reader = pyfirmata.util.Iterator(board) # reads inputs of the circuit
reader.start()

#2, 3, 4, 5 are digital pin numbers and 2038 is the number of steps in the stepper motor I used
motor = StepperLib.Stepper(2038, board, reader, 2, 3, 4, 5)
motor.set_speed(10000)
#0 and 1 are the analog pin  you may need to change them
photo_1 = board.get_pin('a:0:i')
photo_2 = board.get_pin('a:1:i')

#adjustment is based on seeing what the rough difference in base values of the two photoresistors is
adjustment = 100

while 1 == 1:

    input_one = str(photo_1.read())
    #initial values for the photoresistors are "None", so that needs to be eliminated so only numbers
    #are read as values, and then the number is divided by 10 so that it is smaller and easier to work with
    if input_one != "None":
        input_one = input_one[2:6]
        input_1 = int(input_one) / 10
    elif input_one == "None":
        input_1 = 0
    input_two = str(photo_2.read())
    if input_two != "None":
        input_two = input_two[2:6]
        input_2 = int(input_two) / 10
    elif input_two == "None":
        input_2 = 0

    print("Input 1: " + str(input_1) + "   Input 2: " + str(input_2))
    if abs(input_1 - input_2) > 100:
        if input_1 > input_2:
            motor.step(10)
            sleep(.01)
        if input_2 > input_1:
            motor.step(-10)
            sleep(.01)
        
    else:
        sleep(.01)
