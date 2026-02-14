# Daily-Use AI Chatbot with 40 Common Keywords

responses = {
    # Greetings
    "hello": "Hello! How can I help you?",
    "hi": "Hi there!",
    "hey": "Hey! 😊",
    "hii": "Hello!",
    "hola": "Hello!",

    # Time-based greetings
    "morning": "Good morning ☀️",
    "afternoon": "Good afternoon!",
    "evening": "Good evening 🌆",
    "night": "Good night 🌙",

    # Feelings / status
    "how": "I'm doing great! Thanks for asking 😊",
    "fine": "Nice to hear that!",
    "good": "Glad to know!",
    "okay": "Alright 👍",
    "ok": "Okay 👍",
    "sad": "I'm here for you 💙",
    "happy": "That's awesome 😄",

    # Identity
    "name": "I am an AI chatbot built using Python.",
    "who": "I am a simple chatbot created for an internship.",
    "creator": "I was created by a student during the CODTECH internship.",
    "created": "I was created using Python programming.",

    # Help / capability
    "help": "I can answer basic daily questions.",
    "do": "I can chat with you and answer simple queries.",
    "work": "I work as a rule-based chatbot.",
    "use": "People use me to practice chatbot concepts.",

    # Internship / study
    "internship": "This chatbot is part of the CODTECH internship.",
    "project": "This is a Python NLP mini project.",
    "python": "Python is a powerful and beginner-friendly language.",
    "coding": "Coding is fun and logical!",

    # Polite words
    "thanks": "You're welcome 😊",
    "thank": "Happy to help!",
    "sorry": "No worries 🙂",
    "please": "Sure!",

    # Exit words
    "bye": "Goodbye! Have a great day 👋",
    "exit": "Bye! See you soon 👋",
    "quit": "Chat ended. Take care!",
    "close": "Closing chat. Bye 👋"
}

print("🤖 Chatbot is running (type 'bye' to exit)")

while True:
    user_input = input("You: ").lower()

    tokens = user_input.split()

    if any(word in ["bye", "exit", "quit", "close"] for word in tokens):
        print("Bot:", responses["bye"])
        break

    reply = None
    for word in tokens:
        if word in responses:
            reply = responses[word]
            break

    if reply:
        print("Bot:", reply)
    else:
        print("Bot: Sorry, I didn't understand that.")
