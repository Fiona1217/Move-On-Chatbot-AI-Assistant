import os
from groq import Groq
from tkinter import *

# Beginning of the chat.
print("Hello! I am Move On's AI Chatbot. I'm excited to help you with home workouts.\n\nHow's your motivation level today? Are you feeling energetic and ready to " \
+ "challenge yourself, or do you need something easy to get started? :)")

# To store chat history (for memory)
memory = []

def chatAIMemory_User(userInput):
    memory.append({
        "role": "user",
        "content": userInput
    })

def chatAIMemory_Bot(botInput):
    memory.append({
        "role": "assistant",
        "content": botInput
    })

def main(userInput):
    chatAIMemory_User(userInput)

    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY"),
    )

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
                + "If they ask you question, always answer"
        },
        {
            "role": "user",
            "content": userInput,
        },
    ]

    messages.extend(memory)

    chat_completion = client.chat.completions.create(
        messages=messages,
        model="llama-3.3-70b-versatile",
        temperature=1.2,
        max_completion_tokens=1024,
        top_p=1,
        stop=None,
        stream=False,
    )
    
    # Print the completion returned by the LLM.
    print(chat_completion.choices[0].message.content)

    chatAIMemory_Bot(chat_completion.choices[0].message.content)

    userExitOrNot(userInput)

    if userExitOrNot(userInput) == True:
        askUser()

def askUser():
    userInput = input("Enter message: ")
    checkUserInput(userInput)

def checkUserInput(userInput):
    if userInput:
        main(userInput)
    else:
        print("Please input something :)")
        askUser()

def userExitOrNot(userInput):
    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY"),
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a checker for whether or not the user wants to stop the conversation. You can either say 'true' or 'false'. If user wants to exit, you say false."
                "But if user looked like they still want more information, you say true."
            },
            {
                "role": "user",
                "content": userInput,
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

if __name__ == "__main__":
    askUser()
