import pymysql
pymysql.install_as_MySQLdb()
try:
    from django.db.backends.mysql.operations import DatabaseOperations
    def _last_executed_query(self, cursor, sql, params):
        query = getattr(cursor, '_executed', None)
        if isinstance(query, bytes):
            query = query.decode(errors='replace')
        return query
    DatabaseOperations.last_executed_query = _last_executed_query
except Exception:
    pass
