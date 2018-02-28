from tkinter import Tk, Label
import serial

ser = serial.Serial()
ser.port = "/dev/ttyUSB0"
ser.baudrate = 9600
try:
  ser.open()
except serial.SerialException:
  print("Could not open serial port: " + ser.port)

root = Tk()
root.geometry('{}x{}'.format(200, 100))
label = Label(root, font=("Helvetica", 26))
label.pack(fill='both')


def read_serial_data():
  if ser.isOpen():
    try:
      response = ser.readline()
      print(response)
      label.config(
          text='Distance : \n' + response.decode("utf-8").rstrip() + ' cm')
    except serial.SerialException:
      print("no message received")
  root.after(100, read_serial_data)


read_serial_data()
root.mainloop()
