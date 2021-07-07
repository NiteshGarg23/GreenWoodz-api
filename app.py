from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Test run"

@app.route("/vendors")
def show_vendors():
    vendors = {
        "vendors": [
            {
                "id": 1,
                "title": "Recycling Solutions Pvt Ltd",
                "address": "Pramukh Plaza, FF-11, opp. Voltamp Company, near Maneja, Crossing, Maneja",
                "services": ["waste", "ewaste", "home service"],
                "img": "https://lh5.googleusercontent.com/p/AF1QipOOFoSyrf7oPStTJJPRMv-6R4MPTJOuj4Cs7K6N=s338-k-no" 
            },
            {
                "id": 2,
                "title": "Tierra Recycling",
                "address": "Ajwa Rd, Jalram Nagar, Madhavpura",
                "services": ["waste collection", "hazardous waste disposal", "regular collections"],
                "img": "https://img.uenicdn.com/image/upload/v1542047185/category/shutterstock_434026039.jpg" 
            }
        ]
    }
            
    return vendors

if __name__ == "__main__":
    app.run(debug=True)