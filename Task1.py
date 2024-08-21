# importing modules to create GUI
import tkinter as Tk
from tkinter import messagebox

# Function to allow users to submit the data entered
def register():
    name=name_entry.get()
    email=email_entry.get()
    age=age_entry.get()
    gender=gender_entry.get()
    
    # Validating if all the fields are filled
    if (name and email and age and gender):
        try:
            age = int(age)         # To validate that age is a number
            messagebox.showinfo("Registration",f"Name: {name}\nEmail: {email}\nAge: {age}\nGender: {gender}")
        except ValueError:
            messagebox.showerror("Error","Please enter valid age")
    else:
        messagebox.showerror("Error", "PLease fill in all the details")

# Creating the application window
root = Tk.Tk()
root.title("Registration Form")     # Givnig the tile name

# Defining the labels and showing input field so that user can enter details
name = Tk.Label(root, text="Name: ")
name.grid(row=0,column=0,padx=5,pady=5)
name_entry = Tk.Entry(root)
name_entry.grid(row=0,column=1,padx=5,pady=5)   # row=,column= allows to define the position of the label and entry field in the window

email = Tk.Label(root, text="Email: ")      # Label() is used to show the text on the window
email.grid(row=1,column=0,padx=5,pady=5)    
email_entry = Tk.Entry(root)                # Entry() is used to allow users to input text 
email_entry.grid(row=1,column=1,padx=5,pady=5)

age = Tk.Label(root, text="Age: ")
age.grid(row=2,column=0,padx=5,pady=5)    
age_entry = Tk.Entry(root)
age_entry.grid(row=2,column=1,padx=5,pady=5)

gender = Tk.Label(root,text="Gender: ")
gender.grid(row=3,column=0,padx=5,pady=5)
 
gender_entry = Tk.StringVar(root)
gender_entry.set("Male")

male = Tk.Radiobutton(root, text="Male",variable=gender_entry,value="Male")
male.grid(row=3,column=1,padx=5,pady=5,sticky='w')   # Radiobutton is used to give the user options to choose between different values

female = Tk.Radiobutton(root, text="Female", variable=gender_entry, value="Female")
female.grid(row=3, column=2,padx=5,pady=5,sticky='w')

submit = Tk.Button(root, text="Submit", command=register)
submit.grid(row=4,columnspan=2,padx=5,pady=5)       # colspan allows you to merge columns 

Tk.mainloop()   # Closing the application window