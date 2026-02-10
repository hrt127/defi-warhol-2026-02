#!/usr/bin/env python3
"""
Airdrop farm action logger
Usage: python farm_log.py add <protocol> <action> [wallet] [tx_hash] [size_usd]
       python farm_log.py summary
       python farm_log.py by-wallet
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
            writer.writerow(['timestamp', 'protocol', 'action', 'wallet', 'tx_hash', 'size_usd', 'notes'])

def add_action(protocol, action, wallet='', tx_hash='', size_usd='0'):
    init_log()
    timestamp = datetime.now().isoformat()
    with open(LOG_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, protocol, action, wallet, tx_hash, size_usd, ''])
    print(f"✓ Logged: {protocol} → {action} (wallet: {wallet or 'unspecified'})")

def summary():
    init_log()
    if not LOG_FILE.exists():
        print("No actions logged yet")
        return

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

def by_wallet():
    init_log()
    if not LOG_FILE.exists():
        print("No actions logged yet")
        return

    with open(LOG_FILE, 'r') as f:
        reader = csv.DictReader(f)
        actions = list(reader)
    
    if not actions:
        print("No actions logged yet")
        return
    
    wallets = {}
    for row in actions:
        w = row['wallet'] or 'unspecified'
        if w not in wallets:
            wallets[w] = []
        wallets[w].append(row)
    
    print("\n=== Actions by Wallet ===")
    for wallet, acts in wallets.items():
        print(f"\n{wallet}:")
        protocols = {}
        for a in acts:
            p = a['protocol']
            protocols[p] = protocols.get(p, 0) + 1
        for protocol, count in protocols.items():
            print(f"  {protocol}: {count} actions")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    
    cmd = sys.argv[1]
    if cmd == "add" and len(sys.argv) >= 4:
        # Expected args for 'add': protocol, action, [wallet], [tx_hash], [size_usd]
        # sys.argv[2:7] gets up to 5 positional args
        args = sys.argv[2:7]
        add_action(*args)
    elif cmd == "summary":
        summary()
    elif cmd == "by-wallet":
        by_wallet()
    else:
        print(__doc__)
