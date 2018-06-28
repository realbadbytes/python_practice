from DBcm import UseDatabase

dbconfig = { 'host' : '127.0.0.1',
             'user' : 'vsearch',
             'password' : 'vsearchpassword',
             'database' : 'vsearchlogDB' }

with UseDatabase(dbconfig) as cursor:

    _SQL = """insert into log
              (phrase, letters, ip, browser_string, results) 
              values
              (%s, %s, %s, %s, %s)"""

    cursor.execute(_SQL, (req.form['phrase'],
                          req.form['letters'],
                          req.remote_addr,
                          req.user_agent.browser,
                          res, ))
