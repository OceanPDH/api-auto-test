from api.base_api import BaseAPI


class AuthAPI(BaseAPI):
    def basic_auth(self, username, password):
        """Basic Auth认证"""
        url = f"{self.base_url}/users"
        import requests
        response = requests.get(
            "https://httpbin.org/basic-auth/admin/123456",
            auth=(username, password),
            timeout=self.timeout
        )
        return response

    def bearer_token(self, token):
        """Bearer Token认证"""
        import requests
        response = requests.get(
            "https://httpbin.org/bearer",
            headers={"Authorization": f"Bearer {token}"},
            timeout=self.timeout
        )
        return response
    