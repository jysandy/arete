import psycopg2

try:
    conn = psycopg2.connect("dbname='kmain' user='xchange' host='localhost' password='(edjMOhkv7z4Qi&`t.YoLy$wARe9!B[:'")
    print("Connection Successful")
except:
    print("I am unable to connect to that database")
