from flask import Flask, render_template, request, jsonify # type: ignore
from flask_socketio import SocketIO, emit # type: ignore
from transformers import pipeline # type: ignore

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

# Load a general-purpose language model
chatbot = pipeline("text-generation", model="gpt2")  # You can also use `chatbot = pipeline("chat")` if available

@app.route("/")
def home():
    return render_template("index.html")

@socketio.on('send_message')
def handle_message(data):
    user_message = data['message']

    # Pass the query directly to the model
    try:
        response = chatbot(user_message, max_length=100, num_return_sequences=1)[0]['generated_text']
    except Exception as e:
        response = "I'm sorry, I couldn't find an answer to that."

    # Emit the response back to the client
    emit('receive_message', {'response': response})

if __name__ == "__main__":
    socketio.run(app, debug=True)
