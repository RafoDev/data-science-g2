from mysql import connector

class MySQLDatabase:
  def __init__(self, host, user, password, database):
    self.conn = self.connect_to_db(host, user, password, database)

  def connect_to_db(self, host, user, password, database):
    try:
      conn = connector.connect(
        host = host,
        user = user,
        password = password,
        database = database
      )
      return conn
    except Exception as error:
      print("Error: ", error)
  
  def close_conn(self):
    if self.conn.is_connected():
      self.conn.close()