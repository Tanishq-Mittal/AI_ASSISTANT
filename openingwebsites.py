import tkinter as tk
from tkinter import Entry, Label, Button
import webbrowser

#Define the main window
root = tk.Tk()
root.title("YOUR AI ASSISTANT")

#Adding a background color
root.configure(bg='steelblue')

def search_youtube():
    query = entry.get()
    url = f"https:www.youtube.com/results?search_query={query}"
    webbrowser.open(url)

def search_google():
    query = entry.get()
    url = f"https:www.google.com/search?q={query}"
    webbrowser.open(url)

def search_instagram():
    Username = entry.get().replace('@',"") #Ensure username is clean of '@'
    url = f"www.instagram.com/{Username}/"
    webbrowser.open(url)

Label(root, text="Enter your command : ").pack(pady=10) #10 pixels gap rako labels ke upar or niche
entry = Entry(root, width=50)
entry.pack(pady=10)
Button(root, text="Search on youtube",command=search_youtube).pack(pady=5)
Button(root, text="Search on google",command=search_google).pack(pady=5)
Button(root, text="Search on Instagram",command=search_instagram).pack(pady=5)

#Run the GUI event loop
root.mainloop()