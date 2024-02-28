import tkinter as tk
from matplotlib import pyplot as plt
from tkinter import simpledialog, messagebox
from matplotlib_venn import venn2, venn3

class ConjuntosApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Conjuntos")
        self.master.geometry("600x500")
        self.conjuntos = [{"1","2","3","4"}, {"4","5","6","7"}, {"4","8","9"}]
        

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

        self.boton_cardinalidad = tk.Button(self.master, text="Cardinalidad", command=self.cardinalidad_conjuntos)
        self.boton_cardinalidad.pack(pady=5)

        self.boton_disyuncion = tk.Button(self.master, text="Validar Disyunción", command=self.validar_disyuncion)
        self.boton_disyuncion.pack(pady=5)

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

        
            if len(self.conjuntos) == 2:
                for i in conjuntoA:
                    conjuntoUnion.add(i)
                for i in conjuntoB:
                    if i not in conjuntoUnion:
                        conjuntoUnion.add(i)
                venn_diagram = venn2([conjuntoA, conjuntoB], set_labels=("Conjunto A", "Conjunto B"))
                venn_diagram.get_label_by_id('100').set_text(', '.join(map(str, conjuntoA - conjuntoB)))
                venn_diagram.get_label_by_id('010').set_text(', '.join(map(str, conjuntoB - conjuntoA)))
                venn_diagram.get_label_by_id('110').set_text(', '.join(map(str, conjuntoA & conjuntoB)))
                

        # Utiliza venn3 si tienes tres conjuntos
        if len(self.conjuntos) == 3:
            for i in conjuntoA:
                conjuntoUnion.add(i)
            for i in conjuntoB:
                if i not in conjuntoUnion:
                    conjuntoUnion.add(i)
            for i in conjuntoC:
                if i not in conjuntoUnion:
                    conjuntoUnion.add(i)
            venn3([conjuntoA, conjuntoB, conjuntoC], set_labels=("Conjunto A", "Conjunto B", "Conjunto C"))
            
                    

        plt.title("Union")
        plt.annotate(conjuntoUnion, xy=(0.5, 1), xycoords="axes fraction",ha="center", va="center", fontsize=12, color="red")
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

        if len(self.conjuntos) == 3:
            for i in conjuntoA:
                if i in conjuntoB and i in conjuntoC:
                    conjuntoInterseccion.add(i)
            venn3([conjuntoA, conjuntoB, conjuntoC], set_labels=("Conjunto A", "Conjunto B", "Conjunto C"))

        
        
        plt.title("Intersección")
        plt.annotate(conjuntoInterseccion, xy=(0.5, 0.95), xycoords="axes fraction",ha="center", va="center", fontsize=12, color="red")
        plt.show()

    def realizar_diferencia(self):
        conjuntoDifenrenciaAB = set()
        conjuntoDifenrenciaBA = set()
        conjuntoDifenrenciaAC = set()
        conjuntoDifenrenciaCA = set()
        conjuntoDifenrenciaBC = set()
        conjuntoDifenrenciaCB = set()
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
            plt.annotate("conjuntoDifenrenciaAB:" + str(conjuntoDifenrenciaAB), xy=(-0.2, 0.97), xycoords="axes fraction",ha="center", va="center", fontsize=12, color="red")
            plt.annotate("conjuntoDifenrenciaBA:" + str(conjuntoDifenrenciaBA), xy=(-0.2, 0.92), xycoords="axes fraction",ha="center", va="center", fontsize=12, color="red")

        if len(self.conjuntos)==3:
            for i in conjuntoA:
                if i not in conjuntoB:
                    conjuntoDifenrenciaAB.add(i)
                if i not in conjuntoC:
                    conjuntoDifenrenciaAC.add(i)

            for i in conjuntoB:
                if i not in conjuntoA:
                    conjuntoDifenrenciaBA.add(i)
                if i not in conjuntoC:
                    conjuntoDifenrenciaBC.add(i)

            for i in conjuntoC:
                if i not in conjuntoA:
                    conjuntoDifenrenciaCA.add(i)
                if i not in conjuntoB:
                    conjuntoDifenrenciaCB.add(i)
            venn3([conjuntoA, conjuntoB, conjuntoC], set_labels=("Conjunto A", "Conjunto B", "Conjunto C"))
            plt.annotate("conjuntoDifenrenciaAB: " + str(conjuntoDifenrenciaAB), xy=(-0.2, 0.9), xycoords="axes fraction", ha="center", va="center", fontsize=12, color="red")
            plt.annotate("conjuntoDifenrenciaBA: " + str(conjuntoDifenrenciaBA), xy=(-0.2, 0.8), xycoords="axes fraction", ha="center", va="center", fontsize=12, color="red")
            plt.annotate("conjuntoDifenrenciaAC: " + str(conjuntoDifenrenciaAC), xy=(-0.2, 0.7), xycoords="axes fraction", ha="center", va="center", fontsize=12, color="red")
            plt.annotate("conjuntoDifenrenciaCA: " + str(conjuntoDifenrenciaCA), xy=(-0.2, 0.6), xycoords="axes fraction", ha="center", va="center", fontsize=12, color="red")
            plt.annotate("conjuntoDifenrenciaBC: " + str(conjuntoDifenrenciaBC), xy=(-0.2, 0.5), xycoords="axes fraction", ha="center", va="center", fontsize=12, color="red")
            plt.annotate("conjuntoDifenrenciaCB: " + str(conjuntoDifenrenciaCB), xy=(-0.2, 0.4), xycoords="axes fraction", ha="center", va="center", fontsize=12, color="red")
                    


        plt.title("Diferencia")
        
        plt.show()

        

    def realizar_complemento(self):
        conjuntoA = self.conjuntos[0]
        conjuntoB = self.conjuntos[1]
        if len(self.conjuntos) == 3:
            conjuntoC = self.conjuntos[2]
        conjuntoCA = set()
        conjuntoCB = set()
        conjuntoCC = set()
        conjuntoU = set()

        if len(self.conjuntos) ==2:
            for i in conjuntoA:
                conjuntoU.add(i)

            for i in conjuntoB:
                if i not in conjuntoU:
                    conjuntoU.add(i)
            
            for i in conjuntoU:
                if i not in conjuntoA:
                    conjuntoCA.add(i)
            
            for i in conjuntoU:
                if i not in conjuntoB:
                    conjuntoCB.add(i)
            
            venn_diagram = venn2([conjuntoA, conjuntoB], set_labels=("Conjunto A", "Conjunto B"))
            venn_diagram.get_label_by_id('100').set_text(', '.join(map(str, conjuntoA - conjuntoB)))
            venn_diagram.get_label_by_id('010').set_text(', '.join(map(str, conjuntoB - conjuntoA)))
            venn_diagram.get_label_by_id('110').set_text(', '.join(map(str, conjuntoA & conjuntoB)))

            plt.annotate("conjunto CA:" + str(conjuntoCA), xy=(-0.29, 0.97), xycoords="axes fraction",ha="center", va="center", fontsize=12, color="red")
            plt.annotate("conjunto CB:" + str(conjuntoCB), xy=(-0.29, 0.92), xycoords="axes fraction",ha="center", va="center", fontsize=12, color="red")

        if len(self.conjuntos) == 3:
                
            for i in conjuntoA:
                conjuntoU.add(i)
                
            for i in conjuntoB:
                if i not in conjuntoU:
                    conjuntoU.add(i)

                # Agregar elementos de conjuntoC que aún no están en conjuntoU
            for i in conjuntoC:
                if i not in conjuntoU:
                    conjuntoU.add(i)

                # Encontrar el complemento de conjuntoA dentro de conjuntoU
            for i in conjuntoU:
                if i not in conjuntoA:
                    conjuntoCA.add(i)

                # Encontrar el complemento de conjuntoB dentro de conjuntoU
            for i in conjuntoU:
                if i not in conjuntoB:
                    conjuntoCB.add(i)

                # Encontrar el complemento de conjuntoC dentro de conjuntoU
            for i in conjuntoU:
                if i not in conjuntoC:
                    conjuntoCC.add(i)

                # Anotar los conjuntos obtenidos
            
                # Anotar nombres de conjuntos
            plt.annotate("conjunto CA:" + str(conjuntoCA), xy=(-0.2, 0.88), xycoords="axes fraction", ha="center", va="center", fontsize=12, color="red")
            plt.annotate("conjunto CB:" + str(conjuntoCB), xy=(-0.2, 0.92), xycoords="axes fraction", ha="center", va="center", fontsize=12, color="red")
            plt.annotate("conjunto CC:" + str(conjuntoCC), xy=(-0.2, 0.96), xycoords="axes fraction", ha="center", va="center", fontsize=12, color="red")
            venn3([conjuntoA, conjuntoB, conjuntoC], set_labels=("Conjunto A", "Conjunto B", "Conjunto C"))             

        
        plt.title("Complemento")
        plt.show()

    def cardinalidad_conjuntos(self):
        cantidadA = 0
        cantidadB = 0
        cantidadC = 0

        conjuntoA = self.conjuntos[0]
        conjuntoB = self.conjuntos[1]

        for elemento in conjuntoA:
            cantidadA += 1

        for elemento in conjuntoB:
            cantidadB += 1

        if len(self.conjuntos) == 3:
            conjuntoC = self.conjuntos[2]
            for elemento in conjuntoC:
                cantidadC += 1

        if len(self.conjuntos) == 2:
            messagebox.showinfo("Cardinalidades", "El conjunto A tiene: {} elementos\nEl conjunto B tiene: {} elementos".format(cantidadA, cantidadB))
        else:
            messagebox.showinfo("Cardinalidades", "El conjunto A tiene: {} elementos\nEl conjunto B tiene: {} elementos\nEl conjunto C tiene: {} elementos".format(cantidadA, cantidadB, cantidadC))


    def validar_disyuncion(self):
        if len(self.conjuntos) < 2:
            messagebox.showwarning("Error", "Se requieren al menos dos conjuntos para la validación de disyunción.")
            return

        conjuntoA = self.conjuntos[0]
        conjuntoB = self.conjuntos[1]

        for i in range(len(self.conjuntos) - 1):
            for j in range(i + 1, len(self.conjuntos)):
                conjuntoC = self.conjuntos[j]
                if any(elemento in conjuntoC for elemento in conjuntoA) or any(elemento in conjuntoC for elemento in conjuntoB):
                    messagebox.showinfo("Validación de Disyunción", "Los conjuntos NO son disjuntos.")
                    return

        messagebox.showinfo("Validación de Disyunción", "Los conjuntos son disjuntos.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ConjuntosApp(root)
    root.mainloop()
