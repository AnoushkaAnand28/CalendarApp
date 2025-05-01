import tkinter as tk
import calendar
from tkinter import messagebox

def show_calendar():
    try:
        year = int(year_entry.get())
        month = int(month_entry.get())

        if 1 <= month <= 12:
            cal_text = calendar.month(year, month)
            cal_display.delete("1.0", tk.END)
            cal_display.insert(tk.END, cal_text)
        else:
            messagebox.showerror("Invalid Input", "Month must be between 1 and 12.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")

# Create the main window
app = tk.Tk()
app.title("Calendar App")
app.geometry("400x300")
app.configure(bg="#f0f0f0")

# Widgets
tk.Label(app, text="Enter Year:", bg="#f0f0f0").pack()
year_entry = tk.Entry(app)
year_entry.pack()

tk.Label(app, text="Enter Month (1-12):", bg="#f0f0f0").pack()
month_entry = tk.Entry(app)
month_entry.pack()

tk.Button(app, text="Show Calendar", command=show_calendar, bg="#4CAF50", fg="white").pack(pady=10)

cal_display = tk.Text(app, height=10, width=40, font=("Courier", 10))
cal_display.pack()

# Run the app
app.mainloop()
