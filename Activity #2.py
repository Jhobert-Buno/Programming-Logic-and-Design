import tkinter
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import PhotoImage

def is_valid_name(entry_text):
    return all(char.isalpha() or char.isspace() for char in entry_text)

def enter_data():
    firstname = first_name_entry.get()
    middlename = middle_name_entry.get()
    lastname = last_name_entry.get()
    age = age_spinbox.get()
    barangay = barangay_label_entry.get()
    cityormunicipality = city_or_municipality_label_entry.get()
    stateorprovince = state_or_province_label_entry.get()

    fullname = firstname +" " + middlename + " " +lastname
    if not all(is_valid_name(entry_text) for entry_text in (fullname)):
            messagebox.showwarning("Invalid Input", "Please enter a name using LETTERS ONLY.")
            return

    if firstname and middlename and lastname and age and barangay and cityormunicipality and stateorprovince:
        firstname = first_name_entry.get()
        middlename = middle_name_entry.get()
        lastname = last_name_entry.get()
        age = age_spinbox.get()
        
        barangay = barangay_label_entry.get()
        cityormunicipality = city_or_municipality_label_entry.get()
        stateorprovince = state_or_province_label_entry.get()

        fullname = firstname +" " + middlename + " " +lastname
        address = barangay+", "+ cityormunicipality+", "+ stateorprovince
        age_final = age + " years old"

        result_window = tkinter.Tk()
        result_window.title("Personal Information")
        result_window.geometry('830x400')
        result_window.configure(bg='#CD6090')


        frame = tkinter.Frame(result_window)
        frame.pack(padx=20, pady=20)
        frame.configure(bg='#FFEFDB')


        result = tkinter.LabelFrame(frame, text="RESULT", font=('Georgia',15), bg='#FAEBD7',width=800, height=500)
        result.grid(row= 0, column =0, padx=20, pady=10)
        result.configure(bg='#FFEFDB')
        
        name_result = tkinter.Label(result, text="YOU ARE", font='Arial, 12', bg='#FAEBD7')
        name_result.grid(row= 1, column =2, padx=30, pady=15)

        firstname_result_input = tkinter.Label(result, text = fullname, font=("Georgia Bold", 30), bg='#FAEBD7')
        firstname_result_input.grid(row= 2, column =2, padx=30, pady=5)

        age_result = tkinter.Label(result, text="YOUR AGE IS", font='Arial, 12', bg='#FAEBD7')
        age_result.grid(row= 3, column =2, padx=10, pady=5)

        age_result_input = tkinter.Label(result, text= age_final, font=("Georgia Bold", 30), bg='#FAEBD7')
        age_result_input.grid(row= 4, column =2, padx=30, pady=5)

        address_result = tkinter.Label(result, text="YOU LIVE IN", font='Arial, 12',bg='#FAEBD7')
        address_result.grid(row= 5, column =2, padx=30, pady=5)


        address_result_input = tkinter.Label(result, text=address, font=("Georgia Bold", 30),bg='#FAEBD7')
        address_result_input.grid(row= 6, column =2, padx=30, pady=5)

        

    else:
        tkinter.messagebox.showwarning(title="Error", message="Complete information is required")


window = tkinter.Tk()
window.title("Personal Information")
window.geometry('830x400')


image_path=PhotoImage(file=r"C:\Users\jhobert\Pictures\386886ed-6375-4924-96f3-aab3a6b43658.png")
bg_image=tkinter.Label(window,image=image_path)
bg_image.place(relheight=1, relwidth=1)

frame = tkinter.Frame(window)
frame.pack(padx=20, pady=20)
frame.configure(bg='#FFEFDB')

user_info_frame =tkinter.LabelFrame(frame, text="USER INFORMATION", font=('Georgia',15), bd=5)
user_info_frame.grid(row= 3, column =0, padx=20, pady=10)
user_info_frame.configure(bg='#FFEFDB')

first_name_label = tkinter.Label(user_info_frame, text="First Name", font='Arial, 12', bg='#FFEFDB')
first_name_label.grid(row= 0, column= 0)

middle_name_label = tkinter.Label(user_info_frame, text="Middle Name", font='Arial, 12', bg='#FFEFDB')
middle_name_label.grid(row=0, column=1)

last_name_label = tkinter.Label(user_info_frame, text="Last Name", font='Arial, 12', bg='#FFEFDB')
last_name_label.grid(row=0, column=2)

first_name_entry = tkinter.Entry(user_info_frame, font='Arial, 15')
middle_name_entry = tkinter.Entry(user_info_frame, font='Arial, 15')
last_name_entry = tkinter.Entry(user_info_frame, font='Arial, 15')
first_name_entry.grid(row=1, column=0)
middle_name_entry.grid(row=1, column=1)
last_name_entry.grid(row=1, column=2)

age_label = tkinter.Label(user_info_frame, text="Age", font='Arial, 12', bg='#FFEFDB')
age_spinbox = tkinter.Spinbox(user_info_frame, from_=15, to=75, font='Arial, 15')
age_label.grid(row=2, column=1)
age_spinbox.grid(row=3, column=1)


address_label = tkinter.Label(user_info_frame, text="Address", font='Arial, 12', bg='#FFEFDB')
address_label.grid(row=4, column=1)

barangay_label = tkinter.Label(user_info_frame, text="Barangay", font='Arial, 11', bg='#FFEFDB')
city_or_municipality_label = tkinter.Label(user_info_frame, text="City/Municipality", font='Arial, 11', bg='#FFEFDB')
state_or_province_label = tkinter.Label(user_info_frame, text="State/Province", font='Arial, 11', bg='#FFEFDB')
barangay_label.grid(row=5, column=0)
city_or_municipality_label.grid(row=5, column=1)
state_or_province_label.grid(row=5, column=2)

barangay_label_entry = tkinter.Entry(user_info_frame, font='Arial, 15')
city_or_municipality_label_entry = tkinter.Entry(user_info_frame, font='Arial, 15')
state_or_province_label_entry = tkinter.Entry(user_info_frame, font='Arial, 15')
barangay_label_entry.grid(row=6, column=0)
city_or_municipality_label_entry.grid(row=6, column=1)
state_or_province_label_entry.grid(row=6, column=2)


for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

button = tkinter.Button(frame, text="Submit", command=enter_data, font='Arial, 11', fg='#DCDCDC')
button.grid(row=4, column=0, sticky="news", padx=20, pady=10)
button.configure(bg='#1A1A1A')



window.mainloop()