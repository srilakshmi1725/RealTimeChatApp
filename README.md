# RealTimeChatApp 🧑‍💻💬

A terminal-based real-time chat application built using Python socket programming. This app allows multiple users to connect to a server and chat with each other in real time.

---

## 🚀 Features

- Multi-client support using threading
- Real-time messaging
- Broadcasts messages to all users
- Clean separation of client and server logic

---

## 🧠 How It Works

- The `server.py` handles all connected clients and broadcasts messages to everyone.
- The `client.py` connects each user to the server and handles message sending/receiving in real-time using threads.

---

## 📦 Requirements

- Python 3.x

---

## 🔧 How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/RealTimeChatApp.git
cd RealTimeChatApp
python server.py
python client.py

# Server terminal
Server started on 127.0.0.1:12345
Connected with ('127.0.0.1', 55678)
Username: Sri
Username: Bablu

# Client terminal (Sri)
Enter your username: Sri
Connected to chat server!
Bablu joined the chat!
Bablu: Hello Sri!

# Client terminal (Bablu)
Enter your username: Bablu
Connected to chat server!
Sri: Hi Bablu!

👨‍💻 Author
Parise Srilakshmi

Git Hub:- https://github.com/srilakshmi1725# RealTimeChatApp
