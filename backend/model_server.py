from flask import Flask, request, jsonify
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

print("Loading Qwen2-0.5B-Instruct for Minitalker…")

tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2-0.5B-Instruct")
model = AutoModelForCausalLM.from_pretrained(
    "Qwen/Qwen2-0.5B-Instruct",
    torch_dtype=torch.float16,
    low_cpu_mem_usage=True
).to("cpu")
model.eval()
# Warm-up to reduce first-token delay
_ = model.generate(
    **tokenizer("Hello", return_tensors="pt"),
    max_new_tokens=1
)


# --------------------------
# Minitalker Personality Layer
# --------------------------


    if "your name" in p:
        return "I’m Minitalker — sarcastic, fast, and built by Shlok Singh."

    if "who made you" in p:
        return "Shlok Singh built me. I’m basically his digital sidekick."

    return None  # means no override → use model

# --------------------------
# API Endpoint
# --------------------------

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    prompt = data.get("prompt", "").strip()

    # Check special rules first
    special_reply = apply_special_rules(prompt)
    if special_reply:
        return jsonify({"response": special_reply})

    # System + user formatting for Qwen chat format
    system_prompt = (
    "You are Minitalker, a helpful but slightly sarcastic AI assistant built by Shlok Singh.\n"
    "You MUST:\n"
    "- reply naturally\n"
    "- stay in context\n"
    "- avoid making up random scenes unless asked\n"
    "- keep responses clean, short, and direct\n"
)


    formatted = f"<|system|>\n{system_prompt}\n<|user|>\n{prompt}\n<|assistant|>\n"

    inputs = tokenizer(formatted, return_tensors="pt")

    with torch.no_grad():
        output_ids = model.generate(
            **inputs,
            max_new_tokens=60,
            do_sample=True,
            temperature=0.85,
            top_p=0.8,
            eos_token_id=tokenizer.eos_token_id,
            repetition_penalty=1.05
        )

    reply = tokenizer.decode(output_ids[0], skip_special_tokens=True)

    # Remove system+user echo Qwen sometimes outputs
    if "<|assistant|>" in reply:
        reply = reply.split("<|assistant|>")[-1].strip()

    return jsonify({"response": reply})


if __name__ == "__main__":
    print("Minitalker is ready.")
    app.run(host="0.0.0.0", port=5000)
