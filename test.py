import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=200, height=200, bg="black")
canvas.pack()

# Create some canvas items
rect1 = canvas.create_rectangle(10, 10, 60, 60, fill="green")
rect2 = canvas.create_rectangle(40, 40, 90, 90, fill="green")
oval1 = canvas.create_oval(70, 70, 120, 120, fill="green")

# Check for items overlapping a specific area
overlapping_items = canvas.find_overlapping(30, 30, 70, 70)
print(f"Items overlapping the area (30,30,70,70): {overlapping_items}")

root.mainloop()
