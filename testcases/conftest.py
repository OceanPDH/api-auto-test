import pytest
from api.posts_api import PostsAPI


@pytest.fixture
def posts_api():
    return PostsAPI()


@pytest.fixture
def sample_post(posts_api):
    """创建一个临时文章，供测试使用，测试结束后清理"""
    response = posts_api.create_post(
        title="fixture post",
        body="created by fixture",
        user_id=1
    )
    data = response.json()
    yield data
    # teardown: 清理数据
    posts_api.delete_post(data["id"])
    