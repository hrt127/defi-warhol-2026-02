#!/usr/bin/env python3
"""
Airdrop farm action logger
Usage: python scripts/farm_log.py add <protocol> <action> [tx_hash] [size_usd]
       python scripts/farm_log.py summary
"""
import csv
import sys
from datetime import datetime
from pathlib import Path

# Adapted for Dojo standard structure
ROOT_DIR = Path(__file__).parent.parent
LOG_FILE = ROOT_DIR / "data" / "logs" / "farm_actions.csv"
LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

def init_log():
    if not LOG_FILE.exists():
        with open(LOG_FILE, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['timestamp', 'protocol', 'action', 'tx_hash', 'size_usd', 'notes'])

def add_action(protocol, action, tx_hash='', size_usd='0'):
    init_log()
    timestamp = datetime.now().isoformat()
    with open(LOG_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, protocol, action, tx_hash, size_usd, ''])
    print(f"✓ Logged: {protocol} → {action}")

def summary():
    init_log()
    with open(LOG_FILE, 'r') as f:
        reader = csv.DictReader(f)
        actions = list(reader)
    
    if not actions:
        print("No actions logged yet")
        return
    
    protocols = {}
    for row in actions:
        p = row['protocol']
        protocols[p] = protocols.get(p, 0) + 1
    
    print("\n=== Farm Summary ===")
    for protocol, count in sorted(protocols.items(), key=lambda x: -x[1]):
        print(f"{protocol}: {count} actions")
    print(f"\nTotal: {len(actions)} actions")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    
    cmd = sys.argv[1]
    if cmd == "add" and len(sys.argv) >= 4:
        add_action(*sys.argv[2:6])
    elif cmd == "summary":
        summary()
    else:
        print(__doc__)
