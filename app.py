from flask import Flask, render_template, request, make_response
from google import genai

app = Flask(__name__)

def process_text(action, text, api_key):
    """Perform different actions based on button clicked"""
    client = genai.Client(api_key=api_key)
    
    if action == "rephrase":
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents="only rephrase this dont give anything infront or back just give what i asked for here is the text : " + text
        )
        return response.text.strip()
    elif action == "refine":
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents="only refine this dont give anything infront or back just give what i asked for here is the text : " + text
        )
        return response.text.strip()
    elif action == "summarize":
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents="only summarize this dont give anything infront or back just give what i asked for here is the text : "+text
        )
        return response.text.strip()
    elif action == "expand":
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents="only expand this dont give anything infront or back just give what i asked for here is the text : "+text
        )
        return response.text.strip()
    elif action == "rewrite":
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents="only rewrite this dont give anything infront or back just give what i asked for here is the text : "+text
        )
        return response.text.strip()
    return text

@app.route('/')
def index():
    api_key = request.cookies.get('api_key', '')  # Default to empty if not set
    return render_template('index.html', result="", api_key=api_key)

@app.route('/process', methods=['POST'])
def process():
    text = request.form.get("text")
    action = request.form.get("action")
    api_key = request.form.get("api_key")

    if not text:
        return render_template('index.html', result="Error: No text provided", api_key=api_key)

    # Save the API key in a cookie
    resp = make_response(render_template('index.html', result=process_text(action, text, api_key), api_key=api_key))
    resp.set_cookie('api_key', api_key)

    return resp

if __name__ == '__main__':
    app.run(debug=True)
