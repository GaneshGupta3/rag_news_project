from flask import Flask, request, jsonify
from utils.retriever import retrieve_news 
from utils.generator_llama import generate_llama_response

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    query = data.get("query", "")
    retrieved = retrieve_news(query)
    context = "\n".join(retrieved)
    answer = generate_llama_response(query, context)
    return jsonify({"response": answer})
