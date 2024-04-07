from tkinter import Tk
from MainApp import MainApp
from LoginApp import LoginApp

class AppController:
    def __init__(self):
        self.root = Tk()
        self.current_frame = None
        self.switch_frame("MainApp")

    def switch_frame(self, frame_name):
        if self.current_frame:
            self.current_frame.destroy()  # Destroy il widget Tk corrente

        if frame_name == "MainApp":
            self.current_frame = MainApp(self.root, self.switch_frame)
        elif frame_name == "LoginApp":
            self.current_frame = LoginApp(self.root, self.switch_frame)

        self.current_frame.pack()

if __name__ == "__main__":
    app = AppController()
    app.root.mainloop()
