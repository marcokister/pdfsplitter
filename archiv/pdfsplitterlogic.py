from pathlib import Path
from pypdf import PdfReader, PdfWriter

class PDFSplitter:
    def __init__(self, input_file: str, output_dir: str):
        self.input_file = Path(input_file)
        self.output_dir = Path(output_dir)
        self.reader = PdfReader(str(self.input_file))
        self._prepare_output_dir()

    def _prepare_output_dir(self):
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def split_by_pairs(self):
        total_pages = len(self.reader.pages)
        if total_pages % 2 != 0:
            print("Warnung: Die Seitenzahl ist ungerade. Die letzte Seite wird ignoriert.")

        for i in range(0, total_pages - 1, 2):
            writer = PdfWriter()
            writer.add_page(self.reader.pages[i])
            writer.add_page(self.reader.pages[i + 1])

            output_path = self.output_dir / f"{(i // 2) + 1}.pdf"
            with open(output_path, "wb") as f_out:
                writer.write(f_out)
            print(f"Gespeichert: {output_path}")



if __name__ == "__main__":
    splitter = PDFSplitter("input.pdf", "output/")
    splitter.split_by_pairs()