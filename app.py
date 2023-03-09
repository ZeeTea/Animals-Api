from flask import Flask, jsonify

app = Flask(__name__)

Bears = [{
    'Sceintific_Name' : 'Ursidae',
    'Types' : 'Mammals',
    'Diet' : 'Omnivore',
    'Size' : '4 to 8 feet tall',
    'Weight' : '60 to 1,600'
}]

Sloth = [{
    'Sceintific_Name': 'Bradypus',
    'Types': 'Mammals',
    'Diet': 'Herbivore',
    'Size': '23 inches',
    'Weight': '8.75 pounds'
}]

Arctic_Fox = [{
    'Sceintific_Name': 'Vulpes_Lagopus',
    'Types': 'Mammals',
    'Diet': 'Omnivore',
    'Size': 'Head and body: 18 to 26.75 inches',
    'Weight': '6.5 to 17 pounds'
}]

@app.route('/')
def index():
    return "LETS TALK ABOUT ANIMALS PEOPLE!"

@app.route('/bears', methods=['GET'])
def get():
    return jsonify({'Bears':Bears})

@app.route('/sloth', methods=['GET'])
def get_s():
    return jsonify({'sloth':Sloth})

@app.route('/arctic_fox', methods=['GET'])
def get_a():
    return jsonify({'arctic_fox':Arctic_Fox})

if __name__ == '__main__':
    app.run()