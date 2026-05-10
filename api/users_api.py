from api.base_api import BaseAPI


class UsersAPI(BaseAPI):
    def get_all_users(self):
        return self.get("/users")

    def get_user(self, user_id):
        return self.get(f"/users/{user_id}")

    def get_user_posts(self, user_id):
        return self.get(f"/users/{user_id}/posts")

    def create_user(self, name, username, email):
        payload = {"name": name, "username": username, "email": email}
        return self.post("/users", json=payload)
    