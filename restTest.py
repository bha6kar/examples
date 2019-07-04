from flask import Flask, jsonify, render_template, request
import requests
app = Flask(__name__)

all_records = [
    {
        'name': 'Radiohead',
        'albums': [
            {
                'title': 'First album',
                'songs': 'First song'
            }, {
                'title': 'Second album',
                'songs': 'Second song'
            }
        ]
    },
    {
        'name': 'MJ',
        'albums': [
            {
                'title': 'first MJ album',
                'songs': 'List mj'
            },
            {
                'title': 'second album',
                'songs': 'sewce'
            }
        ]
    }
]

crime_url_template = 'https://data.police.uk/api/crimes-street/all-crime?lat={lat}&lng={lng}&date={data}'


@app.route('/')
def tests():
    return '<h4>HJe</h4>'


@app.route('/getall', methods=['GET'])
def get_all():
    return jsonify(all_records)


@app.route('/a', methods=['GET'])
def album():
    respons = [i['name']for i in all_records]
    return jsonify(respons)


@app.route('/get/<album_name>', methods=['GET'])
def get_album(album_name):
    for item in all_records:
        if item['name'] == album_name:
            respons = [i['title'] for i in item['albums']]
            return jsonify(respons)


@app.route('/ext', methods=['GET'])
def extg():
    my_latitude = request.args.get('lat', '51.52369')
    my_longitude = request.args.get('lng', '-0.0395857')
    my_date = request.args.get('date', '2018-11')

    crime_url = crime_url_template.format(
        lat=my_latitude, lng=my_longitude, data=my_date)
    print(crime_url)
    respons = requests.get(crime_url)
    if respons.ok:

        return jsonify(respons.json())
    else:
        return respons.reason


if __name__ == '__main__':
    app.run(debug=True)
