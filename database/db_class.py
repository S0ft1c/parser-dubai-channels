import sqlite3


class Database:
    def __init__(self):
        self.conn = sqlite3.connect("database.sqlite3")
        self.cursor = self.conn.cursor()

        # create table for channels
        self.cursor.execute("""create table if not exists channels (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        channel text
        )""")

        # create table for phrases
        self.cursor.execute("""create table if not exists phrases (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        phrase text
        )""")

    def execute(self, query, params=()):
        self.cursor.execute(query, params)
        self.conn.commit()

    def fetchall(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def fetchone(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchone()

    def __del__(self):
        self.conn.close()


db = Database()
# for el in ["@Dubai_chat", "@relocation_dubai", "@DubaiChatik", "@chatrudubai",
#            "@crypto_dybai", "@Exchange_Dubaii", "@dubaitravellers",
#            "@Exchange_Dubaii", "@UAE_chat", "@livingindubai", "@vakansii_oae",
#            "@forumdubai", "@russkie_v_dubae_choogl", "@biznesuae", "@LIFE_inDUBAI",
#            "@russkie_v_oae", "@oae_rabota", "@beauty_services_dubai", "@sblokong",
#            "@chat_dubai", "@obmen_Dubai11", "@rcDUBAI_2022", "@chatrussianemirates",
#            "@womanDubai", "@Real_Life_UAE", "@russiandxb", "@freelancedubai",
#            "@kazakhindubai", "@advertisinguae", "@dubai_rr", "@vopros_otvet_dubai",
#            "@dubaieeexpats", "@uae_lawyer", "@exchange_dubai_chat", "@Change_OAE",
#            "@dirham_dubai", "@dubai_russo"]:
#     db.execute("INSERT INTO channels (channel) VALUES (?)", (el,))

# print(db.fetchall("SELECT * FROM channels"))

# for el in "Куплю дирхамы, продам рубль, продам usdt, перевод, Тинькофф, тинек, сбер, обмен, обменять деньги, наличка, наличные, обменник, rub, Aed, обменяю, поменять, перевести рубли, usdt, тезер, доллары, обналичить, обнал".split(", "):
#     db.execute("INSERT INTO phrases (phrase) VALUES (?)", (el,))

# print(db.fetchall("SELECT * FROM phrases"))
