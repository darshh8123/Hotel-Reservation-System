from flask import Flask, render_template, request, redirect, url_for
from models import db, Room, Booking

app = Flask(__name__)

# Database setup
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hotel.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search_rooms():
    room_type = request.args.get('room_type')
    check_in = request.args.get('check_in')
    check_out = request.args.get('check_out')
    
    available_rooms = Room.query.filter_by(room_type=room_type, availability=True).all()
    return render_template('search_results.html', rooms=available_rooms)

@app.route('/book/<int:room_id>', methods=['POST'])
def book_room(room_id):
    # Similar to the example code above, you can capture booking details here.
    pass

@app.route('/pay/<int:booking_id>', methods=['POST'])
def pay_booking(booking_id):
    # Handle payment processing here with Stripe
    pass

if __name__ == '__main__':
    app.run(debug=True)
