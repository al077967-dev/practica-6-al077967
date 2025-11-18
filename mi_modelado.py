import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np

def ejecutar_programa():
    try:
        f_c      = float(entry_fc.get())
        volumen  = float(entry_volumen.get())
        tam_max  = int(combo_agregado.get())
    except:
        messagebox.showerror("Error", "Ingresa valores válidos.")
        return

    # Validar resistencia mínima
    if f_c < 150:
        messagebox.showwarning(
            "Advertencia",
            "La resistencia ingresada es menor a 150 kg/cm².\nEl concreto no tiene la resistencia adecuada."
        )
        return

    if f_c > 400:
        messagebox.showwarning("Aviso", "f'c máximo permitido: 400 kg/cm²")
        f_c = 400

    # TABLA ACI
    tabla_aci = np.array([
        [150, 0.70],
        [200, 0.60],
        [250, 0.55],
        [300, 0.50],
        [350, 0.45],
        [400, 0.40]
    ])

    tabla_agua = np.array([
        [20, 205],
        [40, 185],
        [80, 170]
    ])

    materiales = ["Cemento", "Arena", "Grava", "Agua"]
    pesos_esp  = np.array([1400, 1600, 1500, 1000])

    # Obtener relación Agua/Cemento según f'c
    wc = next((fila[1] for fila in tabla_aci if f_c <= fila[0]), tabla_aci[-1][1])

    # Agua según tamaño de agregado
    agua_kg_m3 = next((tabla_agua[i][1] for i in range(len(tabla_agua)) if tam_max <= tabla_agua[i][0]), tabla_agua[-1][1])

    # Cálculo cemento
    cemento_kg_m3 = agua_kg_m3 / wc

    # Proporción típica ACI
    proporciones = np.array([1, 1.5, 2.5])
    partes       = proporciones.sum()
    volumen_rel  = proporciones / partes

    arena_kg_m3  = volumen_rel[1] * pesos_esp[1]
    grava_kg_m3  = volumen_rel[2] * pesos_esp[2]

    # Matriz final
    masas = np.array([cemento_kg_m3, arena_kg_m3, grava_kg_m3, agua_kg_m3])
    masas_totales = masas * volumen

    # Limpiar tabla
    for i in tree.get_children():
        tree.delete(i)

    # Insertar resultados en la tabla
    for i in range(4):
        tree.insert("", "end", values=(materiales[i], f"{masas[i]:.2f}", f"{masas_totales[i]:.2f}"))

    # Mostrar resumen
    label_resumen.config(
        text=f"f'c ingresado: {f_c} kg/cm² | Relación A/C: {wc} | Tamaño agregado: {tam_max} mm | Volumen: {volumen} m³"
    )

# -----------------------------
# INTERFAZ PROFESIONAL
# -----------------------------

root = tk.Tk()
root.title("Dosificación Automática de Concreto (ACI)")
root.geometry("700x550")
root.resizable(False, False)

# Estilo ttk
style = ttk.Style(root)
style.theme_use("clam")
style.configure("TLabel", font=("Helvetica", 12))
style.configure("TButton", font=("Helvetica", 12), foreground="#ffffff", background="#007acc")
style.map("TButton", background=[('active', '#005f99')])
style.configure("Treeview", font=("Helvetica", 11), rowheight=25)
style.configure("Treeview.Heading", font=("Helvetica", 12, "bold"))

# Título
label_titulo = ttk.Label(root, text="DOSIFICACIÓN AUTOMÁTICA DE CONCRETO (ACI)", font=("Helvetica", 18, "bold"))
label_titulo.pack(pady=15)

# Frame de entrada
frame = ttk.LabelFrame(root, text="Datos de Entrada", padding=(20,10))
frame.pack(padx=20, pady=10, fill="x")

# f'c
ttk.Label(frame, text="f'c deseado (kg/cm²):").grid(row=0, column=0, sticky="w", padx=5, pady=5)
entry_fc = ttk.Entry(frame)
entry_fc.grid(row=0, column=1, padx=5, pady=5)

# Volumen
ttk.Label(frame, text="Volumen total (m³):").grid(row=1, column=0, sticky="w", padx=5, pady=5)
entry_volumen = ttk.Entry(frame)
entry_volumen.grid(row=1, column=1, padx=5, pady=5)

# Tamaño máximo del agregado
ttk.Label(frame, text="Tamaño máximo del agregado (mm):").grid(row=2, column=0, sticky="w", padx=5, pady=5)
combo_agregado = ttk.Combobox(frame, values=[20, 40, 80], state="readonly")
combo_agregado.current(0)
combo_agregado.grid(row=2, column=1, padx=5, pady=5)

# Botón calcular
btn = ttk.Button(root, text="Calcular", command=ejecutar_programa)
btn.pack(pady=10)

# Tabla de resultados
frame_tabla = ttk.LabelFrame(root, text="Resultados", padding=(20,10))
frame_tabla.pack(padx=20, pady=10, fill="both", expand=True)

columns = ("Material", "kg/m³", "Total kg")
tree = ttk.Treeview(frame_tabla, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor="center")
tree.pack(fill="both", expand=True)

# Resumen
label_resumen = ttk.Label(root, text="", font=("Helvetica", 12, "italic"))
label_resumen.pack(pady=5)

root.mainloop()

   
