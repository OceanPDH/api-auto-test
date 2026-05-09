# API Auto Test

基于 pytest + requests 的接口自动化测试框架，针对 JSONPlaceholder API 进行测试。

## 技术栈

- Python 3.11
- pytest - 测试框架
- requests - HTTP 请求
- allure-pytest - 测试报告
- PyYAML - 数据驱动

## 项目结构
api-auto-test/
├── api/                    # 接口封装层
│   ├── base_api.py         # HTTP 方法封装（GET/POST/PUT/DELETE）
│   └── posts_api.py        # Posts 资源接口封装
├── config/                 # 配置管理
│   ├── config.py           # 配置加载
│   └── config.yaml         # 环境配置（base_url、timeout）
├── data/                   # 测试数据
│   └── posts_data.yaml     # 参数化测试数据
├── testcases/              # 测试用例
│   ├── conftest.py         # pytest fixtures
│   ├── test_posts.py       # Posts CRUD 测试（含 Allure 标签）
│   ├── test_posts_fixture.py       # Fixture 示例测试
│   └── test_posts_parametrize.py   # 数据驱动参数化测试
├── utils/                  # 工具类
│   ├── data_loader.py      # YAML 数据加载
│   └── logger.py           # 日志封装
├── .github/workflows/ci.yml  # GitHub Actions CI
├── requirements.txt
└── README.md

## 框架特性

- **分层设计**：config / api / testcase / utils 四层分离，职责清晰
- **数据驱动**：通过 YAML 文件管理测试数据，支持 pytest parametrize 参数化
- **Fixture 管理**：conftest.py 统一管理测试前置和清理逻辑
- **Allure 报告**：集成 Allure，支持 feature/story/step 分层展示
- **日志记录**：请求和响应自动记录，支持控制台和文件双输出
- **CI 集成**：GitHub Actions 自动触发测试，push 即验证

## 快速开始

```bash
# 克隆项目
git clone git@github.com:OceanPDH/api-auto-test.git
cd api-auto-test

# 创建虚拟环境
python3 -m venv venv
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt

# 运行测试
pytest testcases/ -v

# 生成 Allure 报告
pytest testcases/ -v --alluredir=reports/allure-results
allure serve reports/allure-results
```

## 测试覆盖

| 场景 | 用例数 | 说明 |
|------|--------|------|
| CRUD 基础测试 | 7 | 增删改查 + 异常 + 嵌套资源 |
| Fixture 测试 | 2 | fixture 注入和数据清理 |
| 参数化测试 | 11 | 有效/无效 ID + 多组创建数据 |
| **合计** | **20** | |

## CI

每次 push 到 main 分支自动触发测试，状态见 Actions 页面。