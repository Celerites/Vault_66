import tkinter as tk
import tkinter.font as tkFont
import serial 

#ser = serial.Serial('COM3', 9600)

# Definir ventana principal
root = tk.Tk()
root.title("Brazo Robot B1 Battle Droid") #Nombre de la ventana
root.wm_geometry("600x750") #Tamaño de ventana
root.configure(bg="#566573") #Color del fondo de la ventana
root.bind('<Escape>', lambda e, w=root: w.destroy()) #Cerrar con tecla Escape

default_font = tkFont.nametofont("TkDefaultFont")
default_font.configure(size=15)


# Variable global para saber que pagina esta actualmente 
current_page = 1

#sliderValues
slider1Value = 0
slider2Value = 0
slider3Value = 0
slider4Value = 0
slider5Value = 0
slider6Value = 0

# funcion para mandar datos Serial
def send_command(command):
    try:
        ser.write(command)
        print(f"Sent command: {command.decode()}")  # imprime el comando por si hay errores
    except serial.SerialException as e:
        print(f"Serial error: {e}")  # para ver si hay errores en Serial

# inicia conexion serial
try:
    ser = serial.Serial("COM3", 9600)
    print("Serial connection established")
except serial.SerialException as e:
    print(f"Serial connection error: {e}")
    quit()  # se desconecta de conexion serial si no hay conexion
#


#definir variables para botones de la gui para serial read
grip_command = b'grip'
move_command = b'move'
updown_command = b'updown'
side_command = b'side'

# Crear frames a cada pagina
page1 = tk.Frame(root, background="#f4d03f", width=200, height=200)
page2 = tk.Frame(root, background="#f4d03f", width=200, height=200)
page3 = tk.Frame(root, background="#f4d03f", width=200, height=200)

# Poner frames en la ventana
page1.grid()
page2.grid_forget()
page3.grid_forget()

# --- Pagina 1: Deslizar ---

# Create a horizontal slider on page 1
slider1_label = tk.Label(page1, text="Servo Base:", bg="#273746", fg="white",)
slider1_label.grid(row=0, column=0)
slider1 = tk.Scale(page1, from_=0, to=180, orient=tk.HORIZONTAL, length=300, command=lambda val: updateSlider1(val), bg="#273746", fg="white")
slider1.grid(row=1, column=0, sticky="nsew")

slider2_label = tk.Label(page1, text="Servo Brazo1", bg="#273746", fg="white")
slider2_label.grid(row=2, column=0)
slider2 = tk.Scale(page1, from_=0, to=90, orient=tk.HORIZONTAL, length=300, command=lambda val: updateSlider2(val), bg="#273746", fg="white")
slider2.grid(row=3, column=0)

slider3_label = tk.Label(page1, text="Servo Brazo2", bg="#273746", fg="white")
slider3_label.grid(row=4, column=0)
slider3 = tk.Scale(page1, from_=0, to=180, orient=tk.HORIZONTAL, length=300, command=lambda val: updateSlider3(val), bg="#273746", fg="white")
slider3.grid(row=5, column=0)

slider4_label = tk.Label(page1, text="Servo Brazo3", bg="#273746", fg="white")
slider4_label.grid(row=6, column=0)
slider4 = tk.Scale(page1, from_=0, to=180, orient=tk.HORIZONTAL, length=300, command=lambda val: updateSlider4(val), bg="#273746", fg="white")
slider4.grid(row=7, column=0)

slider5_label = tk.Label(page1, text="Servo Brazo4", bg="#273746", fg="white")
slider5_label.grid(row=8, column=0)
slider5 = tk.Scale(page1, from_=0, to=180, orient=tk.HORIZONTAL, length=300, command=lambda val: updateSlider5(val), bg="#273746", fg="white")
slider5.grid(row=9, column=0)

slider6_label = tk.Label(page1, text="Servo Grip", bg="#273746", fg="white")
slider6_label.grid(row=10, column=0)
slider6 = tk.Scale(page1, from_=0, to=180, orient=tk.HORIZONTAL, length=300, command=lambda val: updateSlider6(val), bg="#273746", fg="white")
slider6.grid(row=11, column=0)

# Function to update slider value and display it in a label
def updateSlider1(val):
  global slider1Value
  slider1Value = int(val)
  
  # enviar angulo servo 1
  #ser.write(f"servo1:{slider1Value}\n".encode())

