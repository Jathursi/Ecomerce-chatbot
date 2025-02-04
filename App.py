# # # # from flask import Flask, render_template, request
# # # # import torch
# # # # import random
# # # # import json
# # # # import mysql.connector
# # # # from nltk_utils import tokenize, bag_of_words
# # # # from model import NeuralNet

# # # # app = Flask(__name__)

# # # # # Load your intents JSON file
# # # # with open('intents.json', 'r') as f:
# # # #     intents = json.load(f)

# # # # # Load your chatbot model
# # # # device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
# # # # data = torch.load('data.pth')  # Load the trained model file

# # # # input_size = data["input_size"]
# # # # hidden_size = data["hidden_size"]
# # # # output_size = data["output_size"]
# # # # all_words = data['all_words']
# # # # tags = data['tags']
# # # # model_state = data["model_state"]

# # # # model = NeuralNet(input_size, hidden_size, output_size).to(device)
# # # # model.load_state_dict(model_state)
# # # # model.eval()

# # # # # Database connection
# # # # db = mysql.connector.connect(
# # # #     host="localhost",
# # # #     user="root",
# # # #     password="",
# # # #     database="chatbot"
# # # # )
# # # # cursor = db.cursor()

# # # # def get_response(msg):
# # # #     sentence = tokenize(msg)
# # # #     X = bag_of_words(sentence, all_words)
# # # #     X = torch.from_numpy(X).to(device)

# # # #     output = model(X)
    
# # # #     # Check the shape of output
# # # #     print("Output shape:", output.shape)

# # # #     # Check if output is a 2D tensor, then perform the operation
# # # #     if len(output.shape) == 2:
# # # #         _, predicted = torch.max(output, dim=1)
# # # #     else:
# # # #         # In case the output has an unexpected shape (e.g., 1D)
# # # #         predicted = torch.argmax(output)
    
# # # #     tag = tags[predicted.item()]

# # # #     # Find the corresponding intent and pick a random response
# # # #     for intent in intents['intents']:
# # # #         if tag == intent['tag']:
# # # #             response = random.choice(intent['responses'])
# # # #             return response
# # # #     return "Sorry, I didn't understand that."

# # # # # Create routes
# # # # @app.route("/")
# # # # def home():
# # # #     return render_template("index.html")

# # # # @app.route("/get", methods=["POST"])
# # # # def chatbot_response():
# # # #     user_message = request.form["msg"]
    
# # # #     # Check if the question already exists in the database
# # # #     cursor.execute("SELECT COUNT(*) FROM questions WHERE question = %s", (user_message,))
# # # #     result = cursor.fetchone()
    
# # # #     if result[0] == 0:
# # # #         # Store the question in the database if it doesn't exist
# # # #         cursor.execute("INSERT INTO questions (question) VALUES (%s)", (user_message,))
# # # #         db.commit()
    
# # # #     response = get_response(user_message)
# # # #     return response

# # # # if __name__ == "__main__":
# # # #     app.run(debug=True)


# # # from flask import Flask, render_template, request, jsonify
# # # import torch
# # # import random
# # # import json
# # # import mysql.connector
# # # from nltk_utils import tokenize, bag_of_words
# # # from model import NeuralNet

# # # app = Flask(__name__)

# # # # Load your intents JSON file
# # # with open('intents.json', 'r') as f:
# # #     intents = json.load(f)

# # # # Load your chatbot model
# # # device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
# # # data = torch.load('data.pth')  # Load the trained model file

# # # input_size = data["input_size"]
# # # hidden_size = data["hidden_size"]
# # # output_size = data["output_size"]
# # # all_words = data['all_words']
# # # tags = data['tags']
# # # model_state = data["model_state"]

# # # model = NeuralNet(input_size, hidden_size, output_size).to(device)
# # # model.load_state_dict(model_state)
# # # model.eval()

# # # # Database connection
# # # db = mysql.connector.connect(
# # #     host="localhost",
# # #     user="root",
# # #     password="",
# # #     database="chatbot"
# # # )
# # # cursor = db.cursor()

# # # def get_response(msg):
# # #     sentence = tokenize(msg)
# # #     X = bag_of_words(sentence, all_words)
# # #     X = torch.from_numpy(X).to(device)

# # #     output = model(X)
    
# # #     # Check if output is a 2D tensor
# # #     if len(output.shape) == 2:
# # #         _, predicted = torch.max(output, dim=1)
# # #     else:
# # #         predicted = torch.argmax(output)
    
