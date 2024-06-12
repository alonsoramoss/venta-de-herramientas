import tkinter as tk
import mysql.connector

conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="ferreteria"
)
cursor = conn.cursor()

def login():
    try:
        username = username_entry.get()
        password = password_entry.get()
        cursor.execute("SELECT * FROM usuarios WHERE nombre=%s", (username,))
        user = cursor.fetchone()
        if user:
            stored_password = user[6]
            if password == stored_password:
                show_boleta_window(user[0])
            else:
                error_label.config(text="Usuario o contraseña inválidos")
        else:
            error_label.config(text="Usuario o contraseña inválidos")
    except Exception as e:
        error_label.config(text="Error de conexión")

def show_register_window():
    register_window = tk.Toplevel()
    register_window.title("Registro de usuario")

    nombres_label = tk.Label(register_window, text="Nombres:")
    nombres_entry = tk.Entry(register_window)
    apellidos_label = tk.Label(register_window, text="Apellidos:")
    apellidos_entry = tk.Entry(register_window)
    dni_label = tk.Label(register_window, text="DNI:")
    dni_entry = tk.Entry(register_window)
    telefono_label = tk.Label(register_window, text="Teléfono:")
    telefono_entry = tk.Entry(register_window)
    correo_label = tk.Label(register_window, text="Correo:")
    correo_entry = tk.Entry(register_window)
    password_label = tk.Label(register_window, text="Contraseña:")
    password_entry = tk.Entry(register_window, show="*")
    register_button = tk.Button(register_window, text="Registrar", command=lambda: register(nombres_entry.get(), apellidos_entry.get(), dni_entry.get(), telefono_entry.get(), correo_entry.get(), password_entry.get(), error_label_register))
    error_label_register = tk.Label(register_window, text="", fg="red")

    nombres_label.grid(row=0, column=0, padx=5, pady=5)
    nombres_entry.grid(row=0, column=1, padx=5, pady=5)
    apellidos_label.grid(row=1, column=0, padx=5, pady=5)
    apellidos_entry.grid(row=1, column=1, padx=5, pady=5)
    dni_label.grid(row=2, column=0, padx=5, pady=5)
    dni_entry.grid(row=2, column=1, padx=5, pady=5)
    telefono_label.grid(row=3, column=0, padx=5, pady=5)
    telefono_entry.grid(row=3, column=1, padx=5, pady=5)
    correo_label.grid(row=4, column=0, padx=5, pady=5)
    correo_entry.grid(row=4, column=1, padx=5, pady=5)
    password_label.grid(row=5, column=0, padx=5, pady=5)
    password_entry.grid(row=5, column=1, padx=5, pady=5)
    register_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5)
    error_label_register.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

def register(nombres, apellidos, dni, telefono, correo, password, error_label_register):
    try:
        cursor.execute("INSERT INTO usuarios (nombre, apellido, dni, telefono, correo, password) VALUES (%s, %s, %s, %s, %s, %s)", (nombres, apellidos, dni, telefono, correo, password))
        conn.commit()
        error_label_register.config(text="Registro exitoso", fg="green")
    except Exception as e:
        error_label_register.config(text="Error al registrar usuario", fg="red")

