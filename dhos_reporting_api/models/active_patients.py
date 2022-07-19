from flask_batteries_included.sqldb import db


class ActivePatients(db.Model):
    year_week = db.Column(db.String, primary_key=True, index=True)
    product_name = db.Column(db.String, primary_key=True, index=True)
    trust = db.Column(db.String, primary_key=True, index=True)
    count = db.Column(db.Integer)

    def to_dict(self) -> dict:
        return {
            "year_week": self.year_week,
            "product_name": self.product_name,
            "trust": self.trust,
            "count": self.count,
        }
