#Match case

choice = input("Enter your choice (a/b/c): ")
match choice:
  case 'a':
    print("Your choice is A")
  case 'b':
    print("Your choice is B")
  case 'c':
    print("Your choice is C")
  case _:
    print("Invalid choice")