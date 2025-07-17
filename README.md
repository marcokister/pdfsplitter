![Static Badge](https://img.shields.io/badge/pdfSplitter-with_python-brightgreen)

PDFSplitter – Smart PDF Document Splitting
PDFSplitter is a lightweight Python application that allows you to split multi-page PDF files into smaller, separate files based on a user-defined number of pages.
It is particularly useful for processing scanned documents that contain multiple multi-page items (e.g., invoices, contracts, forms).

🔧 Key Features
Split PDF files into chunks of N pages (user-defined)

Simple and clean Tkinter-based GUI

Cross-platform compatibility (Windows, macOS, Linux)

Ideal for scanned documents: scan all pages at once and split afterwards

💡 Use Case Example
You scanned 100 pages of two-page documents (e.g., 50 invoices). Instead of manually scanning or splitting each one, simply:

Scan everything into a single PDF.

Use PDFSplitter to divide it into 50 PDFs, each with 2 pages.

🚀 How It Works
Select the input PDF file.

Set the number of pages per split.

Choose the output directory.

Click Split – done!

-------------------------------------------------------------------------

PDFSplitter ist eine schlanke Python-Anwendung zum Aufteilen mehrseitiger PDF-Dateien in kleinere Einzeldateien – basierend auf einer vom Benutzer festgelegten Seitenanzahl.
Besonders hilfreich ist das Tool beim Verarbeiten gescannter Dokumente mit mehreren Einzeldokumenten (z. B. Rechnungen, Verträge, Formulare).

🔧 Funktionen
Aufteilen von PDFs in Abschnitte mit N Seiten (frei wählbar)

Einfache und übersichtliche Benutzeroberfläche mit Tkinter

Plattformunabhängig (Windows, macOS, Linux)

Perfekt für gescannte Stapel: Alles auf einmal scannen, danach bequem aufteilen

💡 Anwendungsbeispiel
Du hast 100 Seiten mit je zwei Seiten pro Dokument gescannt (z. B. 50 Rechnungen). Statt jede Datei einzeln zu scannen oder zu schneiden:

Alles in eine einzige PDF-Datei scannen.

Mit PDFSplitter automatisch in 50 Zwei-Seiten-PDFs aufteilen.

🚀 So funktioniert’s
Eingabe-PDF auswählen

Anzahl Seiten pro Teil angeben

Ausgabeverzeichnis wählen

Auf Split klicken – fertig!


# Create exe file
pyinstaller --onefile --windowed pdfsplitter.py


