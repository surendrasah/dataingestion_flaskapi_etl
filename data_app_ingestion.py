from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import PrimaryKeyConstraint
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.getcwd(), 'data.db')
db = SQLAlchemy(app)

class MachineData(db.Model):
    __tablename__ = 'machine_data'
    id = db.Column(db.Integer)
    val = db.Column(db.Float)
    time = db.Column(db.Integer)
    __table_args__ = (PrimaryKeyConstraint('id','val','time'), )

class ProductionData(db.Model):
    __tablename__ = 'production_data'
    product = db.Column(db.Integer)
    production = db.Column(db.Float)
    time = db.Column(db.Integer)
    __table_args__ = (PrimaryKeyConstraint('time','product'), )

with app.app_context():
    db.create_all()

@app.route('/ingestion', methods=['POST'])
def ingestion():
    data = request.get_json()
    for item in data:
        if 'val' in item:
            existing_data = db.session.query(MachineData).filter_by(id=item['id'],val=item['val'], time=item['time']).first()
            if not existing_data:
                db.session.add(MachineData(id=item['id'], val=item['val'], time=item['time']))

        elif 'product' in item:
            existing_data = db.session.query(ProductionData).filter_by(time=item['time'], product=item['product']).first()
            if not existing_data:
                db.session.add(ProductionData(time=item['time'], product=item['product'], production=item['production']))
    db.session.commit()
    return jsonify({'message': 'Data ingested successfully!'}), 201

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=True,use_reloader=True)
