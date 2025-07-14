# 🧠 Reddit User Persona Extractor

This project automatically generates a **detailed user persona** from a Reddit user's posts and 
comments using **NVIDIA's Meta LLaMA3-70B-Instruct** model and the official Reddit API via `PRAW`.

It creates structured persona files like this:

- Age, Occupation, Location, Archetype
- Motivations, Goals, Frustrations
- MBTI-style personality
- Reddit activity **quoted as citations** for each insight

---

## 🚀 Features

✅ Extracts Reddit posts and comments via API  
✅ Sends data to NVIDIA LLaMA3 for persona generation  
✅ Cites Reddit quotes for every trait or habit  
✅ Outputs structured `.txt` files  
✅ Modular and extensible Python code

---

## 📁 Project Structure
reddit-project/
├── reddit_persona_extractor.py
├── personas/ # Output folder for persona .txt files
├── .env # Store Reddit and NVIDIA credentials here
└── utils/
├── reddit_scraper.py # Reddit data collection via PRAW
├── persona_builder.py # Sends data to NVIDIA API, builds persona
└── citation_tracker.py # Matches quotes for traceability

---

## ⚙️ Setup Instructions

### 1. Clone this repository

```
git clone https://github.com/nairanujit3/Reddit-User-Persona-Extractor
cd Reddit-User-Persona-Extractor
```

### 2. Create and activate a virtual environment
```
python -m venv reddit-env
source reddit-env/bin/activate   # macOS/Linux
# OR
reddit-env\Scripts\activate      # Windows
```

### 3. Install dependencies
```
pip install -r requirements.txt
```

### 4. Add API credentials
Create a .env file in the project root:
```
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_secret
REDDIT_USER_AGENT=reddit_persona_app:v1.0 (by /u/yourusername)

NVIDIA_API_KEY=your_nvidia_ai_key
```

### ▶️ How to Run
To extract a persona from any Reddit user:
```
python persona_extraction.py
```

Paste the Reddit profile URL when prompted:
```
Enter Reddit profile URL: https://www.reddit.com/user/kojied/
```
A persona file will be saved to personas/kojied_persona.txt.


### 📌 Requirements
Python 3.8+

Reddit Developer Account: https://www.reddit.com/prefs/apps

NVIDIA AI API access: https://platform.nvidia.com
