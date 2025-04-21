# 区块链智能合约体验平台

<div align="center">
  <img src="https://img.shields.io/badge/Flask-v2.0+-blue.svg" alt="Flask"/>
  <img src="https://img.shields.io/badge/Web3.js-v1.5.0-orange.svg" alt="Web3.js"/>
  <img src="https://img.shields.io/badge/Moonshot%20AI-API-green.svg" alt="Moonshot AI"/>
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License"/>
</div>

## 📝 项目概述

本项目是一个基于Flask的区块链智能合约体验平台，集成了AI问答和以太坊智能合约交互功能。平台旨在为用户提供一个直观、易用的界面，探索区块链技术和智能合约的应用。

### ✨ 主要特点

- 🤖 **AI智能问答**：集成月之暗面(Moonshot)的AI模型，回答用户关于区块链技术的问题
- 🔗 **智能合约交互**：支持与以太坊智能合约的直接交互，实现数值的存储与读取
- 🔐 **钱包连接**：支持MetaMask钱包连接，安全地进行区块链交易
- 🎨 **现代化界面**：采用玻璃拟态设计风格，提供流畅的用户体验
- 🌐 **Markdown渲染**：支持AI回答中的Markdown格式显示
- 📱 **响应式设计**：适配不同屏幕尺寸的设备

## 🚀 快速开始

### 前置条件

- Python 3.7+
- MetaMask钱包浏览器扩展
- 以太坊测试网络访问能力（如Goerli、Sepolia等）

### 安装步骤

1. 克隆本仓库

```bash
git clone https://github.com/yourusername/blockchain-contract-platform.git
cd blockchain-contract-platform
```

2. 安装依赖

```bash
pip install -r requirements.txt
```

3. 配置环境变量

创建`.env`文件，添加Moonshot API密钥：

```
MOONSHOT_API_KEY=your_api_key_here
```

4. 启动应用

```bash
python app.py
```

应用将在本地运行，访问 `http://127.0.0.1:5000/` 即可使用。

## 💻 功能展示

### 1. 用户登录

- 美观的登录界面
- 简单的用户名输入即可体验平台功能

### 2. AI智能问答

- 专业的区块链知识库
- 支持复杂问题解答
- Markdown格式渲染，提升阅读体验
- 问题建议功能，帮助用户学习区块链知识

### 3. 智能合约交互

- 一键连接MetaMask钱包
- 简化的合约调用界面
- 直观的数据存储和查询操作
- 交互状态实时反馈

## 🛠️ 技术架构

### 前端技术

- HTML5/CSS3/JavaScript
- Vue.js和Element UI组件
- Web3.js与区块链交互
- Marked.js渲染Markdown内容

### 后端技术

- Flask框架
- OpenAI兼容接口
- Session管理用户状态
- 集成Moonshot大语言模型API

### 区块链技术

- 以太坊智能合约
- Web3交互接口
- MetaMask钱包集成

## 📂 项目结构

```
blockchain-contract-platform/
├── app.py                  # Flask应用主文件
├── requirements.txt        # 项目依赖
├── .env                    # 环境变量配置
├── static/                 # 静态资源
│   └── web3.min.js         # Web3.js库
└── templates/              # HTML模板
    ├── index.html          # 登录页面
    ├── main.html           # 主页面
    ├── genAI.html          # AI回答页面
    └── DApp.html           # 智能合约交互页面
```

## 🔄 使用流程

1. **登录**：输入用户名进入系统
2. **主页面**：选择AI问答或智能合约功能
3. **AI问答**：输入问题，获取AI回答
4. **智能合约**：连接钱包，进行存储和查询操作

## 📊 未来计划

- [ ] 添加更多智能合约模板（如NFT、代币交易等）
- [ ] 实现用户注册和认证系统
- [ ] 支持更多钱包类型
- [ ] 添加区块链浏览器功能
- [ ] 集成更多链（如Polygon、BSC等）

## 📜 许可证

本项目采用MIT许可证 - 详情请查看LICENSE文件

## 📞 联系方式

如有任何问题或建议，请联系：

- 邮箱：gaomingce8@gmail.com

---

<div align="center">
  <p>用❤️打造</p>
  <p>欢迎Star和Fork！</p>
</div> 