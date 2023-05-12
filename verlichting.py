import time
import board
import neopixel
import sqlite3

pixels1 = neopixel.NeoPixel(board.D18, 55, brightness=1)

book_id = int(input("Id of the book: "))
conn = sqlite3.connect('belevings_ruimte.db')

to_execute_sql_command = conn.cursor()


# timing
def timing_from_databank():
    sql_query_time = """SELECT lightTiming 
                        FROM db_file.LightBook 
                        WHERE bookId = ?"""
    to_execute_sql_command.execute(sql_query_time, (book_id))

    timing = to_execute_sql_command.fetchone()
    return timing


#color
def color_from_databank():
    sql_query_color = """SELECT lightFilePath 
            FROM db_file.Light 
            WHERE lightId in
                (SELECT lightId
                 FROM LightBook 
                 WHERE bookId = ?)"""
    to_execute_sql_command.execute(sql_query_color, (book_id))

    color_tuple = tuple(map(int, sql_query_color.split(",")))
    return color_tuple


time.sleep(timing_from_databank)
pixels1.fill(color_from_databank)


