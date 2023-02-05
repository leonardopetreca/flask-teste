from flask import Flask, render_template,request
import gspread as gp

#connect to google sheet
gc =  gp.service_account('secrets.json')
spreadsheet = gc.open('Employee')
global counter_lead 

counter_lead =1

app = Flask(__name__)

@app.route("/")
def home():
    
    #print(data)
    return render_template("index.html")


@app.route("/",methods=['POST'])
def home_post():
   # counter_lead = counter_lead+1
    nome = request.form['nome']
    tel = request.form['tel']
    email = request.form['email']
    print(nome, tel, email)
    
    lead=list([nome,tel, email])
    

    
    worksheet= spreadsheet.get_worksheet(0)
    data = worksheet.get_all_values()
    
    cols =int(len(data[0]))+1
    row = len(data)+1 
    count =0
    
    
    for i in range(1,cols):
        worksheet.update_cell(row, i, lead[i-1])
            
        


    return render_template("index.html", nomef =nome, telf =tel, emailf =email)


app.run(host='0.0.0.0')
