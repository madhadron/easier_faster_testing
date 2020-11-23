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