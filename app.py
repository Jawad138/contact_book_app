import os
import csv
from flask import Flask, render_template, request, redirect, url_for, flash, send_file
from flask_sqlalchemy import SQLAlchemy
from io import StringIO, BytesIO

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'contacts.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=False)

@app.route('/')
def index():
    contacts = Contact.query.all()
    return render_template('index.html', contacts=contacts)

@app.route('/add', methods=['GET', 'POST'])
def add_contact():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']

        # Check if a contact with the same phone number or email already exists
        existing_contact = Contact.query.filter(
            (Contact.phone == phone) |
            (Contact.email == email)
        ).first()

        if existing_contact:
            flash('A contact with the same phone number or email already exists!', 'danger')
            return redirect(url_for('add_contact'))

        # If no duplicate, add the new contact
        new_contact = Contact(name=name, phone=phone, email=email)
        db.session.add(new_contact)
        db.session.commit()
        flash('Contact added successfully!', 'success')
        return redirect(url_for('index'))

    return render_template('add.html')



@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_contact(id):
    contact = Contact.query.get_or_404(id)
    if request.method == 'POST':
        contact.name = request.form['name']
        contact.phone = request.form['phone']
        contact.email = request.form['email']
        db.session.commit()
        flash('Contact updated successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('edit.html', contact=contact)

@app.route('/delete/<int:id>')
def delete_contact(id):
    contact = Contact.query.get_or_404(id)
    db.session.delete(contact)
    db.session.commit()
    flash('Contact deleted successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/export')
def export_contacts():
    contacts = Contact.query.all()
    si = StringIO()
    cw = csv.writer(si)
    cw.writerow(['Name', 'Phone', 'Email'])  # Write header
    for contact in contacts:
        cw.writerow([contact.name, contact.phone, contact.email])
    output = si.getvalue()
    mem = BytesIO()
    mem.write(output.encode('utf-8'))
    mem.seek(0)  # Important: reset the BytesIO object to the beginning
    return send_file(mem,
                     mimetype='text/csv',
                     as_attachment=True,
                     download_name='contacts.csv')

def init_db():
    with app.app_context():
        db.create_all()
        print("Database initialized")

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
else:
    init_db()
