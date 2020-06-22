from flask import Flask,jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager
from resources.user import Userlogin,User_reg,Sport_Registration,Team_status,Sportdetails,Reporting_time,Sport_category,Schedules

app=Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS']=True
app.config['JWT_SECRET_KEY']='group10'
app.config['PREFERRED_URL_SCHEME']='http'
api=Api(app)
jwt=JWTManager(app)
@jwt.unauthorized_loader
def missing_token_callback(error):
    return jsonify({
        'error': 'authorization_required',
        "description": "Request does not contain an access token."
    }), 401

@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify({
        'error': 'invalid_token',
        'message': 'Signature verification failed.'
    }), 401
api.add_resource(Userlogin,'/Userlogin')
api.add_resource(User_reg,'/User_reg')
api.add_resource(Sport_Registration,'/registration')
api.add_resource(Team_status,'/team_status')
api.add_resource(Sportdetails,'/sportdetails')
api.add_resource(Reporting_time,'/reporting_time')
api.add_resource(Sport_category,'/sportcategory')
api.add_resource(Schedules,'/schedule')


if __name__ == "__main__":
    app.run(debug=True)
