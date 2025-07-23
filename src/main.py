import pyaudio
import wave
import json
from vosk import Model, KaldiRecognizer
import numpy as np
from resemblyzer import VoiceEncoder, preprocess_wav
import os

# --- Configuration ---
CONFIG_FILE = "config.json"
MODEL_PATH = "../vosk-model-small-fr-0.22"
EMBEDDING_PATH = "../data/embedding_ref.npy"
EMBEDDING_AUTH_PATH = "../data/embedding_auth.npy"

# Audio settings
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5

# --- 1. Charger la configuration ---
def load_config():
    """Charge la phrase secrète depuis le fichier JSON."""
    try:
        with open(CONFIG_FILE, 'r') as f:
            config = json.load(f)
            return config.get("secret_phrase", "").lower()
    except FileNotFoundError:
        print(f"Erreur : Fichier de configuration '{CONFIG_FILE}' non trouvé.")
        return None

def load_embedding():
    if not os.path.exists(EMBEDDING_PATH):
        print(f"Erreur : Empreinte biométrique non trouvée ({EMBEDDING_PATH})")
        return None
    return np.load(EMBEDDING_PATH)

# --- 2. Enregistrer l'audio ---
def record_audio(filename):
    audio = pyaudio.PyAudio()
    print("\nParlez maintenant...")
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)
    frames = []
    for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print("Enregistrement terminé.")
    stream.stop_stream()
    stream.close()
    audio.terminate()
    wf = wave.open(filename, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    return filename

# --- 3. Transcrire l'audio ---
def transcribe_audio(audio_data, model):
    rec = KaldiRecognizer(model, RATE)
    rec.AcceptWaveform(audio_data)
    result_json = rec.FinalResult()
    result_dict = json.loads(result_json)
    return result_dict.get('text', '')

# --- 4. Extraire l'empreinte biométrique ---
def extract_embedding(filename):
    encoder = VoiceEncoder()
    wav = preprocess_wav(filename)
    emb = encoder.embed_utterance(wav)
    return emb

# --- Script principal ---
def main():
    secret_phrase = load_config()
    embedding_ref = load_embedding()
    if not secret_phrase or embedding_ref is None:
        return
    print(f"Phrase secrète attendue : '{secret_phrase}'")
    try:
        model = Model(MODEL_PATH)
    except Exception as e:
        print(f"Erreur lors du chargement du modèle Vosk : {e}")
        return
    # Enregistrer la voix de l'utilisateur
    voiceprint_auth_file = "../data/voiceprint_auth.wav"
    record_audio(voiceprint_auth_file)
    # Reconnaissance vocale (texte)
    with wave.open(voiceprint_auth_file, "rb") as wf:
        audio_data = wf.readframes(wf.getnframes())
    print("Reconnaissance vocale en cours...")
    recognized_text = transcribe_audio(audio_data, model)
    print(f"Texte reconnu : '{recognized_text}'")
    # Vérification biométrique vocale
    emb_test = extract_embedding(voiceprint_auth_file)
    # Sauvegarder l'embedding d'authentification
    np.save(EMBEDDING_AUTH_PATH, emb_test)
    similarity = np.dot(embedding_ref, emb_test) / (np.linalg.norm(embedding_ref) * np.linalg.norm(emb_test))
    print(f"Similarité biométrique : {similarity:.3f}")
    # Seuil à ajuster selon les tests (0.75 recommandé)
    threshold = 0.75
    # Double vérification
    if secret_phrase in recognized_text and similarity > threshold:
        print("\n=======================")
        print(" AUTHENTIFICATION RÉUSSIE ")
        print("=======================")
    else:
        print("\n=====================")
        print(" AUTHENTIFICATION ÉCHOUÉE ")
        print("=====================")

if __name__ == "__main__":
    main()
