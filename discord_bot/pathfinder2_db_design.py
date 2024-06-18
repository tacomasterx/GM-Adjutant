import sqlite3


DB_NAME = "pathfinder2_characters"


async def create_pf_db():
    conn = sqlite3.connect(DB_NAME + ".db")
    cursor = conn.cursor()

    databases = [
        """CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        member_id INTEGER NOT NULL,
        guild_id INTEGER NOT NULL,
        UNIQUE (member_id, guild_id)
        );""",

        """CREATE TABLE IF NOT EXISTS characters (
        user_id INTEGER NOT NULL,
        name TEXT NOT NULL,
        class TEXT NOT NULL,
        dualClass TEXT NOT NULL,
        level INTEGER NOT NULL,
        ancestry TEXT NOT NULL,
        herritage TEXT NOT NULL,
        background TEXT NOT NULL,
        alignment TEXT NOT NULL,
        gender TEXT,
        age INTEGER NOT NULL,
        deity TEXT NOT NULL,
        size INTEGER NOT NULL,
        sizeName TEXT NOT NULL,
        keyability TEXT NOT NULL,
        focusPoints INTEGER NOT NULL,
        PRIMARY KEY (user_id, name),
        FOREIGN KEY ( user_id ) REFERENCES users(id)
        );""",

        """CREATE TABLE IF NOT EXISTS languages (
        id INTEGER PRIMARY KEY,
        language_list TEXT,
        character_user INTEGER NOT NULL,
        character_name TEXT NOT NULL,
        FOREIGN KEY (character_user) REFERENCES characters (user_id),
        FOREIGN KEY (character_name) REFERENCES characters (name)
        );""",

        """CREATE TABLE IF NOT EXISTS rituals (
        id INTEGER PRIMARY KEY,
        rituals_list TEXT,
        character_user INTEGER NOT NULL,
        character_name TEXT NOT NULL,
        FOREIGN KEY (character_user) REFERENCES characters (user_id),
        FOREIGN KEY (character_name) REFERENCES characters (name)
        );""",

        """CREATE TABLE IF NOT EXISTS resistances (
        id INTEGER PRIMARY KEY,
        resistances_list TEXT,
        character_user INTEGER NOT NULL,
        character_name TEXT NOT NULL,
        FOREIGN KEY (character_user) REFERENCES characters (user_id),
        FOREIGN KEY (character_name) REFERENCES characters (name)
        );""",

        """CREATE TABLE IF NOT EXISTS attributes (
        id INTEGER PRIMARY KEY,
        ancestryhp INTEGER NOT NULL,
        classhp INTEGER NOT NULL,
        bonushp INTEGER NOT NULL,
        bonushpPerLevel INTEGER NOT NULL,
        speed INTEGER NOT NULL,
        speedBonus INTEGER NOT NULL,
        character_user INTEGER NOT NULL,
        character_name TEXT NOT NULL,
        FOREIGN KEY (character_user) REFERENCES characters (user_id),
        FOREIGN KEY (character_name) REFERENCES characters (name)
        );""",

        """CREATE TABLE IF NOT EXISTS abilities (
        id INTEGER PRIMARY KEY,
        breakdown TEXT,
        str INTEGER NOT NULL,
        dex INTEGER NOT NULL,
        con INTEGER NOT NULL,
        int INTEGER NOT NULL,
        wis INTEGER NOT NULL,
        cha INTEGER NOT NULL,
        character_user INTEGER NOT NULL,
        character_name TEXT NOT NULL,
        FOREIGN KEY (character_user) REFERENCES characters (user_id),
        FOREIGN KEY (character_name) REFERENCES characters (name)
        );""",

        """CREATE TABLE IF NOT EXISTS proficiencies (
        id INTEGER PRIMARY KEY,
        classDC INTEGER NOT NULL,
        perception INTEGER NOT NULL,
        fortitude INTEGER NOT NULL,
        reflex INTEGER NOT NULL,
        will INTEGER NOT NULL,
        heavy INTEGER NOT NULL,
        medium INTEGER NOT NULL,
        light INTEGER NOT NULL,
        unarmored INTEGER NOT NULL,
        advanced INTEGER NOT NULL,
        martial INTEGER NOT NULL,
        simple INTEGER NOT NULL,
        unarmed INTEGER NOT NULL,
        castingArcane INTEGER NOT NULL,
        castingDivine INTEGER NOT NULL,
        castingOccult INTEGER NOT NULL,
        castingPrimal INTEGER NOT NULL,
        acrobatics INTEGER NOT NULL,
        arcana INTEGER NOT NULL,
        athletics INTEGER NOT NULL,
        crafting INTEGER NOT NULL,
        deception INTEGER NOT NULL,
        diplomacy INTEGER NOT NULL,
        intimidation INTEGER NOT NULL,
        medicine INTEGER NOT NULL,
        nature INTEGER NOT NULL,
        occultism INTEGER NOT NULL,
        performance INTEGER NOT NULL,
        religion INTEGER NOT NULL,
        society INTEGER NOT NULL,
        stealth INTEGER NOT NULL,
        survival INTEGER NOT NULL,
        thievery INTEGER NOT NULL,
        character_user INTEGER NOT NULL,
        character_name TEXT NOT NULL,
        FOREIGN KEY (character_user) REFERENCES characters (user_id),
        FOREIGN KEY (character_name) REFERENCES characters (name)
        );""",

        """CREATE TABLE IF NOT EXISTS mods (
        id INTEGER PRIMARY KEY,
        mods_list TEXT,
        character_user INTEGER NOT NULL,
        character_name TEXT NOT NULL,
        FOREIGN KEY (character_user) REFERENCES characters (user_id),
        FOREIGN KEY (character_name) REFERENCES characters (name)
        );""",

        """CREATE TABLE IF NOT EXISTS feats (
        id INTEGER PRIMARY KEY,
        feats_list TEXT,
        character_user INTEGER NOT NULL,
        character_name TEXT NOT NULL,
        FOREIGN KEY (character_user) REFERENCES characters (user_id),
        FOREIGN KEY (character_name) REFERENCES characters (name)
        );""",

        """CREATE TABLE IF NOT EXISTS specials (
        id INTEGER PRIMARY KEY,
        specials_list TEXT,
        character_user INTEGER NOT NULL,
        character_name TEXT NOT NULL,
        FOREIGN KEY (character_user) REFERENCES characters (user_id),
        FOREIGN KEY (character_name) REFERENCES characters (name)
        );""",

        """CREATE TABLE IF NOT EXISTS lores (
        id INTEGER PRIMARY KEY,
        lores_list TEXT,
        character_user INTEGER NOT NULL,
        character_name TEXT NOT NULL,
        FOREIGN KEY (character_user) REFERENCES characters (user_id),
        FOREIGN KEY (character_name) REFERENCES characters (name)
        );""",

        """CREATE TABLE IF NOT EXISTS equipmentContainers (
        id INTEGER PRIMARY KEY,
        equipmentContainers_list TEXT,
        character_user INTEGER NOT NULL,
        character_name TEXT NOT NULL,
        FOREIGN KEY (character_user) REFERENCES characters (user_id),
        FOREIGN KEY (character_name) REFERENCES characters (name)
        );""",

        """CREATE TABLE IF NOT EXISTS equipment (
        id INTEGER PRIMARY KEY,
        equipment_list TEXT,
        character_user INTEGER NOT NULL,
        character_name TEXT NOT NULL,
        FOREIGN KEY (character_user) REFERENCES characters (user_id),
        FOREIGN KEY (character_name) REFERENCES characters (name)
        );""",

        """CREATE TABLE IF NOT EXISTS specificProficiencies (
        id INTEGER PRIMARY KEY,
        trained_list TEXT,
        expert_list TEXT,
        master_list TEXT,
        legendary_list TEXT,
        character_user INTEGER NOT NULL,
        character_name TEXT NOT NULL,
        FOREIGN KEY (character_user) REFERENCES characters (user_id),
        FOREIGN KEY (character_name) REFERENCES characters (name)
        );""",

        """CREATE TABLE IF NOT EXISTS weapons (
        id INTEGER PRIMARY KEY,
        weapons_list TEXT,
        character_user INTEGER NOT NULL,
        character_name TEXT NOT NULL,
        FOREIGN KEY (character_user) REFERENCES characters (user_id),
        FOREIGN KEY (character_name) REFERENCES characters (name)
        );""",

        """CREATE TABLE IF NOT EXISTS money (
        id INTEGER PRIMARY KEY,
        cp INTEGER NOT NULL,
        sp INTEGER NOT NULL,
        gp INTEGER NOT NULL,
        pp INTEGER NOT NULL,
        character_user INTEGER NOT NULL,
        character_name TEXT NOT NULL,
        FOREIGN KEY (character_user) REFERENCES characters (user_id),
        FOREIGN KEY (character_name) REFERENCES characters (name)
        );""",

        """CREATE TABLE IF NOT EXISTS armor (
        id INTEGER PRIMARY KEY,
        armor_list TEXT,
        character_user INTEGER NOT NULL,
        character_name TEXT NOT NULL,
        FOREIGN KEY (character_user) REFERENCES characters (user_id),
        FOREIGN KEY (character_name) REFERENCES characters (name)
        );""",

        """CREATE TABLE IF NOT EXISTS spellCasters (
        id INTEGER PRIMARY KEY,
        spellCasters_list TEXT,
        character_user INTEGER NOT NULL,
        character_name TEXT NOT NULL,
        FOREIGN KEY (character_user) REFERENCES characters (user_id),
        FOREIGN KEY (character_name) REFERENCES characters (name)
        );""",

        """CREATE TABLE IF NOT EXISTS focus (
        id INTEGER PRIMARY KEY,
        focus_list TEXT,
        character_user INTEGER NOT NULL,
        character_name TEXT NOT NULL,
        FOREIGN KEY (character_user) REFERENCES characters (user_id),
        FOREIGN KEY (character_name) REFERENCES characters (name)
        );""",

        """CREATE TABLE IF NOT EXISTS formula (
        id INTEGER PRIMARY KEY,
        formula_list TEXT,
        character_user INTEGER NOT NULL,
        character_name TEXT NOT NULL,
        FOREIGN KEY (character_user) REFERENCES characters (user_id),
        FOREIGN KEY (character_name) REFERENCES characters (name)
        );""",

        """CREATE TABLE IF NOT EXISTS acTotal (
        id INTEGER PRIMARY KEY,
        acProfBonus INTEGER NOT NULL,
        acAbilityBonus INTEGER NOT NULL,
        acItemBonus INTEGER NOT NULL,
        acTotal INTEGER NOT NULL,
        shieldBonus INTEGER,
        character_user INTEGER NOT NULL,
        character_name TEXT NOT NULL,
        FOREIGN KEY (character_user) REFERENCES characters (user_id),
        FOREIGN KEY (character_name) REFERENCES characters (name)
        );""",

        """CREATE TABLE IF NOT EXISTS pets (
        id INTEGER PRIMARY KEY,
        pets_list TEXT,
        character_user INTEGER NOT NULL,
        character_name TEXT NOT NULL,
        FOREIGN KEY (character_user) REFERENCES characters (user_id),
        FOREIGN KEY (character_name) REFERENCES characters (name)
        );""",

        """CREATE TABLE IF NOT EXISTS familiars (
        id INTEGER PRIMARY KEY,
        familiars_list TEXT,
        character_user INTEGER NOT NULL,
        character_name TEXT NOT NULL,
        FOREIGN KEY (character_user) REFERENCES characters (user_id),
        FOREIGN KEY (character_name) REFERENCES characters (name)
        );"""
        ]

    try:
        for statement in databases:
            cursor.execute(statement)

    except sqlite3.Error as err:
        print(f'Error creating database. {err.sqlite_errorname}: {err.sqlite_errorcode}.')

    else:
        print("Successfully created or connected to database!")

    conn.close()

