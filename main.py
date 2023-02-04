from flask import *
from datetime import datetime, timedelta
from model import *

app = Flask(__name__)
database = app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///PassTable.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_first_request
def create_database():
 with app.app_context():
    # db.drop_all()
    # db.create_all()
    outside_date = datapoints(logged_at='2022-01-28', calories=1)
    # #new_thing = Staff(first_name="sussy", last_name="baki")
    # new_ward = Ward(ward_name="sunshine ward", bed_count=201)
    # new_staff = UserModel(first_name="bam", last_name="salt", staff_role="Admin")
    # new_patient = Patient(first_name="men", last_name="yearner", address="EX19 834", DOB="15/02/2001", patient_link=new_ward, consultant_link=new_staff)
    # #db.session.add(new_thing)
    # db.session.add(new_ward)
    # db.session.add(new_patient)
    # db.session.add(new_staff)
    #db.session.add(outside_date)
    db.session.commit()

@app.route('/', methods=['POST', 'GET'])
def index():
    today = datetime.now()
    day_name = today.strftime("%A")
    month_name = today.strftime("%B")
    week_ago = today - timedelta(days=7)
    print(week_ago, today, day_name, month_name)
    table_data = datapoints.query.filter(datapoints.logged_at.between(week_ago, today)).all()
    #days_labels = [,day_name]
    days_total = [0,0,0,0,0,0,0]
    for i in table_data:
        day = i.logged_at
        all_days = day.strftime("%A")
        print(all_days)
    return render_template('index.html', data=table_data)

@app.route('/new', methods=['POST', 'GET'])
def new():
    return render_template('add.html')

@app.route('/newpatient', methods=['POST'])
def newpatient():
    if request.method == 'POST':
        with app.app_context():
            calorie = request.form['f_name']
            new_entry = datapoints(calories=calorie)
            db.session.add(new_entry)
            db.session.commit()
            return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)