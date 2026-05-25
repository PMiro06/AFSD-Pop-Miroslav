import tkinter as tk
import random


class SemaforInteligentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Semafor Inteligent - Optimizare Intersecții")
        self.root.geometry("850x600")
        self.root.resizable(False, False)

        self.masini_NS = random.randint(1, 10)
        self.masini_EV = random.randint(1, 10)

        #Lista ID masini
        self.desene_masini = []

        # Lumini semafor
        self.verde_NS = True
        self.timp_ramas = 10
        self.mod_inteligent = tk.BooleanVar(value=True)

        self.creeaza_interfata()
        self.actualizeaza_simulare()
        self.bucla_principala()

    def creeaza_interfata(self):
        panou_control = tk.Frame(self.root, width=280, bg="#f0f0f0", bd=2, relief=tk.GROOVE)
        panou_control.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        tk.Label(panou_control, text="PANOU CONTROL", font=("Arial", 14, "bold"), bg="#f0f0f0").pack(pady=10)

        # but AI
        tk.Checkbutton(panou_control, text="Activează Algoritm Inteligent", variable=self.mod_inteligent,
                       font=("Arial", 11), bg="#f0f0f0").pack(pady=10, anchor="w", padx=10)

        # Control masini manuakl
        tk.Label(panou_control, text="Control Trafic Manual:", font=("Arial", 11, "bold"), bg="#f0f0f0").pack(pady=10)

        # Axa N-S
        tk.Label(panou_control, text="Axa Nord-Sud:", font=("Arial", 10, "italic"), bg="#f0f0f0").pack(anchor="w",
                                                                                                       padx=20)
        frame_ns = tk.Frame(panou_control, bg="#f0f0f0")
        frame_ns.pack(fill=tk.X, padx=20, pady=5)

        btn_add_ns = tk.Button(frame_ns, text="+5 Mașini", command=lambda: self.modifica_masini('NS', 5), bg="#c8e6c9",
                               width=10)
        btn_add_ns.pack(side=tk.LEFT, expand=True, padx=2)

        btn_sub_ns = tk.Button(frame_ns, text="-5 Mașini", command=lambda: self.modifica_masini('NS', -5), bg="#ffcdd2",
                               width=10)
        btn_sub_ns.pack(side=tk.RIGHT, expand=True, padx=2)

        # Axa E-V
        tk.Label(panou_control, text="Axa Est-Vest:", font=("Arial", 10, "italic"), bg="#f0f0f0").pack(anchor="w",
                                                                                                       padx=20,
                                                                                                       pady=(10, 0))
        frame_ev = tk.Frame(panou_control, bg="#f0f0f0")
        frame_ev.pack(fill=tk.X, padx=20, pady=5)

        btn_add_ev = tk.Button(frame_ev, text="+5 Mașini", command=lambda: self.modifica_masini('EV', 5), bg="#c8e6c9",
                               width=10)
        btn_add_ev.pack(side=tk.LEFT, expand=True, padx=2)

        btn_sub_ev = tk.Button(frame_ev, text="-5 Mașini", command=lambda: self.modifica_masini('EV', -5), bg="#ffcdd2",
                               width=10)
        btn_sub_ev.pack(side=tk.RIGHT, expand=True, padx=2)

        # Stats
        tk.Label(panou_control, text="STATISTICI", font=("Arial", 12, "bold"), bg="#f0f0f0").pack(pady=20)
        self.lbl_stat_ns = tk.Label(panou_control, text="", font=("Arial", 10), bg="#f0f0f0", justify=tk.LEFT)
        self.lbl_stat_ns.pack(anchor="w", padx=10)

        self.canvas = tk.Canvas(self.root, width=540, height=580, bg="#2e7d32")
        self.canvas.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.canvas.create_rectangle(220, 0, 320, 580, fill="#555555", outline="")  # Șosea N-S
        self.canvas.create_rectangle(0, 240, 540, 340, fill="#555555", outline="")  # Șosea E-V

        self.canvas.create_line(270, 0, 270, 580, fill="white", dash=(10, 10))
        self.canvas.create_line(0, 290, 540, 290, fill="white", dash=(10, 10))

        # Corp semafor
        self.sem_NS_corp = self.canvas.create_rectangle(330, 170, 360, 230, fill="black")
        self.sem_EV_corp = self.canvas.create_rectangle(180, 350, 240, 380, fill="black")

        # Lumini semafoare
        self.lumina_N = self.canvas.create_oval(335, 175, 355, 195, fill="grey")
        self.lumina_S = self.canvas.create_oval(335, 205, 355, 225, fill="grey")

        self.lumina_E = self.canvas.create_oval(185, 355, 205, 375, fill="grey")
        self.lumina_V = self.canvas.create_oval(215, 355, 235, 375, fill="grey")

        # Afisez nr masini + timp
        self.txt_timp = self.canvas.create_text(270, 290, text="", font=("Arial", 24, "bold"), fill="yellow")
        self.txt_masini_NS = self.canvas.create_text(270, 20, text="", font=("Arial", 14, "bold"), fill="white")
        self.txt_masini_EV = self.canvas.create_text(90, 210, text="", font=("Arial", 14, "bold"), fill="white")

    def modifica_masini(self, directie, nr):
        if directie == 'NS':
            self.masini_NS += nr
        else:
            self.masini_EV += nr

        self.masini_NS = max(0, self.masini_NS)
        self.masini_EV = max(0, self.masini_EV)
        self.actualizeaza_simulare()

    def calculeaza_timp_inteligent(self):
        if not self.mod_inteligent.get():
            return 10

        baza = self.masini_NS if self.verde_NS else self.masini_EV
        timp = 5 + int(baza * 0.8)
        return min(max(timp, 5), 25)

    def actualizeaza_simulare(self):
        # Schimbare culori semafoare
        if self.verde_NS:
            self.canvas.itemconfig(self.lumina_N, fill="#00ff00")
            self.canvas.itemconfig(self.lumina_S, fill="grey")
            self.canvas.itemconfig(self.lumina_E, fill="#ff0000")
            self.canvas.itemconfig(self.lumina_V, fill="grey")
        else:
            self.canvas.itemconfig(self.lumina_N, fill="grey")
            self.canvas.itemconfig(self.lumina_S, fill="#ff0000")
            self.canvas.itemconfig(self.lumina_E, fill="grey")
            self.canvas.itemconfig(self.lumina_V, fill="#00ff00")

        self.canvas.itemconfig(self.txt_timp, text=str(self.timp_ramas))
        self.canvas.itemconfig(self.txt_masini_NS, text=f"Mașini N-S: {self.masini_NS}")
        self.canvas.itemconfig(self.txt_masini_EV, text=f"Mașini E-V: {self.masini_EV}")

        mod_text = "Inteligent (Dinamic)" if self.mod_inteligent.get() else "Clasic (Fix - 10s)"
        stat_text = f"Mod curent:\n{mod_text}\n\nTrafic în așteptare:\n- Axa Nord-Sud: {self.masini_NS} mașini\n- Axa Est-Vest: {self.masini_EV} mașini"
        self.lbl_stat_ns.config(text=stat_text)


        for masina in self.desene_masini:
            self.canvas.delete(masina)
        self.desene_masini.clear()


        for i in range(self.masini_NS):
            y_pos = 200 - (i * 30)
            if y_pos > 0:
                id_masina = self.canvas.create_rectangle(235, y_pos - 25, 250, y_pos, fill="#1e88e5", outline="white")
                self.desene_masini.append(id_masina)

        for i in range(self.masini_EV):
            x_pos = 190 - (i * 30)
            if x_pos > 0:
                id_masina = self.canvas.create_rectangle(x_pos - 25, 245, x_pos, 260, fill="#e53935", outline="white")
                self.desene_masini.append(id_masina)

    def bucla_principala(self):
        if self.timp_ramas > 0:
            self.timp_ramas -= 1

            if self.verde_NS and self.masini_NS > 0:
                self.masini_NS -= random.randint(0, 2)
            elif not self.verde_NS and self.masini_EV > 0:
                self.masini_EV -= random.randint(0, 2)

            if random.random() < 0.4: self.masini_NS += random.randint(1, 2)
            if random.random() < 0.4: self.masini_EV += random.randint(1, 2)

            self.masini_NS = max(0, self.masini_NS)
            self.masini_EV = max(0, self.masini_EV)
        else:
            self.verde_NS = not self.verde_NS
            self.timp_ramas = self.calculeaza_timp_inteligent()

        self.actualizeaza_simulare()
        self.root.after(1000, self.bucla_principala)


if __name__ == "__main__":
    root = tk.Tk()
    app = SemaforInteligentApp(root)
    root.mainloop()