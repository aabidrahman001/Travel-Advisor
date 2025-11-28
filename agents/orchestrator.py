class Orchestrator:
    def __init__(self, flight_agent, hotel_agent, budget_agent, aggregator, memory, sessions):
        self.flight_agent = flight_agent
        self.hotel_agent = hotel_agent
        self.budget_agent = budget_agent
        self.aggregator = aggregator
        self.memory = memory
        self.sessions = sessions
    
    def run(self, user_query):
        # Parse query
        # Initiate parallel workflows for flights and hotels
        # Retrieve user session & memory
        # Aggregate results
        # Handle loop for confirmation
        return "Final itinerary with flights and hotels"
