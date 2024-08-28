from flask import Flask, render_template, request, jsonify
import google.generativeai as genai


app = Flask(__name__)

# Configure API key
genai.configure(api_key="AIzaSyA_akOlIRf3LKC-RZybFAf-AYw1Q4MvFq0")

# Create the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

chat_session = model.start_chat(history=[])

def jarvis_response(user_input):
    user_input = user_input.lower()
    
    patterns = [
        "who are you", "who are u", "who r u", "who r you", "who is you",
        "who's this", "who's you", "wru", "whr u", "whos u", "whos you",
        "whois u", "whois you", "what's your name", "who am i talking to",
        "who's on the line", "who's on the screen", "who's behind this",
        "who's behind the screen", "who's the one", "who's the bot", "who's the ai",
        "wut r u", "wat r u", "whas r u", "whut r u", "wuts r u", "yur", "ur", "nam",
        "wut r u called", "wat r u called"
    ]

    for pattern in patterns:
        if pattern == user_input:
            return "I'm Jarvis, your personal assistant"
    
    name_statements = [
        "what is your name", "what's your name", "who are you", "what's your username",
        "what do they call you", "what's your handle", "what's your moniker",
        "what's your designation", "what's your title", "what's your label",
        "what's your identifier", "what's your tag", "what's your nickname",
        "what's your alias", "what's your pseudonym", "what's your screen name",
        "what's your login name", "what's your identity", "what's your persona",
        "what's your character", "wut's ur name", "wat's ur name", "whas ur name",
        "whut's ur name", "wuts ur name", "yur name", "ur name", "nam",
        "wut r u called", "wat r u called"
    ]

    for statement in name_statements:
        if statement == user_input:
            return "I'm Jarvis, your personal assistant"

    creator = [
        "who made you", "who made u", "who created u", "who created you",
        "who developed u", "who developed you", "who built you", "who built u",
        "who designed you", "who designed u", "who programmed you", "who programmed u",
        "who wrote you", "who wrote u", "who is your creator", "who is ur creator",
        "who is your maker", "who is ur maker", "who is your developer", "who is ur developer"
    ]

    for cre in creator:
        if cre == user_input:
            return "I was created by Fahim"

    if any(phrase in user_input for phrase in ["quit", "bye", "bye bye", "tata", "good bye", "good night", "ok talk to you later"]):
        return "Goodbye!"

    response = chat_session.send_message(user_input)
    return response.text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = jarvis_response(user_input)
    
    # Return the chatbot response as JSON
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
