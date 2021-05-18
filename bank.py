from tkinter import *
from tkinter import messagebox
import database
import random
import bcrypt
import time

app = Tk()
app.title("Bank Management System")
app.geometry("750x500")
app.config(bg="white")

def login_menu():
      ################### TOP HEADER #######################
      login_header = Frame(app, bg = "#3279a8")
      login_header.place(relwidth=1, relheight=0.25, rely=0)
      login_text = Label(login_header, text = "Login", font=("Bold", 25),bg = "#3279a8", fg="white")
      login_text.place(relwidth = 0.5, relheight = 0.5, relx = 0.25, rely = 0.25)

      ################## MAIN LOGIN FRAME #########################
      main_login_frame = Frame(app, bg = "white")
      main_login_frame.place(relwidth = 1, relheight = 0.73, rely = 0.27 )

      ################# LEFT CONTAINER ###########################

      login_container = LabelFrame(main_login_frame,bg = "white", padx = 10, pady = 10)
      login_container.place(relwidth = 0.75, relheight = 0.75, relx = 0.125, rely = 0.1)

      user_name = Label(login_container, text = "User Name", font=("bold", 15), anchor = W, bg = "white")
      user_name.place(relwidth = 0.5, relheight = 0.15, relx = 0.01, rely = 0.05)

      user_name_entry = Entry(login_container, font = ("bold", 15))
      user_name_entry.place(relwidth = 0.79, relheight = 0.15, relx = 0.01, rely = 0.21)

      user_password = Label(login_container, text = "Password", font=("bold", 15), anchor = W, bg = "white")
      user_password.place(relwidth = 0.5, relheight = 0.15, relx = 0.01, rely = 0.37)

      user_password_entry = Entry(login_container, font = ("bold", 15))
      user_password_entry.place(relwidth = 0.79, relheight = 0.15, relx = 0.01, rely = 0.54)

      user_admin = IntVar()
      is_admin = Checkbutton(login_container, text = "Administrator", font = ("bold", 15), variable = user_admin, anchor = W, bg = "white")
      is_admin.place(relwidth = 0.5, relheight = 0.12, relx = 0.01, rely = 0.7)

      login_button = Button(login_container, text = "Login", font = ("bold", 15), padx = 15, pady = 15, bg = "white", command = lambda: log_in(user_admin.get(),user_name_entry.get(), user_password_entry.get()))
      login_button.place(relwidth = 0.25, relheight = 0.15, relx = 0.01, rely = 0.84)

      clear_button = Button(login_container, text = "Clear", font = ("bold", 15), bg = "white")
      clear_button.place(relwidth = 0.25, relheight = 0.15, relx = 0.28, rely = 0.84)

      exit_button = Button(login_container, text = "Exit", font = ("bold", 15), bg = "white", command = quit_app)
      exit_button.place(relwidth = 0.25, relheight = 0.15, relx = 0.55, rely = 0.84)

      #################### RIGHT CONTAINER ####################

