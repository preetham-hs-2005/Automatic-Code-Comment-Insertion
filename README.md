# Automatic Code Comment Generator

An NLP-powered full-stack implementation that automatically adds meaningful English comments to your Python code snippets. It leverages Hugging Face's `transformers` library with a code-explanation T5 model (`SEBIS/code_trans_t5_small_code_documentation_generation_python`).

## Features
- **Frontend**: Clean, modern glassmorphism UI built with HTML, CSS, and Vanilla JavaScript. Features syntax highlighting powered by PrismJS.
- **Backend API**: Lightning-fast asynchronous API powered by `FastAPI` and `Uvicorn`.
- **Intelligent AST Parsing**: Extracts AST nodes from source Python code (Functions, Loops, Conditions, Variables) and precisely inserts the AI-generated comments.
- **Offline ML Inference**: Automatically downloads the necessary small LLM model and runs purely locally. No API keys required, completely private.

## Project Structure
```text
Automatic-Code-Comment-Insertion/
├── backend/
│   ├── main.py         # FastAPI application and endpoints
│   ├── nlp_model.py    # Hugging Face AutoModel generation logic
│   ├── code_parser.py  # `ast` walker that injects comments into code
│   └── requirements.txt
├── frontend/
│   ├── index.html      # Main webpage GUI
│   ├── style.css       # UI Design and layout
│   └── script.js       # App logic and API integration
└── README.md
```

## How to Run Locally

### 1. Backend Setup
Make sure you have Python 3.8+ installed.

1. Open a terminal and navigate to the project directory:
   ```cmd
   cd path/to/Automatic-Code-Comment-Insertion
   ```
2. Create and activate a Virtual Environment (Recommended):
   ```cmd
   python -m venv venv
   .\venv\Scripts\activate
   ```
3. Install the dependencies:
   ```cmd
   pip install -r backend/requirements.txt
   pip install sentencepiece protobuf  # Model specific requirements
   ```
4. Start the FastAPI server (it runs on port 8001 to avoid conflicts):
   ```cmd
   cd backend
   uvicorn main:app --port 8001 --reload
   ```

> **Note**: The first time you execute a request via the UI, it might take a moment as the backend needs to download the 240MB Hugging Face Transformers model locally.

### 2. Frontend Setup
The frontend is completely static!

1. Simply open the `frontend/index.html` file in any modern web browser.
2. Paste any Python snippet into the "Source Code" window and click on "Generate Comments". 
3. Watch the AI auto-document your codebase.