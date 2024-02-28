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

        self.boton_cardinalidad = tk.Button(self.master, text="Cardinalidad", command=self.cardinalidad_conjuntos)
        self.boton_cardinalidad.pack(pady=5)

        self.boton_disyuncion = tk.Button(self.master, text="Validar Disyunción", command=self.validar_disyuncion)
        self.boton_disyuncion.pack(pady=5)

        self.boton_salir = tk.Button(self.master, text="Salir", command=self.salir)
        self.boton_salir.pack(pady=5)

    def salir(self):
        self.master.destroy()

    def agregar_conjunto(self):
    # Verificar que no se hayan ingresado más de 3 conjuntos
        if len(self.conjuntos) < 3:
            # Crear una ventana secundaria para ingresar un nuevo conjunto
            ventana_agregar_conjunto = tk.Toplevel(self.master)
            ventana_agregar_conjunto.title("Agregar Conjunto")

            # Etiqueta con instrucciones
            etiqueta_instrucciones = tk.Label(ventana_agregar_conjunto, text="Ingrese elementos del conjunto separados por comas:")
            etiqueta_instrucciones.pack(pady=10)

            # Campo de entrada para el nuevo conjunto
            entry_conjunto = tk.Entry(ventana_agregar_conjunto)
            entry_conjunto.pack(pady=10)

            # Botón para guardar el conjunto ingresado
            btn_guardar_conjunto = tk.Button(ventana_agregar_conjunto, text="Guardar Conjunto", command=lambda: self.guardar_conjunto(entry_conjunto.get(), ventana_agregar_conjunto))
            btn_guardar_conjunto.pack(pady=10)
        else:
            # Mostrar mensaje de advertencia si ya se han ingresado tres conjuntos
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
        # Conjunto para almacenar la unión de los conjuntos
        conjuntoUnion = set()
        
        # Obtener los conjuntos A y B
        conjuntoA = self.conjuntos[0]
        conjuntoB = self.conjuntos[1]
        
        # Verificar si hay un tercer conjunto
        if len(self.conjuntos) == 3:
            conjuntoC = self.conjuntos[2]

        # Caso para dos conjuntos
        if len(self.conjuntos) == 2:
            # Agregar elementos de A a la unión
            for i in conjuntoA:
                conjuntoUnion.add(i)
            # Agregar elementos de B a la unión si no están presentes
            for i in conjuntoB:
                if i not in conjuntoUnion:
                    conjuntoUnion.add(i)
            
            # Crear diagrama de Venn para dos conjuntos
            venn_diagram = venn2([conjuntoA, conjuntoB], set_labels=("Conjunto A", "Conjunto B"))
            # Configurar etiquetas para las áreas del diagrama
            venn_diagram.get_label_by_id('100').set_text(', '.join(map(str, conjuntoA - conjuntoB)))
            venn_diagram.get_label_by_id('010').set_text(', '.join(map(str, conjuntoB - conjuntoA)))
            venn_diagram.get_label_by_id('110').set_text(', '.join(map(str, conjuntoA & conjuntoB)))

        # Caso para tres conjuntos
        if len(self.conjuntos) == 3:
            # Agregar elementos de A a la unión
            for i in conjuntoA:
                conjuntoUnion.add(i)
            # Agregar elementos de B a la unión si no están presentes
            for i in conjuntoB:
                if i not in conjuntoUnion:
                    conjuntoUnion.add(i)
            # Agregar elementos de C a la unión si no están presentes
            for i in conjuntoC:
                if i not in conjuntoUnion:
                    conjuntoUnion.add(i)
            
            # Crear diagrama de Venn para tres conjuntos
            venn3([conjuntoA, conjuntoB, conjuntoC], set_labels=("Conjunto A", "Conjunto B", "Conjunto C"))

        # Configurar título y anotación para la unión
        plt.title("Unión")
        plt.annotate(conjuntoUnion, xy=(0.5, 1), xycoords="axes fraction", ha="center", va="center", fontsize=12, color="red")
        
        # Mostrar el gráfico
        plt.show()

    def realizar_interseccion(self):
        # Conjunto para almacenar la intersección de los conjuntos
        conjuntoInterseccion = set()
        
        # Obtener los conjuntos A y B
        conjuntoA = self.conjuntos[0]
        conjuntoB = self.conjuntos[1]
        
        # Verificar si hay un tercer conjunto
        if len(self.conjuntos) == 3:
            conjuntoC = self.conjuntos[2]

        # Caso para dos conjuntos
        if len(self.conjuntos) == 2:
            # Encontrar elementos comunes y agregarlos al conjunto de intersección
            for i in conjuntoA:
                if i in conjuntoB:
                    conjuntoInterseccion.add(i)
            
            # Crear diagrama de Venn para dos conjuntos
            venn_diagram = venn2([conjuntoA, conjuntoB], set_labels=("Conjunto A", "Conjunto B"))
            # Configurar etiquetas para las áreas del diagrama
            venn_diagram.get_label_by_id('100').set_text(', '.join(map(str, conjuntoA - conjuntoB)))
            venn_diagram.get_label_by_id('010').set_text(', '.join(map(str, conjuntoB - conjuntoA)))
            venn_diagram.get_label_by_id('110').set_text(', '.join(map(str, conjuntoA & conjuntoB)))

        # Caso para tres conjuntos
        if len(self.conjuntos) == 3:
            # Encontrar elementos comunes en A, B y C y agregarlos al conjunto de intersección
            for i in conjuntoA:
                if i in conjuntoB and i in conjuntoC:
                    conjuntoInterseccion.add(i)
            
            # Crear diagrama de Venn para tres conjuntos
            venn3([conjuntoA, conjuntoB, conjuntoC], set_labels=("Conjunto A", "Conjunto B", "Conjunto C"))

        # Configurar título y anotación para la intersección
        plt.title("Intersección")
        plt.annotate(conjuntoInterseccion, xy=(0.5, 0.95), xycoords="axes fraction", ha="center", va="center", fontsize=12, color="red")
        
        # Mostrar el gráfico
        plt.show()

    def realizar_diferencia(self):
        # Conjuntos para almacenar las diferencias entre los conjuntos
        conjuntoDiferenciaAB = set()
        conjuntoDiferenciaBA = set()
        conjuntoDiferenciaAC = set()
        conjuntoDiferenciaCA = set()
        conjuntoDiferenciaBC = set()
        conjuntoDiferenciaCB = set()

        # Obtener los conjuntos A y B
        conjuntoA = self.conjuntos[0]
        conjuntoB = self.conjuntos[1]

        # Verificar si hay un tercer conjunto
        if len(self.conjuntos) == 3:
            conjuntoC = self.conjuntos[2]

        # Caso para dos conjuntos
        if len(self.conjuntos) == 2:
            # Encontrar elementos en A que no están en B
            for i in conjuntoA:
                if i not in conjuntoB:
                    conjuntoDiferenciaAB.add(i)
            
            # Encontrar elementos en B que no están en A
            for i in conjuntoB:
                if i not in conjuntoA:
                    conjuntoDiferenciaBA.add(i)
            
            # Crear diagrama de Venn para dos conjuntos
            venn_diagram = venn2([conjuntoA, conjuntoB], set_labels=("Conjunto A", "Conjunto B"))
            # Configurar etiquetas para las áreas del diagrama
            venn_diagram.get_label_by_id('100').set_text(', '.join(map(str, conjuntoA - conjuntoB)))
            venn_diagram.get_label_by_id('010').set_text(', '.join(map(str, conjuntoB - conjuntoA)))
            venn_diagram.get_label_by_id('110').set_text(', '.join(map(str, conjuntoA & conjuntoB)))
            # Anotar las diferencias entre conjuntos en el gráfico
            plt.annotate("conjuntoDiferenciaAB:" + str(conjuntoDiferenciaAB), xy=(-0.2, 0.97), xycoords="axes fraction", ha="center", va="center", fontsize=12, color="red")
            plt.annotate("conjuntoDiferenciaBA:" + str(conjuntoDiferenciaBA), xy=(-0.2, 0.92), xycoords="axes fraction", ha="center", va="center", fontsize=12, color="red")

        # Caso para tres conjuntos
        if len(self.conjuntos) == 3:
            # Encontrar elementos en A que no están en B y en C
            for i in conjuntoA:
                if i not in conjuntoB:
                    conjuntoDiferenciaAB.add(i)
                if i not in conjuntoC:
                    conjuntoDiferenciaAC.add(i)

            # Encontrar elementos en B que no están en A y en C
            for i in conjuntoB:
                if i not in conjuntoA:
                    conjuntoDiferenciaBA.add(i)
                if i not in conjuntoC:
                    conjuntoDiferenciaBC.add(i)

            # Encontrar elementos en C que no están en A y en B
            for i in conjuntoC:
                if i not in conjuntoA:
                    conjuntoDiferenciaCA.add(i)
                if i not in conjuntoB:
                    conjuntoDiferenciaCB.add(i)

            # Crear diagrama de Venn para tres conjuntos
            venn3([conjuntoA, conjuntoB, conjuntoC], set_labels=("Conjunto A", "Conjunto B", "Conjunto C"))
            # Anotar las diferencias entre conjuntos en el gráfico
            plt.annotate("conjuntoDiferenciaAB: " + str(conjuntoDiferenciaAB), xy=(-0.2, 0.9), xycoords="axes fraction", ha="center", va="center", fontsize=12, color="red")
            plt.annotate("conjuntoDiferenciaBA: " + str(conjuntoDiferenciaBA), xy=(-0.2, 0.8), xycoords="axes fraction", ha="center", va="center", fontsize=12, color="red")
            plt.annotate("conjuntoDiferenciaAC: " + str(conjuntoDiferenciaAC), xy=(-0.2, 0.7), xycoords="axes fraction", ha="center", va="center", fontsize=12, color="red")
            plt.annotate("conjuntoDiferenciaCA: " + str(conjuntoDiferenciaCA), xy=(-0.2, 0.6), xycoords="axes fraction", ha="center", va="center", fontsize=12, color="red")
            plt.annotate("conjuntoDiferenciaBC: " + str(conjuntoDiferenciaBC), xy=(-0.2, 0.5), xycoords="axes fraction", ha="center", va="center", fontsize=12, color="red")
            plt.annotate("conjuntoDiferenciaCB: " + str(conjuntoDiferenciaCB), xy=(-0.2, 0.4), xycoords="axes fraction", ha="center", va="center", fontsize=12, color="red")

        # Configurar título y mostrar el gráfico
        plt.title("Diferencia")
        plt.show()

    def realizar_complemento(self):
        # Obtener conjuntos A y B
        conjuntoA = self.conjuntos[0]
        conjuntoB = self.conjuntos[1]

        # Verificar si hay un tercer conjunto
        if len(self.conjuntos) == 3:
            conjuntoC = self.conjuntos[2]

        # Conjuntos para almacenar complementos y el conjunto universal
        conjuntoCA = set()
        conjuntoCB = set()
        conjuntoCC = set()
        conjuntoU = set()

        # Caso para dos conjuntos
        if len(self.conjuntos) == 2:
            # Construir el conjunto universal como la unión de A y B
            for i in conjuntoA:
                conjuntoU.add(i)
            for i in conjuntoB:
                if i not in conjuntoU:
                    conjuntoU.add(i)

            # Encontrar el complemento de A en el conjunto universal
            for i in conjuntoU:
                if i not in conjuntoA:
                    conjuntoCA.add(i)

            # Encontrar el complemento de B en el conjunto universal
            for i in conjuntoU:
                if i not in conjuntoB:
                    conjuntoCB.add(i)

            # Crear diagrama de Venn para dos conjuntos
            venn_diagram = venn2([conjuntoA, conjuntoB], set_labels=("Conjunto A", "Conjunto B"))
            venn_diagram.get_label_by_id('100').set_text(', '.join(map(str, conjuntoA - conjuntoB)))
            venn_diagram.get_label_by_id('010').set_text(', '.join(map(str, conjuntoB - conjuntoA)))
            venn_diagram.get_label_by_id('110').set_text(', '.join(map(str, conjuntoA & conjuntoB)))

            # Anotar los complementos en el gráfico
            plt.annotate("conjunto CA:" + str(conjuntoCA), xy=(-0.2, 0.97), xycoords="axes fraction", ha="center", va="center", fontsize=12, color="red")
            plt.annotate("conjunto CB:" + str(conjuntoCB), xy=(-0.2, 0.92), xycoords="axes fraction", ha="center", va="center", fontsize=12, color="red")

        # Caso para tres conjuntos
        if len(self.conjuntos) == 3:
            # Construir el conjunto universal como la unión de A, B y C
            for i in conjuntoA:
                conjuntoU.add(i)
            for i in conjuntoB:
                if i not in conjuntoU:
                    conjuntoU.add(i)
            for i in conjuntoC:
                if i not in conjuntoU:
                    conjuntoU.add(i)

            # Encontrar el complemento de A en el conjunto universal
            for i in conjuntoU:
                if i not in conjuntoA:
                    conjuntoCA.add(i)

            # Encontrar el complemento de B en el conjunto universal
            for i in conjuntoU:
                if i not in conjuntoB:
                    conjuntoCB.add(i)

            # Encontrar el complemento de C en el conjunto universal
            for i in conjuntoU:
                if i not in conjuntoC:
                    conjuntoCC.add(i)

            # Crear diagrama de Venn para tres conjuntos
            venn3([conjuntoA, conjuntoB, conjuntoC], set_labels=("Conjunto A", "Conjunto B", "Conjunto C"))

            # Anotar los complementos en el gráfico
            plt.annotate("conjunto CA:" + str(conjuntoCA), xy=(-0.2, 0.88), xycoords="axes fraction", ha="center", va="center", fontsize=12, color="red")
            plt.annotate("conjunto CB:" + str(conjuntoCB), xy=(-0.2, 0.92), xycoords="axes fraction", ha="center", va="center", fontsize=12, color="red")
            plt.annotate("conjunto CC:" + str(conjuntoCC), xy=(-0.2, 0.96), xycoords="axes fraction", ha="center", va="center", fontsize=12, color="red")

        # Configurar título y mostrar el gráfico
        plt.title("Complemento")
        plt.show()

    def cardinalidad_conjuntos(self):
        # Inicializar contadores de cantidad
        cantidadA = 0
        cantidadB = 0
        cantidadC = 0

        # Obtener conjuntos A y B
        conjuntoA = self.conjuntos[0]
        conjuntoB = self.conjuntos[1]

        # Contar elementos en conjunto A
        for elemento in conjuntoA:
            cantidadA += 1

        # Contar elementos en conjunto B
        for elemento in conjuntoB:
            cantidadB += 1

        # Verificar si hay un tercer conjunto
        if len(self.conjuntos) == 3:
            conjuntoC = self.conjuntos[2]

            # Contar elementos en conjunto C
            for elemento in conjuntoC:
                cantidadC += 1

        # Mostrar mensajes de cardinalidades según la cantidad de conjuntos
        if len(self.conjuntos) == 2:
            messagebox.showinfo("Cardinalidades", "El conjunto A tiene: {} elementos\nEl conjunto B tiene: {} elementos".format(cantidadA, cantidadB))
        else:
            messagebox.showinfo("Cardinalidades", "El conjunto A tiene: {} elementos\nEl conjunto B tiene: {} elementos\nEl conjunto C tiene: {} elementos".format(cantidadA, cantidadB, cantidadC))

    def validar_disyuncion(self):
        # Verificar si hay al menos dos conjuntos
        if len(self.conjuntos) < 2:
            messagebox.showwarning("Error", "Se requieren al menos dos conjuntos para la validación de disyunción.")
            return

        # Obtener conjuntos A y B
        conjuntoA = self.conjuntos[0]
        conjuntoB = self.conjuntos[1]

        # Iterar sobre pares de conjuntos
        for i in range(len(self.conjuntos) - 1):
            for j in range(i + 1, len(self.conjuntos)):
                conjuntoC = self.conjuntos[j]

                # Verificar si hay elementos comunes entre los conjuntos
                if any(elemento in conjuntoC for elemento in conjuntoA) or any(elemento in conjuntoC for elemento in conjuntoB):
                    messagebox.showinfo("Validación de Disyunción", "Los conjuntos NO son disjuntos.")
                    return

        # Si no se encontraron elementos comunes, los conjuntos son disjuntos
        messagebox.showinfo("Validación de Disyunción", "Los conjuntos son disjuntos.")


if __name__ == "__main__":
    root = tk.Tk()
    app = ConjuntosApp(root)
    root.mainloop()