def updateSlider2(val):
    global slider2Value
    slider2Value = int(val)
    
   # enviar angulo servo 2
    #ser.write(f"servo2:{slider2Value}\n".encode())

def updateSlider3(val):
    global slider3Value
    slider3Value = int(val)
    
   # enviar angulo servo 3
    #ser.write(f"servo3:{slider3Value}\n".encode())

def updateSlider4(val):
    global slider4Value
    slider4Value = int(val)
    
   # enviar angulo servo 4
    #ser.write(f"servo4:{slider4Value}\n".encode())

def updateSlider5(val):
    global slider5Value
    slider5Value = int(val)
    
   # enviar angulo servo 5
    #ser.write(f"servo5:{slider5Value}\n".encode())

def updateSlider6(val):
    global slider6Value
    slider6Value = int(val)
    slider6_label.config(text=f"Slider Value: {slider6Value}")
   # enviar angulo servo 6
    #ser.write(f"servo6:{slider6Value}\n".encode())

creditos = tk.Label(text="Developed by:\nfe.galleguillosc@duocuc.cl", bg="#273746", fg="white")
creditos.grid(row= 12, column=0, sticky="ew")



# --- Page 2: Botones ---

# crear botones con texto
grip_button = tk.Button(page2, text="Grip", command=lambda: grip(), width=20, height=3, bg="#273746", fg="white")
grip_button.grid(row=0, column=0, padx=20, pady=20)

move_button = tk.Button(page2, text="Mover Base 180", command=lambda: move(), width=20, height=3, bg="#273746", fg="white")
move_button.grid(row=0, column=1, padx=20, pady=20)

updown_button = tk.Button(page2, text="Arriba-Abajo", command=lambda: updown(), width=20, height=3, bg="#273746", fg="white")
updown_button.grid(row=1, column=0, padx=20, pady=20)

side_button = tk.Button(page2, text="Lado a Lado", command=lambda: side(), width=20, height=3, bg="#273746", fg="white")
side_button.grid(row=1, column=1, padx=20, pady=20)

# funcion para mostrar texto para cada boton presionado // 

def grip():
    print("Boton grip presionado")
    send_command(grip_command)

def move():
    print("Boton move presionado")
    send_command(move_command)

def updown():
    print("Boton updown presionado")
    send_command(updown_command)

def side():
    print("Boton side presionado")
    send_command(side_command)

# --- Pagina 3: 5x5 Grid con numeros ---

# Crear grid de 5x5 con etiquetas de numeros en la pagina 3
for row in range(5):
    for col in range(5):
        number_button = tk.Button(page3, text=f"{row+1},{col+1}", relief=tk.GROOVE, borderwidth=5, bg="black", fg="white")
        number_button.grid(row=row, column=col, padx=15, pady=15)


textorobot = tk.Label(master=page3, text="ROBOT", bg="#273746", fg="white")
textorobot.grid(row=10, column=2, padx=10, pady=10)

# --- Comandos de los botones para cambiar de pagina ---

next_button = tk.Button(root, text="Next", command=lambda: show_next_page(), bg="#273746", fg="white")
back_button = tk.Button(root, text="Back", command=lambda: show_previous_page(), state=tk.DISABLED, bg="#273746", fg="white")

next_button.grid(sticky="s", padx=10, pady=10,)
back_button.grid(sticky="s", padx=10, pady=10,)

# --- Funciones para cambiar de pagina ---

def show_next_page():
    global current_page
    if current_page == 1:
        page2.grid()
        page1.grid_forget()
        current_page = 2
        next_button.config(state=tk.NORMAL)
        back_button.config(state=tk.NORMAL)
    elif current_page == 2:
        page3.grid()
        page2.grid_forget()
        current_page = 3
        next_button.config(state=tk.DISABLED)

def show_previous_page():
    global current_page
    if current_page == 3:
        page2.grid()
        page3.grid_forget()
        current_page = 2
        next_button.config(state=tk.NORMAL)
    elif current_page == 2:
        page1.grid()
        page2.grid_forget()
        current_page = 1
        back_button.config(state=tk.DISABLED)

# Inicio en la pagina 1
current_page = 1

root.mainloop() #iniciar ventana