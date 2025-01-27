import tkinter as tk
from tkinter import messagebox
import random

class Character:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def decrease_health(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def is_alive(self):
        return self.health > 0

class SurvivalIslandGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Survival Island")

        self.day = 1
        self.group = [
            Character("Aaron"),
            Character("Jasper"),
            Character("Susma"),
            Character("Aisha"),
            Character("Imo"),
            Character("Alizada"),
            Character("Bob")
        ]

        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="Survival Island", font=("Arial", 24))
        self.title_label.pack(pady=10)

        self.status_label = tk.Label(self.root, text="", font=("Arial", 16))
        self.status_label.pack(pady=10)

        self.update_status()

        self.options_frame = tk.Frame(self.root)
        self.options_frame.pack(pady=10)

        self.search_food_button = tk.Button(self.options_frame, text="Search for Food", command=self.search_food, width=20)
        self.search_food_button.grid(row=0, column=0, padx=5, pady=5)

        self.build_shelter_button = tk.Button(self.options_frame, text="Build Shelter", command=self.build_shelter, width=20)
        self.build_shelter_button.grid(row=0, column=1, padx=5, pady=5)

        self.explore_island_button = tk.Button(self.options_frame, text="Explore Island", command=self.explore_island, width=20)
        self.explore_island_button.grid(row=1, column=0, padx=5, pady=5)

        self.rest_button = tk.Button(self.options_frame, text="Rest", command=self.rest, width=20)
        self.rest_button.grid(row=1, column=1, padx=5, pady=5)

    def update_status(self):
        status = f"Day {self.day}\n"
        for member in self.group:
            status += f"{member.name}: {member.health} health\n"
        self.status_label.config(text=status)

    def check_game_over(self):
        if all(not member.is_alive() for member in self.group):
            messagebox.showinfo("Game Over", "All members of the group have perished. Game over.")
            self.root.quit()
        elif any(member.is_alive() for member in self.group):
            self.day += 1
            self.update_status()

    def search_food(self):
        if random.random() < 0.7:
            messagebox.showinfo("Success", "The group finds some edible berries and fish. The group eats and gains some health.")
            for member in self.group:
                if member.is_alive():
                    member.health += 10
                    if member.health > 100:
                        member.health = 100
        else:
            messagebox.showwarning("Danger", "They eat some poisonous mushrooms by mistake! The group loses health.")
            for member in self.group:
                if member.is_alive():
                    member.decrease_health(20)

        self.check_game_over()

    def build_shelter(self):
        if random.random() < 0.8:
            messagebox.showinfo("Success", "They successfully build a shelter. The group gains protection from the elements.")
            for member in self.group:
                if member.is_alive():
                    member.health += 5
                    if member.health > 100:
                        member.health = 100
        else:
            messagebox.showwarning("Danger", "While building the shelter, they encounter wild animals! The group loses health.")
            for member in self.group:
                if member.is_alive():
                    member.decrease_health(15)

        self.check_game_over()

    def explore_island(self):
        if random.random() < 0.6:
            messagebox.showinfo("Success", "They find fresh water and medicinal plants. The group gains health.")
            for member in self.group:
                if member.is_alive():
                    member.health += 15
                    if member.health > 100:
                        member.health = 100
        else:
            messagebox.showwarning("Danger", "They encounter a group of snakes! The group loses health.")
            for member in self.group:
                if member.is_alive():
                    member.decrease_health(25)

        self.check_game_over()

    def rest(self):
        messagebox.showinfo("Rest", "The group decides to rest and regains some health.")
        for member in self.group:
            if member.is_alive():
                member.health += 20
                if member.health > 100:
                    member.health = 100

        self.check_game_over()

if __name__ == "__main__":
    root = tk.Tk()
    game = SurvivalIslandGame(root)
    root.mainloop()
