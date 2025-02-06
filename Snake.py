import tkinter as tk
import random

class SnakeGame:
    def __init__(self, master):
        self.master = master
        self.master.title("贪吃蛇游戏")
        self.canvas = tk.Canvas(master, width=400, height=400, bg='black')
        self.canvas.pack()
        self.score = 0
        self.speed = 50  # Adjusted initial speed to be slower
        self.snake = [(20, 20), (20, 30), (20, 40)]
        self.direction = 'Down'
        self.food_position = self.place_food()
        self.game_running = False  # Changed to False to prevent immediate start
        self.master.bind("<KeyPress>", self.change_direction)

        # Speed selection
        self.speed_label = tk.Label(master, text="选择速度等级 (1-10):")
        self.speed_label.pack()
        self.speed_scale = tk.Scale(master, from_=1, to=10, orient=tk.HORIZONTAL)
        self.speed_scale.pack()

        self.start_button = tk.Button(master, text="开始游戏", command=self.start_game)
        self.start_button.pack()

        # Score display
        self.score_label = tk.Label(master, text="得分: 0")
        self.score_label.pack()

        # Restart button (initially hidden)
        self.restart_button = tk.Button(master, text="再来一局", command=self.restart_game)
        self.restart_button.pack()
        self.restart_button.pack_forget()  # Hide the button initially

    def start_game(self):
        self.speed = 150 - (self.speed_scale.get() - 1) * 10  # Adjust speed based on selection
        self.game_running = True
        self.update()

    def place_food(self):
        x = random.randint(0, 19) * 20
        y = random.randint(0, 19) * 20
        return (x, y)

    def change_direction(self, event):
        if event.keysym in ['Up', 'Down', 'Left', 'Right']:
            self.direction = event.keysym

    def update(self):
        if self.game_running:
            self.move_snake()
            self.check_collisions()
            self.draw_elements()
            self.score_label.config(text=f"得分: {self.score}")  # Update score display
            self.master.after(self.speed, self.update)

    def move_snake(self):
        head_x, head_y = self.snake[0]
        if self.direction == 'Up':
            head_y -= 20
        elif self.direction == 'Down':
            head_y += 20
        elif self.direction == 'Left':
            head_x -= 20
        elif self.direction == 'Right':
            head_x += 20
        self.snake.insert(0, (head_x, head_y))
        if (head_x, head_y) == self.food_position:
            self.score += 1
            self.food_position = self.place_food()
        else:
            self.snake.pop()

    def check_collisions(self):
        head_x, head_y = self.snake[0]
        if (head_x < 0 or head_x >= 400 or head_y < 0 or head_y >= 400 or
                len(self.snake) != len(set(self.snake))):
            self.game_running = False
            self.flash_game_over_message()

    def flash_game_over_message(self):
        for _ in range(5):  # Flash 5 times
            self.canvas.create_text(200, 200, text="你失败了！", fill="red", font=("Arial", 20))
            self.canvas.update()
            self.master.after(500)  # Wait for 500 ms
            self.canvas.delete(tk.ALL)
            self.draw_elements()  # Redraw the snake and food
            self.canvas.update()
            self.master.after(500)  # Wait for 500 ms
        self.canvas.create_text(200, 200, text="游戏结束! 得分: " + str(self.score), fill="white", font=("Arial", 20))
        self.restart_button.pack()  # Show the restart button

    def restart_game(self):
        self.score = 0
        self.speed = 50
        self.snake = [(20, 20), (20, 30), (20, 40)]
        self.direction = 'Down'
        self.food_position = self.place_food()
        self.game_running = False
        self.restart_button.pack_forget()  # Hide the restart button
        self.score_label.config(text="得分: 0")  # Reset score display

        # Optionally, you can call start_game() here if you want to start immediately
        self.start_game()

    def draw_elements(self):
        self.canvas.delete(tk.ALL)
        for segment in self.snake:
            self.canvas.create_rectangle(segment[0], segment[1], segment[0] + 20, segment[1] + 20, fill="green")
        food_x, food_y = self.food_position
        self.canvas.create_oval(food_x, food_y, food_x + 20, food_y + 20, fill="red")

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
