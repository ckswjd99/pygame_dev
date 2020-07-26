import tkinter as tk

window = tk.Tk()

# ADD WIDGETS
window.title("Map Maker")
window.geometry("1500x900+100+50")
window.resizable(False, False)

top_buttons_frame = tk.Frame(window, background="yellow")
top_buttons_frame.pack(fill=tk.X, ipady=10)



window.mainloop()