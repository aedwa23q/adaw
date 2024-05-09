from flask import Flask
from key import KEY
from openai import OpenAI

app = Flask(__name__)
client = OpenAI(api_key=KEY)


@app.route('/')
def hello_world():
    stream = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": "Say this is a test"}],
        stream=True,
    )
    return str(stream)


if __name__ == '__main__':
    app.run()
