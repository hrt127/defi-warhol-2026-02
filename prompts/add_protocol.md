# Add New Airdrop Protocol

## Context
I found a new airdrop protocol to track in the DeFi Warhol system.

## Source
- **From:** [Twitter/Substack/Discord/Manual]
- **Link:** [URL to source]
- **Date Found:** [YYYY-MM-DD]

## Protocol Details
- **Name:** 
- **Website:** 
- **Funding:** [Amount if known, or "Unknown"]
- **Narrative/Category:** [RWA Perps / Gaming / Social / Infra / etc.]
- **Backers:** [Key investors if known]

## Initial Tasks Identified
1. 
2. 
3. 

## Time/Effort Estimate
- **Time Cost:** [Low/Medium/High]
- **KYC Required:** [Yes/None]

---

## Instructions for LLM

Using the above information:

1. **Score the protocol** using `scripts/score_projects.py` logic:
   - Funding score (0-10)
   - Narrative strength (0-10) 
   - Task complexity (Low=10, Med=6, High=3)
   - Time cost (Low=10, Med=6, High=3)
   - KYC penalty (None=10, Yes=0)
   - Calculate weighted score and assign Tier (S/A/B)

2. **Add to projects.csv:**
   ```csv
   protocol,tier,funding,narrative,tasks,time_cost,kyc_risk,ev_score,notes
   ```

3. **Create protocol doc** at `docs/protocols/[protocol-name].md` using this template:
   ```markdown
   # [Protocol Name]
   
   **Tier:** [S/A/B]
   **Narrative:** [Category]
   **Link:** [URL]
   **Added:** [Date]
   
   ## Actions
   - [ ] Task 1
   - [ ] Task 2
   - [ ] Task 3
   
   ## Tracking
   | Date | Action | Wallet | Notes |
   |------|--------|--------|-------|
   |      |        |        |       |
   
   ## Research Notes
   *Updated as meta evolves*
   ```

4. **Commit to git:**
   ```bash
   git add data/projects.csv docs/protocols/[protocol-name].md
   git commit -m "Add [Protocol Name] - Tier [X] airdrop"
   git push
   ```

5. **Verify:**
   ```bash
   make rank  # Should show new protocol in ranked list
   ```