def main_application():

      ################ HEADER FRAME ###########################
      header_frame = Frame(app, bg = "#3279a8")
      header_frame.place(relwidth=1, relheight=0.25, rely=0)
      header_text = Label(header_frame, text = "Welcome", font=("Bold", 25),bg = "#3279a8", fg="white")
      header_text.place(relwidth = 0.5, relheight = 0.5, relx = 0.25, rely = 0.25)

      ############## OPTION FRAME #############################
      option_frame = Frame(app, bg = "#3279a8")
      option_frame.place(relwidth = 1, relheight = 0.1, rely = 0.265)

      transfer_button = Button(option_frame, text = "Transfer", font = ("bold", 15),bg = "white",  command = transfer_page)
      withdraw_button = Button(option_frame, text = "Withdraw", font = ("bold", 15),bg = "white",  command = withdraw_page)
      deposit_button = Button(option_frame, text = "Deposit", font = ("bold", 15),bg = "white",  command = deposit_page)
      trans_history_button = Button(option_frame, text = "History", font = ("bold", 15),bg = "white",  command = trans_history_page)

      transfer_button.place(relwidth = 0.22, relheight = 0.8, relx = 0.01, rely = 0.05)
      withdraw_button.place(relwidth = 0.22, relheight = 0.8, relx = 0.25, rely = 0.05)
      deposit_button.place(relwidth = 0.22, relheight = 0.8, relx = 0.52, rely = 0.05)
      trans_history_button.place(relwidth = 0.22, relheight = 0.8, relx = 0.76, rely = 0.05)

      ############## USER INFROMATION FRAME #######################

      user_info_frame = Frame(app, bg = "white")
      user_info_frame.place(relwidth = 1, relheight = 0.6, rely = 0.37)


      user_info_container = LabelFrame(user_info_frame, text = "Personal Information", font = ("bold", 15), bg = "white")
      user_info_container.place(relwidth = 0.65, relheight = 0.85, relx = 0.05, rely = 0.1)

      Label(user_info_container, text = "Account Number", font = ("bold", 15), bg = "white", anchor  = W).place(
            relwidth = 0.45, relheight = 0.1, relx = 0.01, rely = 0.05
      )
      Label(user_info_container, text = "Account Type", font = ("bold", 15), bg = "white", anchor  = W).place(
            relwidth = 0.45, relheight = 0.1, relx = 0.01, rely = 0.17
      )
      Label(user_info_container, text = "First Name", font = ("bold", 15), bg = "white", anchor  = W).place(
            relwidth = 0.45, relheight = 0.1, relx = 0.01, rely = 0.29
      )
      Label(user_info_container, text = "Last Name", font = ("bold", 15), bg = "white", anchor  = W).place(
            relwidth = 0.45, relheight = 0.1, relx = 0.01, rely = 0.41
      )
      Label(user_info_container, text = "Email", font = ("bold", 15), bg = "white", anchor  = W).place(
            relwidth = 0.45, relheight = 0.1, relx = 0.01, rely = 0.53
      )
      Label(user_info_container, text = "Id Number", font = ("bold", 15), bg = "white", anchor  = W).place(
            relwidth = 0.45, relheight = 0.1, relx = 0.01, rely = 0.65
      )
      Label(user_info_container, text = "Gender", font = ("bold", 15), bg = "white", anchor  = W).place(
            relwidth = 0.45, relheight = 0.1, relx = 0.01, rely = 0.77
      )
      Label(user_info_container, text = "Cell Phone", font = ("bold", 15), bg = "white", anchor  = W).place(
            relwidth = 0.45, relheight = 0.1, relx = 0.01, rely = 0.89
      )

