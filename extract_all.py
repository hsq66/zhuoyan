#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sqlite3
import json
import html

conn = sqlite3.connect('data/ebbd52a25d7554547e1bbce925e83e90.db')
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

# 提取所有label
cursor.execute("SELECT * FROM ay_label")
labels = {}
for row in cursor.fetchall():
    labels[row['name']] = row['value']

# 提取配置
cursor.execute("SELECT * FROM ay_config")
configs = {}
for row in cursor.fetchall():
    configs[row['name']] = row['value']

# 提取公司信息
cursor.execute("SELECT * FROM ay_company WHERE acode='cn'")
company = dict(cursor.fetchone()) if cursor.fetchone() else {}
cursor.execute("SELECT * FROM ay_company WHERE acode='cn'")
company = dict(cursor.fetchone())

# 保存
with open('site_data.json', 'w', encoding='utf-8') as f:
    json.dump({
        'labels': labels,
        'configs': configs,
        'company': company
    }, f, ensure_ascii=False, indent=2)

print("提取完成！")
print(f"Labels: {len(labels)}")
print(f"Configs: {len(configs)}")
print(f"Company: {company.get('name', 'N/A')}")
