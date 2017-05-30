import RPi.GPIO as GPIO
import time

S_A = 25
S_B = 24
S_C = 23
S_D = 18

def main():
    
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)      

    GPIO.setup(S_A, GPIO.OUT) 
    GPIO.setup(S_B, GPIO.OUT) 
    GPIO.setup(S_C, GPIO.OUT) 
    GPIO.setup(S_D, GPIO.OUT) 

    while True:

        stepper_motor_clock();
        time.sleep(5)
        stepper_motor_Anti_clock();
        time.sleep(5)                

def stepper_motor_clock():
    stepper_motor(0x03)
    time.sleep(0.6)
    stepper_motor(0x06)
    time.sleep(0.6)
    stepper_motor(0x0C)
    time.sleep(0.6)
    stepper_motor(0x09)
    time.sleep(0.6)
    
   

def stepper_motor_Anti_clock():
    stepper_motor(0x09)
    time.sleep(0.6)
    stepper_motor(0x0C)
    time.sleep(0.6)
    stepper_motor(0x06)
    time.sleep(0.6)
    stepper_motor(0x03)
    time.sleep(0.6)

def stepper_motor(bits):
    
    GPIO.output(S_A, False)
    GPIO.output(S_B, False)
    GPIO.output(S_C, False)
    GPIO.output(S_D, False)
    
    if bits&0x01==0x01:
        GPIO.output(S_A, True)
    if bits&0x02==0x02:
        GPIO.output(S_B, True)
    if bits&0x04==0x04:
        GPIO.output(S_C, True)
    if bits&0x08==0x08:
        GPIO.output(S_D, True)

if __name__ == '__main__':

  try:
    main()
  except KeyboardInterrupt:
    pass
  finally:
    GPIO.cleanup()
