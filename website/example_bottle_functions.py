import sqlite3
from bottle import route, run, get, post, request

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

