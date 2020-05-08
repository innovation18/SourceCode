import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc, func
import json
from flask_cors import CORS
from database.models import db_drop_and_create_all, setup_db, Drink, db
from auth.auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)
CORS(app)


db_drop_and_create_all()

@app.route('/drinks', methods=['GET'])
def get_drinks():
    try:
        drinks = list(map(Drink.short, Drink.query.all()))
    except Exception as e:
        abort(400, str(e))

    return jsonify(
        {
            "success": True,
            "drinks": drinks
        }
    )


@app.route('/drinks-detail', methods=['GET'])
@requires_auth('get:drinks-detail')
def get_drink_details(valid):
    if valid:
        drinks = list(map(Drink.long, Drink.query.all()))

    return jsonify(
        {
            "success": True,
            "drinks": drinks
        }
    )



@app.route('/drinks', methods=['POST'])
@requires_auth('post:drinks')
def insert_drinks(valid):
    if valid:
        new_drink = request.get_json()
        # the required datatype is [{'color': string, 'name':string, 'parts':number}]
        drink = Drink(
            title=new_drink['title'],
            recipe=json.dumps(new_drink['recipe'])
        )

        try:
            Drink.insert(drink)
        except:
            db.session.rollback()

        finally:
            return jsonify(
                {
                    'success': True,
                    'drinks': list(map(Drink.long, Drink.query.filter(Drink.title == new_drink['title']).all()))
                }
            )


@app.route('/drinks/<int:id>', methods=['PATCH'])
@requires_auth('patch:drinks')
def update_drinks(valid, id):

    if valid:
        drink = Drink.query.filter(Drink.id == id).one_or_none()

        if drink:
            new_drink = request.get_json()
            if 'title' in new_drink:
                drink.title = new_drink['title']
            if 'recipe' in new_drink:
                drink.recipe = json.dumps(new_drink['recipe'])

            try:
                Drink.update(drink)
            except Exception as e:
                db.session.rollback()

            return jsonify({
                'success': True,
                'drinks': list(map(Drink.long, Drink.query.filter(Drink.title == drink.title).all()))
            })



@app.route('/drinks/<int:id>', methods=['DELETE'])
@requires_auth('delete:drinks')
def delete_drinks(valid, id):
    if valid:
        data = Drink.query.get(id)
        if data:
            Drink.delete(data)
        else:
            raise abort(404)

        return jsonify({
            'success': True,
            'delete': id
        })



@app.errorhandler(401)
def unprocessable(error):
    return jsonify({
                    "success": False, 
                    "error": 401,
                    "message": str(error)
                    }), 401


