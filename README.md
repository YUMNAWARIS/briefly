# Briefly
An AI-powered text summarization app built with Streamlit and LangChain. Users can input text, and the app generates a concise summary by leveraging LangChain’s LLM API.

---

## 🚀 Features
- Summarize long text (up to 10,000 words).  
- Powered by LangChain + DeepSeek API.  
- Beginner-friendly and lightweight.  
- Built with Streamlit for a clean web interface.  

---

## 📦 Setup & Installation

This project uses [uv](https://docs.astral.sh/uv/) as the Python package manager. You can use pip or any other package manager of your choice.

### 1. Clone the repository
```bash
git clone https://github.com/your-username/ai-text-summarizer.git
cd ai-text-summarizer
```

### 2. Install dependencies
```bash
uv sync
```

### 3. Configure environment variables
Create a .env file in the root directory and add your DeepSeek API key:
```env
DEEPSEEK_API_KEY=<YOUR_API_KEY>
```


### ▶️ Running the Application
Create a .env file in the root directory and add your DeepSeek API key:
```bash
uv run streamlit run app.py
```

The application will be available at http://localhost:8501
 
---

## 🛠 Tech Stack

- **[Streamlit](https://streamlit.io/)** – Web UI  
- **[LangChain](https://www.langchain.com/)** – LLM integration  
- **[DeepSeek API](https://platform.deepseek.com)** – Summarization engine  
- **[uv](https://docs.astral.sh/uv/)** – Python package manager  

# 📄 License
This project is open-source and available under the MIT License.
