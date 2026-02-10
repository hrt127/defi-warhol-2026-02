# DeFi Warhol Airdrop Farm (Feb 2026)

**Role:** Layer 2 Intelligence / Activity Tracking  
**Status:** Active  

A system to track and optimize airdrop farming activity for the "DeFi Warhol" season (Feb 2026). This project provides a weighted scoring system to prioritize protocols and a logging utility to maintain an audit trail of farm actions.

## 1. Directory Structure

- `config/`: Configuration files (if any).
- `data/`: Source data (`projects.csv`) and activity logs (`logs/farm_actions.csv`).
- `docs/protocols/`: Per-protocol deep dives and task checklists.
- `scripts/`: Python logic for scoring and logging.
- `Makefile`: Command orchestration.

## 2. Usage

### Ranking Projects
To see which projects currently have the highest EV based on the scoring system:
```bash
make rank
```

### Logging Actions
To log a farming action (e.g., protocol interaction, trade):
```bash
make log protocol="Moca Network" action="Verified proofs" tx="0x..." size="0"
```

### Viewing Summary
To see a summary of all logged actions:
```bash
make summary
```

## 3. Scoring Weights
- **Funding:** 30%
- **Narrative:** 25%
- **Tasks Complexity:** 20%
- **Time Cost:** 15%
- **KYC Risk:** 10%

## 4. Automation Schedule
- Manual logging.
- Weekly review of protocol files in `docs/protocols/`.
