from pathlib import Path
from pypdf import PdfReader, PdfWriter

class PDFSplitter:
    def __init__(self, input_file: str, output_dir: str, pages_per_split: int = 2):
        self.input_file = Path(input_file)
        self.output_dir = Path(output_dir)
        self.pages_per_split = pages_per_split
        self.reader = PdfReader(str(self.input_file))
        self._prepare_output_dir()

    def _prepare_output_dir(self):
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def split(self):
        return_error_code = "0"
        total_pages = len(self.reader.pages)
        if total_pages % self.pages_per_split != 0:
            return "1"  # abort if pages are not divisible

        for i in range(0, total_pages, self.pages_per_split):
            writer = PdfWriter()
            for j in range(self.pages_per_split):
                if i + j < total_pages:
                    writer.add_page(self.reader.pages[i + j])
            output_path = self.output_dir / f"{(i // self.pages_per_split) + 1}.pdf"
            with open(output_path, "wb") as f_out:
                writer.write(f_out)
        
        return "2"  # Return "2" if the split was successful



if __name__ == "__main__":
    splitter = PDFSplitter("input.pdf", "output/", pages_per_split=2)
    splitter.split_by_pairs()