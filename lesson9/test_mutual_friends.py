import os
import psycopg2
import psycopg2.sql as sql
import math
import time
from typing import Dict
import unittest

class TestCaseWithDatabase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        dbname = f'testdb{math.floor(time.time())}'
        with psycopg2.connect(dbname='postgres') as conn:
            conn.autocommit = True
            st = sql.SQL(
                'CREATE DATABASE {dbname}'
            ).format(dbname=sql.Identifier(dbname))
            with conn.cursor() as cur:
                cur.execute(st)

        conn = psycopg2.connect(dbname=dbname)
        with conn.cursor() as cur:
            cls.table_names = []
            for name, statement in cls.get_schema().items():
                cls.table_names.append(name)
                cur.execute(statement)
        cls.conn = conn
        cls.dbname = dbname

    @classmethod
    def get_schema(cls) -> Dict[str, str]:
        """Get the CREATE TABLE statements for tables."""
        raise NotImplemented(
            'Override get_schema in your subclass.'
        )

    def clear_database(self):
        # Truncate all tables in the schema. We make this
        # a separate method, as we will want to run it from
        # subTests.
        with self.conn.cursor() as cur:
            for table in self.table_names:
                st = sql.SQL(
                    'TRUNCATE TABLE {table} CASCADE'
                ).format(table=sql.Identifier(table))
                cur.execute(st)

    def teardown(self):
        self.clear_database()

    @classmethod
    def teardownClass(cls):
        cls.conn.close()
        with psycopg2.connect(dbname='postgres') as conn:
            conn.autocommit = True
            sql = sql.SQL(
                'DROP DATABASE {dbname}'
            ).format(dbname=sql.Identifier(dbname))
            with conn.cursor() as cur:
                cur.execute(sql)

from mutual_friends import mutual_friends

class TestCaseWithFriendsDatabase(TestCaseWithDatabase):
    @classmethod
    def get_schema(cls) -> Dict[str, str]:
        return {
            'people': '''CREATE TABLE people (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL
            )''',
            'friends': '''CREATE TABLE friends (
                id1 INTEGER REFERENCES people(id),
                id2 INTEGER REFERENCES people(id),
                PRIMARY KEY (id1, id2)
            )''',
        }

    def load(self, names, friendships):
        with self.conn.cursor() as cur:
            for i, name in enumerate(names):
                cur.execute(
                  'INSERT INTO people(id,name) VALUES (%s,%s)',
                  (i, name),
                )
            for (id1, id2) in friendships:
                st = 'INSERT INTO friends(id1,id2) VALUES (%s,%s)'
                cur.execute(st, (id1, id2))
                cur.execute(st, (id2, id1))
    
    def test_mutual_friends(self):
        # We don't care about names here, just need 
        # them to make the database happy.
        names = ['']*20
        cases = [ # We will always use 0 and 1 as our ids.
            ([], []),
            ([(0, 2), (1, 3)], []),
            ([(0, 2), (1, 2)], [2]),
            ([(0, 2), (0, 3), (1, 2), (1, 4)], [2]),
            ([
                (0, 2), (0, 3), (1, 2), (1, 3), 
                (0, 4), (1, 5)
             ], [2, 3]),
            ([
                (0, 2), (0, 3), (0, 4), (0, 5), 
                (0, 6), (0, 7), (0, 8), (0, 9),
                (1, 4), (1, 5), (1, 6), (1, 7), 
                (1, 8), (1, 9), (1, 10), (1, 11),
             ], [4, 5, 6, 7, 8, 9]),
        ]
        for (friendships, expected) in cases:
            with self.subTest(friendships=friendships):
                self.clear_database()
                self.load(names, friendships)
                found = mutual_friends(self.conn, 0, 1)
                self.assertEqual(expected, found)