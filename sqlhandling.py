import psycopg2

class Sql():

    conn = None
    cursor = None

    @classmethod
    def openDataBase(cls, dbname, user, host, password):

        try:
            connect_str = "dbname=%s user=%s host=%s password=%s" % (dbname, user, host, password)
            cls.conn = psycopg2.connect(connect_str)
            cls.conn.autocommit = True
        except Exception as e:
            print("Cannot open database.")
            print(e)

    @classmethod
    def writeQuery(cls, command):
        try:
            cls.cursor = cls.conn.cursor()
            cls.cursor.execute('''%s''' % command)
        except Exception as e:
            print("Invalid format.")
            print(e)

    @classmethod
    def getData(cls):
        rows = cls.cursor.fetchall()
        return rows

    @classmethod
    def runSql(cls):
        dbname = "TothBalint"
        user = "postgres"
        host = "localhost"
        password = "Fuzzwktrka88bcykjypt"
        cls.openDataBase(dbname, user, host, password)
        command = input("SELECT * FROM ")
        cls.writeQuery("SELECT * FROM " + command)
        all_info = cls.getData()
        return [a_list for list(a_list) in all_info]
