# Project Context: DeFi Warhol Airdrop Farm

## Overview
This project is an activity tracker and EV calculator for a specific set of airdrops identified in February 2026. It follows the Dojo v2.1 pattern of separating intelligence (scripts) from state (data/csv) and views (markdown).

## Objectives
- Rank projects based on funding, narrative, and risk.
- Maintain a canonical log of all wallet interactions.
- Provide a clear checklist for each protocol to ensure zero missed tasks.

## Intelligence Layer
- `scripts/score_projects.py`: Real-time ranking based on CSV data.
- `scripts/farm_log.py`: Append-only interaction logging.

## Data Layer
- `data/projects.csv`: The list of projects and their metadata.
- `data/logs/farm_actions.csv`: The audit trail of actions.

## Identity Integration
- Protocols are selected based on the user's primary interests (Gaming, Perps, Infra).
