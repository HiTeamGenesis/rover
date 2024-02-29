import logger
from colorama import init, Fore, Back, Style
from flask import Flask, request, jsonify
from control import move_wrapper

init(autoreset=True)

app = Flask(__name__)

@app.route('/wrapper', methods=['GET'])
def get_wrapper():
    logger.info("Received GET request on /wrapper")
    return jsonify({'message': 'This is the /wrapper endpoint'})

@app.route('/move', methods=['POST'])
def move():
    data = request.json
    distance = data.get('distance')
    if distance is None:
        logger.error("No distance provided in the request body")
        return jsonify({'error': 'Distance is required in the request body'}), 400
    move_wrapper(distance)
    logger.info(f"Moving {distance} units")

    return jsonify({'message': f'Moving {distance} units'})

if __name__ == '__main__':
    logger.info("Starting Rover...")
    app.run(debug=True)
