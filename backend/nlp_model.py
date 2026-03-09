from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

MODEL_NAME = "SEBIS/code_trans_t5_small_code_documentation_generation_python"

class NLPModel:
    def __init__(self):
        self.tokenizer = None
        self.model = None
        # Default to CPU if CUDA is not available
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

    def load_model(self):
        if self.model is None:
            print(f"Loading {MODEL_NAME} on {self.device}...")
            self.tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
            self.model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME).to(self.device)
            print("Model loaded successfully.")

    def generate_comment(self, code_snippet: str) -> str:
        self.load_model()
        if not code_snippet.strip():
            return "No code provided."
        
        # Preprocess input
        inputs = self.tokenizer(code_snippet, return_tensors="pt", max_length=512, truncation=True).to(self.device)
        
        # Generate summary (comment)
        outputs = self.model.generate(
            **inputs, 
            max_length=64, 
            num_beams=4, 
            early_stopping=True
        )
        
        # Decode and clean the output
        comment = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return comment.strip()

nlp = NLPModel()
