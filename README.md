City Risk Analysis System
城市风险分析与空间数据处理系统

这是一个基于 PostgreSQL、SQL、Pandas 和 GeoPandas 构建的城市风险数据分析项目。
项目实现了从数据库读取、SQL 联表查询、数据质量校验、风险等级分类，到空间数据构建、城市距离分析和 GeoJSON 导出的完整流程。
---
1. 项目背景

城市风险分析通常需要同时处理：
- 风险指标
- 城市人口
- 城市空间位置

本项目使用 PostgreSQL 管理城市风险和人口数据，
通过 SQL JOIN 获取统一分析数据，并使用 Python 完成
数据验证、风险分类和空间分析。
---

2. 系统流程

PostgreSQL
 ↓
SQL JOIN
 ↓
Pandas DataFrame
↓
Data Validation
 ↓
Risk Classification
↓
GeoPandas Spatial Analysis
↓
CSV / GeoJSON Output
