# Move-On-Chatbot-AI-Assistant 🤖💪
Move On AI Assistant is a Terminal-based AI fitness coach using Groq LLM. Delivers smart, mood-based home workouts with memory and real-time conversation. It uses a powerful AI brain (LLaMA 3) to understand what you say and reply in a natural way. The chatbot keeps track of your chat history so it can make relevant responses, and it knows when to end the conversation politely. It's designed to be simple but effective, focusing on giving you clear answers without unnecessary complexity.

## Key Features
✨ **Context-Aware Memory** - Remembers conversation history for coherent follow-ups  
⚡ **Groq API Powered** - Uses LLaMA 3 70B for ultra-fast responses  
🎯 **Motivation-Based Suggestions** - Adapts to user's energy level (challenging vs easy workouts)  
🛡️ **Safety-First Approach** - Warns users about possible injuries  
📱 **Dual Interface** - Choose between graphical or terminal interaction  

## Versions
Two versions available:
1. **GUI version**: Tkinter interface with chat history (Main.py and UserInterface.py)
2. **Terminal version**: Lightweight command-line version (chatBot2.py)


### GUI version
<p align="center">
  <img src="https://github.com/user-attachments/assets/12eea38a-98c0-4f97-b1da-9dca884df9e1" width="450">
</p>
<p align="center">This is the starting page.</p>

<p align="center"> ⋆ . ˚  ᡣ 𐭩  . 𖥔 ˚</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/bdd9361a-f31b-422a-a55a-82bdf90fbaf2" width="450">
</p>
<p align="center">When user type something.</p>

### Terminal version
<p align="center">
  <img src="https://github.com/user-attachments/assets/c327dbe8-5656-452c-b52e-b1d480f74750" width="980">
</p>
<p align="center">This is an example of the output.</p>

## Setup Instructions
1. Get Groq API key from cloud.groq.com
2. Set as environment variable: export GROQ_API_KEY="your-key"
3. Install requirements: ``` pip install groq tkinter pillow ```
4. Run:
   - GUI version: ``` python UserInterface.py ```
   - Terminal version: ``` python chatBot2.py ```
