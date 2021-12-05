from flask import jsonify, request
from flask.views import MethodView
from app import db, app
from models import Ad
from schema import AD_CREATE
from validator import validate


class AdView(MethodView):
    def get(self, ad_id):
        ad = Ad.query.get(ad_id)
        return jsonify(ad.to_dict())

    @validate('json', AD_CREATE)
    def post(self):
        ad = Ad(**request.json)
        db.session.add(ad)
        db.session.commit()
        return jsonify(ad.to_dict())

    def delete(self, ad_id):
        ad = Ad.query.get(ad_id)
        db.session.delete(ad)
        db.session.commit()
        return f'Объект {ad.title} автора {ad.owner} удален'


app.add_url_rule('/ads/<int:ad_id>', view_func=AdView.as_view('ads_get'), methods=['GET', ])
app.add_url_rule('/ads/', view_func=AdView.as_view('ads_create'), methods=['POST', ])
app.add_url_rule('/ads/delete/<int:ad_id>', view_func=AdView.as_view('ads_delete'), methods=['DELETE', ])