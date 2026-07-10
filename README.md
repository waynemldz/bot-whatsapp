# 🤖 Nexa

<div align="center">

AI-powered WhatsApp virtual assistant built with **FastAPI**, **Google Gemini** and **WhatsApp Web**.

![Python](https://img.shields.io/badge/Python-3.14-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-red?style=for-the-badge)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker)
![Google Gemini](https://img.shields.io/badge/Google-Gemini-4285F4?style=for-the-badge&logo=google)

</div>

---

## 📸 Preview

> _GIF do projeto em funcionamento será adicionado aqui._

---

## 📌 Overview

Nexa is a virtual assistant for WhatsApp that combines predefined conversation flows with generative AI to provide a more natural customer service experience.

The assistant is capable of:

- answering questions about the company;
- presenting services and pricing;
- opening support tickets;
- scheduling appointments;
- transferring conversations to a human agent;
- maintaining conversation state and history.

The project was designed following a service-oriented architecture using the Repository Pattern and Command Pattern.
## 🚀 Features

- 📱 WhatsApp integration with `whatsapp-web.js`
- 🤖 AI responses powered by Google Gemini
- 💬 Conversation state management
- 🎫 Human support ticket creation
- 🧠 Company knowledge base
- 📝 Conversation history
- 🗄️ SQLite database with SQLAlchemy
- 🐳 Docker support
- 📚 Interactive API documentation with Swagger

---

## 🛠️ Tech Stack

- Python 3.14
- FastAPI
- SQLAlchemy
- SQLite
- Google Gemini API
- Node.js
- whatsapp-web.js
- Axios
- Docker

---

## 🏗️ Architecture

```text
                         WhatsApp User
                               │
                               ▼
                  whatsapp-web.js (Node.js)
                               │
                               ▼
                         FastAPI API
                               │
                     Message Service
                               │
                     Command Dispatcher
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
  Menu Command   Support Command  Schedule Command
        │              │              │
        └──────────────┼──────────────┘
                       ▼
                 Conversation State
                       │
             ┌─────────┴─────────┐
             ▼                   ▼
       Business Logic      Google Gemini
             │                   │
             └─────────┬─────────┘
                       ▼
                  SQLAlchemy ORM
                       │
                       ▼
                     SQLite
```

---

## 📂 Project Structure

```text
api
│
├── app
│   ├── commands
│   ├── config
│   ├── knowledge
│   ├── models
│   ├── repositories
│   ├── routes
│   └── services
│
├── database.py
├── main.py
├── Dockerfile
└── docker-compose.yml
```

---

## ⚙️ How it Works

```
WhatsApp

        │

        ▼

Node.js (whatsapp-web.js)

        │

        ▼

FastAPI

        │

        ▼

Command Dispatcher

        │
        ├───────────────┐
        │               │
        ▼               ▼

Commands          Google Gemini

        │               │
        └───────┬───────┘
                ▼

           Response
```

The assistant first attempts to identify predefined intents such as:

- Support
- Pricing
- Scheduling
- Menu navigation

If no command matches the user's message, the request is forwarded to Google Gemini, which answers based on the company's knowledge base.

---

## 📖 Conversation Flow

```
User

↓

Main Menu

↓

Pricing
Support
Scheduling

↓

If necessary

↓

AI (Gemini)

↓

Human Support
```

---

## 🧠 AI

The assistant uses Google Gemini together with a local knowledge base (`company.txt`).

The AI only answers questions related to the company.

Unknown questions are gracefully redirected to human support.

---

## 🐳 Running the Project

Clone the repository:

```bash
git clone https://github.com/waynemldz/nexa.git
```

Navigate to the project:

```bash
cd nexa
```

Start with Docker:

```bash
docker compose up --build
```

The API will be available at:

```
http://localhost:8000
```

Swagger documentation:

```
http://localhost:8000/docs
```

---

## 📌 Future Improvements

- Conversation timeout
- Rich WhatsApp buttons
- Admin dashboard
- Authentication
- PostgreSQL support
- Automated testing
- CI/CD pipeline

---

## 👨‍💻 Author

Wayne Gabriel

GitHub:
https://github.com/waynemldz

LinkedIn:
https://www.linkedin.com/in/gabrielmldz
