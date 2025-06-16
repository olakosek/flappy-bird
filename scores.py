import os
import json
SCORES_FILE = "best_scores.json"
def load_scores():
    if os.path.exists(SCORES_FILE):
        try:
            with open(SCORES_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    else:
        return []
    
def save_scores(scores):
    with open(SCORES_FILE, "w") as f:
        json.dump(scores, f)
def add_score(new_score):
    scores = load_scores()
    scores.append(new_score)
    scores = sorted(scores, reverse=True)[:10]
    save_scores(scores)

