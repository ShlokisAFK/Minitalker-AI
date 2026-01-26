# Minitalker-AI

<p align="center">
  <strong>Local AI assistant running entirely on a Raspberry Pi</strong><br>
  No cloud inference • No external APIs • Always-on
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Inference-Local--only-black">
  <img src="https://img.shields.io/badge/Model-Falcon--RW--1B-blue">
  <img src="https://img.shields.io/badge/Backend-Flask-lightgrey">
  <img src="https://img.shields.io/badge/Hardware-Raspberry%20Pi%205-red">
</p>

---

## Overview

**Minitalker-AI** is a fully local AI assistant designed to run continuously on low-power hardware.  
It provides a browser-based chat interface backed by on-device language model inference, without relying on external APIs or cloud compute.

The project focuses on **stability**, **predictable performance**, and **long-term reliability** rather than model size or novelty.

---

## Demo

> Chat interface running locally with on-device inference

- Chat-style conversational UI  
- Animated typing indicator  
- Smooth message flow  
- Mobile-friendly layout
- https://server.defaultrpi.xyz/

---

## Design Goals

- Local-first by default  
- Low memory footprint  
- Predictable latency  
- Simple, debuggable architecture  
- Designed for continuous uptime  

---

## Architecture

Browser
->
NGINX (Reverse Proxy)
->
Flask API
->
Local LLM (CPU inference)


### Components

- **Language Model**
  - Runs fully on Raspberry Pi CPU
  - No GPU required
  - Optimized for constrained hardware

- **Backend**
  - Flask-based REST API
  - Handles prompt routing and response streaming

- **Frontend**
  - HTML / CSS / JavaScript
  - Chat-style interface inspired by modern conversational apps
  - Responsive across desktop and mobile

- **Networking**
  - NGINX for reverse proxy
  - Cloudflare for DNS and HTTPS only
  - No inference leaves the device

---

## Model Selection

The project initially used **TinyLlama-1.1B-Chat**, but testing on Raspberry Pi 5 (4GB) revealed:

- Slow load times  
- High RAM usage  
- Occasional generation stalls  

To improve real-world usability, the model was switched to **qwen2.gguf**, resulting in:

- Faster CPU inference  
- Lower memory pressure  
- Improved stability during long sessions  

This change significantly improved responsiveness and reliability.

---

## Features

- Fully local language model inference  
- Lightweight Flask backend  
- Modern chat interface  
- Smooth message animations and typing indicator  
- Mobile-friendly responsive layout  
- Reverse-proxied with NGINX  
- HTTPS via Cloudflare  
- Public access through custom domain  
- Auto-start on boot using systemd  
- Custom personality logic  

---

## Why This Project Exists

Most AI projects assume cloud compute, large GPUs, or paid APIs.  
Minitalker-AI explores a different direction:

> What is realistically possible with local AI on constrained hardware?

The result is a system that values **simplicity, reliability, and control** over scale.

---

## Running Locally

- Designed to run continuously once configured  
- Automatically starts on boot  
- Recovers cleanly after restarts  
- No external services required for inference  

---

## Status

- Focused on refinement and stability  
- Built as a long-term personal system  

---

## Author

**Shlok Singh**  
GitHub: https://github.com/ShlokisAFK
