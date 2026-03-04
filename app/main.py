def greet(name: str):
    return f"hello, {name}! Welcome to your GenAI Journey."

if __name__ == "__main__":
    name = input("Enter your Name: ")
    print(greet(name))