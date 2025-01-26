from flask import Flask,render_template
app=Flask(__name__)
@app.route("/")
def home():
    list1 =[1,2,3,4,5]
    result=True
    return render_template("index.html",list1=list1,result=result)

   
@app.route("/p")
def product():
    return render_template("product.html")
if __name__=="__main__":
    app.run(debug=True)