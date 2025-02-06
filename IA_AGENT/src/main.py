# Main entry point of the IA_AGENT application

from agent import AIAgent
from utils.helpers import some_utility_function

def main():
    agent = AIAgent()
    # Main logic for running the AI agent
    while True:
        user_input = input("Enter your query: ")
        if user_input.lower() in ['exit', 'quit']:
            break
        response = agent.process_input(user_input)
        print("AI Response:", response)

if __name__ == "__main__":
    main()