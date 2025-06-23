# 🎙️ Jarvis – Python Voice Assistant

Jarvis is a simple voice-controlled assistant built in Python that can open websites, play music, and fetch the latest news headlines — all using your voice.

---

## ✨ Features

- 🎤 Voice activation with the keyword **"Jarvis"**
- 🌐 Opens common websites like Google, YouTube, Facebook, and LinkedIn
- 🎶 Plays songs using predefined YouTube links
- 🗞️ Reads out top news headlines using NewsAPI
- 🔊 Responds with text-to-speech (TTS) feedback

---

## 🛠️ Requirements

Install dependencies using:

```bash
pip install speechrecognition pyttsx3 requests
```

You’ll also need to install:

- `PyAudio`: for microphone access
  - On Windows:
    ```bash
    pip install pipwin
    pipwin install pyaudio
    ```
  - On macOS/Linux: use system package managers like `brew` or `apt`

---

## 📁 Project Structure

```
Jarvis/
├── main.py             # Core voice assistant logic
├── musiclibrary.py     # Dictionary of songs and media URLs
```

---

## 🚀 How to Run

1. Clone or download the repository.
2. Open a terminal in the project directory.
3. Run the assistant:
   ```bash
   python main.py
   ```

Speak **"Jarvis"** into your microphone — it will activate and prompt you for a command.

### 🎧 Example Commands

- "Jarvis" → "How can I help you sir?"
- "Open Google"
- "Open YouTube"
- "Play afsos"
- "News"

---

## 🔑 API Key Setup

This project uses [NewsAPI](https://newsapi.org) for fetching news.

- Get a free API key by signing up at [newsapi.org](https://newsapi.org/register)
- Replace the `newsapi` variable in `main.py`:
  ```python
  newsapi = "YOUR_NEWS_API_KEY"
  ```

---

## 🧠 Customization

- To add more songs, update the `music` dictionary in `musiclibrary.py`.
- You can easily extend `processCommand()` in `main.py` to support more websites or tasks.

---

## 🧩 Limitations

- Works best in a quiet environment for accurate voice recognition
- Limited error handling — will print basic exceptions to the console
- Fixed command keywords (e.g., “play [song name]”)

---

## 📬 Contact

Maintained by **Ayush54555**  
Feel free to open an [issue](https://github.com/Ayush54555/Jarvis/issues) for bugs or suggestions.

---

> ⭐ If you found this useful, give the repo a star to support the project!