def transfer_page():
      header_frame = Frame(app, bg = "#3279a8")
      header_frame.place(relwidth=1, relheight=0.25, rely=0)
      header_text = Label(header_frame, text = "Transfer Money", font=("Bold", 25),bg = "#3279a8", fg="white")
      header_text.place(relwidth = 0.5, relheight = 0.5, relx = 0.25, rely = 0.25)

      ############## OPTION FRAME #############################
      option_frame = Frame(app, bg = "#3279a8")
      option_frame.place(relwidth = 1, relheight = 0.1, rely = 0.265)

      transfer_button = Button(option_frame, text = "Transfer", font = ("bold", 15),bg = "white",  state = "disabled")
      withdraw_button = Button(option_frame, text = "Withdraw", font = ("bold", 15),bg = "white",  command = withdraw_page)
      deposit_button = Button(option_frame, text = "Deposit", font = ("bold", 15),bg = "white",  command = deposit_page)
      trans_history_button = Button(option_frame, text = "History", font = ("bold", 15),bg = "white",  command = trans_history_page)
      trans_history_button.place(relwidth = 0.22, relheight = 0.8, relx = 0.76, rely = 0.05)

      transfer_button.place(relwidth = 0.22, relheight = 0.8, relx = 0.01, rely = 0.05)
      withdraw_button.place(relwidth = 0.22, relheight = 0.8, relx = 0.25, rely = 0.05)
      deposit_button.place(relwidth = 0.22, relheight = 0.8, relx = 0.52, rely = 0.05)

      main_frame = Frame(app, bg = "white")
      main_frame.place(relwidth = 1, relheight = 0.6, rely = 0.37)

      ################### FROM LABEL FRAME ##################

      from_container = LabelFrame(main_frame, bg = "white", text = "From", font = ("bold", 15))
      from_container.place(relwidth = 0.43, relheight = 0.6, relx = 0.05, rely = 0.15)

      acc_type_list = ["Savings", "Debit", "Credit"]
      acc_type = StringVar()
      acc_type.set(acc_type_list[0])
      drop_menu = OptionMenu(from_container, acc_type, *acc_type_list  )

      account_name_label = Label(from_container, text = "Account", font = ("bold", 15),bg = "white", anchor = W)
      drop_menu.place(relwidth = 0.53, relheight = 0.25, relx = 0.47, rely = 0.05)
      account_name_label.place(relwidth = 0.45, relheight = 0.25, relx = 0.01, rely = 0.05)


      amount = Entry(from_container, font = ("bold", 15))
      currency_sign = Label(from_container, text = "R", font = ("bold", 15), bg = "white")
      comma_separate = Label(from_container, text = ",", font = ("bold", 15),bg = "white", anchor = W)
      decimal_value = Entry(from_container, font = ("bold", 15))

      amount.place(relwidth = 0.5, relheight = 0.23, relx = 0.2, rely = 0.5)
      currency_sign.place(relwidth = 0.15, relheight = 0.25, relx = 0.01, rely = 0.5)
      comma_separate.place(relwidth = 0.05, relheight = 0.25, relx = 0.72, rely = 0.5)
      decimal_value.place(relwidth = 0.15, relheight = 0.25, relx = 0.78, rely = 0.5)


      ############### TO LABEL FRAME ##########################33
      to_container = LabelFrame(main_frame, bg = "white", text = "To", font = ("bold", 15))
      to_container.place(relwidth = 0.43, relheight = 0.6, relx = 0.52, rely = 0.15)

      ref_label = Label(to_container, text = "Reference", font = ("bold", 15), bg = "white", anchor = W)
      ref_entry = Entry(to_container, font = ("bold", 15))

      to_account_label = Label(to_container, text = "Account Number", font = ("bold", 15), bg = "white", anchor = W) 
      to_account_entry = Entry(to_container, font = ("bold", 15))

      ref_label.place(relwidth = 0.5, relheight = 0.2, relx = 0.01, rely = 0.01)
      ref_entry.place(relwidth = 0.75, relheight = 0.2, relx = 0.01, rely = 0.23)
      to_account_label.place(relwidth = 0.5, relheight = 0.2, relx = 0.01, rely = 0.45)
      to_account_entry.place(relwidth = 0.75, relheight = 0.2, relx = 0.01, rely = 0.67)


      #################### BUTTONS ############################

      trans_btn = Button(main_frame, text = "Transfer", font = ("bold", 15))
      clear_btn = Button(main_frame, text = "Clear", font = ("bold", 15))
      back_btn = Button(main_frame, text = "Back", font = ("bold", 15), command = main_application)
      logout_btn = Button(main_frame, text = "Logout", font = ("bold", 15), command = login_menu)

      trans_btn.place(relwidth = 0.2, relheight = 0.1, relx = 0.05, rely = 0.8)
      clear_btn.place(relwidth = 0.21, relheight = 0.1, relx = 0.27, rely = 0.8)
      back_btn.place(relwidth = 0.2, relheight = 0.1, relx = 0.75, rely = 0.8)
      logout_btn.place(relwidth = 0.2, relheight = 0.1, relx = 0.52, rely = 0.8)


