import sqlite3
from bottle import route, run, get, post, request

database_name = 'first_database.db'
with open('homepage.html', 'r') as file:
    homepage_html = file.read().replace('\n', '')
# with open('homepage.css', 'r') as file:
#     homepage_css = file.read().replace('\n', '')
# homepage_html = homepage_html.replace('<!--CSS-PlaceHolder-->', homepage_css)

@route('/')
def homepage():
    return homepage_html

@post('/SearchUser')
def search_user():
    user_info = request.forms.get('SearchData')
    # SELECT column_name1, column_name2 FROM table_name WHERE condition
    sql_search_statement = "SELECT Full_Name, Country FROM User_Information WHERE Full_Name='" \
                           "" + user_info + "' OR Country='" + user_info + "'"
    rows = try_execute_select(sql_search_statement)

    search_results_html = ""
    for row in rows:
        search_results_html += "<tr>"
        for element in row:
            search_results_html += element + ", "
        search_results_html += "<br>"
        search_results_html += "</tr>"

    homepage_html = homepage_html.replace("<!--SearchResults-->", search_results_html)

    return homepage_html


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
