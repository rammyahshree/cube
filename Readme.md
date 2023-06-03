/Users/ramyashree.dr/cube/.venv/bin/python3 -m pip install --upgrade pip
pip install fastapi sqlalchemy pymysql uvicorn



Database
docker run --name cube-mysql -e MYSQL_ROOT_PASSWORD=cube12 -d -p 3306:3306 mysql:latest


 Database           |
+--------------------+
| cube_db