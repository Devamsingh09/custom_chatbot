import os
from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.llms import Replicate
from dotenv import load_dotenv
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import FAISS

load_dotenv()


#API Key
replicate_api_token = os.getenv("REPLICATE_API_TOKEN")
if not replicate_api_token:
    raise ValueError("Missing REPLICATE_API_TOKEN. Set it as an environment variable.")
os.environ["REPLICATE_API_TOKEN"] = replicate_api_token
# flask app
app = Flask(__name__)
api = Api(app)
# just for testing
@app.route('/')
def home():
    return '''
    <h1>Chatbot API</h1>
    <input type="text" id="question" placeholder="Type your question">
    <button onclick="askQuestion()">Ask</button>
    <p id="response"></p>

    <script>
        function askQuestion() {
            const question = document.getElementById("question").value;
            fetch("/ask", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ question: question })
            })
            .then(response => response.json())
            .then(data => {
                document.getElementById("response").innerText = "Answer: " + data.answer;
            })
            .catch(error => {
             document.getElementById("response").innerText = "Error: " + error;
            });
        }
    </script>
    '''

#checking and loading faiss_index
vector_store_path = "embeddings/vector_store/faiss_index"
if not os.path.exists(vector_store_path):
    raise FileNotFoundError(f"FAISS index not found at {vector_store_path}")

#vector database
vector_db = FAISS.load_local(
    vector_store_path,
    HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2"),
    allow_dangerous_deserialization=True
)

#LLM
llm = Replicate(
    model="meta/llama-2-7b-chat",
    model_kwargs={"temperature": 0.7, "max_new_tokens": 1000}  # Fixed kwargs
)

# chain
qa_chain = RetrievalQA.from_chain_type(llm, retriever=vector_db.as_retriever())

#chatbot resource
class Chatbot(Resource):
    def post(self):
        try:
            data = request.get_json()
            query = data.get("question")
            if not query:
                return jsonify({"error": "No question provided"}), 400

            response = qa_chain.run(query)
            return jsonify({"answer": response})

        except Exception as e:
            return jsonify({"error": str(e)}), 500

api.add_resource(Chatbot, "/ask")

if __name__ == "__main__":
    app.run(debug=True)
