import sqlite3
from bottle import route, run, get, post, request

# what you want the website to do?
# upload user information to database from form

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




#
# def insert_user():
#     p1 = request.forms.get('Name')
#     p2 = request.forms.get('Country')
#     p3 = request.forms.get('Work')
#
#     output = try_execute_sql("INSERT INTO User_Information(Full_Name, Country, Work) VALUES \
#          ('" + p1 + ', "' + p2 + '", ' + p3 + "')")
#     if output == "":
#         output = 'Successful Insert! <br>'
#         output += '<a href="http://localhost:8080/">Back to home page</a>'
#     return output


@route('/delete/property/<property_ID>')
def delete_by_ID(property_ID):
    if not check_int(property_ID):
        return 'Property ID needs to be an integer! <br> <a href="http://localhost:8080/">Back to home search page</a>'
    conn = sqlite3.connect(database_name)
    c = conn.cursor()
    c.execute("SELECT * FROM Property WHERE Property_ID = " + property_ID)
    result = c.fetchall()
    if len(result) == 0:
        return "There are no entries with that property ID."
    c.execute("DELETE FROM Property WHERE Property_ID = " + property_ID)
    conn.commit()
    conn.close()
    output = 'Successful Delete! <br>'
    output += f'<a href="http://localhost:8080/">Back to home search page</a>'
    return output

@post('/SearchResult')
def search():
    p1 = request.forms.get('p1')
    p2 = request.forms.get('p2')
    if not (check_int(p1) or p1 ==""):
        return 'Property ID needs to be an integer! <br> <a href="http://localhost:8080/">Back to home search page</a>'
    conn = sqlite3.connect(database_name)
    c = conn.cursor()
    if p1 == "" and p2 == "":
        c.execute("SELECT * FROM Property LIMIT 20")
    if p1 != "" and p2 == "":
        c.execute("SELECT * FROM Property WHERE Property_ID = " + p1 + " LIMIT 20")
    if p1 == "" and p2 != "":
        c.execute("SELECT * FROM Property WHERE Property_Type LIKE '%" + p2 + "%' LIMIT 20")
    if p1 != "" and p2 != "":
        c.execute("SELECT * FROM Property WHERE Property_ID = " + p1 + " AND Property_Type LIKE '%" + p2 + "%' LIMIT 20")

    result = c.fetchall()
    conn.close()
    return property_results(result)

@route('/view/property/<property_ID>')
def view_by_ID(property_ID):
    conn = sqlite3.connect(database_name)
    c = conn.cursor()
    c.execute("SELECT * FROM Property WHERE Property_ID = " + property_ID)
    result = c.fetchall()[0]
    conn.close()
    output = f'Update the property with ID {property_ID} using the following form: <br>'
    output += f'''
                <form action="/UpdateProperty/{property_ID}" method="post" >
                Property_Type: <input name = "p2" type="text" list="Types" value={result[1]}>
                <datalist id="Types">
                    <option value="Residential">
                    <option value="Industrial">
                    <option value="Agricultural">
                    <option value="Commercial">
                    <option value="Government">
                </datalist>
                Acreage: <input name="p3" type="text" value="{result[2]}" />
                Estimated_Value: <input name="p4" type="text" value="{result[3]}"  />
                Assessed_Value: <input name="p5" type="text" value="{result[4]}"  />
                <input value="Update Property" type="submit" />
            </form>
    '''
    return output

@route('/viewRU/<property_ID>')
def view_by_ID(property_ID):
    conn = sqlite3.connect(database_name)
    c = conn.cursor()
    c.execute("SELECT * FROM Residential_Unit WHERE Property_ID = " + property_ID)
    result = c.fetchall()
    conn.close()
    return RU_result_to_table(result)

@route('/AddRU/<property_ID>')
def main(property_ID):
    return "Add Residential Unit to Property with ID " + property_ID + \
        f''' <br>        
            <form action="/InsertRU/{property_ID}" method="post">
                Unit_ID: <input name="p1" type="text" />
                Unit_Type: <input name="p2" type="text" />
                Sq_Footage: <input name="p3" type="text" />
                Num_Bedrooms: <input name="p4" type="text" />
                Num_Bathrooms: <input name="p5" type="text" />
                Year_Built: <input name="p6" type="text" />
                <input value="Add Unit" type="submit" />
            </form>
        '''

@route('/AddProperty')
def main():
    return "Add New Property " + \
        f''' <br>     
            <form action="/InsertProperty" method="post">
                Property_ID: <input name="p1" type="text" />
                Property_Type: <input name="p2" type="text" list="Types">
                <datalist id="Types">
                    <option value="Residential">
                    <option value="Industrial">
                    <option value="Agricultural">
                    <option value="Commercial">
                    <option value="Government">
                </datalist>
                Acreage: <input name="p3" type="text" />
                Estimated_Value: <input name="p4" type="text" />
                Assessed_Value: <input name="p5" type="text" />
                <input value="Insert Property" type="submit" />
            </form>
        '''

