import tkinter as tk
class ContadorClics:
    def __init__(self, root):
        self.root = root
        self.root.title("Contador de Clics")
        self.contador = 0
        self.etiqueta = tk.Label(self.root, text=  , font=("Arial", 12))
        self.etiqueta.pack(pady=10)
        self.boton =tk.Button(self.root, text="Contar Clics", command=self.contar_clics) 
        self.boton.pack(padx=20, pady=20)
        
    def contar_clics(self):
        self.contador +=1
        webo=print(f"numero de clic {self.contador}")
        
if __name__ == "__main__" :
    ventana = tk . Tk()
    app = ContadorClics(ventana)
    ventana.mainloop()
    