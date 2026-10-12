
from pathlib import Path

from pypdf import PdfReader


def load_pdf(pdf_path: str) -> str:
    """
    Extrait le texte d'un fichier PDF.
    """

    path = Path(pdf_path)

    if not path.exists():
        raise FileNotFoundError(
            f"PDF introuvable : {pdf_path}"
        )

    reader = PdfReader(str(path))

    pages = []

    for page in reader.pages:
        text = page.extract_text()

        if text:
            pages.append(text)

    return "\n\n".join(pages)


def split_text(
    text: str,
    chunk_size: int = 1000,
    chunk_overlap: int = 150,
):
    """
    Découpe le texte en morceaux avec chevauchement.
    """

    text = text.strip()

    if not text:
        return []

    chunks = []

    start = 0
    text_length = len(text)

    while start < text_length:
        end = start + chunk_size

        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        if end >= text_length:
            break

        start = end - chunk_overlap

    return chunks

