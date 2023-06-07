from flask import Flask, jsonify
from flask import request
from flask import render_template
import json
import uuid


# initialise flask server
app = Flask(__name__)

list = []


@app.route('/')
def index():
    #return "<p>Hello, and ciao !</p>"
    #json_data = json.dumps(data)
    return jsonify(data[2])
    # @TODO: hier weitermachen: herausfinden, wie man auf arrays zugreifen kann und dann weiter mit json ausgabe

# Fügt eine neue Todo-Liste hinzu
@app.route('/todo-list', methods=['POST'])
def addNewList():
    # make JSON from POST data (even if content type is not set correctly)
    new_list = request.get_json(force=True)
    print('Got new list to be added: {}'.format(new_list))
    # create id for new list, save it and return the list with id
    new_list['id'] = uuid.uuid4()
    todo_lists.append(new_list)
    return jsonify(new_list), 200

# Liefert alle Einträge einer Todo-Liste zurück.
@app.route('/todo-list/<list_id>', methods=['GET'])
def getList(list_id):
    #for list_id in data
    #return render_template('getList.html')
    json_data = json.dumps(data[list_id])
    return print(json_data)

# Löscht eine komplette Todo-Liste mit allen Einträgen
@app.route('/todo-list/<list_id>', methods=['DELETE'])
def deleteList(list_id):
    return render_template('deleteList.html')

# Fügt einen Eintrag zu einer bestehenden Todo-Liste hinzu
@app.route('/todo-list/<list_id>/entry', methods=['POST'])
def addList(list_id):
    return render_template('addList.html')

# Aktualisiert einen bestehenden Eintrag
@app.route('/todo-list/<list_id>/entry/<entry_id>', methods=['PUT'])
def updateList(list_id, entry_id):
    return render_template('updateList.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug = True)