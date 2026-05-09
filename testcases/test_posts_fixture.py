class TestPostsFixture:
    def test_fixture_post_created(self, posts_api, sample_post):
        """验证fixture创建的文章数据完整"""
        assert sample_post["title"] == "fixture post"
        assert sample_post["body"] == "created by fixture"
        assert "id" in sample_post

    def test_get_all_with_fixture(self, posts_api):
        """使用fixture注入api实例"""
        response = posts_api.get_all_posts()
        assert response.status_code == 200
        assert len(response.json()) == 100
        