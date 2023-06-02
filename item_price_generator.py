import json
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog


def generate_json_file():
    try:
        start_range = int(start_range_entry.get())
        end_range = int(end_range_entry.get())

        data = {
            "customSalePrices": {},
            "primaryLootValueSources": {}
        }

        # Generate primary loot value sources within the specified range
        for i in range(start_range, end_range + 1):
            data["primaryLootValueSources"][str(i)] = "market"

        # Prompt the user to choose the directory to save the JSON file
        file_path = filedialog.asksaveasfilename(
            initialdir="/",
            initialfile="itemprices.json",
            title="Select Save Location",
            filetypes=(("JSON Files", "*.json"), ("All Files", "*.*"))
        )

        # Check if the user canceled the file selection
        if not file_path:
            return

        # Write the data to a JSON file with proper indentation
        with open(file_path, "w") as json_file:
            json.dump(data, json_file, indent=4)

        messagebox.showinfo("JSON File Generated", f"The JSON file has been generated and saved to:\n{file_path}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid integer values for the range.")


# Create the main window
window = tk.Tk()
window.title("JSON File Generator")

# Set the window size
window_width = 400
window_height = 200

# Get the screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calculate the x and y positions to center the window
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

# Set the window geometry
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Create a style object from ttk
style = ttk.Style()

# Configure the style for the labels and entry fields
style.configure("TLabel", foreground="black", font=("Arial", 12))
style.configure("TEntry", font=("Arial", 12))

# Create the range input labels and entry fields with proper spacing
start_range_label = ttk.Label(window, text="Start Range:")
start_range_label.pack(pady=(20, 5))
start_range_entry = ttk.Entry(window)
start_range_entry.pack(pady=5)

end_range_label = ttk.Label(window, text="End Range:")
end_range_label.pack()
end_range_entry = ttk.Entry(window)
end_range_entry.pack()

# Create the generate button
generate_button = ttk.Button(window, text="Generate JSON File", command=generate_json_file)
generate_button.pack(pady=10)

# Start the Tkinter event loop
window.mainloop()
