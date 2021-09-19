import sqlite3
import pathlib

DATABASE_FILE   =   "database.db"

FIRST_RUN   =   True
if (pathlib.Path.cwd() / DATABASE_FILE).exists():
    FIRST_RUN   =   False

CONNECTION  =   sqlite3.connect(DATABASE_FILE, check_same_thread=False)
CURSOR      =   CONNECTION.cursor()

def createDatabase():
    global CURSOR, CONNECTION

    CURSOR.execute('''
        CREATE TABLE
            textbooks (
                id INTEGER PRIMARY KEY,
                name TEXT
            )           
    ;''')

    CURSOR.execute('''
        CREATE TABLE
            chapters (
                textbookId INTEGER,
                num INTEGER,
                name TEXT
            )           
    ;''')

    CURSOR.execute('''
        CREATE TABLE
            sections (
                textbookId INTEGER,
                chapterNum INTEGER,
                sectionNum INTEGER,
                text TEXT
            )           
    ;''')

    CURSOR.execute('''
        CREATE TABLE
            tags (
                textbookId INTEGER,
                tag TEXT
            )           
    ;''')

    CONNECTION.commit()

def addTextbook(name):

    CURSOR.execute('''
        INSERT INTO
            textbooks(
                name
            )
        VALUES(
            ?
        )           
    ;''',[name]).fetchone()

    CONNECTION.commit()

    index = CURSOR.execute('''
        SELECT
            id
        FROM 
            textbooks
        ORDER BY
            id DESC
    ;''').fetchone()[0]

    return index

def getInfo(textbookId):
    name = CURSOR.execute('''
        SELECT
            name
        FROM 
            textbooks
        WHERE
            id = ?
    ;''',[textbookId]).fetchone()[0]

    chapters = CURSOR.execute('''
        SELECT
            name,
            num
        FROM 
            chapters
        WHERE
            textbookId = ?
    ;''',[textbookId]).fetchall()

    data = [name]

    for chapter in chapters:
        chapterName = chapter[0]
        chapterNum  = chapter[1]

        chapterContent = CURSOR.execute('''
            SELECT
                text
            FROM 
                chapters
            WHERE
                textbookId = ?,
                chapterNum = ?
            ORDER BY
                sectionNum ASC
        ;''',[textbookId,chapterNum]).fetchall()

        data.append(chapterContent)

    print(data)
    return data

def getUsersBooks():
    global CURSOR
    books = CURSOR.execute('''
        SELECT
            *
        FROM
            textbooks
        ORDER BY
            id DESC    
    ;''').fetchall()
    return books

if FIRST_RUN == True:
    createDatabase()