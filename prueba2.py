import tkinter as tk
from matplotlib import pyplot as plt
from tkinter import simpledialog, messagebox
from matplotlib_venn import venn2, venn3

class ConjuntosApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Conjuntos")
        self.master.geometry("600x500")
        self.conjuntos = [{"1","2","3","4"}, {"4","5","6","7"}]
        

        # Botón para agregar conjuntos
        self.boton_agregar = tk.Button(self.master, text="Agregar Conjunto", command=self.agregar_conjunto)
        self.boton_agregar.pack(pady=5)

        # Botones de operaciones
        self.boton_union = tk.Button(self.master, text="Unión", command=self.realizar_union)
        self.boton_union.pack(pady=5)

        self.boton_interseccion = tk.Button(self.master, text="Intersección", command=self.realizar_interseccion)
        self.boton_interseccion.pack(pady=5)

        self.boton_diferencia = tk.Button(self.master, text="Diferencia", command=self.realizar_diferencia)
        self.boton_diferencia.pack(pady=5)

        self.boton_complemento = tk.Button(self.master, text="Complemento", command=self.realizar_complemento)
        self.boton_complemento.pack(pady=5)

        self.boton_salir = tk.Button(self.master, text="Salir", command=self.salir)
        self.boton_salir.pack(pady=5)

    def salir(self):
        self.master.destroy()

    def agregar_conjunto(self):
        if len(self.conjuntos) < 3:
            ventana_agregar_conjunto = tk.Toplevel(self.master)
            ventana_agregar_conjunto.title("Agregar Conjunto")

            etiqueta_instrucciones = tk.Label(ventana_agregar_conjunto, text="Ingrese elementos del conjunto separados por comas:")
            etiqueta_instrucciones.pack(pady=10)

            entry_conjunto = tk.Entry(ventana_agregar_conjunto)
            entry_conjunto.pack(pady=10)

            btn_guardar_conjunto = tk.Button(ventana_agregar_conjunto, text="Guardar Conjunto", command=lambda: self.guardar_conjunto(entry_conjunto.get(), ventana_agregar_conjunto))
            btn_guardar_conjunto.pack(pady=10)
        else:
            messagebox.showinfo("Aviso", "Ya se han ingresado tres conjuntos. No se pueden agregar más.")

    def guardar_conjunto(self, conjunto, ventana_agregar_conjunto):
        # Validar que el conjunto sea una cadena
        if isinstance(conjunto, str):
            self.conjuntos.append(set(conjunto.split(',')))
            messagebox.showinfo("Éxito", "Conjunto agregado con éxito.")
            ventana_agregar_conjunto.destroy()  # Cerrar la ventana después de guardar el conjunto
        else:
            messagebox.showerror("Error", "El conjunto debe ser una cadena de texto.")

    def realizar_union(self):
        conjuntoUnion = set()
        conjuntoA = self.conjuntos[0]
        conjuntoB = self.conjuntos[1]
        if len(self.conjuntos) == 3:
            conjuntoC = self.conjuntos[2]

        if 2 <= len(self.conjuntos) <= 3:
            if len(self.conjuntos) == 2:
                for i in conjuntoA:
                    conjuntoUnion.add(i)
                    print(i)

                for i in conjuntoB:
                    if i not in conjuntoUnion:
                        conjuntoUnion.add(i)
                        print(i)
                venn_diagram = venn2([conjuntoA, conjuntoB], set_labels=("Conjunto A", "Conjunto B"))
                venn_diagram.get_label_by_id('100').set_text(', '.join(map(str, conjuntoA - conjuntoB)))
                venn_diagram.get_label_by_id('010').set_text(', '.join(map(str, conjuntoB - conjuntoA)))
                venn_diagram.get_label_by_id('110').set_text(', '.join(map(str, conjuntoA & conjuntoB)))

        # Utiliza venn3 si tienes tres conjuntos
        if len(self.conjuntos) == 3:
            venn3([conjuntoA, conjuntoB, conjuntoC], set_labels=("Conjunto A", "Conjunto B", "Conjunto C"))
                    

        plt.title("Union")
        plt.annotate(conjuntoUnion, xy=(0.5, 0.95), xycoords="axes fraction",ha="center", va="center", fontsize=12, color="red")
        plt.show()

    def realizar_interseccion(self):
        conjuntoInterseccion = set()
        conjuntoA = self.conjuntos[0]
        conjuntoB = self.conjuntos[1]
        if len(self.conjuntos) == 3:
            conjuntoC = self.conjuntos[2]
    
        if(len(self.conjuntos) == 2 ):
            for i in conjuntoA:
                if i in conjuntoB:
                    conjuntoInterseccion.add(i)
            venn_diagram = venn2([conjuntoA, conjuntoB], set_labels=("Conjunto A", "Conjunto B"))
            venn_diagram.get_label_by_id('100').set_text(', '.join(map(str, conjuntoA - conjuntoB)))
            venn_diagram.get_label_by_id('010').set_text(', '.join(map(str, conjuntoB - conjuntoA)))
            venn_diagram.get_label_by_id('110').set_text(', '.join(map(str, conjuntoA & conjuntoB)))
        
        
        plt.title("Intersección")
        plt.annotate(conjuntoInterseccion, xy=(0.5, 0.95), xycoords="axes fraction",ha="center", va="center", fontsize=12, color="red")
        plt.show()

    def realizar_diferencia(self):
        conjuntoDifenrenciaAB = set()
        conjuntoDifenrenciaBA = set()
        conjuntoA = self.conjuntos[0]
        conjuntoB = self.conjuntos[1]
        if len(self.conjuntos) == 3:
            conjuntoC = self.conjuntos[2]

        if len(self.conjuntos)==2:
            for i in conjuntoA:
                if i not in conjuntoB:
                    conjuntoDifenrenciaAB.add(i)
        
            for i in conjuntoB:
                if i not in conjuntoA:
                    conjuntoDifenrenciaBA.add(i)
            venn_diagram = venn2([conjuntoA, conjuntoB], set_labels=("Conjunto A", "Conjunto B"))
            venn_diagram.get_label_by_id('100').set_text(', '.join(map(str, conjuntoA - conjuntoB)))
            venn_diagram.get_label_by_id('010').set_text(', '.join(map(str, conjuntoB - conjuntoA)))
            venn_diagram.get_label_by_id('110').set_text(', '.join(map(str, conjuntoA & conjuntoB)))


        plt.title("Diferencia")
        plt.annotate(conjuntoDifenrenciaAB, xy=(0.5, 0.97), xycoords="axes fraction",ha="center", va="center", fontsize=12, color="red")
        plt.annotate(conjuntoDifenrenciaBA, xy=(0.5, 0.92), xycoords="axes fraction",ha="center", va="center", fontsize=12, color="red")
        plt.annotate("conjuntoDifenrenciaAB:", xy=(0.2, 0.97), xycoords="axes fraction",ha="center", va="center", fontsize=12, color="red")
        plt.annotate("conjuntoDifenrenciaBA:", xy=(0.2, 0.92), xycoords="axes fraction",ha="center", va="center", fontsize=12, color="red")
        plt.show()

        

    def realizar_complemento(self):
        print("a")

    def mostrar_resultado(self, resultado):
        self.resultado_var.set(f"Resultado: {resultado}")

    def actualizar_resultado(self):
        self.resultado_var.set("Resultado: ")


if __name__ == "__main__":
    root = tk.Tk()
    app = ConjuntosApp(root)
    root.mainloop()
