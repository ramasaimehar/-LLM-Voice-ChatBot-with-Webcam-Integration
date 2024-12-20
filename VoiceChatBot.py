import gradio as gr
import whisper
from gtts import gTTS
import os
from groq import Groq
from tempfile import NamedTemporaryFile
import cv2
from PIL import Image
import threading
import numpy as np

client = Groq(
    api_key="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",
)

model = whisper.load_model("base")
chat_history = []

def speech_to_text(audio_path):
    transcription = model.transcribe(audio_path)["text"]
    return transcription

def generate_response(text):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": text,
            }
        ],
        model="llama3-8b-8192",
    )
    return chat_completion.choices[0].message.content

def text_to_speech(text):
    tts = gTTS(text)
    output_audio = NamedTemporaryFile(suffix=".mp3", delete=False)
    tts.save(output_audio.name)
    return output_audio.name

def continuous_webcam_feed(frame_callback):
    cap = cv2.VideoCapture(0)

    def capture():
        while True:
            ret, frame = cap.read()
            if ret:
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame_callback(Image.fromarray(image))

    thread = threading.Thread(target=capture, daemon=True)
    thread.start()
    return cap

def chatbot_pipeline(audio_path):
    global chat_history
    try:
        text_input = speech_to_text(audio_path)
        chat_history.append(("🧑Mehar", text_input))
        response_text = generate_response(text_input)
        chat_history.append(("🤖 Assistant", response_text))
        response_audio_path = text_to_speech(response_text)
        return chat_history, response_audio_path
    except Exception as e:
        return [("Error", str(e))], None

def render_interface():
    with gr.Blocks() as iface:
        gr.Markdown(
            "<h1 style='text-align: center;'>🗣️ TensorGo's VoiceBot 🗣️</h1>",
            elem_id="title"
        )

        with gr.Row():
            audio_input = gr.Audio(type="filepath", label="Speak")
            webcam_output = gr.Image(label="Webcam Feed", type="pil")

        submit_btn = gr.Button("Submit")

        chat_display = gr.Chatbot(label="Chat History")
        response_audio = gr.Audio(label="Response Audio")

        def process_chat(audio_path):
            chat, audio_path = chatbot_pipeline(audio_path)
            return chat, audio_path

        def update_webcam(image):
            webcam_output.update(value=image)

        continuous_webcam_feed(update_webcam)

        submit_btn.click(
            process_chat, inputs=[audio_input], outputs=[chat_display, response_audio]
        )

    return iface

iface = render_interface()
iface.launch()
