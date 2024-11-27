from flask import Flask, request, jsonify
import MySQLdb

db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="1234", db="cloud")

app = Flask(__name__)

def save_data_to_db(data):
    try:
        cursor = db.cursor()
        # Assuming 'data' is a dictionary with keys: datetime, temp, humi, node_id, device
        query = "INSERT INTO data (datetime, temp, humi, node_id, device) VALUES (%s, %s, %s, %s, %s)"
        values = (data['datetime'], data['temp'], data['humi'], data['node_id'], data['device'])
        cursor.execute(query, values)
        db.commit()
        cursor.close()
        return True
    except Exception as e:
        print(f"Error saving data to database: {e}")
        db.rollback()
        return False

@app.route('/save', methods=['POST'])
def save():
    try:
        data = request.json
        if save_data_to_db(data):
            return jsonify({"message": "Data saved successfully"}), 200
        else:
            return jsonify({"message": "Failed to save data"}), 500
    except Exception as e:
        print(f"Error processing request: {e}")
        return jsonify({"message": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(debug=True)
