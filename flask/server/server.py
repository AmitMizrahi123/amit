from flask import *
from flask import request , render_template
from db import connection

app = Flask(__name__, template_folder="static")

@app.route("/document" , methods=['POST'])
def createDocument():
    try: 
        with connection.cursor() as cursor:
            sql = "INSERT INTO document (text , employeeID) VALUES (%s, %s)"
            cursor.execute(sql , (request.form["text"] , request.form["employeeId"]))
        connection.commit()
        return jsonify({'isOK':True})
    except:
        return jsonify({'isOK':False,'error':"someting went wrong"})

@app.route("/documents")
def getDocumnets():
    try: 
        with connection.cursor() as cursor:
            sql = "select text, office.name officeName , employee.name employeeName , manager.name managerName"
            sql += " from document "
            sql += "join employee on  document.employeeID = employee.employeeID "
            sql += "join manager on employee.managerID = manager.managerID "
            sql += "join office on manager.officeID = office.officeID"
            cursor.execute(sql)  
            result = cursor.fetchall()
            return jsonify(result)
    except:
        return jsonify({error:"someting went wrong"})


if __name__ == '__main__':
    app.run(debug=False)
