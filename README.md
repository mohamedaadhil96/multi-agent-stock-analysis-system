# 🧠 Multi-Agent Stock Analysis System for Colombo Stock Exchange

This project is a **multi-agent AI system** built using **LangGraph**, **Groq LLM**, and **MCP tools** to analyze, research, and recommend promising **Colombo Stock Exchange (CSE)** stocks for **short-term trading**.

The system uses **four intelligent agents** — each with specialized roles — coordinated by a **supervisor agent** for **end-to-end automated financial analysis**.

---

## 🚀 Features

| Feature | Description |
|--------|-------------|
| 🧩 **Multi-Agent Coordination** | Powered by **LangGraph** for dynamic workflow orchestration |
| ⚡ **Groq LLM** | Ultra-fast inference for real-time reasoning |
| 🔧 **MCP Tool Integration** | Seamless function calling via `langchain_mcp_adapters` |
| 📊 **Stock Market Research & Technical Analysis** | Fundamental + technical indicators evaluation |
| 📰 **News Summarization & Sentiment Classification** | Real-time news impact scoring |
| 💰 **Buy/Sell Recommendations with Target Prices** | Actionable trading signals with entry/exit levels |
| 🌐 **Async and Structured Execution** | Efficient, scalable, and modular design |

## 🧠 Agent Overview

| Agent Name              | Description |
|-------------------------|-------------|
| **stock_finder_agent** | Identifies **2 promising CSE-listed stocks** based on **volume, news, and performance**. |
| **market_data_agent**  | Gathers **recent market data** (price, volume, RSI, trends) for selected stocks. |
| **news_analyst_agent** | Finds and **summarizes latest stock news**, labeling sentiment as **positive**, **neutral**, or **negative**. |
| **price_recommender_agent** | Provides **Buy/Sell/Hold recommendations** and **target price suggestions**. |
| **supervisor**         | **Coordinates all agents step-by-step** to complete the workflow. |

---

> The **supervisor agent** acts as the orchestrator, ensuring structured, sequential execution across all specialized agents using **LangGraph state graphs**.


> ![Multi-Agent Stock Analysis UI](https://github.com/mohamedaadhil96/multi-agent-stock-analysis-system/blob/d1fade02a144ef556f0d66e56ec7448aaaf41942/Screenshot%202025-11-13%20153759.png)


</div>
