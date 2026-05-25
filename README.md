# newonboarding

一个最小可运行代码库，支持连接到本地（SQLite）数据文件。

## 本地构建与运行

```bash
python -m py_compile local_connection.py
python -m unittest -v test_local_connection.py
```

## 快速使用

```python
from local_connection import connect_local_repository, add_repository_item, list_repository_items

conn = connect_local_repository("data/local_repository.db")
add_repository_item(conn, "newonboarding")
print(list_repository_items(conn))
conn.close()
```