def show_boleta_window(idUser):
    login_window.destroy()
    boleta_window = tk.Tk()
    boleta_window.title("Boleta de Venta")

    def search_tool():
        tool_name = tool_entry.get()
        cursor.execute("SELECT id, nombre, precio FROM herramientas WHERE nombre LIKE %s", ('%' + tool_name + '%',))
        tools = cursor.fetchall()
        tool_listbox.delete(0, tk.END)
        for tool in tools:
            tool_listbox.insert(tk.END, f"{tool[0]}:{tool[1]} - ${tool[2]}")

    def calculate_total():
        total_pedido = 0
        for i in range(tool_listbox.size()):
            tool_info = tool_listbox.get(i).split(" - $")
            price = float(tool_info[1])
            quantity = int(quantity_entries[i].get() if quantity_entries[i].get() else 0)
            subtotal = price * quantity
            subtotal_entries[i].config(text=f"${subtotal:.2f}")
            total_pedido += subtotal
        total_entry.config(text=f"${total_pedido:.2f}")

    def comprar():
        try:
            cursor.execute("INSERT INTO venta (idUser) VALUES (%s)", (idUser,))
            venta_id = cursor.lastrowid
            for i in range(tool_listbox.size()):
                tool_info = tool_listbox.get(i).split(":")
                tool_id = int(tool_info[0])
                quantity = int(quantity_entries[i].get() if quantity_entries[i].get() else 0)
                subtotal = float(subtotal_entries[i].cget("text").replace("$", ""))
                cursor.execute("INSERT INTO detalle_venta (venta_id, herramienta_id, cantidad, subtotal) VALUES (%s, %s, %s, %s)", (venta_id, tool_id, quantity, subtotal))
            conn.commit()
            error_label.config(text="Compra realizada exitosamente", fg="green")
        except Exception as e:
            error_label.config(text="Error al realizar la compra", fg="red")

    def anular_compra():
        try:
            cursor.execute("SELECT id FROM venta WHERE idUser = %s", (idUser,))
            venta_ids = cursor.fetchall()
            for venta_id in venta_ids:
                cursor.execute("DELETE FROM detalle_venta WHERE venta_id = %s", (venta_id[0],))
            cursor.execute("DELETE FROM venta WHERE idUser = %s", (idUser,))
            conn.commit()
            error_label.config(text="Compra anulada exitosamente", fg="green")
        except Exception as e:
            error_label.config(text="Error al anular la compra", fg="red")

    tool_label = tk.Label(boleta_window, text="Herramienta:")
    tool_entry = tk.Entry(boleta_window)
    search_button = tk.Button(boleta_window, text="Buscar", command=search_tool)
    tool_listbox = tk.Listbox(boleta_window, width=50, selectmode=tk.MULTIPLE)

    price_label = tk.Label(boleta_window, text="Precio por unidad:")
    quantity_label = tk.Label(boleta_window, text="Cantidad:")
    subtotal_label = tk.Label(boleta_window, text="Subtotal:")
    total_label = tk.Label(boleta_window, text="Total:")
    total_entry = tk.Label(boleta_window, text="$0.00")
    calculate_button = tk.Button(boleta_window, text="Calcular Total", command=calculate_total)
    comprar_button = tk.Button(boleta_window, text="COMPRAR", command=comprar)
    anular_button = tk.Button(boleta_window, text="ANULAR COMPRA", command=anular_compra)

    tool_label.grid(row=0, column=0, padx=5, pady=5)
    tool_entry.grid(row=0, column=1, padx=5, pady=5)
    search_button.grid(row=0, column=2, padx=5, pady=5)
    tool_listbox.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

    price_label.grid(row=2, column=0, padx=5, pady=5)
    quantity_label.grid(row=2, column=1, padx=5, pady=5)
    subtotal_label.grid(row=2, column=2, padx=5, pady=5)

    for i in range(5):
        tk.Label(boleta_window, text="").grid(row=i+3, column=0, padx=5, pady=5)

    total_label.grid(row=8, column=1, padx=5, pady=5)
    total_entry.grid(row=8, column=2, padx=5, pady=5)
    calculate_button.grid(row=9, column=0, columnspan=3, padx=5, pady=5)
    comprar_button.grid(row=9, column=4, padx=5, pady=5)
    anular_button.grid(row=10, column=4, padx=5, pady=5)

    quantity_entries = []
    subtotal_entries = []
    for i in range(5):
        quantity_entry = tk.Entry(boleta_window, width=5)
        quantity_entry.grid(row=i+3, column=1, padx=5, pady=5)
        quantity_entries.append(quantity_entry)
        subtotal_entry = tk.Label(boleta_window, text="$0.00")
        subtotal_entry.grid(row=i+3, column=2, padx=5, pady=5)
        subtotal_entries.append(subtotal_entry)

    error_label = tk.Label(boleta_window, text="", fg="red")
    error_label.grid(row=11, column=0, columnspan=3, padx=5, pady=5)

login_window = tk.Tk()
login_window.title("Inicio de Sesión")

username_label = tk.Label(login_window, text="Nombre de Usuario:")
username_entry = tk.Entry(login_window)
password_label = tk.Label(login_window, text="Contraseña:")
password_entry = tk.Entry(login_window, show="*")
login_button = tk.Button(login_window, text="Iniciar Sesión", command=login)
register_button = tk.Button(login_window, text="Registrarse", command=show_register_window)
error_label = tk.Label(login_window, text="", fg="red")

username_label.grid(row=0, column=0, padx=5, pady=5)
username_entry.grid(row=0, column=1, padx=5, pady=5)
password_label.grid(row=1, column=0, padx=5, pady=5)
password_entry.grid(row=1, column=1, padx=5, pady=5)
login_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
register_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
error_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

login_window.mainloop()
