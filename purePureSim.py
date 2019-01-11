from tkinter import *
from tkinter import ttk


class RobotSim(Frame):
    def __init__(self, master):
        super(RobotSim, self).__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):

        self.CV = Canvas(width = 500, height = 500,bg='pink')
        self.CV.pack()

        path = self.CV.create_line(250,0,250,500)

        self.lb1 = self.CV.create_text(270,10,text='(250,0)')
        self.lb1 = self.CV.create_text(275,490,text='(250,500)')

        self.Robot = self.CV.create_rectangle(130,130,150,150,fill='yellow')
        

if __name__ == "__main__":
    GUI = Tk()
    GUI.title('Simmulation Pure Pursuit')
    GUI.geometry('500x500')
    sim = RobotSim(GUI)
    GUI.mainloop()
