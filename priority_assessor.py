from ticket_analyzer.models.ticket import Ticket, PriorityAssessment

class PriorityAssessor:
    def assess(self, ticket: Ticket) -> PriorityAssessment:
        # Rule 1: Security issues are always critical
        if "security" in ticket.subject.lower() or "vulnerability" in ticket.message.lower():
            return PriorityAssessment(
                level="critical",
                rationale="Security-related issue detected"
            )

        # Rule 2: Enterprise customers get priority boost
        if ticket.customer_tier == "enterprise":
            if "error" in ticket.subject.lower() or "fail" in ticket.message.lower():
                return PriorityAssessment(
                    level="high",
                    rationale="Enterprise customer with system failure"
                )
            return PriorityAssessment(
                level="medium",
                rationale="Enterprise customer with non-critical issue"
            )

        # Rule 3: Premium customers with revenue impact
        if ticket.customer_tier == "premium" and ticket.monthly_revenue > 3000:
            if "error" in ticket.subject.lower():
                return PriorityAssessment(
                    level="high",
                    rationale="High-value premium customer with system issue"
                )

        # Rule 4: Emotional language detection
        emotional_words = ["urgent", "broken", "furious", "disappointed"]
        if any(word in ticket.message.lower() for word in emotional_words):
            return PriorityAssessment(
                level="medium",
                rationale="Customer expresses strong emotions"
            )

        # Default case
        return PriorityAssessment(
            level="low",
            rationale="Standard priority issue"
        )