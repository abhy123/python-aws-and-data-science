import json
from flask_lambda import FlaskLambda
from flask import request
import boto3

app = FlaskLambda(__name__)
ddb = boto3.resource('dynamodb')
table = ddb.Table('students')

@app.route('/')
def index():
    data = {
        "message":  "Hello, World"
    }
    return (
        json.dumps(data),
        200,
        {'Content-Type': "application/json"}
    )

@app.route('/students', methods = ['GET', 'POST'])
def put_or_list_students():
    if request.method == 'GET':
        students = table.scan()['Items']
        return (
            json.dumps(students),
            200,
            {'Content-Type': "application/json"}
        )
    else:
        table.put_item(Item=request.form.to_dict())
        return (
            json.dumps({"message": "student entry created"}),
            200,
            {'Content-Type': "application/json"}
        )

@app.route('/students/<id>', methods=['GET','DELETE','PATCH'])
def get_delete_patch_student(id):
    if request.method == 'GET':
        student = table.get_item(Key={'id': id})['Item']
        return (
            json.dumps(student),
            200,
            {'Content-Type': "application/json"}
        )
    elif request.method == 'DELETE':
        table.delete_item(Key={'id': id})
        return (
            json.dumps({'message': 'student entry deleted'}),
            200,
            {'Content-Type': "application/json"}
        )
