from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime


app = Flask(__name__)


# MongoDB Connection
client = MongoClient("mongodb://localhost:27017/")

db = client["expense_tracker"]

expenses_collection = db["expenses"]



# Home Page
@app.route('/')
def home():

    total_expenses = expenses_collection.count_documents({})

    total_amount = 0

    for expense in expenses_collection.find():
        total_amount += expense.get("amount", 0)

    print("TOTAL EXPENSES:",total_expenses)
    print("TOTAL AMOUNT:",total_amount)    


    return render_template(
        "index.html",
        total_expenses=total_expenses,
        total_amount=total_amount
    )



# Add Expense
@app.route('/add', methods=['GET', 'POST'])
def add():

    if request.method == 'POST':

        title = request.form['title']
        amount = request.form['amount']
        category = request.form['category']


        expense = {

            "title": title,
            "amount": float(amount),
            "category": category,
            "date": datetime.now().strftime("%d-%m-%Y")

        }


        expenses_collection.insert_one(expense)


        return redirect('/view')


    return render_template("add.html")



# View + Search Expenses
@app.route('/view')
def view():

    search = request.args.get('search')


    if search:

        expenses = list(expenses_collection.find(
            {
                "$or": [

                    {
                        "title": {
                            "$regex": search,
                            "$options": "i"
                        }
                    },

                    {
                        "category": {
                            "$regex": search,
                            "$options": "i"
                        }
                    }

                ]
            }
        ))

    else:

        expenses =list (expenses_collection.find())



    return render_template(
        "view.html",
        expenses=expenses
    )



# Delete Expense
@app.route('/delete/<id>')
def delete(id):

    expenses_collection.delete_one(
        {
            "_id": ObjectId(id)
        }
    )


    return redirect('/view')



# Edit Expense
@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):

    if request.method == 'POST':

        title = request.form['title']
        amount = request.form['amount']
        category = request.form['category']


        expenses_collection.update_one(
            {"_id": ObjectId(id)},
            {
                "$set": {
                    "title": title,
                    "amount": float(amount),
                    "category": category
                }
            }
        )


        return redirect('/view')


    expense = expenses_collection.find_one(
        {
            "_id": ObjectId(id)
        }
    )


    return render_template(
        "edit.html",
        expense=expense
    )



if __name__ == '__main__':

    app.run(debug=True)
Displaying app.py.
