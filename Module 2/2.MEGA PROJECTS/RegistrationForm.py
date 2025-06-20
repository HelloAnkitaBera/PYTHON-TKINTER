import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


def validate_inputs(name, age, email):
    if not name or not age or not email:
        return "All fields are required."
    if not age.isdigit():
        return "Age must be a number."
    if "@" not in email or "." not in email:
        return "Invalid email format."
    return None
   
def clear_form():
    firstname_var.set("")
    lastname_var.set("")
    fathersname_var.set("")
    age_var.set("")
    email_var.set("")
    gender_var.set("")
    course_var.set("")
    DOB_var.set("")
    phoneno_var.set("")
    gurdainphone_var.set("")
    gurdainemail_var.set("")
    nationality_var.set("")
    religion_var.set("")
    bloodgroup_var.set("")
    Occupation_var.set("")
    Country_var.set("")
    term_var.set(0)

def save_to_file(data):
    with open("registrations.txt", "a") as file:
        file.write(data + "\n")

def register_student():
    firstname = firstname_var.get()
    lastname = lastname_var.get()
    fathersname = fathersname_var.get()
    mothersname = mothersname_var.get()
    age = age_var.get()
    DOB = DOB_var.get()
    gender = gender_var.get()
    course = course_var.get()
    phoneno = phoneno_var.get()
    gurdainphone = gurdainphone_var.get()
    gurdainemail = gurdainemail_var.get()
    email = email_var.get()
    nationality = nationality_var.get()
    religion = religion_var.get()
    bloodgroup = bloodgroup_var.get()
    occupation = Occupation_var.get()
    address = address_var.get()
    town = town_var.get()
    disirict = district_var.get() 
    state = state_var.get() 
    pincode = pincode_var.get()
    AdmissionType = AdmissionType_var.get()
    Country = Country_var.get()
    FatherOccupation = FatherOccupation_var.get()
    MotherOccupation = MotherOccupation_var.get()
    terms_accepted = "Yes" if term_var.get() else "No"


    error = validate_inputs(f"{firstname} {lastname}", age, email)
    if error:
        messagebox.showerror("Validation Error", error)
        return

    entry = f"{firstname},{lastname},{gender},{DOB},{age},{phoneno},{email},{fathersname},{mothersname},{gurdainphone},{gurdainemail},{course}, {nationality}, {religion}, {bloodgroup}, {FatherOccupation},{MotherOccupation}, {address}, {town}, {disirict}, {state}, {pincode}, {AdmissionType}, {Country}"
    save_to_file(entry)
    messagebox.showinfo("Success", "Student registered successfully.")
    clear_form()



# Setup window
root = tk.Tk()
root.title("Student Registration Form")
root.geometry("854x480")



# Variables
firstname_var = tk.StringVar()
lastname_var = tk.StringVar()
name_var = tk.StringVar()
fathersname_var = tk.StringVar()
age_var = tk.StringVar()
gender_var = tk.StringVar(value="Male")
course_var = tk.StringVar()
email_var = tk.StringVar()
DOB_var = tk.StringVar()
phoneno_var = tk.StringVar()
mothersname_var = tk.StringVar()
gurdainemail_var = tk.StringVar()
gurdainphone_var = tk.StringVar()
nationality_var = tk.StringVar()
religion_var = tk.StringVar()
bloodgroup_var = tk.StringVar()
Occupation_var = tk.StringVar()
FatherOccupation_var = tk.StringVar()
MotherOccupation_var = tk.StringVar()
address_var = tk.StringVar()
town_var = tk.StringVar()
district_var = tk.StringVar()
state_var = tk.StringVar()
pincode_var = tk.StringVar()
AdmissionType_var = tk.StringVar()
Country_var = tk.StringVar()
term_var = tk.IntVar() 


form_frame = tk.Frame(root, padx=20, pady=20)
form_frame.pack(fill="both", expand=True)


student_frame = tk.LabelFrame(root, text="Student's Details", padx=10, pady=10)
student_frame.pack(fill="both", expand=True, padx=10, pady=5)


tk.Label(student_frame, text="First Name:").grid(row=0, column=0, sticky="e")
tk.Label(student_frame, text="Last Name:").grid(row=0, column=2, sticky="e")
tk.Entry(student_frame, textvariable=firstname_var).grid(row=0, column=1, pady=5)
tk.Entry(student_frame, textvariable=lastname_var).grid(row=0, column=3, pady=5)


tk.Label(student_frame, text="Gender:").grid(row=2, column=0, sticky="e")
gender_frame = tk.Frame(student_frame)
gender_frame.grid(row=2, column=1, pady=5, sticky="w")
tk.Radiobutton(gender_frame, text="Male", variable=gender_var, value="Male").pack(side="left")
tk.Radiobutton(gender_frame, text="Female", variable=gender_var, value="Female").pack(side="left")
tk.Radiobutton(gender_frame, text="Others", variable=gender_var, value="Others").pack(side="left")

tk.Label(student_frame, text="Date Of Birth:").grid(row=3, column=0, sticky="e")
tk.Entry(student_frame, textvariable=DOB_var).grid(row=3, column=1, pady=5)

