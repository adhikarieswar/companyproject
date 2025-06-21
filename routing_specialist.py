from ticket_analyzer.models.ticket import Ticket, RoutingRecommendation, PriorityAssessment

class RoutingSpecialist:
    def route(self, ticket: Ticket, priority: PriorityAssessment) -> RoutingRecommendation:
        # Security issues go to security team immediately
        if "security" in ticket.subject.lower():
            return RoutingRecommendation(
                department="security",
                rationale="Security-related issue requires immediate attention",
                expected_response_time="1 hour"
            )

        # API/Technical issues
        if "api" in ticket.subject.lower() or "error" in ticket.message.lower():
            response_time = "4 hours" if priority.level in ["high", "critical"] else "24 hours"
            return RoutingRecommendation(
                department="technical",
                rationale="Technical issue requiring engineering support",
                expected_response_time=response_time
            )

        # Feature requests
        if "feature" in ticket.subject.lower() or "request" in ticket.subject.lower():
            return RoutingRecommendation(
                department="feature_request",
                rationale="Customer feature request",
                expected_response_time="1 week"
            )

        # Enterprise customer success
        if ticket.customer_tier == "enterprise":
            return RoutingRecommendation(
                department="customer_success",
                rationale="Enterprise customer requires dedicated support",
                expected_response_time="8 hours"
            )

        # Default to technical support
        return RoutingRecommendation(
            department="technical",
            rationale="General technical support",
            expected_response_time="48 hours"
        )