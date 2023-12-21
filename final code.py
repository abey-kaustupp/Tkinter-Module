import tkinter as tk
from tkinter import ttk, filedialog, messagebox

def submit_form():
    name = name_entry.get()
    address = address_entry.get()
    gender = gender_var.get()
    education = education_var.get()

    # Photo path may be empty if the user hasn't selected a photo
    photo_path_text = f"Photo Path: {photo_path}" if photo_path else "Photo Path: Not selected"

    # Create a formatted string with the collected information
    info_text = f"Name: {name}\nAddress: {address}\nGender: {gender}\nEducation: {education}\n{photo_path_text}\n\n"

    # Write the information to a text file (append mode)
    with open("final code.txt", "a", encoding="utf-8") as file:
        file.write(info_text)

    # Display a success message
    messagebox.showinfo("Success", "Form submitted successfully!")

def browse_photo():
    global photo_path
    photo_path = filedialog.askopenfilename()
    photo_label.config(text=f"Photo Path: {photo_path}")

# Create the main window
root = tk.Tk()
root.title("Student Information Form")

# Helper function to create labeled entry widgets
def create_labeled_entry(parent, label_text):
    label = tk.Label(parent, text=label_text)
    label.pack()
    entry = tk.Entry(parent)
    entry.pack()
    return entry

# Helper function to create labeled combobox widgets
def create_labeled_combobox(parent, label_text, values):
    label = tk.Label(parent, text=label_text)
    label.pack()
    var = tk.StringVar()
    combobox = ttk.Combobox(parent, textvariable=var, values=values)
    combobox.pack()
    return var, combobox

# Name Section
name_entry = create_labeled_entry(root, "Name:")

# Address Section
address_entry = create_labeled_entry(root, "Address:")

# Gender Section
gender_var, gender_dropdown = create_labeled_combobox(root, "Gender:", ["Male", "Female", "Other"])

# Education Section
education_var, education_dropdown = create_labeled_combobox(root, "Education:", ["UG", "PG", "PhD"])

# Photo Section
photo_label = tk.Label(root, text="Photo Path:")
photo_label.pack()
browse_button = tk.Button(root, text="Browse Photo", command=browse_photo)
browse_button.pack()

# Submit Button
submit_button = tk.Button(root, text="Submit Form", command=submit_form)
submit_button.pack(pady=20)

# Run the main loop
root.mainloop()
