
# Wersja z przyciskami

# from flask import Flask, render_template, request, jsonify
# import requests
# import json
# import logging

# app = Flask(__name__)

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)

# # Create console handler and set level to debug
# ch = logging.StreamHandler()
# ch.setLevel(logging.DEBUG)

# # Create formatter
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# # Add formatter to ch
# ch.setFormatter(formatter)

# # Add ch to logger
# logger.addHandler(ch)


# @app.route("/get")
# def get_bot_response():
#     logger.info("enter_bot_res")
#     userText = str(request.args.get('text', default=None, type=str))
#     logger.info(f"userText: {userText}")
#     data = json.dumps({"sender": "Rasa", "message": userText})

#     headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
#     response = requests.post('http://localhost:5005/webhooks/rest/webhook', data=data, headers=headers)

#     respo_json = response.json()
#     logger.info(json.dumps(respo_json))

#     if respo_json:
#         bot_response = respo_json[0]['text']
#     else:
#         bot_response = 'Sorry, I did not understand that.'

#     return jsonify(response=bot_response)


# @app.route('/get', methods=['GET'])
# def get_data():
#     text = request.args.get('text')
#     if text == 'buttons':
#         # Przykładowe dane przycisków
#         buttons = [
#             {"title": "Przycisk 1", "payload": "Opcja 1"},
#             {"title": "Przycisk 2", "payload": "Opcja 2"}
#         ]
#         return jsonify(buttons=buttons)
#     else:
#         # Inna logika przetwarzania żądania
#         return jsonify(response="Odpowiedź od chatbota")


# @app.route("/chatbot_response", methods=['POST'])
# def chatbot_response():
#     msg = request.form["msg"]
#     data = json.dumps({
#         "sender": "Rasa",
#         "message": msg
#     })
#     headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
#     res = requests.post('http://localhost:5005/webhooks/rest/webhook', data=data, headers=headers)
#     res = res.json()
#     resp = []
#     for i in range(len(res)):
#         message = {
#             "text": res[i].get("text")
#         }
#         if res[i].get("buttons"):
#             options = [b.get("title") for b in res[i].get("buttons")]
#             message["options"] = options
#         resp.append(message)
#     result = resp
#     return jsonify(result)


# @app.route("/")
# def home():
#     data = {"test": "test_data"}
#     return render_template("index.html", data=data)


# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, render_template, request, jsonify
import requests
import json
import logging  

app = Flask(__name__)

logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)

# Create console handler and set level to debug
ch = logging.StreamHandler()

ch.setLevel(logging.DEBUG)

# Create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Add formatter to ch
ch.setFormatter(formatter)

# Add ch to logger
logger.addHandler(ch)

@app.route("/")
def home():
    data = {"test": "test_data"}
    return render_template("index.html", data=data)

@app.route("/get")
def get_bot_response():
    logger.info("enter_bot_res")
    userText = str(request.args.get('text', default=None, type=str))
    logger.info(f"userText: {userText}")
    data = json.dumps({"sender": "Rasa", "message": userText})

    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
    response = requests.post('http://localhost:5005/webhooks/rest/webhook', data=data, headers=headers)
    
    respo_json = response.json()
    logger.info(json.dumps(respo_json))

    if respo_json:
        bot_response = respo_json[0]['text']
    else:
        bot_response = 'Sorry, I did not understand that.'

    return jsonify(response=bot_response)


if __name__ == "__main__":
    app.run(debug=True)



# from flask import Flask, render_template, request, jsonify
# import requests
# import json
# import logging

# app = Flask(__name__)

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)

# # Create console handler and set level to debug
# ch = logging.StreamHandler()
# ch.setLevel(logging.DEBUG)

# # Create formatter
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# # Add formatter to ch
# ch.setFormatter(formatter)

# # Add ch to logger
# logger.addHandler(ch)

# selected_language = "english"  # Domyślny język

# @app.route("/")
# def home():
#     data = {"test": "test_data"}
#     return render_template("index.html", data=data)

# @app.route("/set-language")
# def set_language():
#     global selected_language
#     selected_language = request.args.get('language')
#     return jsonify(status="success")
#     # logger.info(json.dumps(selected_language))

# @app.route("/get")
# def get_bot_response():
#     logger.info("enter_bot_res")
#     userText = str(request.args.get('text', default=None, type=str))
#     logger.info(f"userText: {userText}")

#     # # Utwórz obiekt payload w zależności od wybranego języka
#     # payload = {
#     #     "sender": "Rasa",
#     #     "message": userText,
#     #     "language": selected_language
#     # }
#     data = json.dumps(payload)

#     headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
#     response = requests.post('http://localhost:5005/webhooks/rest/webhook', data=data, headers=headers)

#     respo_json = response.json()
#     logger.info(json.dumps(respo_json))


#     if respo_json:
#         bot_response = respo_json[0]['text']
#     else:
#         bot_response = 'Sorry, I did not understand that.'

#     return jsonify(response=bot_response)

# if __name__ == "__main__":
#     app.run(debug=True)
























# from flask import Flask, render_template, request, jsonify
# import requests
# import json
# import logging  

# app = Flask(__name__)

# logger = logging.getLogger(__name__)

# logger.setLevel(logging.DEBUG)

# # Create console handler and set level to debug
# ch = logging.StreamHandler()

# ch.setLevel(logging.DEBUG)

# # Create formatter
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# # Add formatter to ch
# ch.setFormatter(formatter)

# # Add ch to logger
# logger.addHandler(ch)

# @app.route("/")
# def home():
#     data = {"test": "test_data"}
#     return render_template("index.html", data=data)



# @app.route("/get")
# def get_bot_response():
#      logger.info("enter_bot_res")
#      userText = str(request.args.get('text', default=None, type=str))
#      logger.info(f"userText: {userText}")
#      data = json.dumps({"sender": "Rasa", "message": userText})

#      headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
#      response = requests.post('http://localhost:5005/webhooks/rest/webhook', data=data, headers=headers)
    
#      respo_json = response.json()
#      logger.info(json.dumps(respo_json))

#      if respo_json:
#         bot_response = respo_json[0]['text']
#      else:
#         bot_response = 'Sorry, I did not understand that.'

#      return jsonify(response=bot_response)


# if __name__ == "__main__":
#     app.run(debug=True)




# @app.route("/get")
# def get_bot_response():
#     logger.info("enter_bot_res")
#     userText = str(request.args.get('text', default=None, type=str))
#     logger.info(f"userText: {userText}")
#     data = json.dumps({"sender": "Rasa", "message": userText})

#     headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
#     response = requests.post('http://localhost:5005/webhooks/rest/webhook', data=data, headers=headers)
    
#     respo_json = response.json()
#     logger.info(json.dumps(respo_json))

#     if respo_json:
#         bot_response = respo_json[0]['text']
#     else:
#         bot_response = 'Sorry, I did not understand that.'

#     return jsonify(response=bot_response)


# if __name__ == "__main__":
#     app.run(debug=True)






