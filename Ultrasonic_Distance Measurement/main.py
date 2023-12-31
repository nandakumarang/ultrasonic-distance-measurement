import serial
import tkinter as tk

def update_distance():
    ainput = ser.readline().decode().strip()
    sinput = ainput.split(",")
    distance = sinput[0]
    delay = sinput[1]
    
    distance_label.config(text=f"Distance: {distance} cm")
    delay_label.config(text=f"Delay: {delay} ms")
    
    root.after(1000, update_distance)

ser = serial.Serial('COM3', 9600)

root = tk.Tk()
root.title("Ultrasonic Sensor Distance Measurement")

title_label = tk.Label(root, text="Ultrasonic Sensor Distance Measurement", font=("Comic Sans MS", 40, "underline"))
title_label.pack(pady=5)

made_label = tk.Label(root, text="Made By Group 6", font=("Helvetica", 20, "italic"))
made_label.pack(pady=5)

distance_label = tk.Label(root, text="Distance: N/A cm", font=("Helvetica", 30))
distance_label.pack(pady=30)

delay_label = tk.Label(root, text="Delay: N/A ms", font=("Helvetica", 30))
delay_label.pack(pady=20)

sound_label = tk.Label(root, text="Speed of sound is 340 m/s", font=("Tahoma", 20))
sound_label.pack(pady=20)

exit_button = tk.Button(root, text="Exit", command=root.destroy)
exit_button.pack()

update_distance()

root.mainloop()

ser.close()
