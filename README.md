# Infra Pilot: Terraform MCP Server

Infra Pilot is an **MCP-compliant, agentic DevOps copilot** that understands and answers questions about your Terraform infrastructure code using a local LLM (LLaMA via Ollama), LangGraph agent flow, and vector-based RAG.

> Think of it as a ChatGPT-like assistant that knows your actual Terraform setup — and can generate documentation, answer questions, and be extended to detect drift, security issues, or cost spikes.

---

## 🚀 Features

* ✅ Local LLM inference (LLaMA 3 via Ollama — no OpenAI key required)
* ✅ LangGraph-powered multi-step agent with structured context
* ✅ Embeds `.tf` files and answers natural language questions
* ✅ Auto-generates Markdown documentation from code
* ✅ Streamlit UI for easy querying
* ✅ FastAPI backend with `/ask` and `/docs/generate`

---

## 📁 Project Structure

```
infra-pilot/
├── app/
│   ├── main.py                # FastAPI app
│   ├── routes/                # /ask and /docs endpoints
│   ├── services/              # Embedding + inference logic
│   ├── agents/                # LangGraph reasoning flow
│   ├── templates/             # Structured prompt template
│   └── ui/app.py              # Streamlit UI
├── infra/                    # Your Terraform code (.tf files)
├── chroma_store/             # Vector DB store (auto-generated)
├── docs_output/              # Markdown docs (generated)
├── embed_terraform.py        # Script to re-embed .tf files
├── requirements.txt
└── README.md
```

---

## 🧠 How It Works (MCP Pipeline)

1. 🧾 **Code context** is embedded with HuggingFace + Chroma
2. 🧠 A LangGraph agent uses a structured prompt template:

   ```
   ## Code: {code_chunks}
   ## Vars: {tf_vars}
   ## Question: {user_query}
   ```
3. 🤖 LLaMA model (via Ollama) generates answers
4. 📘 Markdown docs are generated with the same reasoning chain

---

## 🛠️ Setup Instructions

### 1. Install requirements

```bash
pip install -r requirements.txt
```

### 2. Start Ollama with LLaMA

```bash
ollama run llama3
```

### 3. Embed your Terraform code

```bash
python embed_terraform.py
```

### 4. Run the FastAPI backend

```bash
uvicorn app.main:app --reload
```

### 5. Launch the Streamlit UI

```bash
streamlit run app/ui/app.py
```

---

## 💬 Example Questions (Try These in Streamlit)

* "What does this module create?"
* "What IAM permissions are given to Lambda?"
* "Is the RDS database publicly accessible?"
* "List the input variables and their defaults."

---

## 📘 Generate Docs

Click **"📝 Generate Markdown Documentation"** in the Streamlit UI,
or call it directly:

```bash
curl -X POST http://localhost:8000/docs/generate
```

Output saved to:

```
docs_output/infra-doc-YYYYMMDD-HHMMSS.md
```

---

## 🧱 Roadmap Ideas

* ✅ Slack bot interface: `/ask-infra`
* 🧠 Drift detection with AWS SDK / TF state
* 💸 Cost estimation with Infracost
* 🧪 Test mode for mocking plan/apply
* 🗃️ Auto-export docs to GitHub/Confluence

---

## 🤝 Contributing

Want to build a plugin, add an agent tool, or enhance UI?
PRs and ideas welcome — let’s build InfraPilot into the ultimate infra copilot.

---

## 💬 Questions / Feedback

Open an issue or ping `@siva` if you need help, extensions, or a demo setup!
