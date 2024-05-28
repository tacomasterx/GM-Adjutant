import sqlite3

dbname = "pathfinder2_character"
conn = sqlite3.connect(dbname + ".db")
cursor = conn.cursor()

databases = [
        """CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        member_id INTEGER NOT NULL,
        guild_id INTEGER NOT NULL
        );""",

        """CREATE TABLE IF NOT EXISTS characters (
        id INTEGER PRIMARY KEY,
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
        user_id INTEGER NOT NULL,
        FOREIGN KEY ( user_id ) REFERENCES users(id)
        );""",

        """CREATE TABLE IF NOT EXISTS languages (
        id INTEGER PRIMARY KEY,
        character_id INTEGER NOT NULL,
        language_list TEXT,
        FOREIGN KEY (character_id) REFERENCES characters (id)
        );""",

        """CREATE TABLE IF NOT EXISTS rituals (
        id INTEGER PRIMARY KEY,
        character_id INTEGER NOT NULL,
        rituals_list TEXT,
        FOREIGN KEY (character_id) REFERENCES characters (id)
        );""",

        """CREATE TABLE IF NOT EXISTS resistances (
        id INTEGER PRIMARY KEY,
        character_id INTEGER NOT NULL,
        resistances_list TEXT,
        FOREIGN KEY (character_id) REFERENCES characters (id)
        );""",

        """CREATE TABLE IF NOT EXISTS attributes (
        id INTEGER PRIMARY KEY,
        character_id INTEGER NOT NULL,
        ancestryhp INTEGER NOT NULL,
        classhp INTEGER NOT NULL,
        bonushp INTEGER NOT NULL,
        bonushpPerLevel INTEGER NOT NULL,
        speed INTEGER NOT NULL,
        speedBonus INTEGER NOT NULL,
        FOREIGN KEY (character_id) REFERENCES characters (id)
        );""",

        """CREATE TABLE IF NOT EXISTS abilities (
        id INTEGER PRIMARY KEY,
        character_id INTEGER NOT NULL,
        breakdown TEXT,
        str INTEGER NOT NULL,
        dex INTEGER NOT NULL,
        con INTEGER NOT NULL,
        int INTEGER NOT NULL,
        wis INTEGER NOT NULL,
        cha INTEGER NOT NULL,
        FOREIGN KEY (character_id) REFERENCES characters (id)
        );""",

        """CREATE TABLE IF NOT EXISTS proficiencies (
        id INTEGER PRIMARY KEY,
        character_id INTEGER NOT NULL,
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
        FOREIGN KEY (character_id) REFERENCES characters (id)
        );""",

        """CREATE TABLE IF NOT EXISTS mods (
        id INTEGER PRIMARY KEY,
        character_id INTEGER NOT NULL,
        mods_list TEXT,
        FOREIGN KEY (character_id) REFERENCES characters (id)
        );""",

        """CREATE TABLE IF NOT EXISTS feats (
        id INTEGER PRIMARY KEY,
        character_id INTEGER NOT NULL,
        feats_list TEXT,
        FOREIGN KEY (character_id) REFERENCES characters (id)
        );""",

        """CREATE TABLE IF NOT EXISTS specials (
        id INTEGER PRIMARY KEY,
        character_id INTEGER NOT NULL,
        specials_list TEXT,
        FOREIGN KEY (character_id) REFERENCES characters (id)
        );""",

        """CREATE TABLE IF NOT EXISTS lores (
        id INTEGER PRIMARY KEY,
        character_id INTEGER NOT NULL,
        lores_list TEXT,
        FOREIGN KEY (character_id) REFERENCES characters (id)
        );""",

        """CREATE TABLE IF NOT EXISTS equipmentContainers (
        id INTEGER PRIMARY KEY,
        character_id INTEGER NOT NULL,
        equipmentContainers_list TEXT,
        FOREIGN KEY (character_id) REFERENCES characters (id)
        );""",

        """CREATE TABLE IF NOT EXISTS equipment (
        id INTEGER PRIMARY KEY,
        character_id INTEGER NOT NULL,
        equipment_list TEXT,
        FOREIGN KEY (character_id) REFERENCES characters (id)
        );""",

        """CREATE TABLE IF NOT EXISTS specificProficiencies (
        id INTEGER PRIMARY KEY,
        character_id INTEGER NOT NULL,
        trained_list TEXT,
        expert_list TEXT,
        master_list TEXT,
        legendary_list TEXT,
        FOREIGN KEY (character_id) REFERENCES characters (id)
        );""",

        """CREATE TABLE IF NOT EXISTS weapons (
        id INTEGER PRIMARY KEY,
        character_id INTEGER NOT NULL,
        weapons_list TEXT,
        FOREIGN KEY (character_id) REFERENCES characters (id)
        );""",

        """CREATE TABLE IF NOT EXISTS money (
        id INTEGER PRIMARY KEY,
        character_id INTEGER NOT NULL,
        cp INTEGER NOT NULL,
        sp INTEGER NOT NULL,
        gp INTEGER NOT NULL,
        pp INTEGER NOT NULL,
        FOREIGN KEY (character_id) REFERENCES characters (id)
        );""",

        """CREATE TABLE IF NOT EXISTS armor (
        id INTEGER PRIMARY KEY,
        character_id INTEGER NOT NULL,
        armor_list TEXT,
        FOREIGN KEY (character_id) REFERENCES characters (id)
        );""",

        """CREATE TABLE IF NOT EXISTS spellCasters (
        id INTEGER PRIMARY KEY,
        character_id INTEGER NOT NULL,
        spellCasters_list TEXT,
        FOREIGN KEY (character_id) REFERENCES characters (id)
        );""",

        """CREATE TABLE IF NOT EXISTS focus (
        id INTEGER PRIMARY KEY,
        character_id INTEGER NOT NULL,
        focus_list TEXT,
        FOREIGN KEY (character_id) REFERENCES characters (id)
        );""",

        """CREATE TABLE IF NOT EXISTS formula (
        id INTEGER PRIMARY KEY,
        character_id INTEGER NOT NULL,
        formula_list TEXT,
        FOREIGN KEY (character_id) REFERENCES characters (id)
        );""",

        """CREATE TABLE IF NOT EXISTS acTotal (
        id INTEGER PRIMARY KEY,
        character_id INTEGER NOT NULL,
        acProfBonus INTEGER NOT NULL,
        acAbilityBonus INTEGER NOT NULL,
        acItemBonus INTEGER NOT NULL,
        acTotal INTEGER NOT NULL,
        shieldBonus INTEGER,
        FOREIGN KEY (character_id) REFERENCES characters (id)
        );""",

        """CREATE TABLE IF NOT EXISTS pets (
        id INTEGER PRIMARY KEY,
        character_id INTEGER NOT NULL,
        pets_list TEXT,
        FOREIGN KEY (character_id) REFERENCES characters (id)
        );""",

        """CREATE TABLE IF NOT EXISTS familiars (
        id INTEGER PRIMARY KEY,
        character_id INTEGER NOT NULL,
        familiars_list TEXT,
        FOREIGN KEY (character_id) REFERENCES characters (id)
        );"""
        ]

try:
    for statement in databases:
        cursor.execute(statement)

except sqlite3.Error as err:
    print(f'Error creating database. {err.sqlite_errorname}: {err.sqlite_errorcode}.')

conn.close()

