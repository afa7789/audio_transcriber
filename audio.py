import os
import whisper

model = whisper.load_model("tiny")

def recognize_speech(audio_file):
    result = model.transcribe(audio_file, language="pt")
    return result["text"]

folder_path = '/app/audios'

for filename in os.listdir(folder_path):
    if filename.endswith('.ogg'):
        audio_path = os.path.join(folder_path, filename)
        try:
            text_pt = recognize_speech(audio_path)
            txt_filename = filename.replace('.ogg', '.txt')
            with open(os.path.join(folder_path, txt_filename), 'w', encoding='utf-8') as f:
                f.write(text_pt)
            print(f"Processado {filename}: {text_pt}")
        except Exception as e:
            print(f"Erro ao processar {filename}: {str(e)}")