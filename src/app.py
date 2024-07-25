import os
from dotenv import load_dotenv
from src.chatbot.chatbot_interface import main as chatbot_main

def main():
    print("Starting the application...")
    # Load environment variables from .env file
    load_dotenv()
    
    # Run the chatbot main function
    chatbot_main()

if __name__ == "__main__":
    main()
