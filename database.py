import sqlite3

class Database:
    def __init__(self):
        self.con = sqlite3.connect('db.sqlite3')
        self.cursor = self.con.cursor()

    def add_booking(self, user, date, doctor):
        self.cursor("INSERT INTO booking_booking (user, time, doctor) VALUES (?, ?, ?)", (user, date, doctor))
        self.con.commit()