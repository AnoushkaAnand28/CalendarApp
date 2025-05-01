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
app.title("💗 Pink Calendar App")
app.geometry("420x320")
app.configure(bg="#ffe6f0")  # Soft pink background

# Widgets
tk.Label(app, text="Enter Year:", bg="#ffe6f0", fg="#cc0066", font=("Helvetica", 12)).pack(pady=(10, 0))
year_entry = tk.Entry(app, bg="#fff0f5", fg="#cc0066", font=("Helvetica", 11))
year_entry.pack()

tk.Label(app, text="Enter Month (1-12):", bg="#ffe6f0", fg="#cc0066", font=("Helvetica", 12)).pack(pady=(10, 0))
month_entry = tk.Entry(app, bg="#fff0f5", fg="#cc0066", font=("Helvetica", 11))
month_entry.pack()

tk.Button(app, text="Show Calendar", command=show_calendar, bg="#ff99cc", fg="white", font=("Helvetica", 12, "bold")).pack(pady=10)

cal_display = tk.Text(app, height=10, width=40, font=("Courier", 10), bg="#fff0f5", fg="#660033")
cal_display.pack(pady=5)

# Run the app
app.mainloop()
