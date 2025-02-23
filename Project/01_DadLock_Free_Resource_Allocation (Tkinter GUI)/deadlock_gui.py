import tkinter as tk
from tkinter import messagebox

def is_safe_state(available, max_need, allocated):
    num_processes = len(max_need)
    num_resources = len(available)
    need = [[max_need[i][j] - allocated[i][j] for j in range(num_resources)] for i in range(num_processes)]
    work = available[:]
    finish = [False] * num_processes
    safe_sequence = []

    while len(safe_sequence) < num_processes:
        allocated_this_round = False
        for i in range(num_processes):
            if not finish[i] and all(need[i][j] <= work[j] for j in range(num_resources)):
                work = [work[j] + allocated[i][j] for j in range(num_resources)]
                safe_sequence.append(i)
                finish[i] = True
                allocated_this_round = True
                break
        if not allocated_this_round:
            return False, []

    return True, safe_sequence

def generate_table():
    try:
        num_processes = int(num_processes_entry.get())
        num_resources = int(num_resources_entry.get())

        # Clear previous content
        for widget in tables_frame.winfo_children():
            widget.destroy()

        # Create Available Resources table
        available_table = tk.LabelFrame(tables_frame, text="Available Resources", padx=10, pady=10)
        available_table.grid(row=0, column=0, pady=5, padx=5)

        tk.Label(available_table, text="Available").grid(row=0, column=0, padx=5)
        for j in range(num_resources):
            tk.Entry(available_table, width=5, textvariable=available_vars[j]).grid(row=0, column=j + 1)

        # Create Max Need table
        max_need_table = tk.LabelFrame(tables_frame, text="Max Need", padx=10, pady=10)
        max_need_table.grid(row=1, column=0, pady=5, padx=5)

        for i in range(num_processes):
            tk.Label(max_need_table, text=f"Process {i + 1} →").grid(row=i + 1, column=0, padx=5)
            for j in range(num_resources):
                tk.Entry(max_need_table, width=5, textvariable=max_need_vars[i][j]).grid(row=i + 1, column=j + 1)

        # Create Allocated table
        allocated_table = tk.LabelFrame(tables_frame, text="Allocated Resources", padx=10, pady=10)
        allocated_table.grid(row=2, column=0, pady=5, padx=5)

        for i in range(num_processes):
            tk.Label(allocated_table, text=f"Process {i + 1} →").grid(row=i + 1, column=0, padx=5)
            for j in range(num_resources):
                tk.Entry(allocated_table, width=5, textvariable=allocated_vars[i][j]).grid(row=i + 1, column=j + 1)

        # Create Check Safety button
        check_button = tk.Button(tables_frame, text="Check Safety", command=check_safety)
        check_button.grid(row=3 + num_processes * 2, column=0, columnspan=num_resources + 1, pady=10)

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for processes and resources.")

def check_safety():
    try:
        num_processes = int(num_processes_entry.get())
        num_resources = int(num_resources_entry.get())

        available = [available_vars[j].get() for j in range(num_resources)]
        max_need = [[max_need_vars[i][j].get() for j in range(num_resources)] for i in range(num_processes)]
        allocated = [[allocated_vars[i][j].get() for j in range(num_resources)] for i in range(num_processes)]

        safe, sequence = is_safe_state(available, max_need, allocated)
        if safe:
            result_label.config(text=f"Safe Sequence: {' → '.join(map(str, sequence))}")
        else:
            result_label.config(text="Unsafe State!")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers in all fields.")

root = tk.Tk()
root.title("Deadlock-Free Resource Allocation")

frame = tk.Frame(root)
frame.pack(pady=10)

# Inputs for number of processes and resources
tk.Label(frame, text="Number of Processes:").grid(row=0, column=0, padx=5, pady=5)
num_processes_entry = tk.Entry(frame)
num_processes_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="Number of Resources:").grid(row=1, column=0, padx=5, pady=5)
num_resources_entry = tk.Entry(frame)
num_resources_entry.grid(row=1, column=1, padx=5, pady=5)

generate_button = tk.Button(frame, text="Generate Table", command=generate_table)
generate_button.grid(row=2, column=0, columnspan=2, pady=5)

# Result Label
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Frame to hold the tables
tables_frame = tk.Frame(root)
tables_frame.pack(pady=10)

# Variables to hold the entry values
available_vars = [tk.IntVar() for _ in range(10)]
max_need_vars = [[tk.IntVar() for _ in range(10)] for _ in range(10)]
allocated_vars = [[tk.IntVar() for _ in range(10)] for _ in range(10)]

root.mainloop()
