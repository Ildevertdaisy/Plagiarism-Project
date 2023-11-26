import zipfile
import PyPDF2
import io
import json
import requests


url = 'https://download.eu-west-3.fromsmash.co/transfer/buh3GRluIy-ct/file/59532deda5ca3c0b08ad8e0f3ab7f46d76220282?identity=14be8c24313a4e2a111daadcc65d7395-cda111bd7bd61bef88deefabfc4fb864685192c963b9bb1d30b9e60df200cb70eaa01bd6e0be2215aadc6061f13e8eba41ccf159a3e2ba48b45be10a8f50ed1b09d939f584d417f0b81fb11572092fdd&Expires=1701023312&Key-Pair-Id=APKAIM76HR2FWFZRN3HA&Signature=DXl6FLxG1HlrOQtBNZ09wjKfIJd~HacdOjdByx1NMqpCaKUvVE08f3rAhkQ4DnY3oQszk0u3tyPD4fpYC4ySnsecYABBMqoK0iw9PhLgNXX~izGA2nepoWOLScrCry8UoSBwcG2x2G-lore56qZSQyTpk7CLss3WHCJEzxOmemWtYRJqfuR8-KVmJ0JsNgUWvSeM9ESklACqx~5YCB5XPh7yznPXlRfa6IWj8l3MQhbiPAvSImIVVlJbivwDPKdVH1zlPvCJ8kziNf4CDGeaEedOyM5N0CR6fYNKEakLYiBqjShNHkoCAhq3zGfgVCk7aTGQf42COExfzMS6YUYBhA__'

def extract_pdf_text(url):

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
                reader = PyPDF2.PdfReader(pdf_file)
                # Lire le texte de chaque page
                text = ""
                for page in reader.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
                texts.append({"file": pdf_name, "text": text})
    
    return texts


def main():
    zip_path = "./test.zip"

    # Extraire et lire le texte de tous les fichiers PDF
    texts = extract_pdf_text(url)

    # Convertir en JSON et afficher
    output = {
        "text": texts[0]["text"]
    }
    json_data = json.dumps(output)

    print(json_data)


if __name__ == "__main__":
    main()
