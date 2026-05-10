import allure
import pytest
from api.posts_api import PostsAPI


@allure.feature("预期失败场景")
class TestExpectedFailures:
    def setup_method(self):
        self.api = PostsAPI()

    @allure.story("响应时间校验")
    @allure.title("验证响应时间小于100ms（预期失败）")
    def test_response_time_too_strict(self):
        with allure.step("请求文章列表"):
            response = self.api.get_all_posts()
        with allure.step("断言响应时间小于100ms"):
            assert response.elapsed.total_seconds() < 0.1, \
                f"响应时间 {response.elapsed.total_seconds():.3f}s 超过阈值 0.1s"

    @allure.story("数据校验")
    @allure.title("验证文章数量为200（预期失败）")
    def test_wrong_post_count(self):
        with allure.step("请求文章列表"):
            response = self.api.get_all_posts()
        with allure.step("断言文章数量为200"):
            data = response.json()
            assert len(data) == 200, f"实际数量 {len(data)}，预期 200"

    @allure.story("数据校验")
    @allure.title("验证文章列表正常返回（预期成功）")
    def test_post_count_correct(self):
        with allure.step("请求文章列表"):
            response = self.api.get_all_posts()
        with allure.step("断言文章数量为100"):
            data = response.json()
            assert len(data) == 100
            