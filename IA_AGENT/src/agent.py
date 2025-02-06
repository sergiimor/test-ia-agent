class AIAgent:
    def __init__(self):
        self.name = "IA Agent"

    def process_input(self, user_input):
        # Process the user input and generate a response
        response = f"Processed input: {user_input}"
        return response

    def generate_response(self, processed_input):
        # Generate a response based on the processed input
        response = f"Response generated for: {processed_input}"
        return response

    def run(self, user_input):
        processed_input = self.process_input(user_input)
        return self.generate_response(processed_input)