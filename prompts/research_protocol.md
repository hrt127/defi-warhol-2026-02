# Protocol Deep Dive Research

## Target
- **Protocol:** [Name]
- **Current Tier:** [S/A/B]
- **Research Date:** [YYYY-MM-DD]
- **Trigger:** [Meta shift / New announcement / Narrative change / Time-based check]

## Research Objectives
Gather intelligence on:
1. **Funding updates** (new rounds, valuations)
2. **Product changes** (new features, mainnet launch, testnets)
3. **Points/rewards changes** (multipliers, deadlines, caps)
4. **Competitive landscape** (similar protocols, relative positioning)
5. **Narrative shifts** (sector momentum, VC interest, community size)
6. **Risk factors** (rug signals, team changes, exploit history)

## Sources to Check
- [ ] Protocol Twitter/X (@handle)
- [ ] Protocol Discord/Telegram
- [ ] Official blog/docs
- [ ] DeFiLlama (TVL, volume trends)
- [ ] Dune Analytics (if available)
- [ ] Recent CT discourse (search protocol name on X)
- [ ] Competitive intel (other S/A tier protocols in same category)

---

## Instructions for LLM

1. **Web search** for recent news (last 30 days):
   - "[Protocol] airdrop"
   - "[Protocol] funding round"
   - "[Protocol] mainnet launch"

2. **Analyze findings** and update:
   
   **In `data/projects.csv`:**
   - Adjust tier if funding/narrative changed
   - Update ev_score if needed
   - Add notes field with key insight
   
   **In `docs/protocols/[protocol].md`:**
   - Add to "Research Notes" section with timestamp
   - Update task list if new opportunities emerged
   - Flag risks/changes in bold

3. **Create research artifact** at `docs/protocols/[protocol]_research_[YYYY-MM-DD].md`:
   ```markdown
   # [Protocol] Research - [Date]
   
   ## Key Findings
   - Finding 1
   - Finding 2
   
   ## Tier Recommendation
   Current: [X] → Proposed: [Y] (if changed)
   Reasoning: ...
   
   ## Action Updates
   - New task: ...
   - Deprecated: ...
   
   ## Timeline Changes
   - Deadline: ...
   - Multiplier window: ...
   
   ## Sources
   - [Link 1]
   - [Link 2]
   ```

4. **Commit:**
   ```bash
   git add data/projects.csv docs/protocols/
   git commit -m "Research update: [Protocol] - [key change]"
   git push
   ```

5. **Re-rank:**
   ```bash
   make rank  # Verify new positioning
   ```
