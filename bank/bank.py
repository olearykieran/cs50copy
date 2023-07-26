greeting = (input("Greeting: "))
new_greeting = greeting.strip().lower()
if new_greeting.startswith("hello"):
    print("$0")
elif new_greeting.startswith("h") and new_greeting != "hello":
    print("$20")
else:
    print("$100")


