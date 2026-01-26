<h1 align="center">Minitalker-AI</h1>
<p align="center">
Local AI assistant running entirely on a Raspberry Pi
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Local%20Inference-Yes-black" />
  <img src="https://img.shields.io/badge/Raspberry%20Pi-5-black" />
  <img src="https://img.shields.io/badge/LLM-Falcon--RW--1B-black" />
  <img src="https://img.shields.io/badge/Backend-Flask-black" />
</p>

<hr/>

<p align="center">
A lightweight, fully local AI assistant designed for stability and continuous operation on low-power hardware.
</p>

---

## Demo

<p align="center">
  <img src="demo.gif" width="800" />
</p>

<sub align="center">
Chat interface running on-device with local inference
</sub>

---

## Overview

Minitalker-AI is a personal AI assistant built to run entirely on a Raspberry Pi 5 without relying on external inference APIs.

The system exposes a Flask-based API and serves a web-based chat interface inspired by modern conversational UIs. All inference happens locally, while NGINX and Cloudflare are used only for routing and public access.

---

## Architecture

<p align="center">
  <img src="architecture.png" width="700" />
</p>

- Local LLM inference on Raspberry Pi  
- Flask API for prompt handling  
- Web-based chat frontend  
- NGINX reverse proxy  
- Cloudflare for DNS and HTTPS  

---

## Model Selection

The project initially used TinyLlama-1.1B-Chat. Testing on Raspberry Pi 5 (4GB RAM) revealed performance limitations, including long load times and memory pressure.

The model was later replaced with Falcon-RW-1B to improve responsiveness and runtime stability on CPU-only hardware.

This change significantly reduced latency and improved generation reliability.

---

## Features

- Fully local language model inference  
- Lightweight Flask backend  
- Responsive chat interface  
- Animated message flow and typing indicator  
- Mobile-friendly layout  
- Reverse-proxied with NGINX  
- Public access through custom domain  
- Auto-start on boot using systemd  
- Custom personality logic  

---

## Why This Exists

This project explores what is realistically possible when running modern language models on constrained hardware.

The focus is not maximum model size, but reliability, simplicity, and local-first design.

---

## Running Locally

```bash
git clone https://github.com/ShlokisAFK/Minitalker-AI
cd Minitalker-AI
python app.py
