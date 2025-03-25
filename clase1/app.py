from laptop_gaming import laptop_gaming
from laptop_business import Laptop_Business  
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random

class App:
    def __init__(self, root):
        self.root = root
        self.laptops = []
        self.imagenes = ["C:\\Users\\LENOVO\\Desktop\\modulo 5\\clase1\\img\\laptop2.png",
                         "C:\\Users\\LENOVO\\Desktop\\modulo 5\\clase1\\img\\laptop1.jpg",
                         "C:\\Users\\LENOVO\\Desktop\\modulo 5\\clase1\\img\\laptop3.jpg",
                         "C:\\Users\\LENOVO\\Desktop\\modulo 5\\clase1\\img\\laptop4.jpg"
                         ]

        root.title("Ingresar datos")

        self.setup_ui()

    def setup_ui(self):
        
        ttk.Label(self.root, text="Marca (Gaming)").grid(row=0, column=0)
        self.marca_gaming = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.marca_gaming).grid(row=0, column=1)

        ttk.Label(self.root, text="Procesador (Gaming)").grid(row=1, column=0)
        self.procesador_gaming = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.procesador_gaming).grid(row=1, column=1)

        ttk.Label(self.root, text="Memoria (Gaming)").grid(row=2, column=0)
        self.memoria_gaming = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.memoria_gaming).grid(row=2, column=1)

        ttk.Label(self.root, text="Targeta gráfica").grid(row=3, column=0)
        self.tar_grafica = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.tar_grafica).grid(row=3, column=1)

        ttk.Label(self.root, text="Precio (Gaming)").grid(row=4, column=0)
        self.precio_gaming = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.precio_gaming).grid(row=4, column=1)

        ttk.Button(self.root, text="Agregar Laptop Gaming", command=self.agregar_laptop_gaming).grid(row=5, column=0)

        
        ttk.Label(self.root, text="Marca (Business)").grid(row=6, column=0)
        self.marca_business = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.marca_business).grid(row=6, column=1)

        ttk.Label(self.root, text="Procesador (Business)").grid(row=7, column=0)
        self.procesador_business = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.procesador_business).grid(row=7, column=1)

        ttk.Label(self.root, text="Memoria (Business)").grid(row=8, column=0)
        self.memoria_business = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.memoria_business).grid(row=8, column=1)

        ttk.Label(self.root, text="Almacenamiento (Business)").grid(row=9, column=0)
        self.almacenamiento_business = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.almacenamiento_business).grid(row=9, column=1)

        ttk.Label(self.root, text="Duración de Batería (Business)").grid(row=10, column=0)
        self.duracion_bateria_business = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.duracion_bateria_business).grid(row=10, column=1)

        ttk.Label(self.root, text="Precio (Business)").grid(row=11, column=0)
        self.precio_business = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.precio_business).grid(row=11, column=1)

        ttk.Button(self.root, text="Agregar Laptop Business", command=self.agregar_laptop_business).grid(row=12, column=0)

        self.mostrar_laptops = tk.Text(self.root, height=10, width=50)
        self.mostrar_laptops.grid(row=13, column=0, columnspan=2)

        self.canva = tk.Canvas(self.root, width=200, height=200)
        self.canva.grid(row=1, column=3, rowspan=12)

    def agregar_laptop_gaming(self):
        nueva_laptop = laptop_gaming(self.marca_gaming.get(), self.procesador_gaming.get(),
                                      self.memoria_gaming.get(), self.tar_grafica.get(),
                                      self.precio_gaming.get())
        self.laptops.append(nueva_laptop)
        self.mostrar_laptops.insert(tk.END, f"{nueva_laptop}")
        self.mostrar_imagen_aleatorias()

    def agregar_laptop_business(self):
        nueva_laptop_business = Laptop_Business(self.marca_business.get(), self.procesador_business.get(),
                                                 self.memoria_business.get(), self.almacenamiento_business.get(),
                                                 self.duracion_bateria_business.get(), self.precio_business.get())
        self.laptops.append(nueva_laptop_business)
        self.mostrar_laptops.insert(tk.END, f"{nueva_laptop_business}")
        self.mostrar_imagen_aleatorias()

    def mostrar_imagen_aleatorias(self):
        imagen_path = random.choice(self.imagenes)
        imagen = Image.open(imagen_path)
        imagen = imagen.resize((200, 200), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(imagen)

        self.canva.create_image(0, 0, anchor=tk.NW, image=photo)
        self.canva.image = photo

        pass

root = tk.Tk()
app = App(root)
root.mainloop()