📚 Book Summarizer App

An AI-powered web application that generates concise summaries from book PDFs or text input using the OpenAI GPT API. The app helps readers, students, and researchers save time by quickly understanding the key points of long books or documents.

🚀 Features

Upload book PDFs or paste text directly.

Generate chapter-wise or overall summaries.

AI-powered summarization using OpenAI GPT API.

Clean and user-friendly web interface.

Built with Django (backend) and HTML/CSS (frontend).

🛠 Tech Stack

Backend: Python, Django

AI Integration: OpenAI GPT API

Frontend: HTML, CSS, Bootstrap

Database: SQLite

📌 Use Cases

📖 Students can create quick notes from textbooks.

📑 Researchers can get concise overviews of lengthy papers.

👩‍💻 Professionals can summarize reports for faster review.

⚡ Getting Started

Clone this repository:

git clone https://github.com/your-username/book-summarizer.git
cd book-summarizer


Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows


Install dependencies:

pip install -r requirements.txt


Add your OpenAI API key in settings.py or .env.

Run the server:

python manage.py runserver


Open in browser:

http://127.0.0.1:8000/