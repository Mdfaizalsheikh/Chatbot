from small_talk import small_talks
from commands import command

def main():
    
    
    print("Welcome to the Interactive Chatbot!")
    small_talks()
    
    while True:
        user = input("You: ")
        if user.lower() in ["quit", "exit"]:
            break
        
        response = command(user) 
        print(f"Bot: {response}")
    
    
    print("Goodbye!")

if __name__ == "__main__":
    main()
