from flask import Flask, render_template, redirect, url_for, request, session
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_sqlalchemy import SQLAlchemy
from forms import CreateForm, LoginForm, RegisterForm
from uuid import uuid4

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

login_manager = LoginManager(app)
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column('id', db.Text(length=36), default=lambda: str(uuid4()), primary_key=True)
    username = db.Column(db.String(16))
    password = db.Column(db.String(32))


class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500), nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    has_sockets = db.Column(db.BOOLEAN, nullable=False)
    has_toilet = db.Column(db.BOOLEAN, nullable=False)
    has_wifi = db.Column(db.BOOLEAN, nullable=False)
    can_take_calls = db.Column(db.BOOLEAN, nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    coffee_price = db.Column(db.String(250), nullable=False)


db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/register')
def register():
    pass
    form = RegisterForm()
    return render_template('register.html', form=form)


@app.route('/login')
def login():
    pass
    form = LoginForm()
    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/', methods=['GET', 'POST'])
def home():
    location_filter = Cafe.query.with_entities(Cafe.location).distinct()
    page = request.args.get('page', 1, type=int)
    cafes = Cafe.query.paginate(page=page, per_page=8)

    if request.method == 'POST':
        all_cafes = db.session.query(Cafe)
        if not request.form:
            return redirect(url_for('home'))

        if request.form.getlist('amenity'):
            amenities = request.form.getlist('amenity')
            session['amenities'] = amenities
            all_cafes = all_cafes.filter_by(**{amenity: True for amenity in amenities})

        if request.form.getlist('location'):
            locations = request.form.getlist('location')
            session['location'] = locations
            all_cafes = all_cafes.filter(Cafe.location.in_(locations))

        return render_template('index.html', cafes=all_cafes.paginate(page=page, per_page=8),
                               location_filter=location_filter)
    return render_template('index.html', cafes=cafes, location_filter=location_filter)


@app.route('/add-cafe', methods=['GET', 'POST'])
# @login_required
def add_cafe():
    form = CreateForm()

    if form.validate_on_submit():
        cafe = Cafe(name=form.name.data, map_url=form.map_url.data, img_url=form.img_url.data,
                    location=form.location.data, has_sockets=form.has_sockets.data, has_toilet=form.has_toilet.data,
                    has_wifi=form.has_wifi.data, can_take_calls=form.can_take_calls.data, seats=form.seats.data,
                    coffee_price=form.coffee_price.data)
        db.session.add(cafe)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add_cafe.html', form=form)


@app.route('/update-cafe/<int:id>', methods=['GET', 'POST'])
# @login_required
def update_cafe(id):
    cafe = Cafe.query.get_or_404(id)
    form = CreateForm(obj=cafe)

    if form.validate_on_submit():
        form.populate_obj(cafe)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('update_cafe.html', cafe=cafe, form=form)


@app.route('/delete-cafe/<int:id>', methods=['GET', 'POST'])
# @login_required
def delete_cafe(id):
    cafe = Cafe.query.get_or_404(id)
    db.session.delete(cafe)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run()
