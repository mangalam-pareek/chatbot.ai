# brain.py

def greet():
    return "Hello! I am Chip. How can I help you today?"


def calculator(command):
    try:
        # remove the word "calculate" and evaluate the expression
        expression = command.replace("calculate", "").strip()
        result = eval(expression)
        return f"The answer is {result}"
    except Exception as e:
        return "Sorry, I couldn't calculate that."


def random_fact():
    return "Did you know? Honey never spoils!"


def askLLM(command):
    return "I don't know that yet, but I'm learning!"
