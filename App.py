import customtkinter as ctk
import tkinter.ttk as ttk

 
root = ctk.CTk()
root.geometry('500x600')
root.title('Formulário')

head_frame = ctk.CTkFrame(root, width=400, height=300, fg_color='transparent')
head_frame.pack(pady=10)
head_frame.pack_propagate(False)

heading_lb = ctk.CTkLabel(head_frame, text='Student Registration System', font=('Bold', 13))
heading_lb.pack(fill=ctk.X, pady=5)

student_id_lb = ctk.CTkLabel(head_frame, text='Student ID:', font=('Bold', 10))
student_id_lb.place(x=0, y=50)

student_id = ctk.CTkEntry(head_frame, font=('Bold', 10), width=180)
student_id.place(x=110, y=50)

student_name_lb = ctk.CTkLabel(head_frame, text='Student Name:', font=('Bold', 10))
student_name_lb.place(x=0, y=100)

student_name = ctk.CTkEntry(head_frame, font=('Bold', 10), width=180)
student_name.place(x=110, y=100)

student_email_lb = ctk.CTkLabel(head_frame, text='Student E-Mail:', font=('Bold', 10))
student_email_lb.place(x=0, y=150)

student_email = ctk.CTkEntry(head_frame, font=('Bold', 10), width=180)
student_email.place(x=110, y=150)

student_course_lb = ctk.CTkLabel(head_frame, text='Student Course:', font=('Bold', 10))
student_course_lb.place(x=0, y=200)

student_course = ctk.CTkEntry(head_frame, font=('Bold', 10), width=180)
student_course.place(x=110, y=200)

resgister_btn = ctk.CTkButton(head_frame, text='Register', font=('Bold', 12), width=90)
resgister_btn.place(x=0, y=250)

update_btn = ctk.CTkButton(head_frame, text='Update', font=('Bold', 12), width=90)
update_btn.place(x=100, y=250)

clear_btn = ctk.CTkButton(head_frame, text='Clear', font=('Bold', 12), width=90, fg_color='dark green', hover_color='green')
clear_btn.place(x=210, y=250)

delete_btn = ctk.CTkButton(head_frame, text='Delete', font=('Bold', 12), width=90, fg_color='dark red', hover_color='red')
delete_btn.place(x=310, y=250)


search_bar_frame = ctk.CTkFrame(root,  width=400, height=50, fg_color='transparent')
search_bar_frame.pack(pady=0)
search_bar_frame.propagate(False)

search_lb = ctk.CTkLabel(search_bar_frame, text='Search Student By ID: ', font=('Bold', 10))
search_lb.pack(anchor=ctk.W)

search_entry = ctk.CTkEntry(search_bar_frame, font=('Bold', 10))
search_entry.pack(anchor=ctk.W)

record_frame = ctk.CTkFrame(root, width=400, height=200)
record_frame.pack(pady=10)
record_frame.pack_propagate(False)

record_lb = ctk.CTkLabel(record_frame, text='Select Record for Delete or Update', font=('Bold', 13))
record_lb.pack(fill=ctk.X)

record_table = ttk.Treeview(record_frame)
record_table.pack(fill=ctk.X, pady=5)

record_table['column'] = ['Id', 'Name', 'Email', 'Courses']

record_table.column('#0', anchor=ctk.W, width=0, stretch=ctk.NO)

record_table.column('Id', anchor=ctk.W, width=0)
record_table.column('Name', anchor=ctk.W, width=0)
record_table.column('Email', anchor=ctk.W, width=0)
record_table.column('Courses', anchor=ctk.W, width=0)

root.mainloop()
