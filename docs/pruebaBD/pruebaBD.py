import sqlite3 as lite
import sys

try:
    qry = open('BDNominaMODIFICADA.sql', 'r').read()
    con = lite.connect('BDnomina.db')
    cur = con.cursor()
    cur.executescript(qry)
    con.commit()
    print "Base de Datos Creada"
except lite.Error, e:
    if con:
        con.rollback()
    print "Error %s:" % e.args[0]
    sys.exit(1)
finally:
    if con:
        con.close()

