from sqlalchemy import create_engine, MetaData
engine = create_engine('mysql+pymysql://root:cube12@localhost:3306/cube_db')
# engine = create_engine(
#       "mysql+pymysql://root:cube12@127.0.0.1/cube_db?host=localhost?port=3306")
meta = MetaData()
conn = engine.connect()