# local-ai-lead-agent
A Python-based local AI agent for personalizing business outreach using Llama 3.
# 🚀 Local AI Lead Generation Agent

A high-speed Python pipeline that uses local Small Language Models (SLMs) to personalize business outreach. 

### 💡 Why I built this
Standard cold outreach is often ignored because it lacks personalization. This tool allows companies to process thousands of leads locally, ensuring **data privacy** while maintaining a human-like "peer-to-peer" tone.

### 🛠️ Tech Stack
- **Backend:** Python
- **LLM Engine:** Llama 3 (Running via Ollama)
- **Data:** Pandas
- **UX:** TQDM (Real-time progress monitoring)

### 📈 Performance
- **Throughput:** Processed 100 leads in ~2.5 minutes on local hardware.
- **Privacy:** 100% on-device processing. No data leaks to third-party APIs.
- **Cost:** $0 API usage fees.

### 🚀 How to Run
1. Install [Ollama](https://ollama.com/) and pull Llama 3.
2. Clone this repo.
3. Run `pip install pandas ollama tqdm`.
4. Add leads to `leads.csv`.
5. Run `python main.py`.

⚠️ Test version — fictional data only. 🔜 Real version coming soon with live  website scraping + Claude AI.
