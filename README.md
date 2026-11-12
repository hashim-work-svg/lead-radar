# 🛰️ Lead Radar: Client Buying Signal Scanner & Pitch Synthesizer

**Category**: Autonomous Tooling / Lead Intelligence  
**Author**: Hashim ([@hashim_py](https://x.com/hashim_py) · [hashim.me.uk](https://hashim.me.uk))  
**Status**: Production Ready / Open Source  

---

## 🎯 What it does
Lead Radar scans developer discussion feeds, social posts, and job listings for real **client buying signals** (intent triggers like *"looking for developer"*, *"need automation"*, *"hiring python"*). 

It automatically:
1. **Filters noise**: Distinguishes between promotional chatter and genuine client needs.
2. **Classifies domain**: Categorizes leads into AI/LLMs, Automation/n8n, Web/Backend, or Data Engineering.
3. **Extracts Budget & Urgency**: Identifies stated budgets and timelines.
4. **Synthesizes Tailored Pitches**: Generates crisp, high-signal 2–3 line outreach pitches that directly address the client's problem without marketing fluff.

---

## 🛠️ Architecture & Tech Stack
- **Engine**: Python 3.10+
- **Pattern Matching**: Regex-based budget & urgency extractors
- **NLP Heuristics**: Multi-domain keyword scoring
- **Zero Third-Party Telemetry**: 100% local execution

---

## 🚀 Getting Started

### 1. Run the Demo
```bash
python main.py
```

### 2. Run Unit Tests
```bash
python test_radar.py
```

---

## 🔗 Live Links & Portfolio
- Developer Portfolio & Live Web Tools: [https://hashim.me.uk](https://hashim.me.uk)
- Author on X: [@hashim_py](https://x.com/hashim_py)
