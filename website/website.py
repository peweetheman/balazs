import sqlite3
from bottle import route, run, get, post, request

database_name = 'first_database.db'

@route('/')
def homepage():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <title>Title here</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Lato">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <style>
    body,h1,h2,h3,h4,h5,h6 {font-family: "Lato", sans-serif}
    .w3-bar,h1,button {font-family: "Montserrat", sans-serif}
    .fa-file-photo-o,.fa-keyboard-o {font-size:200px}
    button {font-size: large;}
    
    #form {
      width: 250px;
      margin: 0 auto;
    }
    
    #form label {
      display: block;
      margin-bottom: 0.5em;
      font-weight: bold;
    }
    
    #form input[type="text"], #form input[type="Country"], #form input[type="Work"] {
      width: 100%;
      padding: 0.5em;
      border: 1px solid #ccc;
      box-sizing: border-box;
    }
    
    #form input[type="submit"] {
      display: block;
      margin: 1em auto;
      padding: 0.5em 2em;
      background-color: #333;
      color: #fff;
      font-weight: bold;
      border: none;
      cursor: pointer;
    }
    </style>
    </head>
    <body>
    
    
    
      <!-- Navbar on small screens -->
      <div id="navDemo" class="w3-bar-block w3-white w3-hide w3-hide-large w3-hide-medium w3-large">
        <a href="#" class="w3-bar-item w3-button w3-padding-large">Link 1</a>
        <a href="#" class="w3-bar-item w3-button w3-padding-large">Link 2</a>
        <a href="#" class="w3-bar-item w3-button w3-padding-large">Link 3</a>
        <a href="#" class="w3-bar-item w3-button w3-padding-large">Link 4</a>
      </div>
    </div>
    
    <!-- Header -->
    <header class="w3-container w3-red w3-center" style="padding:128px 16px">
      <h1 class="w3-margin w3-jumbo">Edit Title</h1>
      <p class="w3-xlarge">...................</p>
    </header>
    
    <!-- First Grid -->
    <div class="w3-row-padding w3-padding-64 w3-container">
      <div class="w3-content">
        <div class="w3-twothird">
          <h1>Scan document</h1>
          <h5 class="w3-padding-32">You can edit this part</h5>
    
          <button class="w3-button w3-black w3-padding-large w3-large w3-margin-top">Scan document</button>
        </div>
    
        <div class="w3-third w3-center">
          <i class="fa fa-file-photo-o w3-padding-64 w3-text-red"></i>
        </div>
      </div>
    </div>
    
    <!-- Second Grid -->
    <div class="w3-row-padding w3-light-grey w3-padding-64 w3-container">
      <div class="w3-content">
        <div class="w3-third w3-center">
          <i class="fa fa-keyboard-o w3-padding-64 w3-text-red w3-margin-right"></i>
        </div>
    
        <div class="w3-twothird">
          <h1>Lorem Ipsum</h1>
          <h5 class="w3-padding-32">Type your information here.</h5>
          <div>
              <form id="input_form" method="POST" action="/InsertUser")>
              <label for="Name">Full name:</label><br>
              <input type="text" id="name" name="Name"><br>
              <label for="Country">Country:</label><br>
              <input type="Country" id="Country" name="Country"><br>
              <label for="Work">Work:</label><br>
              <input type="Work" id="Work" name="Work"><br>
              <input type="submit" value="Submit">
              </form>
            </div>
        </div>
      </div>
    </div>
    
    <div class="w3-container w3-black w3-center w3-opacity w3-padding-64">
        <h1 class="w3-margin w3-xlarge">You can whrite what you want here</h1>
    </div>
    
    <!-- Footer -->
    <footer class="w3-container w3-padding-64 w3-center w3-opacity">  
      <div class="w3-xlarge w3-padding-32">
        <i class="fa fa-facebook-official w3-hover-opacity"></i>
    
        <i class="fa fa-linkedin w3-hover-opacity"></i>
     </div>
     <p>Powered by Balázs endzsin</p>
    </footer>
    
    <script>
    // Used to toggle the menu on small screens when clicking on the menu button
    function myFunction() {
      var x = document.getElementById("navDemo");
      if (x.className.indexOf("w3-show") == -1) {
        x.className += " w3-show";
      } else { 
        x.className = x.className.replace(" w3-show", "");
      }
    }
    </script>
    
    </body>
    </html>
    '''

@post('/InsertUser')
def insert_user():
    p1 = request.forms.get('Name')
    p2 = request.forms.get('Country')
    p3 = request.forms.get('Work')
    sql_statement = \
        "INSERT INTO User_Information(Full_Name, Country, Work) VALUES ('" + p1 + "', '" + p2 + "', '" + p3 + "')"
    print(sql_statement)
    output = try_execute_insert(sql_statement)

    if output != "":
        return output
    else:
        sql_statement = "SELECT * FROM User_Information"
        select_output = try_execute_select(sql_statement)
        print(select_output)
        print(type(select_output))

        html = ""
        for row in select_output:
            html += "<tr>"
            for element in row:
                html += element + ", "
            html += "<br>"
            html += "</tr>"

        # formatting HTML to return the table more nicely
        # use <tr> select_output </tr> to make a row

        return "TABLE: \n" + html


def try_execute_select(sql):
    conn = sqlite3.connect(database_name)
    c = conn.cursor()
    c.execute(sql)
    result = c.fetchall()
    conn.close()
    return result

def try_execute_insert(sql):
    conn = sqlite3.connect(database_name)
    c = conn.cursor()
    try:
        c.execute(sql)
        conn.commit()
    except sqlite3.Error as er:
        output = 'ERROR: %s' % (' '.join(er.args))
        output += '<br> Please correct the above mistake and try again!'
        output += '<br> <br> <a href="http://localhost:8080/">Back to home search page</a>'

        return output
    conn.close()
    return ""

def check_int(input):
    isInt = True
    try:
        int(input)
    except ValueError:
        isInt = False
    return isInt

def check_float(input):
    isFloat = True
    try:
        float(input)
    except ValueError:
        isFloat = False
    return isFloat

run(host='localhost', port=8080, debug=True)