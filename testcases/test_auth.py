import allure
import pytest
from api.auth_api import AuthAPI


@pytest.fixture(scope="session")
def auth_api():
    return AuthAPI()


@pytest.fixture(scope="session")
def auth_token(auth_api):
    """模拟登录获取token，整个会话共享"""
    response = auth_api.basic_auth("admin", "123456")
    assert response.status_code == 200
    # httpbin返回的json里有authenticated字段
    token = "fake-jwt-token-for-demo"
    yield token


@allure.feature("认证管理")
class TestAuth:

    @allure.story("Basic Auth")
    @allure.title("正确账号密码认证成功")
    def test_basic_auth_success(self, auth_api):
        with allure.step("使用正确凭证请求"):
            response = auth_api.basic_auth("admin", "123456")
        with allure.step("验证认证成功"):
            assert response.status_code == 200
            assert response.json()["authenticated"] is True

    @allure.story("Basic Auth")
    @allure.title("错误密码认证失败")
    def test_basic_auth_wrong_password(self, auth_api):
        with allure.step("使用错误密码请求"):
            response = auth_api.basic_auth("admin", "wrong")
        with allure.step("验证认证失败返回401"):
            assert response.status_code == 401

    @allure.story("Basic Auth")
    @allure.title("错误用户名认证失败")
    def test_basic_auth_wrong_username(self, auth_api):
        with allure.step("使用错误用户名请求"):
            response = auth_api.basic_auth("nobody", "123456")
        with allure.step("验证认证失败返回401"):
            assert response.status_code == 401

    @allure.story("Bearer Token")
    @allure.title("有效Token访问成功")
    def test_bearer_token_success(self, auth_api, auth_token):
        with allure.step("使用有效Token请求"):
            response = auth_api.bearer_token(auth_token)
        with allure.step("验证访问成功"):
            assert response.status_code == 200
            assert response.json()["authenticated"] is True

    @allure.story("Bearer Token")
    @allure.title("无Token访问被拒")
    def test_bearer_token_missing(self, auth_api):
        with allure.step("不传Token请求"):
            response = auth_api.bearer_token("")
        with allure.step("验证返回401"):
            assert response.status_code == 401
            