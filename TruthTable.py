def load_truth_table(file_path="truth_table.txt"):
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

print(load_truth_table())
