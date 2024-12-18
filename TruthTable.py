import sympy as sp


def load_truth_table(file_path="truthtable.txt"):
    """Lädt die Wahrheitstabelle aus einer .txt-Datei."""
    with open(file_path, "r") as file:
        lines = file.readlines()
    truth_table = []
    for line in lines:
        line = line.strip()
        if line:  # Leere Zeilen überspringen
            inputs, outputs = line.split(",")
            truth_table.append((list(map(int, inputs)), list(map(int, outputs))))
    return truth_table


def generate_boolean_expressions(truth_table):
    """Erstellt Boolesche Ausdrücke für jede Ausgangsvariable."""
    num_vars = len(truth_table[0][0])  # Anzahl der Eingangsvariablen
    num_outputs = len(truth_table[0][1])  # Anzahl der Ausgangsvariablen

    variables = [sp.symbols(f'x{i}') for i in range(num_vars)]
    output_expressions = []

    for output_index in range(num_outputs):
        minterms = []
        for inputs, outputs in truth_table:
            if outputs[output_index] == 1:
                term = []
                for idx, value in enumerate(inputs):
                    if value == 1:
                        term.append(variables[idx])
                    else:
                        term.append(~variables[idx])
                minterms.append(sp.And(*term))

        boolean_expression = sp.Or(*minterms)
        # TODO implementiere den QMA für komplexere Tabellen in der Zukunft
        simplified_expression = sp.simplify(boolean_expression)
        output_expressions.append(simplified_expression)

    return output_expressions


def generate_circuit(*terms):
    """Generiert eine Schaltanleitung aus einem Booleschen Ausdruck."""
    gates = []  # Liste der Gatter
    gate_counter = 1  # Start-ID für Gatter

    def process(expr):
        nonlocal gate_counter
        if isinstance(expr, sp.Symbol):
            # Basisfall: Symbol (Variable) direkt zurückgeben
            return str(expr)
        elif isinstance(expr, sp.Not):
            # NOT-Gatter
            input_gate = process(expr.args[0])
            gate_id = f"G{gate_counter}"
            gate_counter += 1
            gates.append({"type": "NOT", "input": input_gate, "output": gate_id})
            return gate_id
        elif isinstance(expr, sp.And):
            # AND-Gatter
            input_gates = [process(arg) for arg in expr.args]
            gate_id = f"G{gate_counter}"
            gate_counter += 1
            gates.append({"type": "AND", "inputs": input_gates, "output": gate_id})
            return gate_id
        elif isinstance(expr, sp.Or):
            # OR-Gatter
            input_gates = [process(arg) for arg in expr.args]
            gate_id = f"G{gate_counter}"
            gate_counter += 1
            gates.append({"type": "OR", "inputs": input_gates, "output": gate_id})
            return gate_id

    # Start der Verarbeitung
    for term in terms:
        output_gate = process(term)

    return gates, output_gate


def save_results(file_path, expressions):
    """Speichert die Ergebnisse in eine .txt-Datei."""
    with (open(file_path, "w") as file):
        for idx, expr in enumerate(expressions):
            file.write(f"Output y{idx}: {expr}\n")
        for expression in expressions:
            gates, final_output = generate_circuit(expression)
            for i, gate in enumerate(gates):
                print(gate)
                file.write(f"{i}. {gate}\n")


# Pfad zur Eingabedatei
input_file = "negativbinary.txt"
output_file = "boolean_results.txt"

# Schritt 1: Wahrheitstabelle laden
truth_table = load_truth_table(input_file)

# Schritt 2: Boolesche Ausdrücke generieren
expressions = generate_boolean_expressions(truth_table)

# Schritt 3: Ergebnisse speichern
save_results(output_file, expressions)

print(f"Die Ergebnisse wurden in {output_file} gespeichert.")
