import pytest
from api.posts_api import PostsAPI
from utils.data_loader import load_yaml

test_data = load_yaml("posts_data.yaml")


class TestPostsParametrize:
    def setup_method(self):
        self.api = PostsAPI()

    @pytest.mark.parametrize("post_id", test_data["valid_post_ids"])
    def test_get_valid_posts(self, post_id):
        """验证有效ID能正常获取文章"""
        response = self.api.get_post(post_id)
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == post_id

    @pytest.mark.parametrize("post_id", test_data["invalid_post_ids"])
    def test_get_invalid_posts(self, post_id):
        """验证无效ID返回404"""
        response = self.api.get_post(post_id)
        assert response.status_code == 404

    @pytest.mark.parametrize("post", test_data["create_posts"])
    def test_create_post_with_various_data(self, post):
        """验证不同数据组合创建文章"""
        response = self.api.create_post(
            title=post["title"],
            body=post["body"],
            user_id=post["user_id"]
        )
        assert response.status_code == 201
        data = response.json()
        assert data["title"] == post["title"]
        assert data["body"] == post["body"]
        assert data["userId"] == post["user_id"]
        