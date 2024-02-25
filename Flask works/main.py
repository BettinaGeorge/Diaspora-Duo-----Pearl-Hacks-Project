from openai import OpenAI
from flask import Flask, render_template, request
client = OpenAI()

app = Flask(__name__)

@app.route('/')
def chatbot():
    return render_template('chatbot.html')

@app.route('/get' , methods=['POST'])
def get_bot_response():
    print(request.form["state_origin"])
    print(request.form["country"])
    print(request.form["language"])

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a travel assistant and buddy called Diaspora that helps foreigners get acquinted with a destination country of their choice. The language of your response is dependent on the language of the user. You give information about countrieS based on Weather,Security Level, exchange rate in comparison to their state of origin, religion, health precautions, language, transportation, food, electricity, tourism,culture change, landscape and visa requirements. You will also have to give the information in the user's language. When you give your response, it should flow concisely from the perspective of a friend. DO NOT specify Weather:, just let it flow"},
            {"role": "user", "content": f"I am from {request.form['state_origin']} and I want to travel to {request.form['country']}. I speak {request.form['language']}. What do I need to know?"}
            
        ]
    )

    print(completion.choices[0].message)

    return render_template('answer.html', answer=completion.choices[0].message.content)
    
if __name__ == '__main__':
    app.run(debug=True)