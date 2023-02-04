import PyPDF2
import os

def merge_pdfs(pdf_files, output_file):
    pdf_files.sort()
    # Initialisiere einen PDF-Writer
    pdf_writer = PyPDF2.PdfWriter()

    # Iteriere durch alle PDF-Dateien im Ordner
    for filename in pdf_files:
        # Öffne jede PDF-Datei
        pdf_file = open(filename, 'rb')

        # Lese jede PDF-Datei
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        # Füge jede Seite aus jeder PDF-Datei dem PDF-Writer hinzu
        for page in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page])

        # Schließe jede PDF-Datei
        pdf_file.close()

    # Öffne das Ziel-PDF-File
    output_pdf = open(output_file, 'wb')

    # Schreibe alle Seiten zusammen zu einem PDF
    pdf_writer.write(output_pdf)

    # Schließe das Ziel-PDF-File
    output_pdf.close()

if __name__ == '__main__':
    # Pfad des Ordners, in dem die PDF-Dateien gespeichert sind
    folder_path = input("Geben Sie den Pfad des Ordners mit den PDF-Dateien an: ")

    # Liste aller PDF-Dateien im Ordner
    pdf_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.pdf')]

    # Name der Ausgabedatei
    output_file = input("Geben Sie den Namen der ausgegebenen PDF-Datei an: ")

    # Rufe die Funktion zum Zusammenführen der PDFs auf
    merge_pdfs(pdf_files, output_file)
