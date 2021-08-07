import tkinter as tk
import webbrowser
import pyautogui as gui


frame = tk.Tk()
frame.title("TextBox Input")
frame.geometry('400x200')


def download():
	inp = inputlink.get(1.0, "end-1c")
	id = inp[17:]
	webbrowser.open(f'https://www.youtubepp.com/watch?v={id}')
	gui.moveTo(1000,700, duration=0.25)
	gui.press('enter')

inputlink = tk.Text(frame,
				height = 2,
				width = 20)

inputlink.pack()

submit = tk.Button(frame,
						text = "submit",
						command = download)
submit.pack()

lbl = tk.Label(frame, text = "paste the link to download the video",fg="red")
lbl.pack()
frame.mainloop()