# # #     tag = tags[predicted.item()]

# # #     # Find the corresponding intent and pick a random response
# # #     for intent in intents['intents']:
# # #         if tag == intent['tag']:
# # #             response = random.choice(intent['responses'])
# # #             return response
# # #     return "Sorry, I didn't understand that."

# # # # Create routes
# # # @app.route("/")
# # # def home():
# # #     return render_template("index.html", intents=intents)

# # # @app.route("/get", methods=["POST"])
# # # def chatbot_response():
# # #     user_message = request.form["msg"]
    
# # #     # Check if the question already exists in the database
# # #     cursor.execute("SELECT COUNT(*) FROM questions WHERE question = %s", (user_message,))
# # #     result = cursor.fetchone()
    
# # #     if result[0] == 0:
# # #         # Store the question in the database if it doesn't exist
# # #         cursor.execute("INSERT INTO questions (question) VALUES (%s)", (user_message,))
# # #         db.commit()
    
# # #     response = get_response(user_message)
# # #     return response

# # # if __name__ == "__main__":
# # #     app.run(debug=True)


# # from flask import Flask, render_template, request, jsonify
# # import torch
# # import random
# # import json
# # import mysql.connector
# # from nltk_utils import tokenize, bag_of_words
# # from model import NeuralNet

# # app = Flask(__name__)

# # # Load your intents JSON file
# # with open('intents.json', 'r') as f:
# #     intents = json.load(f)

# # # Load your chatbot model
# # device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
# # data = torch.load('data.pth')  # Load the trained model file

# # input_size = data["input_size"]
# # hidden_size = data["hidden_size"]
# # output_size = data["output_size"]
# # all_words = data['all_words']
# # tags = data['tags']
# # model_state = data["model_state"]

# # model = NeuralNet(input_size, hidden_size, output_size).to(device)
# # model.load_state_dict(model_state)
# # model.eval()

# # # Database connection
# # db = mysql.connector.connect(
# #     host="localhost",
# #     user="root",
# #     password="",
# #     database="ecommerce"
# # )
# # cursor = db.cursor()

# # def get_response(msg):
# #     sentence = tokenize(msg)
# #     X = bag_of_words(sentence, all_words)
# #     X = torch.from_numpy(X).to(device)

# #     output = model(X)
    
# #     # Check if output is a 2D tensor
# #     if len(output.shape) == 2:
# #         _, predicted = torch.max(output, dim=1)
# #     else:
# #         predicted = torch.argmax(output)
    
# #     tag = tags[predicted.item()]

# #     # Find the corresponding intent and pick a random response
# #     for intent in intents['intents']:
# #         if tag == intent['tag']:
# #             response = random.choice(intent['responses'])
# #             return response
# #     return "Sorry, I didn't understand that."

# # # Filter patterns based on the tags to exclude greeting, goodbye, and thanks
# # def get_suggested_questions():
# #     suggestions = []
# #     for intent in intents['intents']:
# #         if intent['tag'] not in ['greeting', 'goodbye', 'thanks']:  # Exclude these tags
# #             suggestions.extend(intent['patterns'])  # Add the patterns from the intent
# #     return suggestions

# # # Create routes
# # @app.route("/")
# # def home():
# #     suggested_questions = get_suggested_questions()
# #     return jsonify({"intents": intents, "suggested_questions": suggested_questions})

# # @app.route("/get", methods=["POST"])
# # def chatbot_response():
# #     user_message = request.form["msg"]
    
# #     # Check if the question already exists in the database
# #     cursor.execute("SELECT COUNT(*) FROM questions WHERE question = %s", (user_message,))
# #     result = cursor.fetchone()
    
# #     if result[0] == 0:
# #         # Store the question in the database if it doesn't exist
# #         cursor.execute("INSERT INTO questions (question) VALUES (%s)", (user_message,))
# #         db.commit()
    
# #     response = get_response(user_message)
# #     return response

# # # if __name__ == "__main__":
# # #     app.run(debug=True)


# from flask import Flask, request, jsonify
# import torch
# import random
# import json
# import mysql.connector
# from nltk_utils import tokenize, bag_of_words
# from model import NeuralNet

# app = Flask(__name__)

# # Load your intents JSON file
# with open('intents.json', 'r') as f:
#     intents = json.load(f)

