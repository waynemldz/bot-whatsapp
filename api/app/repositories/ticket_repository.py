from datetime import datetime

from database import SessionLocal
from app.models.ticket import Ticket


def get_open_ticket(user_id: str):
    with SessionLocal() as db:
        return (
            db.query(Ticket)
            .filter(
                Ticket.user_id == user_id,
                Ticket.status.in_(["pending", "in_progress"])
            )
            .order_by(Ticket.id.desc())
            .first()
        )


def create_ticket(user_id: str):
    with SessionLocal() as db:
        existing_ticket = (
            db.query(Ticket)
            .filter(
                Ticket.user_id == user_id,
                Ticket.status.in_(["pending", "in_progress"])
            )
            .first()
        )

        if existing_ticket:
            return existing_ticket

        ticket = Ticket(
            user_id=user_id,
            status="pending"
        )

        db.add(ticket)
        db.commit()
        db.refresh(ticket)

        return ticket


def close_ticket(user_id: str):
    with SessionLocal() as db:
        ticket = (
            db.query(Ticket)
            .filter(
                Ticket.user_id == user_id,
                Ticket.status.in_(["pending", "in_progress"])
            )
            .order_by(Ticket.id.desc())
            .first()
        )

        if ticket is None:
            return None

        ticket.status = "closed"
        ticket.closed_at = datetime.utcnow()

        db.commit()
        db.refresh(ticket)

        return ticket