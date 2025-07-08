from fastapi import Request


class UserController:
    @staticmethod
    def get_users(request: Request):
        return ""