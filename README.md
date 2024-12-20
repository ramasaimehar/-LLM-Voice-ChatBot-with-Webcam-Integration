# **LLM VoiceBot with Web Cam Integration**  
This LLM - VoiceBot is a user-friendly AI-powered chatbot that allows seamless voice interactions. It integrates real-time speech-to-text, AI response generation, and text-to-speech capabilities, along with live webcam feed support and and chat history.

---

## **Features**  
- 🎙️ **Voice Input:** Speak into the microphone to interact with the bot.  
- 🧠 **AI-Powered Responses:** Uses Groq's LLaMA model to generate conversational responses.  
- 🔊 **Audio Output:** Converts responses to speech using Google Text-to-Speech (gTTS).  
- 📹 **Webcam Integration:** Displays a live webcam feed for real-time interaction.  
- 💬 **Chat History:** Tracks all conversations for reference.  
- ⬇️ **Downloadable Audio:** Download chatbot responses as audio files.  
- 🧮 **Simple Queries Support:** Handles questions like "What is 2+2?" or "What is AI?"  

---

## **How It Works**  
1. **Voice Input:** Speak into the microphone. The bot uses **OpenAI Whisper** to transcribe speech into text.  
2. **AI Response Generation:** Sends the transcribed text to **Groq API**, powered by the **LLaMA language model**, to generate a response.  
3. **Text-to-Speech Conversion:** Converts the response text into speech using **gTTS**.  
4. **Chat History:** Updates the conversation in the chat interface.  
5. **Webcam Integration:** Continuously displays live webcam feed using **OpenCV**.  

---

# **Key Libraries Used**  

1. **Gradio**: For creating the user-friendly web interface with voice input, webcam integration, and chat display.  
2. **Whisper**: For converting speech to text using OpenAI’s advanced speech recognition model.  
3. **gTTS**: For generating text-to-speech audio outputs of the chatbot’s responses.  
4. **pydub**: For audio processing and trimming features.  
5. **NumPy**: For efficient numerical operations and data manipulation.  
6. **Requests**: For making HTTP requests to APIs.  
7. **Groq**: For using the **[Groq Console](https://console.groq.com/)** API to generate responses using the LLaMA language model.  
8. **OpenCV-Python**: For integrating a live webcam feed within the interface.  
9. **Pillow**: For handling image data captured from the webcam.  
10. **Tempfile**: For managing temporary files, especially for audio outputs.  
---

## **Installation**  

1. Clone this repository:  
   ```bash  
   git clone https://github.com/your-username/tensorgo-voicebot.git  
   cd tensorgo-voicebot  
   ```  

2. Install the required dependencies:  
   ```bash  
   pip install -r requirements.txt  
   ```  

3. Run the application:  
   ```bash  
   python VoiceChatBot.py  
   ```  

---

## **Results**  

**User Interface using Gradio**
![image](https://github.com/user-attachments/assets/91ea3e86-b947-4981-b603-5ca2e3c5d0c5)

The bot allows you to:  
- Speak to it using a microphone.  
- View live webcam feed while chatting.  
- Get conversational text responses that are also converted to speech.  
- Download the audio responses for later use.
  
**Output :**  
![WhatsApp Image 2024-12-20 at 19 27 20_394df60e](https://github.com/user-attachments/assets/b43ea6f3-ad8f-4a27-867f-a2f8f0f46f79)


---

## **Use Cases**  
- Virtual Assistants  
- Interactive Learning Tools  
- Customer Support Chatbots  
- Voice-based Query Systems  

--- 

## **Contact**  
For questions or support, reach out at:  
- **Email:** ramasaimehar@gmail.com  
