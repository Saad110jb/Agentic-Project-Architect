🏗️ Agentic Project Architect (APA)

Agentic Project Architect** is an AI-driven platform that bridges the gap between a developer's current skill set and rapidly evolving industry trends. By utilizing a multi-agent orchestration framework, the system analyzes your GitHub profile, researches real-time tech trends, and architects a personalized 4-week project roadmap to help you level up your career.

 🌟 Features

* GitHub DNA Analysis**: Automatically scrapes and analyzes your public repositories to identify your core tech stack and experience level.
* Real-time Trend Matching**: Uses RAG (Retrieval-Augmented Generation) and web search to find cutting-edge technologies (like Agentic AI or Transformers) that complement your existing skills.
* Autonomous Roadmap Generation**: A specialized "Architect Agent" designs a step-by-step, 4-week execution plan in Markdown format.
* High-Speed Inference**: Powered by **Groq LPU** hardware for near-instant agent reasoning.
* Professional UI**: A modern React dashboard with Tailwind CSS and real-time status updates.

 🤖 The Agentic Crew

This project is built using **CrewAI**, where specialized agents collaborate to achieve a complex goal:

1. Technical Analyst**: Scrapes repositories and summarizes technical proficiency.
2. Tech Trend Researcher**: Queries a Pinecone vector database and the live web for 2026 industry shifts.
3. Senior Project Architect**: The decision-maker that synthesizes all data into a definitive technical roadmap.

 🛠️ Tech Stack

* Frontend: React.js, Tailwind CSS, Lucide React
* Backend: FastAPI (Python)
* AI Framework**: CrewAI
* LLMs: Groq (Llama 3.1 / 3.3)
* Vector Database**: Pinecone
* Embeddings: SentenceTransformers (HuggingFace)
* **Database**: MongoDB Atlas

🚀 Getting Started

 Prerequisites

* Python 3.11+
* Node.js & npm
* API Keys for: Groq, Pinecone, and GitHub (PAT)

 Backend Setup

1. Clone the repository:
```bash
git clone https://github.com/Saad110jb/Agentic-Project-Architect.git
cd agentic-project-architect/backend

```


2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

```


3. Install dependencies:
```bash
pip install -r requirements.txt

```


4. Create a `.env` file based on `.env.example` and add your keys.
5. Run the server:
```bash
uvicorn main:app --reload

```



### Frontend Setup

1. Navigate to the frontend folder:
```bash
cd ../frontend

```


2. Install dependencies:
```bash
npm install

```


3. Start the application:
```bash
npm start

```



## 📄 License

This project is licensed under the MIT License.

---



