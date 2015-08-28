import sys

import addressbook_pb2


def prompt_for_address(person):
  person.id = int(raw_input("Enter person ID number: "))
  person.name = raw_input("Enter person name: ")
  email = raw_input("Enter person email (blank for none): ")
  if email:
    person.email = email

  while True:
    number = raw_input("Enter a phone number (or leave blank to finish): ")
    if not number:
      break

    phone_number = person.phone.add()
    phone_number.number = number

    type = raw_input("Is this a mobile, home, or work phone? ")
    if type == "mobile":
      phone_number.type = addressbook_pb2.Person.MOBILE
    elif type == "home":
      phone_number.type = addressbook_pb2.Person.HOME
    elif type == "work":
      phone_number.type = addressbook_pb2.Person.WORK
    else:
      print("Unknown phone type; leaving as default value.")


if len(sys.argv) != 2:
  print("Usage: %s ADDRESS_BOOK_FILE" % sys.argv[0])
  sys.exit(-1)

address_book = addressbook_pb2.AddressBook()
address_book_file = sys.argv[1]

# Read the existing address book
try:
  with open(address_book_file, "rb") as fd:
    address_book.ParseFromString(fd.read())
except IOError:
  print("Couldn't open file. Creating a new one")

# add an address
prompt_for_address(address_book.person.add())

# write the new address book back to disk
with open(address_book_file, "wb") as fd:
  fd.write(address_book.SerializeToString())
