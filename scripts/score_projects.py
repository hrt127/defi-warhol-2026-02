#!/usr/bin/env python3
"""
Auto-rank airdrop projects by weighted scoring
Weights: funding(30%), narrative(25%), tasks(20%), time(15%), kyc(10%)
"""
import csv
from pathlib import Path

# Adapted for Dojo standard structure
ROOT_DIR = Path(__file__).parent.parent
PROJECTS_FILE = ROOT_DIR / "data" / "projects.csv"

NARRATIVE_SCORES = {
    'Animoca/Gaming': 10, 'Domains/Infra': 9, 'RWA Perps': 8, 'Perps': 7,
    'Starknet Perps': 7, 'Trading': 6, 'Card/Spending': 5, 'Social Quests': 3,
    'Task Farming': 2, 'Tasks/Points': 2
}

TASK_SCORES = {'Low': 10, 'Medium': 6, 'High': 3}
TIME_SCORES = {'Low': 10, 'Medium': 6, 'High': 3}
KYC_SCORES = {'None': 10, 'Yes': 0}

def score_project(row):
    try:
        funding_str = row['funding'].upper().replace('M','').replace('UNKNOWN','0').replace('$','')
        funding = float(funding_str)
    except ValueError:
        funding = 0
        
    funding_score = min(funding / 5, 10)  # $50M = max 10pts
    
    narrative_score = NARRATIVE_SCORES.get(row['narrative'], 5)
    task_score = TASK_SCORES.get(row['time_cost'], 5)
    time_score = TIME_SCORES.get(row['time_cost'], 5)
    kyc_score = KYC_SCORES.get(row['kyc_risk'], 5)
    
    weighted = (funding_score * 0.3 + narrative_score * 0.25 + 
                task_score * 0.2 + time_score * 0.15 + kyc_score * 0.1)
    
    return round(weighted * 10, 1)

def rank_projects():
    if not PROJECTS_FILE.exists():
        print(f"Error: {PROJECTS_FILE} not found.")
        return

    with open(PROJECTS_FILE, 'r') as f:
        reader = csv.DictReader(f)
        projects = list(reader)
    
    for p in projects:
        p['calc_score'] = score_project(p)
    
    projects.sort(key=lambda x: -x['calc_score'])
    
    print("\n=== Ranked Airdrops ===\n")
    for i, p in enumerate(projects, 1):
        print(f"{i}. {p['protocol']:<15} | Score: {p['calc_score']:<5} | Tier: {p['tier']}")

if __name__ == "__main__":
    rank_projects()
