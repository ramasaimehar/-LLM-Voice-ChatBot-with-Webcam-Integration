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
- 🧮 **Simple Queries Support:** Handles questions like "What is 2+2?" or "What's the time?"  

---

## **How It Works**  
1. **Voice Input:** Speak into the microphone. The bot uses **OpenAI Whisper** to transcribe speech into text.  
2. **AI Response Generation:** Sends the transcribed text to **Groq API**, powered by the **LLaMA language model**, to generate a response.  
3. **Text-to-Speech Conversion:** Converts the response text into speech using **gTTS**.  
4. **Chat History:** Updates the conversation in the chat interface.  
5. **Webcam Integration:** Continuously displays live webcam feed using **OpenCV**.  

---

## **Technologies Used**  
- **Gradio:** For building an interactive user interface.  
- **OpenAI Whisper:** Converts speech to text.  
- **Groq API:** Generates AI responses using LLaMA.  
- **gTTS:** Converts text to speech.  
- **OpenCV:** Integrates real-time webcam feed.  
- **NumPy & PIL:** For image processing and webcam frame handling.  
- **TempFile:** Manages temporary audio files.  

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
   python app.py  
   ```  

---

## **Demo**  
The bot allows you to:  
- Speak to it using a microphone.  
- View live webcam feed while chatting.  
- Get conversational text responses that are also converted to speech.  
- Download the audio responses for later use.  

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