def deposit_page():
      header_frame = Frame(app, bg = "#3279a8")
      header_frame.place(relwidth=1, relheight=0.25, rely=0)
      header_text = Label(header_frame, text = "Deposit Money", font=("Bold", 25),bg = "#3279a8", fg="white")
      header_text.place(relwidth = 0.5, relheight = 0.5, relx = 0.25, rely = 0.25)

      ############## OPTION FRAME #############################
      option_frame = Frame(app, bg = "#3279a8")
      option_frame.place(relwidth = 1, relheight = 0.1, rely = 0.265)

      transfer_button = Button(option_frame, text = "Transfer", font = ("bold", 15),bg = "white",  command = transfer_page)
      withdraw_button = Button(option_frame, text = "Withdraw", font = ("bold", 15),bg = "white",  command = withdraw_page)
      deposit_button = Button(option_frame, text = "Deposit", font = ("bold", 15),bg = "white",  state = "disabled")
      trans_history_button = Button(option_frame, text = "History", font = ("bold", 15),bg = "white",  command = trans_history_page)
      
      trans_history_button.place(relwidth = 0.22, relheight = 0.8, relx = 0.76, rely = 0.05)
      transfer_button.place(relwidth = 0.22, relheight = 0.8, relx = 0.01, rely = 0.05)
      withdraw_button.place(relwidth = 0.22, relheight = 0.8, relx = 0.25, rely = 0.05)
      deposit_button.place(relwidth = 0.22, relheight = 0.8, relx = 0.52, rely = 0.05)


      ########################### Label frame  #########################


def withdraw_page():
      header_frame = Frame(app, bg = "#3279a8")
      header_frame.place(relwidth=1, relheight=0.25, rely=0)
      header_text = Label(header_frame, text = "Withdraw Money", font=("Bold", 25),bg = "#3279a8", fg="white")
      header_text.place(relwidth = 0.5, relheight = 0.5, relx = 0.25, rely = 0.25)

      ############## OPTION FRAME #############################
      option_frame = Frame(app, bg = "#3279a8")
      option_frame.place(relwidth = 1, relheight = 0.1, rely = 0.265)

      transfer_button = Button(option_frame, text = "Transfer", font = ("bold", 15),bg = "white",  command = transfer_page)
      withdraw_button = Button(option_frame, text = "Withdraw", font = ("bold", 15),bg = "white",  state = "disabled")
      deposit_button = Button(option_frame, text = "Deposit", font = ("bold", 15),bg = "white",  command = deposit_page)
      trans_history_button = Button(option_frame, text = "History", font = ("bold", 15),bg = "white",  command = trans_history_page)
      
      trans_history_button.place(relwidth = 0.22, relheight = 0.8, relx = 0.76, rely = 0.05)
      transfer_button.place(relwidth = 0.22, relheight = 0.8, relx = 0.01, rely = 0.05)
      withdraw_button.place(relwidth = 0.22, relheight = 0.8, relx = 0.25, rely = 0.05)
      deposit_button.place(relwidth = 0.22, relheight = 0.8, relx = 0.52, rely = 0.05)

      main_frame = Frame(app, bg = "white")
      main_frame.place(relwidth = 1, relheight = 0.6, rely = 0.37)

       ################### FROM LABEL FRAME ##################

      from_container = LabelFrame(main_frame, bg = "white", text = "Withdraw Money", font = ("bold", 15))
      from_container.place(relwidth = 0.9, relheight = 0.75, relx = 0.05, rely = 0.1)


      acc_type_list = ["Savings", "Debit", "Credit"]
      acc_type = StringVar()
      acc_type.set(acc_type_list[0])

      from_label = Label(from_container, text = "From", font = ("bold", 15), anchor = W )
      amt_label = Label(from_container, text = "Amount R", font = ("bold", 15), anchor = W)
      #comma_separate = Label(from_container, text = ",", font = ("bold", 15))
      contact_label = Label(from_container, text = "Contact", font = ("bold", 15), anchor = W)
      reference_label = Label(from_container, text = "Reference", font = ("bold", 15), anchor = W)

      from_label.place(relwidth = 0.45, relheight = 0.15, relx = 0.03, rely = 0.01)
      amt_label.place(relwidth = 0.45, relheight = 0.15, relx = 0.03, rely = 0.19)
      #comma_separate.place(relwidth = 0.9, relheight = 0.75, relx = 0.05, rely = 0.1)
      contact_label.place(relwidth = 0.45, relheight = 0.15, relx = 0.03, rely = 0.37)
      reference_label.place(relwidth = 0.45, relheight = 0.15, relx = 0.03, rely = 0.55)

      amt_entry = Entry(from_container, font = ("bold", 15))
      contact_entry = Entry(from_container, font = ("bold", 15))
      reference_entry = Entry(from_container, font = ("bold", 15))
      drop_menu = OptionMenu(from_container, acc_type, *acc_type_list  )

      drop_menu.place(relwidth = 0.45, relheight = 0.15, relx = 0.52, rely = 0.01)
      amt_entry.place(relwidth = 0.45, relheight = 0.15, relx = 0.52, rely = 0.19)
      contact_entry.place(relwidth = 0.45, relheight = 0.15, relx = 0.52, rely = 0.37)
      reference_entry.place(relwidth = 0.45, relheight = 0.15, relx = 0.52, rely = 0.55)

      withdraw_button = Button(from_container,text = "Withdraw", font = ("bold", 15))
      withdraw_button.place(relwidth = 0.2, relheight = 0.15, relx = 0.77, rely = 0.75)

