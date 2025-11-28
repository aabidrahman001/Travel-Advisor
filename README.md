# Travel Advisor Agent

## Overview
This project implements a multi-agent travel advisor using Google's ADK and Gemini LLM. It automatically plans flights, hotels, budgets, and aggregates results with an interactive user confirmation loop.

## Features
- Multi-agent workflow: Planner, Flight, Hotel, Budget, Aggregator, Confirmation Loop.
- Memory: Tracks user preferences across sessions.
- Tools: Google Search integration.
- Interactive loop: Allows refining travel plans dynamically.
- Web UI: ADK interface for agent inspection.

## Requirements
- Python 3.10+
- Jupyter Notebook or Kaggle environment
- Packages in `requirements.txt`
- Kaggle Secret: `GOOGLE_API_KEY`

## Setup
1. Clone this repo:

git clone https://github.com//travel-advisor-agent.git
cd travel-advisor-agent


2. Install dependencies:

pip install -r requirements.txt


3. Set Kaggle secret for `GOOGLE_API_KEY`.

4. Open notebook:

jupyter notebook notebooks/travel_agent_demo.ipynb


## Running
- Run cells sequentially from environment setup → agents → runner → loop.
- Use `user_query` input to ask for travel plans.
- Optional: Start the ADK Web UI to visualize agents:

!adk web --url_prefix <url_prefix>


## Memory Debugging
- Use `load_session_memories(memory_service, APP_NAME, USER_ID)` to inspect stored session memory.

## Notes
- No API keys or passwords are included.
- Designed to run in Kaggle or local Jupyter environments.

### Writeup
### Problem Statement

Planning travel today is overwhelming. Airlines, hotels, and travel booking platforms display scattered information, dynamic pricing, and varying transit options. Users often face a deluge of choices, cheap flights with long layovers, affordable hotels with poor ratings, or inconvenient locations, forcing them to spend hours manually comparing options. Budget-sensitive travelers or those with limited schedules are particularly affected, often resulting in stress, suboptimal decisions, or overspending.

The problem is compounded by personal preferences: travelers may want night flights, specific airlines, certain hotel ratings, or minimal transit times. Most booking systems ignore these context-rich preferences, starting every search from scratch.

### Why agents?

Travel planning is inherently a multi-step reasoning task. A single LLM cannot reliably retrieve flights, compare transit times, evaluate prices, check hotel locations, enforce budgets, and synthesize everything into a coherent plan, especially if the user adds constraints mid-process.
Agents solve this problem naturally. Flight agents handle routing, layovers, and pricing; hotel agents handle location, ratings, and amenities; budget agents evaluate trade-offs and affordability. Agents retain user preferences, ensuring personalization across sessions (airline choices, hotel styles, travel times). They combine deterministic tools with reasoning, enabling precise calculations, filtering, and real-time web queries. Another trait can be considered their iterative capabilities that can query the user for refinements (“Do you want to refine the travel plan?”), allowing multi-turn adjustments.

By leveraging multi-agent coordination, memory, and tools, this system automates complex decision-making, creating a seamless travel planning experience.

### What you created -- What's the overall architecture? 

The solution is a multi-agent travel planning system built with Google ADK. Its architecture comprises:

1. Planner Agent: Extracts flight details, hotel requirements, and budget from the user query.

2. Flight Agent: Searches for flights, compares transit times, and evaluates airline preferences.

3. Hotel Agent: Searches hotels based on location, ratings, and dates.

4. Budget Agent: Ensures flight and hotel options fit the user’s budget, returning recommendations and affordability verdicts.

5. Aggregator Agent: Combines outputs from flights, hotels, and budget, producing a coherent travel plan summary.

6. Confirmation Loop Agent: Prompts the user for refinements, iteratively updating the plan according to preferences.

Agents communicate via structured tools and memory, enabling parallel workflows, looped confirmation, and session-based personalization.

Workflow:

User Query → Planner → [Flight Agent || Hotel Agent] → Budget Agent → Aggregator → Confirmation Loop → User Feedback → Memory


### Demo -- Show your solution 

User Input:

“I want flights from Dhaka to Berlin, 30th Nov – 2nd Dec, budget 800 USD.”

Planner Agent: Extracts flights, hotel, and budget constraints.

Flight & Hotel Agents (parallel): Search for cheapest options, optimal transit times, and preferred hotel ratings.

Budget Agent: Checks affordability, suggests alternate options if over budget.

Aggregator Agent: Produces a consolidated plan: cheapest flights, recommended hotels, total cost, transit times.

Confirmation Loop: Asks user:

“Do you want to refine the travel plan? (yes/no)”
User responds “yes” → agents re-run with updated constraints (e.g., night flights only).

Memory: Retains past preferences for future interactions, improving personalization over time.

The notebook demonstrates this workflow via asynchronous calls to the Runner, session memory inspection, and parallel agent execution.

### The Build -- How you created it, what tools or technologies you used.

Google Agent Development Kit (ADK): Multi-agent orchestration, memory management, and tool integration.

Gemini LLM (gemini-2.5-flash-lite): Powers reasoning for all agents.

Python AsyncIO: Supports asynchronous execution for parallel agents.

InMemoryMemoryService & InMemorySessionService: Store user sessions, preferences, and intermediate results.

FunctionTool: Handles user confirmation input in the loop.

Google Search Tool: Retrieves live data for flights and hotels.

Development Highlights:

Sequential & Parallel Agents: Structured agent flow ensures specialized tasks are handled concurrently where possible.

LoopAgent: Supports iterative refinement by the user.

Memory Integration: Preserves session state, ensuring user preferences carry across interactions.

Retry Config: Ensures robust web querying with exponential backoff for transient errors.

### If I had more time, this is what I'd do

1. Integrate real-time APIs for flight and hotel bookings.

2. Add additional agents for destination-specific recommendations (activities, restaurants, transport).

3. Implement dynamic preference learning to automatically adapt plans based on past choices.

4. Deploy a full web-based interface for end-to-end agent interaction.
