import tkinter as tk
from tkinter import filedialog, messagebox
from tkinterdnd2 import DND_FILES, TkinterDnD
from pdfsplitterlogic import PDFSplitter

class PDFSplitterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDFSplitter V1.0")

        self.input_file = tk.StringVar()
        self.output_dir = tk.StringVar()
        self.pages_per_split = tk.IntVar(value=2)

        self._build_gui()

    def increment_pages_per_split(self):
        current_value = self.pages_per_split.get()
        try:
            new_value = int(current_value) + 1
            self.pages_per_split.set(new_value)
        except ValueError:
            self.pages_per_split.set(1)

    def decrement_pages_per_split(self):
        current_value = self.pages_per_split.get()
        try:
            new_value = int(current_value) - 1
            if new_value < 1:
                new_value = 1
            self.pages_per_split.set(new_value)
        except ValueError:
            self.pages_per_split.set(1)

    def _build_gui(self):
        tk.Label(self.root, text="PDF-Datei auswählen:").grid(row=0, column=0, sticky="w", padx=10, pady=(25, 5))
        
        entry = tk.Entry(self.root, textvariable=self.input_file, width=50)
        entry.grid(row=0, column=1, padx=5, pady=(25, 5))
        entry.drop_target_register(DND_FILES)
        entry.dnd_bind('<<Drop>>', self.drop_file)

        tk.Button(self.root, text="Durchsuchen", command=self.select_input_file).grid(row=0, column=2, padx=5, pady=(25, 5))

        tk.Label(self.root, text="Zielordner:").grid(row=1, column=0, sticky="w", padx=10, pady=5)
        tk.Entry(self.root, textvariable=self.output_dir, width=50).grid(row=1, column=1, padx=5)
        tk.Button(self.root, text="Durchsuchen", command=self.select_output_dir).grid(row=1, column=2, padx=5)

        tk.Label(self.root, text="Seiten pro Datei:").grid(row=2, column=0, sticky="w", padx=10, pady=5)
        
        # Frame for pages_per_split entry and buttons
        pages_frame = tk.Frame(self.root)
        pages_frame.grid(row=2, column=1, sticky="w", padx=5)

        tk.Entry(pages_frame, textvariable=self.pages_per_split, width=10).pack(side=tk.LEFT)
        tk.Button(pages_frame, text="+", command=self.increment_pages_per_split, width=3).pack(side=tk.LEFT, padx=(5,0))
        tk.Button(pages_frame, text="-", command=self.decrement_pages_per_split, width=3).pack(side=tk.LEFT)

        tk.Button(self.root, text="PDF aufteilen", command=self.run_split).grid(row=3, column=0, columnspan=3, pady=15)

        tk.Label(self.root, text="(c) 2025 by Marco Kister | Version 1.2 | MIT License", font=("Arial", 7)).grid(row=4, column=0, pady=5, padx=10)


    def drop_file(self, event):
        file_path = event.data
        if file_path.startswith('{') and file_path.endswith('}'):
            file_path = file_path[1:-1]
        self.input_file.set(file_path)

    def select_input_file(self):
        filename = filedialog.askopenfilename(filetypes=[("PDF Dateien", "*.pdf")])
        if filename:
            self.input_file.set(filename)

    def select_output_dir(self):
        folder = filedialog.askdirectory()
        if folder:
            self.output_dir.set(folder)

    def run_split(self):
        input_file = self.input_file.get()
        output_dir = self.output_dir.get()
        try:
            pages = int(self.pages_per_split.get())
            if not input_file or not output_dir or pages < 1:
                raise ValueError
        except ValueError:
            messagebox.showerror("Fehler", "Bitte gültige Werte eingeben.")

        try:
            splitter = PDFSplitter(input_file, output_dir, pages)
            if splitter.split() == "1":
                messagebox.showwarning("Warnung", "Die Anzahl der Seiten ist nicht durch die Anzahl der Seiten pro Datei teilbar.")
            elif splitter.split() == "2":
                messagebox.showinfo("Fertig", "PDF wurde erfolgreich aufgeteilt.")

        except Exception as e:
            messagebox.showerror("Fehler beim Aufteilen", str(e))

if __name__ == "__main__":
    root = TkinterDnD.Tk()
    app = PDFSplitterApp(root)
    root.mainloop()
