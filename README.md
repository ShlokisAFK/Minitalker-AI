🧠 Minitalker-AI
Personal Local AI Assistant Running on Raspberry Pi

Minitalker-AI is a lightweight, fully local AI assistant built using a Raspberry Pi 5, a fast Falcon-RW-1B LLM, a Flask backend, and a ChatGPT-style HTML frontend.

It is accessible through a custom domain using NGINX + Cloudflare, features a clean animated UI with typing indicators, auto-expanding input, and a custom-tuned personality.

🚀 Features

🧠 Runs a 1B-parameter LLM locally on Raspberry Pi

⚡ Fast Flask API backend

🎨 Animated gradient UI inspired by ChatGPT

💬 Smooth chat bubbles + animated typing indicator

🧑‍💻 Top-floating input bar (mobile friendly)

📱 Fully responsive mobile layout

🔐 Reverse-proxied behind NGINX + Cloudflare

🔁 Auto-starts on boot via systemd

🌙 Custom AI personality (keyword-triggered)

🌐 Public access via your own domain

🧠 Model Architecture

Minitalker-AI originally used TinyLlama-1.1B-Chat, but testing on the Raspberry Pi 5 (4GB) showed:

slow load times

high RAM usage

freezes during generation

To ensure fast and stable performance, the model was updated to Falcon-RW-1B, a lightweight CPU-friendly model.

Model Comparison
Model	Parameters	Speed on Pi	Stability	Notes
TinyLlama-1.1B-Chat	1.1B	
❌ Slow	❌ Freezes	Too heavy for 4GB Pi
Falcon-RW-1B	
~1B	✅ Fast	✅ Stable	Ideal for CPU inference
Result:
Minitalker loads faster, never freezes, and responds smoothly while staying fully local.
