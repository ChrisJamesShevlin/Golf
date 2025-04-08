import tkinter as tk
from tkinter import messagebox

def calculate_score():
    try:
        # Retrieve and convert input values from the entry fields
        name = name_entry.get().strip()
        xwins = float(xwins_entry.get())
        total_shots = float(total_shots_entry.get())
        putt = float(putt_entry.get())
        T2G = float(t2g_entry.get())
        SG_true = float(sg_true_entry.get())
        SG_expected = float(sg_expected_entry.get())
        course_fit = float(course_fit_entry.get())
        ranking = float(ranking_entry.get())
        live_odds = float(live_odds_entry.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for all metrics.")
        return

    # Increased multiplier for the pressure (handling) component
    pressure_component = (SG_true - SG_expected) * 15

    # Calculate overall score using a weighted sum
    score = (50 +
             (xwins * 1) +
             (total_shots * 0.5) +
             (putt * 0.5) +
             (T2G * 0.5) +
             pressure_component +
             (course_fit * 20) -
             (ranking * 0.5))
    
    # Clamp score between 0 and 100
    score = max(0, min(score, 100))
    score_str = f"{score:.2f}"
    
    # Calculate a value metric if live odds are provided (must be > 0)
    if live_odds > 0:
        value_metric = score / live_odds
    else:
        value_metric = score  # Fallback in the unlikely case odds are zero
    value_str = f"{value_metric:.2f}"

    # Debug output printed to the terminal in the required format
    print(f"Golfer: {name}, Overall Score: {score_str}, Live Odds: {live_odds:.2f}, Value Metric: {value_str}")
    
    # Update the GUI to display the results as well
    result_label.config(text=f"Golfer: {name}\nOverall Score: {score_str}\nLive Odds: {live_odds:.2f}\nValue Metric: {value_str}")

# Create the main Tkinter window
root = tk.Tk()
root.title("Golf Overall Score Calculator")

# -------------------------
# Define the input fields for each metric
# -------------------------

# Golfer Name
tk.Label(root, text="Golfer Name").grid(row=0, column=0, padx=5, pady=5, sticky="e")
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=5, pady=5)

# Expected Wins (xwins)
tk.Label(root, text="Expected Wins (xwins)").grid(row=1, column=0, padx=5, pady=5, sticky="e")
xwins_entry = tk.Entry(root)
xwins_entry.grid(row=1, column=1, padx=5, pady=5)

# Total Shots Gained
tk.Label(root, text="Total Shots Gained").grid(row=2, column=0, padx=5, pady=5, sticky="e")
total_shots_entry = tk.Entry(root)
total_shots_entry.grid(row=2, column=1, padx=5, pady=5)

# Putt
tk.Label(root, text="Putt").grid(row=3, column=0, padx=5, pady=5, sticky="e")
putt_entry = tk.Entry(root)
putt_entry.grid(row=3, column=1, padx=5, pady=5)

# T2G
tk.Label(root, text="T2G").grid(row=4, column=0, padx=5, pady=5, sticky="e")
t2g_entry = tk.Entry(root)
t2g_entry.grid(row=4, column=1, padx=5, pady=5)

# Strokes Gained (True)
tk.Label(root, text="Strokes Gained (True)").grid(row=5, column=0, padx=5, pady=5, sticky="e")
sg_true_entry = tk.Entry(root)
sg_true_entry.grid(row=5, column=1, padx=5, pady=5)

# Strokes Gained (Expected)
tk.Label(root, text="Strokes Gained (Expected)").grid(row=6, column=0, padx=5, pady=5, sticky="e")
sg_expected_entry = tk.Entry(root)
sg_expected_entry.grid(row=6, column=1, padx=5, pady=5)

# Course Fit
tk.Label(root, text="Course Fit").grid(row=7, column=0, padx=5, pady=5, sticky="e")
course_fit_entry = tk.Entry(root)
course_fit_entry.grid(row=7, column=1, padx=5, pady=5)

# Current Ranking
tk.Label(root, text="Current Ranking").grid(row=8, column=0, padx=5, pady=5, sticky="e")
ranking_entry = tk.Entry(root)
ranking_entry.grid(row=8, column=1, padx=5, pady=5)

# Live Odds for the betting comparison
tk.Label(root, text="Live Odds").grid(row=9, column=0, padx=5, pady=5, sticky="e")
live_odds_entry = tk.Entry(root)
live_odds_entry.grid(row=9, column=1, padx=5, pady=5)

# -------------------------
# Button to trigger the calculation
# -------------------------
calc_button = tk.Button(root, text="Calculate Score", command=calculate_score)
calc_button.grid(row=10, column=0, columnspan=2, padx=5, pady=10)

# Label to display the result in the GUI
result_label = tk.Label(root, text="", font=("Helvetica", 10, "bold"))
result_label.grid(row=11, column=0, columnspan=2, padx=5, pady=10)

# Start the main event loop
root.mainloop()
