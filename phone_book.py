import re
import os
# book = {}

book = 0
def create():
  book = {}
  return book


def select():

  return

def add_contact(book):
  if book == 0:
    print('No phonebook, create one')
    return
  name = input('Enter the name: ')
  if name in book:
    print('Name already exists')
    return
  num = input('Enter the no.: ')
  while (re.search(r'01[0,1,2]\d\d\d\d\d\d\d\d',num) == None):
    print('Invalid no.')
    num = input('Enter the no.: ')
  mail = input('Enter the email: ')
  while (re.search(r'[a-z.0-9.A-Z]+@[a-z.0-9]+.com',mail) == None):
    print('Invalid email')
    mail = input('Enter the email: ')
  gender = input('Enter the gender: ')
  while gender != "male" and gender !="female":
    print('Invalid gender')
    gender = input('Enter the gender: ')
  book[name] = [num,mail,gender]
  
  return 1

def modify_contact(book):
  if book == 0:
    print('No phonebook, create one')
    return
  name = input('Enter the name of the contact you want to modify: ')
  if name in book:
    del book[name]
    print('Enter the new data')
    add_contact(book)

  return 1
  
def show_contact(book):
  if book == 0:
    print('No phonebook, create one')
    return
  name = input('Enter the name: ')
  if name in book:
    print(" Name = ",name)
    print(" Phone number = ",book[name][0])
    print(" Email = ",book[name][1])
    print(" Gender = ",book[name][2])
  else:
    print('Not found')
    return



def show_all(book):
  if book == 0:
    print('No phonebook, create one')
    return
  for i in book.keys():
    print("Name = ",i)
    print("Phone number = ",book[i][0])
    print("Email = ",book[i][1])
    print("Gender = ",book[i][2])
    print(' ')
  


  return
def delete_contact():
  if book == 0:
    print('phonebook is empty, create one')
    return
  name = input('Enter the name of the contact you want to delete: ')
  if name in book:
    del book[name]
  else:
    print('Name does not exist')
  return
  
  
def delete_phonebook(book):
  if book == 0:
    print('No phonebook to delete')
    return
  del book
  return 0



while True:
  select = int(input(" 1. Create phone book\n 2. Select phone book\n 3. Add contact\n 4. Modify contact\n 5. Show contact\n 6. Show all contacts\n 7. Delete a contact\n 8. Delete a phone book\n 9. Exit\n"))
  if select == 1:
    book = create()
  elif select == 2:
    select()
  elif select == 3:
    # book['name']   =  input('Enter the name')
    # book['phone']  =  input('Enter th no.')
    # book['email']  =  input('Enter the email')
    # book['gender'] =  input('Enter the gender')
    add_contact(book)
    
  elif select == 4:
    modify_contact(book)
  elif select == 5:
    show_contact(book)
  elif select == 6:
    show_all(book)
  elif select == 7:
    delete_contact()
  elif select == 8:
    book = delete_phonebook(book)
  elif select == 9:
    break
  else:
    print("Invalid number")

