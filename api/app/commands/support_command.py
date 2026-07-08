from app.commands.base_command import BaseCommand


class SupportCommand(BaseCommand):

    def can_handle(self, user_id: str, message: str) -> bool:
        return False

    def handle(self, user_id: str, message: str) -> str:
        return ""