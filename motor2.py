from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor
 
import time
import atexit

# Creating motor object 64 steps/rev in port 1 (M1&M2), 1000rpm
mh = Adafruit_MotorHAT(addr = 0x60)
myStepper = mh.getStepper(64, 1)
myStepper.setSpeed(1000)

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
        mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
        mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
        mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
        mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)
 
atexit.register(turnOffMotors)

#One turn = 64*32 steps
myStepper.step(64*32, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.DOUBLE)

turnOffMotors()
