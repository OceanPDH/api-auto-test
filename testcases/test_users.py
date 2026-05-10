import allure
import pytest
from api.users_api import UsersAPI


@allure.feature("Users管理")
class TestUsers:
    def setup_method(self):
        self.api = UsersAPI()

    @allure.story("查询用户")
    @allure.title("获取全部用户列表")
    def test_get_all_users(self):
        with allure.step("请求用户列表"):
            response = self.api.get_all_users()
        with allure.step("验证返回10个用户"):
            assert response.status_code == 200
            data = response.json()
            assert len(data) == 10

    @allure.story("查询用户")
    @allure.title("获取单个用户详情")
    def test_get_single_user(self):
        with allure.step("请求ID=1的用户"):
            response = self.api.get_user(1)
        with allure.step("验证用户数据完整"):
            assert response.status_code == 200
            data = response.json()
            assert data["id"] == 1
            assert "name" in data
            assert "email" in data
            assert "address" in data

    @allure.story("查询用户")
    @allure.title("获取用户的文章列表")
    def test_get_user_posts(self):
        with allure.step("请求用户1的文章"):
            response = self.api.get_user_posts(1)
        with allure.step("验证返回文章列表"):
            assert response.status_code == 200
            data = response.json()
            assert isinstance(data, list)
            assert len(data) > 0
            assert all(post["userId"] == 1 for post in data)

    @allure.story("创建用户")
    @allure.title("创建新用户")
    def test_create_user(self):
        with allure.step("发送创建请求"):
            response = self.api.create_user(
                name="Cooper Test",
                username="cooper",
                email="cooper@test.com"
            )
        with allure.step("验证创建成功"):
            assert response.status_code == 201
            data = response.json()
            assert data["name"] == "Cooper Test"
            assert data["email"] == "cooper@test.com"

    @allure.story("异常场景")
    @allure.title("查询不存在的用户")
    def test_get_nonexistent_user(self):
        with allure.step("请求不存在的用户ID"):
            response = self.api.get_user(99999)
        with allure.step("验证返回404"):
            assert response.status_code == 404

    @allure.story("查询用户")
    @allure.title("验证用户数据结构嵌套")
    def test_user_nested_structure(self):
        with allure.step("请求用户详情"):
            response = self.api.get_user(1)
        with allure.step("验证嵌套字段address和company"):
            data = response.json()
            assert "street" in data["address"]
            assert "city" in data["address"]
            assert "geo" in data["address"]
            assert "lat" in data["address"]["geo"]
            assert "name" in data["company"]
            