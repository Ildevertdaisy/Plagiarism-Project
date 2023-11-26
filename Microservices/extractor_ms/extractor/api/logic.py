import zipfile
import PyPDF2
import io
import json
import requests


# Ce fichier va contenir le coeur de l'extracteur

def extract_text_from_zip(url):

    # Envoyer une requête HTTP pour obtenir le fichier
    response = requests.get(url)
    response.raise_for_status() # S'assurer que la requête a réussi

    # Utiliser io.BytesIO pour lire le contenu en mémoire 
    zip_path = io.BytesIO(response.content)

    texts = []
    # Ouvrir le fichier ZIP
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        # Lister tous les fichiers PDF dans le ZIP
        pdf_files = [f for f in zip_ref.namelist() if f.endswith('.pdf')]
        # Traiter chaque fichier PDF
        for pdf_name in pdf_files:
            with zip_ref.open(pdf_name) as pdf_file:
              with io.BytesIO(pdf_file.read()) as binary_pdf_file:
                    reader = PyPDF2.PdfReader(binary_pdf_file)
                    # Lire le texte de chaque page
                    text = ""
                    for page in reader.pages:
                        page_text = page.extract_text()
                        if page_text:
                            text += page_text + "\n"
                    texts.append({"file": pdf_name, "text": text})

      # Convertir en JSON et afficher
   
    return texts[0]["text"]

