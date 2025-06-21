from pydantic import BaseModel
from typing import Literal, Optional

class Ticket(BaseModel):
    ticket_id: str
    customer_tier: Literal["free", "premium", "enterprise"]
    subject: str
    message: str
    previous_tickets: int
    monthly_revenue: float
    account_age_days: int

class PriorityAssessment(BaseModel):
    level: Literal["low", "medium", "high", "critical"]
    rationale: str

class RoutingRecommendation(BaseModel):
    department: Literal["technical", "billing", "security", "feature_request", "customer_success"]  # Added customer_success
    rationale: str
    expected_response_time: str

class TicketAnalysis(BaseModel):
    ticket_id: str
    priority: PriorityAssessment  # Accepts model instance
    routing: RoutingRecommendation  # Accepts model instance
    combined_notes: Optional[str] = None