import sys
from pathlib import Path

print("Python is looking in these paths:")
print(sys.path)
print(f"Project root: {Path(__file__).parent.parent}")

from ticket_analyzer.models.ticket import Ticket, TicketAnalysis, PriorityAssessment, RoutingRecommendation
from ticket_analyzer.agents.priority_assessor import PriorityAssessor
from ticket_analyzer.agents.routing_specialist import RoutingSpecialist


def analyze_ticket(ticket_data: dict) -> TicketAnalysis:
    """Process a support ticket through the multi-agent system."""
    ticket = Ticket(**ticket_data)
    priority = PriorityAssessor().assess(ticket)
    routing = RoutingSpecialist().route(ticket, priority)

    combined_notes = None
    if priority.level == "critical" and routing.department != "security":
        combined_notes = "Warning: Critical issue not routed to security team"

    return TicketAnalysis(
        ticket_id=ticket.ticket_id,
        priority=priority,  # Pass the model instance directly
        routing=routing,  # Pass the model instance directly
        combined_notes=combined_notes
    )


if __name__ == "__main__":
    from ticket_analyzer.tests.test_cases import test_tickets

    for case in test_tickets:
        try:
            result = analyze_ticket(case)
            print(f"\nTicket {result.ticket_id}:")
            print(f"  Priority: {result.priority.level}")  # Access as attribute
            print(f"  Reason: {result.priority.rationale}")
            print(f"  Department: {result.routing.department}")
            print(f"  Response Time: {result.routing.expected_response_time}")
            if result.combined_notes:
                print(f"  Note: {result.combined_notes}")
        except Exception as e:
            print(f"\nError processing ticket {case.get('ticket_id', 'UNKNOWN')}:")
            print(f"  {str(e)}")