from flask import Flask, render_template, request

app = Flask(__name__)

scam_keywords = ["win money", "lottery", "click this link", "urgent", "free gift", "bank details"]

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        message = request.form["message"]
        if any(word in message.lower() for word in scam_keywords):
            result = "⚠️ Warning: This message might be a SCAM!"
        else:
            result = "✅ This message looks safe."
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)