def trans_history_page():
      header_frame = Frame(app, bg = "#3279a8")
      header_frame.place(relwidth=1, relheight=0.25, rely=0)
      header_text = Label(header_frame, text = "Transaction History", font=("Bold", 25),bg = "#3279a8", fg="white")
      header_text.place(relwidth = 0.5, relheight = 0.5, relx = 0.25, rely = 0.25)

      option_frame = Frame(app, bg = "#3279a8")
      option_frame.place(relwidth = 1, relheight = 0.1, rely = 0.265)

      transfer_button = Button(option_frame, text = "Transfer", font = ("bold", 15),bg = "white",  command = transfer_page)
      withdraw_button = Button(option_frame, text = "Withdraw", font = ("bold", 15), bg = "white" )
      deposit_button = Button(option_frame, text = "Deposit", font = ("bold", 15),bg = "white",  command = deposit_page)
      trans_history_button = Button(option_frame, text = "History", font = ("bold", 15), bg = "white",  command = trans_history_page, state = "disabled")
      
      trans_history_button.place(relwidth = 0.22, relheight = 0.8, relx = 0.76, rely = 0.05)
      transfer_button.place(relwidth = 0.22, relheight = 0.8, relx = 0.01, rely = 0.05)
      withdraw_button.place(relwidth = 0.22, relheight = 0.8, relx = 0.25, rely = 0.05)
      deposit_button.place(relwidth = 0.22, relheight = 0.8, relx = 0.52, rely = 0.05)


