from flask import Blueprint, render_template, request, jsonify
from app.services import get_destinations, get_destination_by_id, search_destinations

main = Blueprint('main', __name__)

@main.route('/')
def index():
    destinations = get_destinations()
    return render_template('index.html', destinations=destinations)

@main.route('/destination/<int:id>')
def destination(id):
    destination = get_destination_by_id(id)
    return render_template('destination.html', destination=destination)

@main.route('/search')
def search():
    query = request.args.get('query')
    results = search_destinations(query)
    return render_template('index.html', destinations=results)