# # Load your chatbot model
# device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
# data = torch.load('data.pth')  # Load the trained model file

# input_size = data["input_size"]
# hidden_size = data["hidden_size"]
# output_size = data["output_size"]
# all_words = data['all_words']
# tags = data['tags']
# model_state = data["model_state"]

# model = NeuralNet(input_size, hidden_size, output_size).to(device)
# model.load_state_dict(model_state)
# model.eval()

# # Database connection
# db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="ecommerce"
# )
# cursor = db.cursor()

# def get_response(msg):
#     sentence = tokenize(msg)
#     X = bag_of_words(sentence, all_words)
#     X = torch.from_numpy(X).to(device)

#     output = model(X)
    
#     # Check if output is a 2D tensor
#     if len(output.shape) == 2:
#         _, predicted = torch.max(output, dim=1)
#     else:
#         predicted = torch.argmax(output)
    
#     tag = tags[predicted.item()]

#     # Find the corresponding intent and pick a random response
#     for intent in intents['intents']:
#         if tag == intent['tag']:
#             response = random.choice(intent['responses'])
#             return response
#     return "Sorry, I didn't understand that."

# # Filter patterns based on the tags to exclude greeting, goodbye, and thanks
# def get_suggested_questions():
#     suggestions = []
#     for intent in intents['intents']:
#         if intent['tag'] not in ['greeting', 'goodbye', 'thanks']:  # Exclude these tags
#             suggestions.extend(intent['patterns'])  # Add the patterns from the intent
#     return suggestions

# # Create routes
# @app.route("/")
# def home():
#     suggested_questions = get_suggested_questions()
#     return jsonify({"intents": intents, "suggested_questions": suggested_questions})

# @app.route("/get", methods=["POST"])
# def chatbot_response():
#     user_message = request.form["msg"]
    
#     # Check if the question already exists in the database
#     cursor.execute("SELECT COUNT(*) FROM question WHERE question = %s", (user_message,))
#     result = cursor.fetchone()
    
#     if result[0] == 0:
#         # Store the question in the database if it doesn't exist
#         cursor.execute("INSERT INTO question (question) VALUES (%s)", (user_message,))
#         db.commit()
    
#     response = get_response(user_message)
#     return jsonify({"response": response})

# if __name__ == "__main__":
#     app.run(port=5000, debug=True)

from flask import Flask, request, jsonify
from flask_cors import CORS
import torch
import random
import json
import mysql.connector
from nltk_utils import tokenize, bag_of_words
from model import NeuralNet

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load your intents JSON file
with open('intents.json', 'r') as f:
    intents = json.load(f)

# Load your chatbot model
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
data = torch.load('data.pth')  # Load the trained model file

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="ecommerce"
)
cursor = db.cursor()

def get_response(msg):
    sentence = tokenize(msg)
    X = bag_of_words(sentence, all_words)
    X = torch.from_numpy(X).to(device)

    output = model(X)
    
    # Check if output is a 2D tensor
    if len(output.shape) == 2:
        _, predicted = torch.max(output, dim=1)
    else:
        predicted = torch.argmax(output)
    
    tag = tags[predicted.item()]

    # Find the corresponding intent and pick a random response
    for intent in intents['intents']:
        if tag == intent['tag']:
            response = random.choice(intent['responses'])
            return response
    return "Sorry, I didn't understand that."

# Filter patterns based on the tags to exclude greeting, goodbye, and thanks
def get_suggested_questions():
    suggestions = []
    for intent in intents['intents']:
        if intent['tag'] not in ['greeting', 'goodbye', 'thanks']:  # Exclude these tags
            suggestions.extend(intent['patterns'])  # Add the patterns from the intent
    return suggestions

# Create routes
@app.route("/")
def home():
    suggested_questions = get_suggested_questions()
    return jsonify({"intents": intents, "suggested_questions": suggested_questions})

@app.route("/get", methods=["POST"])
def chatbot_response():
    user_message = request.json.get("msg")  # Get the message from JSON data
    
    # Check if the question already exists in the database
    cursor.execute("SELECT COUNT(*) FROM question WHERE question = %s", (user_message,))
    result = cursor.fetchone()
    
    if result[0] == 0:
        # Store the question in the database if it doesn't exist
        cursor.execute("INSERT INTO question (question) VALUES (%s)", (user_message,))
        db.commit()
    
    response = get_response(user_message)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(port=5000, debug=True)