def admin_menu():
      header_frame = Frame(app, bg = "#3279a8")
      header_frame.place(relwidth=1, relheight=0.25, rely=0)
      header_text = Label(header_frame, text = "Administrator", font=("Bold", 25),bg = "#3279a8", fg="white")
      header_text.place(relwidth = 0.5, relheight = 0.5, relx = 0.25, rely = 0.25)

      ############## OPTION FRAME #############################
      option_frame = Frame(app, bg = "#3279a8")
      option_frame.place(relwidth = 1, relheight = 0.1, rely = 0.265)

      add_user_button = Button(option_frame, text = "Add Client", font = ("bold", 15), bg = "white", state = DISABLED)
      delete_user_button = Button(option_frame, text = "Remove Client", font = ("bold", 15), bg = "white", command = withdraw_page)
      update_user_button = Button(option_frame, text = "Update Client", font = ("bold", 15), bg = "white", command = deposit_page)
      more_button = Button(option_frame, text = "More", font = ("bold", 15), bg = "white", command = trans_history_page)

      add_user_button.place(relwidth = 0.22, relheight = 0.8, relx = 0.01, rely = 0.05)
      delete_user_button.place(relwidth = 0.22, relheight = 0.8, relx = 0.25, rely = 0.05)
      update_user_button.place(relwidth = 0.22, relheight = 0.8, relx = 0.52, rely = 0.05)
      more_button.place(relwidth = 0.22, relheight = 0.8, relx = 0.76, rely = 0.05)

      admin_info_frame = Frame(app, bg = "white")
      admin_info_frame.place(relwidth = 1, relheight = 0.6, rely = 0.37)

      ################ PERSONAL INFORMATION LABELS #############################
      Label(admin_info_frame, text = "First Name", font = ("bold", 15), anchor = W).place(
            relwidth = 0.45, relheight = 0.1, relx = 0.02, rely = 0.01
      )
      Label(admin_info_frame, text = "Last Name", font = ("bold", 15), anchor = W).place(
            relwidth = 0.45, relheight = 0.1, relx = 0.52, rely = 0.01
      )
      Label(admin_info_frame, text = "Email", font = ("bold", 15), anchor = W).place(
            relwidth = 0.45, relheight = 0.1, relx = 0.02, rely = 0.25
      )
      Label(admin_info_frame, text = "Id Number", font = ("bold", 15), anchor = W).place(
            relwidth = 0.45, relheight =0.1, relx = 0.52, rely = 0.25
      )
      Label(admin_info_frame, text = "Cell Phone Number", font = ("bold", 15), anchor = W).place(
            relwidth = 0.45, relheight = 0.1, relx = 0.02, rely = 0.51
      )
      Label(admin_info_frame, text = "Gender", font = ("bold", 15), anchor = W).place(
            relwidth = 0.45, relheight = 0.1, relx = 0.52, rely = 0.51
      )
      Label(admin_info_frame, text = "Password", font = ("bold", 15), anchor = W).place(
            relwidth = 0.45, relheight = 0.1, relx = 0.02, rely = 0.74
      )

      first_name_entry = Entry(admin_info_frame, font = ("bold", 15))
      last_name_enrty = Entry(admin_info_frame, font = ("bold", 15))
      email_entry = Entry(admin_info_frame, font = ("bold", 15))
      id_num_entry = Entry(admin_info_frame, font = ("bold", 15))
      cell_fone_entry = Entry(admin_info_frame, font = ("bold", 15))
      pass_word = Entry(admin_info_frame, font = ("bold", 15))
      re_pass_word = Entry(admin_info_frame, font = ("bold", 15))

      first_name_entry.place(relwidth = 0.45, relheight = 0.1, relx = 0.02, rely = 0.13)
      last_name_enrty.place(relwidth = 0.45, relheight = 0.1, relx = 0.52, rely = 0.13)
      email_entry.place(relwidth = 0.45, relheight = 0.1, relx = 0.02, rely = 0.36)
      id_num_entry.place(relwidth = 0.45, relheight = 0.1, relx = 0.52, rely = 0.36)
      cell_fone_entry.place(relwidth = 0.45, relheight = 0.1, relx = 0.02, rely = 0.63)
      pass_word.place(relwidth = 0.45, relheight = 0.1, relx = 0.02, rely = 0.85)
      re_pass_word.place(relwidth = 0.45, relheight = 0.1, relx = 0.52, rely = 0.74)

      g_var = StringVar()
      g_var.set("Unkown")
      gender = OptionMenu(admin_info_frame, g_var, "Male", "Female")
      gender.place( relwidth = 0.45, relheight = 0.1, relx = 0.52, rely = 0.63)

      submit_Button = Button(admin_info_frame, text = "Submit", font = ("bold", 15),fg = "white", bg = "#3279a8", command = lambda: adding_new_user(id_num_entry.get() ,first_name_entry.get(), last_name_enrty.get(), email_entry.get(), g_var.get(), cell_fone_entry.get(), pass_word.get(), re_pass_word.get()))
      submit_Button.place(relwidth = 0.2, relheight = 0.1, relx = 0.77, rely = 0.87)

