import tkinter as tk
from tkinter import messagebox, Toplevel
import itertools

class TruthTableSolver:
    def __init__(self, master):
        self.master = master
        self.master.title("Wahrheitstabelle zu Boolescher Term")
        self.master.geometry("400x200")

        self.label = tk.Label(master, text="Anzahl der Eingabe- und Ausgabevariablen:")
        self.label.pack()

        self.entry_inputs = tk.Entry(master)
        self.entry_inputs.insert(0, "Anzahl Eingabevariablen")
        self.entry_inputs.pack()

        self.entry_outputs = tk.Entry(master)
        self.entry_outputs.insert(0, "Anzahl Ausgabevariablen")
        self.entry_outputs.pack()

        self.generate_button = tk.Button(master, text="Wahrheitstabelle erzeugen", command=self.generate_table_window)
        self.generate_button.pack()

        self.solve_button = tk.Button(master, text="Booleschen Term erzeugen", command=self.solve_table)
        self.solve_button.pack()

        self.table_window = None
        self.table_entries = []

    def generate_table_window(self):
        if self.table_window:
            self.table_window.destroy()
            self.table_entries.clear()

        try:
            num_inputs = int(self.entry_inputs.get())
            num_outputs = int(self.entry_outputs.get())
            if num_inputs < 1 or num_inputs > 5 or num_outputs < 1 or num_outputs > 5:
                raise ValueError("Bitte eine Zahl zwischen 1 und 5 für Eingaben und Ausgaben eingeben.")
        except ValueError as e:
            messagebox.showerror("Ungültige Eingabe", str(e))
            return

        self.table_window = Toplevel(self.master)
        self.table_window.title("Wahrheitstabelle Eingabe")
        self.table_window.geometry("600x600")

        variables = [f"Eingabe {i}" for i in range(1, num_inputs + 1)] + [f"Ausgabe {i}" for i in range(1, num_outputs + 1)]
        for i, var in enumerate(variables):
            label = tk.Label(self.table_window, text=var, borderwidth=1, relief="solid", width=10)
            label.grid(row=0, column=i)

        for i, combination in enumerate(itertools.product([0, 1], repeat=num_inputs)):
            row_entries = []
            for j, value in enumerate(combination):
                label = tk.Label(self.table_window, text=str(value), borderwidth=1, relief="solid", width=10)
                label.grid(row=i + 1, column=j)

            output_entries = []
            for k in range(num_outputs):
                output_entry = tk.Entry(self.table_window, width=10)
                output_entry.grid(row=i + 1, column=num_inputs + k)
                output_entries.append(output_entry)

            row_entries.append((combination, output_entries))
            self.table_entries.append(row_entries)

    def solve_table(self):
        try:
            num_inputs = int(self.entry_inputs.get())
            num_outputs = int(self.entry_outputs.get())
        except ValueError:
            messagebox.showerror("Ungültige Eingabe", "Bitte eine gültige Anzahl an Eingabe- und Ausgabevariablen eingeben.")
            return

        all_expressions = []
        for output_index in range(num_outputs):
            terms = []
            for row in self.table_entries:
                combination, output_entries = row[0]
                output_value = output_entries[output_index].get().strip()
                if output_value == "1":
                    term_parts = []
                    for var_index, var_value in enumerate(combination):
                        if var_value == 1:
                            term_parts.append(f"x{var_index + 1}")
                        else:
                            term_parts.append(f"\u00acx{var_index + 1}")
                    terms.append(" & ".join(term_parts))

            if terms:
                boolean_expression = " | ".join(terms)
            else:
                boolean_expression = "0"

            all_expressions.append(f"Ausgabe {output_index + 1}: {boolean_expression}")

        messagebox.showinfo("Boolescher Term", "\n".join(all_expressions))

if __name__ == "__main__":
    root = tk.Tk()
    solver = TruthTableSolver(root)
    root.mainloop()
