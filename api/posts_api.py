from api.base_api import BaseAPI


class PostsAPI(BaseAPI):
    def get_all_posts(self):
        return self.get("/posts")

    def get_post(self, post_id):
        return self.get(f"/posts/{post_id}")

    def get_post_comments(self, post_id):
        return self.get(f"/posts/{post_id}/comments")

    def create_post(self, title, body, user_id):
        payload = {"title": title, "body": body, "userId": user_id}
        return self.post("/posts", json=payload)

    def update_post(self, post_id, title, body, user_id):
        payload = {"title": title, "body": body, "userId": user_id}
        return self.put(f"/posts/{post_id}", json=payload)

    def delete_post(self, post_id):
        return self.delete(f"/posts/{post_id}")
    