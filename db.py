import sqlite3
import json


def create_and_fill_db():
    try:
        sqlite_connection = sqlite3.connect('profile.db')
        cursor = sqlite_connection.cursor()
        
        with open('sql_scripts/create_table.sql', 'r') as f:
            create_table = f.read()
        cursor.executescript(create_table)
        
        if len(get_profiles()) == 0:
            with open('sql_scripts/fill_table.sql', 'r') as f:
                fill_table = f.read()
            
            for _ in range(15):
                cursor.executescript(fill_table)

        cursor.close()

    except sqlite3.Error as error:
        print('SQLite connection error')
    finally:
        if (sqlite_connection):
            sqlite_connection.close()


def update_cookie(profile_id, cookies):
    try:
        sqlite_connection = sqlite3.connect('profile.db')
        cursor = sqlite_connection.cursor()

        with open('sql_scripts/update_profile.sql', 'r') as f:
            update_query = f.read()

        cookies_json = json.dumps(cookies)
        data = (cookies_json, profile_id)
        cursor.execute(update_query, data)
        sqlite_connection.commit()

        cursor.close()

    except sqlite3.Error as error:
        print(error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()

def get_profiles():
    try:
        sqlite_connection = sqlite3.connect('profile.db')
        cursor = sqlite_connection.cursor()

        with open('sql_scripts/get_profiles.sql', 'r') as f:
            get_profiles_query = f.read()

        cursor.execute(get_profiles_query)
        profiles = cursor.fetchall()

        cursor.close()

    except sqlite3.Error as error:
        print('Failed to get profiles')
    finally:
        if (sqlite_connection):
            sqlite_connection.close()

    return profiles
