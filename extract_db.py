#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sqlite3
import json

# 连接数据库
conn = sqlite3.connect('data/ebbd52a25d7554547e1bbce925e83e90.db')
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

# 提取所有内容
cursor.execute("""
    SELECT id, scode, title, subtitle, author, source, keywords, description, content 
    FROM ay_content 
    WHERE status=1 
    ORDER BY scode, sorting DESC
""")

contents = []
for row in cursor.fetchall():
    contents.append({
        'id': row['id'],
        'scode': row['scode'],
        'title': row['title'],
        'subtitle': row['subtitle'],
        'description': row['description'],
        'content': row['content']
    })

# 保存为JSON
with open('content_data.json', 'w', encoding='utf-8') as f:
    json.dump(contents, f, ensure_ascii=False, indent=2)

# 提取分类
cursor.execute("SELECT * FROM ay_content_sort ORDER BY scode")
sorts = []
for row in cursor.fetchall():
    sorts.append(dict(row))

with open('sorts_data.json', 'w', encoding='utf-8') as f:
    json.dump(sorts, f, ensure_ascii=False, indent=2)

# 提取标签
cursor.execute("SELECT * FROM ay_label")
labels = []
for row in cursor.fetchall():
    labels.append(dict(row))

with open('labels_data.json', 'w', encoding='utf-8') as f:
    json.dump(labels, f, ensure_ascii=False, indent=2)

conn.close()
print("数据提取完成！")
print(f"共提取 {len(contents)} 篇内容")
print(f"共提取 {len(sorts)} 个分类")
print(f"共提取 {len(labels)} 个标签")
