import sys

import addressbook_pb2


def list_people(address_book):
  for person in address_book.people:
    print("Person ID: %s" % person.id)
    print("Person name: %s" % person.name)
    if person.HasField('email'):
      print("Person email: %s" % person.email)

    for phone_number in person.phone:
      if phone_number.type == addressbook_pb2.Person.MOBILE:
        print("Mobile phone #: %s" % phone_number.number)
      elif phone_number.type == addressbook_pb2.Person.HOME:
        print("Home phone #: %s" % phone_number.number)
      elif phone_number.type == addressbook_pb2.Person.WORK:
        print("Work phone #: %s" % phone_number.number)
    else:
      print("No phone number found!")


if len(sys.argv) != 2:
  print("Usage: %s ADDRESS_BOOK_FILE" % sys.argv[0])
  sys.exit(-1)

address_book = addressbook_pb2.AddressBook()

with open(sys.argv[1]) as fd:
  address_book.ParseFromString(fd.read())

list_people(address_book)
