import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd  # For handling CSV files

class ModernPumpApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("500x600")
        self.root.title("Pump Control")
        self.root.configure(bg="#1C1C1C")

        # Upload button to select a CSV file
        upload_button = tk.Button(
            root, text="Upload CSV", 
            command=self.upload_csv, 
            font=("SF Pro Display", 16), 
            bg="#4CAF50", fg="white", 
            activebackground="#66BB6A", borderwidth=0
        )
        upload_button.pack(pady=20)

    def upload_csv(self):
        """Open a file dialog for the user to upload a CSV file."""
        try:
            # Open file dialog and allow user to select a CSV file
            file_path = filedialog.askopenfilename(
                title="Select a CSV File",
                filetypes=[("CSV Files", "*.csv")],
            )
            
            if file_path:  # Check if a file was selected
                # Use pandas to read the CSV file
                data = pd.read_csv(file_path)
                print(data.head())  # Display the first few rows (for testing)
                messagebox.showinfo("Upload Successful", f"File '{file_path}' uploaded successfully!")
            else:
                messagebox.showwarning("No File Selected", "Please select a CSV file.")
        
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

# Main application loop
if __name__ == "__main__":
    root = tk.Tk()
    app = ModernPumpApp(root)
    root.mainloop()
