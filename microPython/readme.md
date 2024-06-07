## Installation on raspberry pi pico:

- connect the Pico to pc and open as a folder
- copy inside Pico the adafruit CircuitPython installation file
- then copy inside Pico the folder 'kmk' and the file 'boot.py'
- finally copy the file 'code.py'

## pins map

- keyboard matrix
  - cols: (GP15 - on board 20)  (GP14 - on board 19)
  - rows: (GP13 - on board 17)  (GP12 - on board 16)  (GP11 - on board 15)
- rotary encoder
  - GND( - on board 13) 3V3 CLK(pin_a GP7 - on board 10) DT(pin_b GP8 - on board 11) SW(button_pin GP9 - on board 12)
- i2c screen
  - GND(on board 8) 3V3 SCL(GP5 - on board 7) SDA(GP4 - on board 6)