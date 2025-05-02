import cv2
import requests
from bs4 import BeautifulSoup
import io
import numpy as np
from PIL import Image
import face_recognition
import os


def validate_document(file_content):
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    img = Image.open(io.BytesIO(file_content))
    img_array = np.array(img)
    gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    return len(faces) > 0


def validate_profile_link(link, interests):
    try:
        response = requests.get(link, timeout=5)
        soup = BeautifulSoup(response.content, 'html.parser')
        text = soup.get_text().lower()
        return any(interest.lower() in text for interest in interests.split(','))
    except:
        return False


def compare_selfie_with_document(selfie_content, document_content, threshold=0.6):
    try:
        selfie_img = face_recognition.load_image_file(
            io.BytesIO(selfie_content))
        document_img = face_recognition.load_image_file(
            io.BytesIO(document_content))

        selfie_face_locations = face_recognition.face_locations(selfie_img)
        document_face_locations = face_recognition.face_locations(document_img)

        if not selfie_face_locations or not document_face_locations:
            return False, 1.0  # Não encontrou faces em uma ou ambas as imagens

        # Extrai os encodings (características) das faces
        selfie_face_encoding = face_recognition.face_encodings(
            selfie_img, selfie_face_locations)[0]
        document_face_encoding = face_recognition.face_encodings(
            document_img, document_face_locations)[0]

        # Calcula a distância entre as faces (menor valor = mais similar)
        face_distance = face_recognition.face_distance(
            [selfie_face_encoding], document_face_encoding)[0]

        # Compara se a distância é menor que o limiar
        match = face_distance <= threshold

        return match, face_distance
    except Exception as e:
        print(f"Erro ao comparar faces: {e}")
        return False, 1.0


def test_compare_faces():
    selfie_path = "selfie_test.jpg"
    document_path = "document_test.jpg"

    # Verifica se os arquivos existem
    if not os.path.exists(selfie_path) or not os.path.exists(document_path):
        print(f"Erro: Os arquivos de teste não foram encontrados.")
        print(
            f"Por favor, adicione os arquivos '{selfie_path}' e '{document_path}' ao diretório.")
        return

    # Carrega as imagens
    with open(selfie_path, 'rb') as f_selfie:
        selfie_data = f_selfie.read()

    with open(document_path, 'rb') as f_doc:
        document_data = f_doc.read()

    # Testa com diferentes thresholds
    thresholds = [0.4, 0.5, 0.6, 0.7, 0.8]

    print("Resultados da comparação facial:")
    print("-" * 50)

    for threshold in thresholds:
        match, similarity = compare_selfie_with_document(
            selfie_data, document_data, threshold)

        result = "✅ CORRESPONDE" if match else "❌ NÃO CORRESPONDE"
        confidence = round((1 - similarity) * 100, 2)

        print(f"Threshold {threshold}: {result} (Confiança: {confidence}%)")

    print("-" * 50)
    print("Nota: Quanto maior a confiança, mais similar são as faces.")
    print("Um bom threshold geralmente está entre 0.5 e 0.7.")


if __name__ == "__main__":
    test_compare_faces()
