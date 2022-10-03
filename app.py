import bottle # https://bottlepy.org/docs/dev/tutorial_app.html
import sqlite3
import re, json
from bottle import request, response
from bottle import post, get, put, delete
from tests.models import User


db = sqlite3.connect(':memory:')
db.row_factory = sqlite3.Row
db.executescript('''
    BEGIN TRANSACTION;
    CREATE TABLE wombat(id integer primary key, name varchar(128), dob date);
    INSERT INTO wombat VALUES(1,'Alice','1865-11-26');
    INSERT INTO wombat VALUES(2,'Queen','1951-07-26');
    INSERT INTO wombat VALUES(3,'Johnny','2010-03-05');
    COMMIT;
''')



@bottle.get('/')
def index():
    bottle.response.content_type = 'text/plain'
    return "Inspire Candidate Exercise"

@bottle.post('/wombats')
def save_data():
    
    # bottle.response.content_type = 'text/plain'
    # name1 = request.get_json()
    # age1 = request.forms.get('dob')
   

   #--------connect the db----------- 
    conn = sqlite3.connect('Inspire.db')
    c=conn.cursor()

    # import pdb;pdb.set_trace()
    data = request.json
    name = data['name']
    dob = data['dob']
    ids = data['id']

    c.execute('INSERT INTO LoginData (id,name,dob) VALUES("%s","%s","%s")'%(random.randint(1,1000),name,'b'))
    # CREATE TABLE LoginData (id int AUTO_INCREMENT NOT NULL, login varchar NOT NULL, password varchar NOT NULL, "loggedin" integer NOT NULL DEFAULT '0', "randStri" varchar, PRIMARY KEY(id))

    conn.commit()
    conn.close()
    print(name)


    return data






@bottle.get('/wombats')
def get_data():
    
    data = User.objects.all()
    # SELECT * FROM [table name];

    #     usernick = cursor.fetchall()
    return data



@bottle.get('/nowhere')
def nowhere():
    
    return "status_code == 404"








if __name__ == '__main__':
    import sys
    hostname = 'localhost'
    port = '8080'
    # if len(sys.argv) >= 2:
    #     hostname = sys.argv[1]
    # if len(sys.argv) >= 3:
    #     port = sys.argv[2]

    # bottle.debug()
    bottle.run(host=hostname, port=int(port)) #, reloader=True)
