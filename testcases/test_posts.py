'''
import pytest
from api.posts_api import PostsAPI


class TestPosts:
    def setup_method(self):
        self.api = PostsAPI()

    def test_get_all_posts(self):
        response = self.api.get_all_posts()
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) == 100

    def test_get_single_post(self):
        response = self.api.get_post(1)
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == 1
        assert "title" in data
        assert "body" in data
        assert "userId" in data

    def test_create_post(self):
        response = self.api.create_post(
            title="test title",
            body="test body",
            user_id=1
        )
        assert response.status_code == 201
        data = response.json()
        assert data["title"] == "test title"
        assert data["body"] == "test body"
        assert data["userId"] == 1

    def test_update_post(self):
        response = self.api.update_post(
            post_id=1,
            title="updated title",
            body="updated body",
            user_id=1
        )
        assert response.status_code == 200
        data = response.json()
        assert data["title"] == "updated title"

    def test_delete_post(self):
        response = self.api.delete_post(1)
        assert response.status_code == 200

    def test_get_nonexistent_post(self):
        response = self.api.get_post(99999)
        assert response.status_code == 404

    def test_get_post_comments(self):
        response = self.api.get_post_comments(1)
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) > 0
        assert "email" in data[0]
'''

'''给allure加标签'''
import pytest
import allure
from api.posts_api import PostsAPI


@allure.feature("Posts管理")
class TestPosts:
    def setup_method(self):
        self.api = PostsAPI()

    @allure.story("查询文章")
    @allure.title("获取全部文章列表")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_get_all_posts(self):
        with allure.step("发送GET请求获取所有文章"):
            response = self.api.get_all_posts()
        with allure.step("验证返回状态码为200"):
            assert response.status_code == 200
        with allure.step("验证返回100篇文章"):
            data = response.json()
            assert isinstance(data, list)
            assert len(data) == 100

    @allure.story("查询文章")
    @allure.title("获取单篇文章详情")
    def test_get_single_post(self):
        with allure.step("发送GET请求获取ID=1的文章"):
            response = self.api.get_post(1)
        with allure.step("验证返回数据完整性"):
            assert response.status_code == 200
            data = response.json()
            assert data["id"] == 1
            assert "title" in data
            assert "body" in data
            assert "userId" in data

    @allure.story("创建文章")
    @allure.title("创建新文章")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_post(self):
        with allure.step("发送POST请求创建文章"):
            response = self.api.create_post(
                title="test title",
                body="test body",
                user_id=1
            )
        with allure.step("验证创建成功"):
            assert response.status_code == 201
            data = response.json()
            assert data["title"] == "test title"
            assert data["body"] == "test body"
            assert data["userId"] == 1

    @allure.story("更新文章")
    @allure.title("更新已有文章")
    def test_update_post(self):
        with allure.step("发送PUT请求更新文章"):
            response = self.api.update_post(
                post_id=1,
                title="updated title",
                body="updated body",
                user_id=1
            )
        with allure.step("验证更新成功"):
            assert response.status_code == 200
            data = response.json()
            assert data["title"] == "updated title"

    @allure.story("删除文章")
    @allure.title("删除文章")
    def test_delete_post(self):
        with allure.step("发送DELETE请求"):
            response = self.api.delete_post(1)
        with allure.step("验证删除成功"):
            assert response.status_code == 200

    @allure.story("异常场景")
    @allure.title("查询不存在的文章返回404")
    def test_get_nonexistent_post(self):
        with allure.step("请求不存在的文章ID"):
            response = self.api.get_post(99999)
        with allure.step("验证返回404"):
            assert response.status_code == 404

    @allure.story("查询文章")
    @allure.title("获取文章评论列表")
    def test_get_post_comments(self):
        with allure.step("获取ID=1的文章评论"):
            response = self.api.get_post_comments(1)
        with allure.step("验证评论数据"):
            assert response.status_code == 200
            data = response.json()
            assert isinstance(data, list)
            assert len(data) > 0
            assert "email" in data[0]
            