tk.Label(student_frame, text="Age:").grid(row=3, column=2, sticky="e")
tk.Entry(student_frame, textvariable=age_var).grid(row=3, column=3, pady=5)

tk.Label(student_frame, text="Contact No:").grid(row=4, column=0, sticky="e")
tk.Entry(student_frame, textvariable=phoneno_var).grid(row=4, column=1, pady=5)

tk.Label(student_frame, text="Email:").grid(row=4, column=2, sticky="e")
tk.Entry(student_frame, textvariable=email_var).grid(row=4, column=3, pady=5)

tk.Label(student_frame, text="Nationality:").grid(row=5, column=0, sticky="e")
tk.Entry(student_frame, textvariable=nationality_var).grid(row=5, column=1, pady=5)

tk.Label(student_frame, text="Religion:").grid(row=5, column=2, sticky="e")
tk.Entry(student_frame, textvariable=religion_var).grid(row=5, column=3, pady=5)

tk.Label(student_frame, text="Blood Group:").grid(row=6, column=0, sticky="e")
tk.Entry(student_frame, textvariable=bloodgroup_var).grid(row=6, column=1, pady=5)


guardian_frame = tk.LabelFrame(root, text="Guardian's Details", padx=10, pady=10)
guardian_frame.pack(fill="both", expand=True, padx=10, pady=5)


tk.Label(guardian_frame, text="Father's Name:").grid(row=7, column=0, sticky="e")
tk.Entry(guardian_frame, textvariable=fathersname_var).grid(row=7, column=1, pady=5)

tk.Label(guardian_frame, text="Father's Occupation:").grid(row=7, column=2, sticky="e")
tk.Entry(guardian_frame, textvariable=FatherOccupation_var).grid(row=7, column=3, pady=5)

tk.Label(guardian_frame, text="Mother's Name:").grid(row=8, column=0, sticky="e")
tk.Entry(guardian_frame, textvariable=mothersname_var).grid(row=8, column=1, pady=5)

tk.Label(guardian_frame, text="Mother's Occupation:").grid(row=8, column=2, sticky="e")
tk.Entry(guardian_frame, textvariable=MotherOccupation_var).grid(row=8, column=3, pady=5)

tk.Label(guardian_frame, text="Gurdain's Contact No:").grid(row=9, column=0, sticky="e")
tk.Entry(guardian_frame, textvariable=gurdainphone_var).grid(row=9, column=1, pady=5)

tk.Label(guardian_frame, text="Gurdain's Email Address:").grid(row=9, column=2, sticky="e")
tk.Entry(guardian_frame, textvariable=gurdainemail_var).grid(row=9, column=3, pady=5)


address_frame = tk.LabelFrame(root, text="Permanent Address Details", padx=10, pady=10)
address_frame.pack(fill="both", expand=True, padx=10, pady=5)


tk.Label(address_frame, text="Home Address:").grid(row=10, column=0, sticky="e")
tk.Entry(address_frame, textvariable=address_var).grid(row=10, column=1, pady=5)

tk.Label(address_frame, text="Village/City/Town:").grid(row=10, column=2, sticky="e")
tk.Entry(address_frame, textvariable=town_var).grid(row=10, column=3, pady=5)

tk.Label(address_frame, text="District:").grid(row=11, column=0, sticky="e")
tk.Entry(address_frame, textvariable=district_var).grid(row=11, column=1, pady=5)

tk.Label(address_frame, text="State:").grid(row=11, column=2, sticky="e")
tk.Entry(address_frame, textvariable=state_var).grid(row=11, column=3, pady=5)

tk.Label(address_frame, text="Pin Code:").grid(row=12, column=0, sticky="e")
tk.Entry(address_frame, textvariable=pincode_var).grid(row=12, column=1, pady=5)

tk.Label(address_frame, text="Country:").grid(row=12, column=2, sticky="e")
tk.Entry(address_frame, textvariable=Country_var).grid(row=12, column=3, pady=5)


Course_frame = tk.LabelFrame(root, text="Course Details", padx=10, pady=10)
Course_frame.pack(fill="both", expand=True, padx=10, pady=5)


tk.Label(Course_frame, text="Course:").grid(row=21, column=0, sticky="e")
ttk.Entry(Course_frame, textvariable=course_var).grid(row=21, column=1, pady=5)

tk.Label(Course_frame, text="Admission Type: ").grid(row=22, column=0, sticky="e")
ttk.Entry(Course_frame, textvariable=AdmissionType_var).grid(row=22, column=1, pady=5)

tk.Checkbutton(root, text="I accept all terms and conditions.",variable=term_var).pack(anchor="w", padx=10, pady=10)


# Buttons
button_frame = tk.Frame(root, pady=10)
button_frame.pack()

tk.Button(button_frame, text="Register", command=register_student, fg="black", background="green").pack(side="left", padx=10)
tk.Button(button_frame, text="Clear", command=clear_form, fg="black", background="red").pack(side="left", padx=10)

root.mainloop()
