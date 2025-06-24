import tkinter as tk
from tkinter import filedialog
import csv

bbg = "white"  # Background color
animation_running = True  # Control flag for the animation

class ButtonWindowApp:
    def __init__(self, master):
        self.master = master
        master.title("Metacatalysis Synthesis Machine")
        master.geometry("1200x900")
        master.configure(bg=bbg)

        # Show the initial main screen
        self.show_main_screen()

    def show_main_screen(self):
        """Display the main screen with circular buttons."""
        self.clear_screen()

        # Header label
        header_label = tk.Label(
            self.master,
            text="Metacatalysis Synthesis Machine".upper(),
            bg=bbg,
            font=("Helvetica", 60, "bold")
        )
        header_label.pack(pady=20)

        # Create a frame for the circular buttons
        frame = tk.Frame(self.master, bg=bbg)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Add circular buttons for each function
        self.create_circular_button(frame, "Run!", "lightblue", 0, 0, self.show_run_screen)
        self.create_circular_button(frame, "Wash", "lightgreen", 0, 1, self.show_wash_screen)
        self.create_circular_button(frame, "Configure", "lightcoral", 1, 0, self.show_configure_screen)
        self.create_circular_button(frame, "Settings", "lightgoldenrodyellow", 1, 1, self.show_settings_screen)

    def create_circular_button(self, frame, text, color, row, col, command):
        """Create a circular button with a given color and command."""
        button_radius = 100

        button = tk.Canvas(
            frame, 
            width=2 * button_radius, 
            height=2 * button_radius, 
            highlightthickness=0, 
            bg=bbg
        )
        button.create_oval(0, 0, 2 * button_radius, 2 * button_radius, fill=color, outline="")
        button.create_text(button_radius, button_radius, text=text, font=("Helvetica", 24, "bold"), fill="black")

        # Bind the button click to the corresponding command
        button.bind("<Button-1>", lambda event: command())
        button.grid(row=row, column=col, padx=20, pady=20)

    def show_run_screen(self):
        """Show the Run screen with a loading animation and stop button."""
        self.show_loading_screen("Running...")

    def show_wash_screen(self):
        """Show the Wash screen with a loading animation and stop button."""
        self.show_loading_screen("Washing...")

    def show_loading_screen(self, message):
        """Display a loading animation with a circular stop button."""
        self.clear_screen()

        # Display the message at the top
        label = tk.Label(self.master, text=message, font=("Helvetica", 48), bg=bbg)
        label.pack(pady=20)

        # Create a canvas for the loading wheel
        self.canvas = tk.Canvas(self.master, width=200, height=200, bg=bbg, highlightthickness=0)
        self.canvas.pack(pady=20)

        # Initialize animation variables
        self.angle = 0
        self.animate_loading_wheel()

        # Create a circular STOP button
        stop_button = tk.Canvas(self.master, width=120, height=120, highlightthickness=0, bg=bbg)
        stop_button.create_oval(0, 0, 120, 120, fill="red", outline="")
        stop_button.create_text(60, 60, text="STOP", font=("Helvetica", 24, "bold"), fill="white")
        stop_button.bind("<Button-1>", lambda event: self.stop_action())
        stop_button.pack(pady=20)

    def animate_loading_wheel(self):
        """Create a smooth rotating loading wheel."""
        global animation_running

        if not animation_running:
            return  # Stop the animation if the flag is False

        self.canvas.delete("all")  # Clear the previous frame
        x, y, r = 100, 100, 80  # Circle center and radius

        # Draw multiple arcs to create a sleek loading effect
        for i in range(12):
            angle = (self.angle + i * 30) % 360  # Offset each arc by 30 degrees
            color = f"#{int(255 - i * 20):02x}{int(255 - i * 20):02x}ff"  # Gradient effect
            self.canvas.create_arc(
                x - r, y - r, x + r, y + r,
                start=angle, extent=15, outline=color, width=8, style=tk.ARC
            )

        # Update the angle for the next frame
        self.angle = (self.angle + 5) % 360

        # Schedule the next frame of the animation
        self.master.after(50, self.animate_loading_wheel)

    def stop_action(self):
        """Stop the loading animation and return to the main screen."""
        global animation_running
        animation_running = False  # Stop the animation
        self.show_main_screen()  # Return to the main screen

    def show_configure_screen(self):
        """Display the Configuration screen."""
        self.clear_screen()

        # Header label
        header_label = tk.Label(
            self.master,
            text="Configuration".upper(),
            bg=bbg,
            font=("Helvetica", 60, "bold")
        )
        header_label.pack(pady=20)

        # Create a frame for configuration inputs
        config_frame = tk.Frame(self.master, bg=bbg)
        config_frame.pack(pady=20)

        # Parameters for configuration
        tk.Label(config_frame, text="Pump Speed (RPM):", bg=bbg, font=("Helvetica", 24)).grid(row=0, column=0, padx=10, pady=10)
        self.speed_entry = tk.Entry(config_frame, font=("Helvetica", 24))
        self.speed_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(config_frame, text="Duration (seconds):", bg=bbg, font=("Helvetica", 24)).grid(row=1, column=0, padx=10, pady=10)
        self.duration_entry = tk.Entry(config_frame, font=("Helvetica", 24))
        self.duration_entry.grid(row=1, column=1, padx=10, pady=10)

        # Load CSV button
        load_csv_button = tk.Button(
            self.master, 
            text="Load CSV", 
            font=("Helvetica", 24), 
            command=self.load_csv, 
            bg="lightblue"
        )
        load_csv_button.pack(pady=10)

        # Create New CSV button
        create_csv_button = tk.Button(
            self.master, 
            text="Create New CSV", 
            font=("Helvetica", 24), 
            command=self.create_csv, 
            bg="lightgreen"
        )
        create_csv_button.pack(pady=10)

        # Save button
        save_button = tk.Button(
            self.master, 
            text="Save Configuration", 
            font=("Helvetica", 24), 
            command=self.save_configuration, 
            bg="lightblue"
        )
        save_button.pack(pady=20)

        # Back button
        back_button = tk.Button(
            self.master, 
            text="Back to Main Menu", 
            font=("Helvetica", 24), 
            command=self.show_main_screen, 
            bg="lightcoral"
        )
        back_button.pack(pady=10)

    def load_csv(self):
        """Load a CSV file from the user's computer."""
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if file_path:
            try:
                with open(file_path, mode='r', newline='') as file:
                    reader = csv.reader(file)
                    data = list(reader)
                    print("Loaded CSV Data:")
                    for row in data:
                        print(row)
            except Exception as e:
                print(f"Error loading CSV: {e}")

    def create_csv(self):
        """Create a new CSV file."""
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
        if file_path:
            try:
                # Create an empty CSV file
                with open(file_path, mode='w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(['Column1', 'Column2'])  # Example headers
                print(f"Created new CSV file at: {file_path}")
            except Exception as e:
                print(f"Error creating CSV: {e}")

    def save_configuration(self):
        """Save the configuration parameters."""
        speed = self.speed_entry.get()
        duration = self.duration_entry.get()
        print(f"Configuration Saved: Pump Speed = {speed} RPM, Duration = {duration} seconds")

    def show_settings_screen(self):
        """Display the Settings screen."""
        self.clear_screen()
        label = tk.Label(self.master, text="Settings", font=("Helvetica", 60), bg=bbg)
        label.pack(pady=20)

    def clear_screen(self):
        """Clear the current screen contents"""