def verify_user_info(id_number, first_name, last_name, email, gender, cell_phone):
      pass

def encrypt_password(pass_word):
      pass_w = (str(pass_word)).encode("utf-8")
      pass_word = bcrypt.hashpw(pass_w, bcrypt.gensalt())
      return pass_word

def vefify_password(pass_word, hashed_pass):
      if bcrypt.checkpw(pass_word, hashed_pass):
            return True
      else:
            return False

def submit_to_database():
      pass

def adding_new_user(id_number, first_name, last_name, email, gender, cell_phone, pass_word, re_pass_word):
      if pass_word == re_pass_word:
            hashed_password = encrypt_password(pass_word)
            print("hashed " + str(hashed_password))
            tops = Toplevel()
            tops.title("Account Details")
            tops.geometry("500x300")
            tops.config(bg = "white")

            header_frame = Frame(tops, bg = "#3279a8")
            header_frame.place(relwidth = 0.9, relheight = 0.15, relx = 0.05, rely = 0.05)
            Label(header_frame, text = "Account Details", font = ("bold", 23), bg = "#3279a8", fg = "white").place(
                  relwidth = 0.5, relheight = 0.5, relx = 0.25, rely = 0.25
            )
            main_info_menu = LabelFrame(tops, text = "Account Information", font = ("bold", 15), bg= "white")
            main_info_menu.place(relwidth = 0.9, relheight = 0.73, relx = 0.05, rely = 0.25)

            Label(main_info_menu, text = "Account Number", font = ("bold", 15), bg= "white", anchor = W).place(
                  relwidth = 0.45, relheight = 0.2, relx = 0.01, rely = 0.02
            )
            Label(main_info_menu, text = "Account Type", font = ("bold", 15), bg= "white", anchor = W).place(
                  relwidth = 0.45, relheight = 0.2, relx = 0.01, rely = 0.24
            )
            Label(main_info_menu, text = "Login UserName", font = ("bold", 15), bg= "white", anchor = W).place(
                  relwidth = 0.45, relheight = 0.2, relx = 0.01, rely = 0.45
            )

            acc_type_list = ["Savings", "Debit", "Credit"]
            a_var = StringVar()
            a_var.set("Unknown")
            user_account_number = "6200992020" + str(random.randint(100, 999))
            Label(main_info_menu, text = user_account_number, font = ("bold", 15), bg= "white", anchor = W).place(
                  relwidth = 0.45, relheight = 0.2, relx = 0.5, rely = 0.02
            )
            OptionMenu(main_info_menu, a_var, *acc_type_list).place(relwidth = 0.45, relheight = 0.2, relx = 0.5, rely = 0.24)
            user_name_entry = Entry(main_info_menu, font = ("bold", 15))
            user_name_entry.place(relwidth = 0.45, relheight = 0.2, relx = 0.5, rely = 0.45)
            submit_Button = Button(main_info_menu, text = "Submit", font = ("bold", 15), bg = "#3279a8", fg = "white")
            submit_Button.place(relwidth = 0.25, relheight = 0.2, relx = 0.73, rely = 0.75, commad = lambda: submit_to_database())

      else:
            messagebox.showerror("Incorrect Password", "Password do not match!!")
      
def log_in(is_admin, user_name, pass_word):
      if is_admin == 0:
            if(user_name == "pfano"):
                  main_application()
            else:
                  messagebox.showerror("Invalid Login", "Invalid Login")
      else:
            admin_menu()

def quit_app():
      response = messagebox.askokcancel("Exit", "Do you want to Exit")
      if response == True:
            app.quit()

if __name__=="__main__":
      login_menu()


app.mainloop()
