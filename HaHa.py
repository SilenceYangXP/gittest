import tkinter as tk

class SmileFaceApp:
    def __init__(self, master):
        self.master = master
        self.master.title("哈哈笑脸")
        self.master.bind("<Button-3>", self.change_to_sad_face)  # Right-click
        self.master.bind("<Button-1>", self.change_to_smile_face)  # Left-click
        self.master.bind("<Escape>", self.exit_app)  # Escape key
        self.is_smiling = True
        self.canvas = tk.Canvas(self.master, width=400, height=400)
        self.canvas.pack()
        self.draw_smile_face()

    def draw_smile_face(self):
        self.canvas.delete("all")
        if self.is_smiling:
            self.canvas.create_oval(100, 100, 300, 300, fill="yellow")  # Face
            self.canvas.create_oval(150, 150, 180, 180, fill="black")  # Left eye
            self.canvas.create_oval(220, 150, 250, 180, fill="black")  # Right eye
            self.canvas.create_arc(150, 180, 250, 250, start=0, extent=-180, fill="black")  # Smile
        else:
            self.canvas.create_oval(100, 100, 300, 300, fill="yellow")  # Face
            self.canvas.create_oval(150, 150, 180, 180, fill="black")  # Left eye
            self.canvas.create_oval(220, 150, 250, 180, fill="black")  # Right eye
            self.canvas.create_arc(150, 200, 250, 300, start=0, extent=180, fill="black")  # Sad face

    def change_to_sad_face(self, event):
        self.is_smiling = False
        self.draw_smile_face()

    def change_to_smile_face(self, event):
        self.is_smiling = True
        self.draw_smile_face()

    def exit_app(self, event):
        self.master.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = SmileFaceApp(root)
    root.mainloop()
