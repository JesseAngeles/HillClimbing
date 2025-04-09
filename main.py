import tkinter as tk
from UI.KnapsackWindow import knapsack_problem_window
from UI.TravelSalesmanWindow import travel_salesman_problem_window

def main():
    root = tk.Tk()
    root.title("Main Window")
    root.geometry("300x600")
    root.protocol("WM_DELETE_WINDOW", root.quit)

    tk.Label(root, text="Bienvenido", font=("Arial", 14)).pack(pady=20)
    tk.Button(root, text="Knapsack", command=lambda: knapsack_problem_window(root)).pack(pady=10)
    tk.Button(root, text="Travel Salesman", command=lambda: travel_salesman_problem_window(root)).pack(pady=10)
    tk.Button(root, text="Salir", command=root.quit).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
