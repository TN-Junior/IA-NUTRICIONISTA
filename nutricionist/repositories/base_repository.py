from tinydb import table
from nutricionist.database.engine import Engine



class BaseRepository(Engine):
  def get_table(self, table_name: str) -> Table.Table:
    return self.db.table(table_name)
  