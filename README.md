# AI-Hospital-Assistant
AI-powered assistant that helps patients prepare for hospitalisation using Streamlit and Groq LLM.

This project is a simple AI assistant that helps patients prepare for hospitalisation.

The assistant answers common questions related to hospital admission, surgery preparation, discharge process, and follow-up care.
---
## Objective

The goal of this project is to build an AI assistant that can guide patients through the hospitalisation process.

---
## Example Questions the Assistant Can Answer

- What documents are required for hospital admission?
- What should a patient carry before surgery?
- What happens during discharge?
- What follow-ups may be required after hospitalisation?
---
## Tech Stack
- Python
- Streamlit
- Groq API
- Llama 3 Model
---
## How It Works
1. The user enters a question in the Streamlit interface.
2. The question is sent to the Groq LLM model.
3. The AI model generates a response based on the prompt.
4. The response is displayed in the web interface.

---
## How to Run the Project

Install dependencies:
pip install -r requirements.txt

Create a `.env` file and add your Groq API key:
GROQ_API_KEY=your_api_key_here

Run the application:
streamlit run app.py
