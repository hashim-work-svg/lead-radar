"""
Lead Radar - Autonomous Buying Signal Scanner & Pitch Synthesizer
Author: Hashim (@hashim_py | https://hashim.me.uk)
"""
import re
import json
from typing import List, Dict, Optional
from dataclasses import dataclass

@dataclass
class LeadSignal:
    title: str
    description: str
    source: str
    url: str
    detected_category: str
    budget_hint: Optional[str] = None
    urgency_level: str = "Medium"
    confidence_score: float = 0.0

BUYING_KEYWORDS = {
    "AI & LLM": [
        "ai agent", "llm", "rag", "langchain", "prompt engineer", "openai api", 
        "fine-tuning", "claude api", "vector database", "chatbot"
    ],
    "Automation & Scripting": [
        "n8n", "automation", "python script", "zapier", "telegram bot", 
        "web scraper", "etl pipeline", "selenium", "playwright", "cron"
    ],
    "Backend & Web Engineering": [
        "looking for developer", "hiring backend", "fastapi", "django", 
        "flask", "rest api", "full stack developer", "node.js", "landing page"
    ],
    "Data Engineering & Analysis": [
        "data analyst", "pandas", "sql dashboard", "postgresql", 
        "data pipeline", "airtable", "google sheets script"
    ]
}

BUDGET_PATTERNS = [
    r"\$\d+(?:,\d+)*(?:\s*(?:-\s*\$\d+(?:,\d+)*|\/hr|\/hour|k|usd))?",
    r"\d+\s*(?:usd|eur|gbp)",
    r"budget\s*:\s*[\$\d\w\s,-]+"
]

class LeadRadar:
    def __init__(self, author_name: str = "Hashim", portfolio_url: str = "https://hashim.me.uk"):
        self.author_name = author_name
        self.portfolio_url = portfolio_url

    def analyze_post(self, title: str, body: str, url: str = "", source: str = "web") -> Optional[LeadSignal]:
        content = f"{title} {body}".lower()
        
        intent_markers = [
            "looking for", "need a", "hiring", "seeking", "budget", "paid",
            "developer needed", "can someone build", "quote for", "wanted"
        ]
        has_intent = any(marker in content for marker in intent_markers)
        if not has_intent:
            return None

        # Categorize
        scores = {}
        for category, keywords in BUYING_KEYWORDS.items():
            score = sum(1 for kw in keywords if kw in content)
            if score > 0:
                scores[category] = score

        best_category = max(scores, key=scores.get) if scores else "General Engineering"

        # Budget extraction
        budget_match = None
        for pattern in BUDGET_PATTERNS:
            match = re.search(pattern, content, re.IGNORECASE)
            if match:
                budget_match = match.group(0).strip()
                break

        # Urgency
        urgency = "Standard"
        if any(term in content for term in ["urgent", "asap", "immediate", "today"]):
            urgency = "High / Immediate"

        return LeadSignal(
            title=title,
            description=body[:200] + "..." if len(body) > 200 else body,
            source=source,
            url=url,
            detected_category=best_category,
            budget_hint=budget_match,
            urgency_level=urgency,
            confidence_score=round(min(1.0, 0.4 + (0.15 * len(scores))), 2)
        )

    def generate_pitch(self, signal: LeadSignal) -> str:
        return (
            f"Hey! Saw you're looking for help with {signal.detected_category.lower()}. "
            f"I build reliable, production-tested Python backends and workflows focusing on pragmatic execution over bloated frameworks. "
            f"Live portfolio & developer suite: {self.portfolio_url}"
        )
