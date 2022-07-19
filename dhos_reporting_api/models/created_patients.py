from flask_batteries_included.sqldb import db


class CreatedPatients(db.Model):
    date = db.Column(db.Date, primary_key=True, index=True)
    product_name = db.Column(db.String, primary_key=True, index=True)
    trust = db.Column(db.String, primary_key=True, index=True)
    count = db.Column(db.Integer)

    def to_dict(self) -> dict:
        return {
            "date": self.date.isoformat(),
            "product_name": self.product_name,
            "trust": self.trust,
            "count": self.count,
        }
