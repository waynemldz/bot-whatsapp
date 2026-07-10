from app.repositories.ticket_repository import (
    close_ticket,
    create_ticket,
    get_open_ticket
)


class TicketService:

    def create(self, user_id: str):
        return create_ticket(user_id)

    def get_open(self, user_id: str):
        return get_open_ticket(user_id)

    def close(self, user_id: str):
        return close_ticket(user_id)


ticket_service = TicketService()