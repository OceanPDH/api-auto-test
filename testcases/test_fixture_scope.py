import pytest
from api.posts_api import PostsAPI


@pytest.fixture(scope="session")
def session_api():
    """整个测试会话只创建一次，所有测试文件共享"""
    print("\n>>> SESSION级别: 创建API实例")
    api = PostsAPI()
    yield api
    print("\n>>> SESSION级别: 销毁API实例")


@pytest.fixture(scope="module")
def module_post(session_api):
    """每个测试文件执行一次，文件内所有用例共享"""
    print("\n>>> MODULE级别: 创建测试文章")
    response = session_api.create_post(
        title="module level post",
        body="shared within this file",
        user_id=1
    )
    data = response.json()
    yield data
    print("\n>>> MODULE级别: 清理测试文章")
    session_api.delete_post(data["id"])


@pytest.fixture(scope="class")
def class_post(session_api):
    """每个测试类执行一次，类内所有用例共享"""
    print("\n>>> CLASS级别: 创建测试文章")
    response = session_api.create_post(
        title="class level post",
        body="shared within this class",
        user_id=2
    )
    data = response.json()
    yield data
    print("\n>>> CLASS级别: 清理测试文章")
    session_api.delete_post(data["id"])


@pytest.fixture(scope="function")
def function_post(session_api):
    """每个用例执行前都创建，用完就销毁"""
    print("\n>>> FUNCTION级别: 创建测试文章")
    response = session_api.create_post(
        title="function level post",
        body="only for this test",
        user_id=3
    )
    data = response.json()
    yield data
    print("\n>>> FUNCTION级别: 清理测试文章")
    session_api.delete_post(data["id"])


class TestFixtureScopeA:
    def test_module_fixture(self, module_post):
        """使用module级别fixture"""
        assert module_post["title"] == "module level post"
        print(f"  用例A1读到module_post id: {module_post['id']}")

    def test_class_fixture(self, class_post):
        """使用class级别fixture"""
        assert class_post["title"] == "class level post"
        print(f"  用例A2读到class_post id: {class_post['id']}")

    def test_class_fixture_again(self, class_post):
        """同一个class内再次使用，不会重新创建"""
        assert class_post["userId"] == 2
        print(f"  用例A3读到class_post id: {class_post['id']}（应该和A2一样）")

    def test_function_fixture_first(self, function_post):
        """function级别，每次都是新的"""
        assert function_post["title"] == "function level post"
        print(f"  用例A4读到function_post id: {function_post['id']}")

    def test_function_fixture_second(self, function_post):
        """function级别，id应该和上一个不同"""
        assert function_post["userId"] == 3
        print(f"  用例A5读到function_post id: {function_post['id']}（应该和A4不同）")


class TestFixtureScopeB:
    def test_module_same(self, module_post):
        """不同class使用module fixture，id应该和A1一样"""
        assert module_post["title"] == "module level post"
        print(f"  用例B1读到module_post id: {module_post['id']}（应该和A1一样）")

    def test_class_different(self, class_post):
        """不同class使用class fixture，会重新创建"""
        assert class_post["title"] == "class level post"
        print(f"  用例B2读到class_post id: {class_post['id']}（应该和A2不同）")