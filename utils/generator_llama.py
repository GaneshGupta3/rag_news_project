import subprocess
import json

def generate_llama_response(query, context):
    """
    Generates a response from the LLaMA model using Ollama.
    """
    prompt = f"Context:\n{context}\n\nQuestion: {query}\nAnswer:"
    # cmd = ["ollama", "run", "gemma:2b", prompt]
    cmd = ["ollama", "run", "llama3", prompt]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout.strip()


# ✅ Run directly from terminal
if __name__ == "__main__":
    print("🤖 LLaMA Chatbot (via Ollama)")
    print("Type 'exit' to quit.\n")

    while True:
        query = input("You: ").strip()
        if query.lower() == "exit":
            print("👋 Exiting chatbot.")
            break

        # Example context — in your RAG setup, you’ll pass retrieved news instead
        context = (
            "India recently won the cricket test match against Australia, "
            "with Virat Kohli scoring a century and Bumrah taking 5 wickets."
        )

        response = generate_llama_response(query, context)
        print(f"\nLLaMA: {response}\n")