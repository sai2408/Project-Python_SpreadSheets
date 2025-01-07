from flask import Flask, render_template, request, redirect, url_for, flash
import gspread
gc = gspread.service_account("auth.json")
wks = gc.open("SampleTest").sheet1
print(wks)
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Example hardcoded credentials
        for i in range(len(wks.get_all_values())):
            k = wks.get_all_values()[i]
            if k[1] == username:
                if k[2]==password:
                    return "Login Successfull"
                else:
                    return "Wrong Password"
        else:
            return "No user found"

    return render_template('login.html')

# Register route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        print(password)
        print(confirm_password)
        if password == confirm_password:
            num_rows = len(wks.get_all_values())
            new_row_data = [name,email,password]
            wks.insert_row(new_row_data, index=num_rows + 1)
            print("Inserted sucessfully")
            return redirect(url_for('login'))
        print("Password not entered correctly")
        return redirect(url_for('register'))
    print("Not Post Method")
    return render_template('register.html')

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
