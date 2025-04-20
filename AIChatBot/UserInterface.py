import os
from tkinter import scrolledtext
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from Main import AIChatBot

class ChatbotUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Move On - AI Chatbot")
        self.root.geometry("500x700")
        self.root.configure(background = 'white')

        self.chatbot = AIChatBot()

        # ------------------------ Code for header ------------------------
        header = tk.Frame( root,
            background = "#F0E9D2",
            height = "60",
            width = "500",
            padx = 10,
            pady = 5
        )
        header.pack(fill='x')

        img = (Image.open(r"AIChatBot\pics\AIChatbotIcon.png"))
        img.thumbnail((55, 55), Image.Resampling.LANCZOS)
        self.resultedImg = ImageTk.PhotoImage(img)
        canvas = tk.Canvas(header, width=65, height=65, bg='#F0E9D2', highlightthickness=0)
        canvas.pack(side=LEFT)
        canvas.create_image(32, 32, image=self.resultedImg)

        header2 = tk.Label( header,
            text = "Move On's AI Assistant",
            foreground = "#181D31",
            background = "#F0E9D2",
            font = ('Helvetia', 14),
            padx = 10
        )
        header2.pack(side = LEFT)


        # ------------------------ Code for chat area ------------------------
        self.chatArea = scrolledtext.ScrolledText( root,
            wrap = tk.WORD,
            font = ('Helvetia', 12),
            state = 'disable',
            padx = 10,
            pady =10,
            height = 30
        )
        self.chatArea.pack(expand = True, fill = BOTH)

        self.chatArea.tag_config( 'user',
            foreground = 'white',
            background = '#678983',
            justify = 'right'
        )

        self.chatArea.tag_config( 'assistant',
            foreground = '#181D31',
            justify = 'left'
        )


        # ------------------------ Code for user's input ------------------------
        userPlaceToInput = tk.Frame( root,
            background = "#F0E9D2",
            height = 30,
            width = 500,
            padx = 10,
            pady = 8
        )
        userPlaceToInput.pack(fill='x', expand = True, side = BOTTOM)

        self.userInput = tk.Entry( userPlaceToInput,
            text = "Enter message...",
            font = ('Helvetia', 12),
            width = 45
        )
        self.userInput.pack(side = LEFT, padx = (0, 10), expand = True)

        self.submitButton = tk.Button( userPlaceToInput,
            text = "Submit",
            background = "#678983",
            font = ('Helvetia', 12),
            padx = 5,
            pady = 5,
            command = self.whenSend
        )
        self.submitButton.pack(side = LEFT)

        self.userInput.bind("<Return>", lambda event: self.whenSend())
        self.displayMessage("assistant", self.chatbot.greeting())

    def whenSend(self):
        userInput = self.userInput.get()
        if userInput.strip():
            self.displayMessage("user", userInput)
            self.userInput.delete(0, tk.END)

            AIResponse = self.chatbot.conversation(userInput)
            self.displayMessage("assisant", AIResponse)

            if any(word in AIResponse.lower() for word in ["goodbye", "bye", "see you"]):
                if not self.chatbot.userExitOrNot(AIResponse):
                    self.userInput.config(state = 'disabled')
                    self.submitButton.config(state = 'disabled')
                    self.displayMessage("assistant", "Goodbye :D")
    
    # ------------------------ Code for displaying AI and user's message ------------------------
    def displayMessage(self, sender, message):
        self.chatArea.config(state='normal')
        if sender == "user":
            self.chatArea.insert(tk.END, message + "\n", 'user')
        else:
            self.chatArea.insert(tk.END, "\nAI Assistant:\n" + message + " \n\n", 'assistant')
        
        self.chatArea.see(tk.END)

        self.chatArea.config(state = 'disabled')

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatbotUI(root)
    root.mainloop()
        