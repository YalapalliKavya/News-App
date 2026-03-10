from flask import Flask, render_template, request
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")



app = Flask(__name__)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "system", "content": "You are a news summarizer"},
                {"role": "user", "content": "Generate news digest"}
            ]
        )

        result = response.choices[0].message.content
        return render_template("index.html", result=result)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False, port=8000)

