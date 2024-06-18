import sqlite3
from pathfinder2_db_design import create_pf_db, DB_NAME

async def initialize_db():
    try:
        await create_pf_db()
    except sqlite3.Error as err:
        print(f'Error creating or loading database. {err.sqlite_errorname}: {err.sqlite_errorcode}.')
        exit(1)



async def add_user(member_id: int, guild_id: int) -> int:
    conn = sqlite3.connect(DB_NAME + ".db")
    cursor = conn.cursor()
    user_id = 0

    try: 
        result = cursor.execute("SELECT id FROM users WHERE member_id={member_id} AND guild_id={guild_id};")
        user_id = result.fetchone()
        print(f"Found {user_id}!")
    except sqlite3.Error as err:
        print(f'Error fetching user on the database.\n {err.sqlite_errorname}: {err.sqlite_errorcode}.\nProceeding to add new user...')
        user_id = 0
    
    if user_id != 0:
        print(f"User {user_id} already exists.")
        return user_id

    try: 
        print("Inserting new user...")
        cursor.execute(f"INSERT INTO users VALUES (NULL, '{member_id}', '{guild_id}')")
        result = cursor.lastrowid
        if result:
            user_id = result
            print(f"User {result} added.")
        conn.commit()
    except sqlite3.Error as err:
        print(f'Error inserting new user.\n {err.sqlite_errorname}: {err.sqlite_errorcode}.')

    conn.close()
    print(f"Final id: {user_id}")
    return user_id


async def add_character(user_id: int, character_build):
    conn = sqlite3.connect(DB_NAME + ".db")
    cursor = conn.cursor()
    character_id = 0

    try: 
        cursor.execute(f"""
                       INSERT INTO characters VALUES (
                       NULL, 
                       {character_build [ 'name' ] },
                       {character_build [ 'class' ] },
                       {character_build [ 'dualClass' ] },
                       {character_build [ 'level' ] },
                       {character_build [ 'ancestry' ] },
                       {character_build [ 'herritage' ] },
                       {character_build [ 'background' ] },
                       {character_build [ 'alignment' ] },
                       {character_build [ 'gender' ] },
                       {character_build [ 'age' ] },
                       {character_build [ 'deity' ] },
                       {character_build [ 'size' ] },
                       {character_build [ 'sizeName' ] },
                       {character_build [ 'keyability' ] },
                       {character_build [ 'focusPoints' ] },
                       {user_id},
                       )""")
        conn.commit()
        result = cursor.lastrowid
        if result:
            character_id = result
    except sqlite3.Error as err:
        print(f'Error inserting new character.\n {err.sqlite_errorname}: {err.sqlite_errorcode}.')

    conn.close()

    return character_id


