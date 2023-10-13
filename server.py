import tkinter as tk
from ping3 import ping

def check_server_status():
    server_ip = entry_server_ip.get()
    response_time = ping(server_ip)
    
    if response_time is not None:
        result_label.config(text=f"El servidor está en línea (Tiempo de respuesta: {response_time} ms)")
    else:
        result_label.config(text="El servidor está desconectado")

# Crear la ventana
window = tk.Tk()
window.title("Verificar Estado del Servidor")

# Crear etiquetas y entrada
server_label = tk.Label(window, text="Dirección IP del servidor:")
server_label.pack()

entry_server_ip = tk.Entry(window)
entry_server_ip.pack()

check_button = tk.Button(window, text="Verificar Estado", command=check_server_status)
check_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()
