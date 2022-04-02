import sqlite3


class DBots():
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def check(self, nick):
        with self.connection:
            res = self.cursor.execute("SELECT `nick` FROM `bots` WHERE `nick` = ?", (nick, )).fetchall()
            print(res)
            return bool(len(res))

    def reg(self, nick):
        with self.connection:
            estnick = self.cursor.execute("SELECT `nick` FROM `bots` WHERE `nick` = ?", (nick, )).fetchall()
            res = bool(len(estnick))
            if res == False:
                self.cursor.execute("INSERT INTO `bots` (`nick`) VALUES(?)", (nick, ))
            else:
                pass