@post('/InsertProperty')
def insert_property():
    p1 = request.forms.get('p1')
    p2 = request.forms.get('p2')
    p3 = request.forms.get('p3')
    p4 = request.forms.get('p4')
    p5 = request.forms.get('p5')
    print("value of p2: ", p2)
    output = try_execute_sql("INSERT INTO Property (Property_ID, Property_Type, Acreage, Estimated_Value, Assessed_Value, Neighborhood_ID, Owner_ID) VALUES \
         (" + p1 + ', "' + p2 + '", ' + p3 + ', ' + p4 + ', ' + p5 + ', 0, 0)')
    if output == "":
        output = 'Successful Insert! <br>'
        output += '<a href="http://localhost:8080/">Back to home search page</a>'
    return output

@post('/UpdateProperty/<property_ID>')
def insert_property(property_ID):
    p2 = request.forms.get('p2')
    p3 = request.forms.get('p3')
    p4 = request.forms.get('p4')
    p5 = request.forms.get('p5')

    output = try_execute_sql(f'''
                            UPDATE Property 
                            SET Property_Type = "{p2}",
                                Acreage = {p3},
                                Estimated_Value = {p4},
                                Assessed_Value = {p5}   
                            WHERE
                            Property_ID = {property_ID}
                             ''')
    if output == "":
        output = 'Successful Update! <br>'
        output += '<a href="http://localhost:8080/">Back to home search page</a>'
    return output

@post('/InsertRU/<property_ID>')
def insert_RU(property_ID):
    p1 = request.forms.get('p1')
    p2 = request.forms.get('p2')
    p3 = request.forms.get('p3')
    p4 = request.forms.get('p4')
    p5 = request.forms.get('p5')
    p6 = request.forms.get('p6')
    if (not check_float(p3)):
        return 'There must be a float valued acreage. <br> <a href="http://localhost:8080/">Back to home search page</a>'
    if (not check_float(p4)) or float(p4)<0 or float(p4)>100:
        return 'There must be a float between 0 and 100 bedrooms. <br> <a href="http://localhost:8080/">Back to home search page</a>'
    if (not check_float(p5)) or float(p5)<0 or float(p5)>100:
        return 'There must be a float between 0 and 100 bedrooms. <br> <a href="http://localhost:8080/">Back to home search page</a>'
    if not check_int(p6):
        return "The year must be an integer" + '<br> <a href="http://localhost:8080/">Back to home search page</a>'
    output = try_execute_sql("INSERT INTO Residential_Unit (Residential_ID, residential_type, Sq_Footage, Num_Bedrooms, Num_Bathrooms, Year_Built, Property_ID) VALUES \
         (" + p1 + ', "' + p2 + '", ' + p3 + ', ' + p4 + ', ' + p5 + ', ' + p6 + ', ' + property_ID + ')')
    if output == "":
        output = 'Successful Insert! <br>'
        output += f'<a href="http://localhost:8080/viewRU/{property_ID}">View updated residential units for Property ID {property_ID}</a>'
        output += '<br>'
        output += f'<a href="http://localhost:8080/">Back to home search page</a>'
    return output

def property_results(result):
    out = '    <a href="http://localhost:8080/AddProperty">Insert new property</a> <br>'
    if len(result) == 0:
        return out + "No results found!"
    out += '<table>'
    for r in result:
        out += '''
         <tr> <td> Property ID: {0} </td> 
         <td> - Property type: {1} <td>
         <td> - Property estimated value: {2} <td>
         <td> - <a href="http://localhost:8080/view/property/{0}">View / Edit</a> </td> 
         <td> - <a href="http://localhost:8080/delete/property/{0}">Delete</a> </td> 
         <td> - <a href="http://localhost:8080/viewRU/{0}">Show matching Residential_Units</a> </td>
          <td> - <a href="http://localhost:8080/AddRU/{0}">Add new Residential_Unit</a> </td> </tr>
        '''.format(r[0], r[1], r[3])
    return out + '</table>'

def RU_result_to_table(result):
    if len(result) == 0:
        return "No results found!"
    out = '<table>'
    for r in result:
        out += '''
         <tr> <td> Residential Unit ID: {0} </td> 
         <td> - Residential type: {1} <td>
         <td> - Sq Footage: {2} <td>
         <td> - Num Bedrooms: {3} </td> 
         <td> - Num Bathrooms: {4} </td> 
         <td> - Year Built: {5} </td>
          <td> - On Property ID:  {6} </tr>
        '''.format(r[0], r[1], r[2], r[3], r[4], r[5], r[6])
    return out + '</table>'


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