import os
from groq import Groq
from tkinter import *

class AIChatBot:
    def __init__(self):
        # To store chat history (for memory)
        self.memory = []

    def greeting(self):
        # Beginning of the chat.
        return("Hello! I am Move On's AI Chatbot. I'm excited to help you with home workouts.\n\nHow's your motivation level today? Are you feeling energetic and ready to " \
        + "challenge yourself, or do you need something easy to get started? :)")

    def chatAIMemory_User(self, userInput):
        self.memory.append({
            "role": "user",
            "content": userInput
        })

    def chatAIMemory_Bot(self, botInput):
        self.memory.append({
            "role": "assistant",
            "content": botInput
        })

    def conversation(self, userInput):
        client = Groq(
            api_key=os.environ.get("GROQ_API_KEY"),
        )

        self.chatAIMemory_User(userInput)

        messages=[
            {
                "role": "system",
                "content": "Act as Move On AI Assistant, an expert AI for home workouts. Provide clear, practical advice about:\n"
                    + "- Easy/Challenging Bodyweight exercises based on user's mood and motivation\n"
                    + "- Minimal equipment routines at home. What can they use, warn them about injuries and consequences but don't scare them\n"
                    + "- Proper form techniques based on their body type\n"
                    + "- Workout planning based on their body type, work schedule (if available), and workout motivation\n"
                    + "- Should understand user's mood and motivation in terms of working out\n"
                    + "- Don't scare the users' by asking way too personal questions\n\n"
                    + "Keep responses under 150 words if it's related about giving advice or gym and be sure it's very actionable."
                    + "If not related about gym or workout or motivation, response in less than 50. Ask them kindly of what do they wanna talk about."
                    + "If user say thank you, ask them if they would like to know other things or not. If they say no, say goodbye kindly. And If you actually suggest them a types of workout before, say goodluck."
                    + "If they feel like stopping, say goodbye"
                    + "Don't ask to much questions."
                    + "Don't pressure them too much about fitness or nutrition, but if the conversation goes way out of topic, try to get it back."
            },
            {
                "role": "user",
                "content": userInput,
            },
        ]

        messages.extend(self.memory)

        chat_completion = client.chat.completions.create(
            messages=messages,
            model="llama-3.3-70b-versatile",
            temperature=1.2,
            max_completion_tokens=1024,
            top_p=1,
            stop=None,
            stream=False,
        )
        
        # return the completion returned by the LLM.
        aiResponse = chat_completion.choices[0].message.content
        self.chatAIMemory_Bot(aiResponse)
        return aiResponse

    def userExitOrNot(self, aiResponse):
        goodbyePhrases = [
            "goodbye", "see you", "farewell", "good luck", "bye", "have a great"
        ]

        if any(phrase in aiResponse.lower() for phrase in goodbyePhrases):
            return False

        client = Groq(
            api_key=os.environ.get("GROQ_API_KEY"),
        )

        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a checker for whether or not the conversation ends. You can either say 'true' or 'false'."
                    + "Return 'false' if:\n"
                    + "- The assistant said goodbye\n"
                    + "- The conversation is clearly ending\n"
                    + "- The assistant suggested ending\n\n"
                    + "Return 'true' if:\n"
                    + "- The assistant asked a follow-up question\n"
                    + "- The conversation seems to be continuing\n"
                    + "- The message expects a response"
                },
                {
                    "role": "assistant",
                    "content": aiResponse
                }
            ],

            model="llama-3.3-70b-versatile",
            temperature=0.5,
            max_completion_tokens=1024,
            top_p=1,
            stop=None,
            stream=False,
        )

        checkResult = chat_completion.choices[0].message.content
        trueVar = "true"
        return checkResult.lower() == trueVar