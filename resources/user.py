from flask_restful import Resource,reqparse
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import create_access_token,jwt_required
from db import query

class Userlogin(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('user_name',type=str,required=True,help=" username cannot be left blank!")
    parser.add_argument('password_',type=str,required=True,help="Password cannot be left blank!")
    
    def post(self):
        data=self.parser.parse_args()
        user=User.getUserById(data['user_name'])
        if user and safe_str_cmp(user.password_,data['password_']):
            access_token=create_access_token(identity=user.user_name,expires_delta=False)
            return {'access_token':access_token},200
        return {"message":"Invalid Credentials!"}, 401
class User():
    def __init__(self,user_name,password_):
        self.user_name=user_name
        self.password_=password_
    @classmethod
    def getUserById(cls,user_name):
        result=query(f"""select user_name,password_ from users where user_name='{user_name}'""",return_json=False)
        if len(result)>0:
            return User(result[0]['user_name'],result[0]['password_'])
        else:
            return None

class User_reg(Resource):#user registration

    def post(self):
        parser=reqparse.RequestParser()
        parser.add_argument('user_id',type=int,required=True,help="user_id cannot be left blank!")
        parser.add_argument('user_name',type=str,required=True,help="user_name cannot be left blank!")
        parser.add_argument('phone_num',type=int,required=True,help="phone_num cannot be left blank!")
        parser.add_argument('password_',type=str,required=True,help="password_ cannot be left blank!")
        parser.add_argument('branch',type=str,required=True,help="branch cannot be left blank!")
        parser.add_argument('section',type=int,required=True,help="section cannot be left blank!")
        parser.add_argument('year_',type=int,required=True,help="year cannot be left blank!")
        parser.add_argument('email_id',type=str,required=True,help="branch cannot be left blank!")
        data=parser.parse_args()
        try:
            x=query(f"""SELECT * FROM group10.users WHERE user_id={data['user_id']}""",return_json=False)
            if len(x)>0: return {"message":"A user with that user_id already exists."},400
        except:
            return {"message":"There was an error inserting into users table."},500
        try:
            query(f"""INSERT INTO group10.users (user_id, user_name, phone_num, password_, branch, section, year_, email_id) VALUES ({data['user_id']},
            '{data['user_name']}',{data['phone_num']},'{data['password_']}','{data['branch']}',{data['section']},{data['year_']},'{data['email_id']}');""")
        except:
            return {"message":"There was an error inserting into users table."},500
        return {"message":"Successfully Inserted."},201
class Sport_Registration(Resource):
    @jwt_required
    def post(self):
        parser=reqparse.RequestParser()
        parser.add_argument('sport_name',type=str,required=True,help="sport_name  cannot be left blank!")

        parser.add_argument('member_ID',type=int,required=True,help="Team member id cannot be left blank!")
        parser.add_argument('team_id',type=int,required=True,help="Team id cannot be left blank!")
        parser.add_argument('team_name',type=str,required=True,help="Name cannot be left blank!")
        parser.add_argument('member_name',type=str,required=True,help="Branch cannot be left blank!")
        parser.add_argument('year_and_section',type=str,required=True,help="Year cannot be left blank!")
        parser.add_argument('branch',type=str,required=True,help="Sport_id cannot be left blank!")
        data=parser.parse_args()
        
        #try:
        query(f""" insert into teamdetails (member_ID, sport_name, team_id, team_name, member_name, year_and_section, branch) values
             ({data['member_ID']},'{data['sport_name']}',{data['team_id']},'{data['team_name']}','{data['member_name']}','{data['year_and_section']}','{data['branch']}');""") 
        #except:
            #return {"message":"There was an error inserting in the table."},500


       # return {"message":"Successfully Inserted."},201
        
        # sport[f"""{data['sport name']}"""]
        
class Team_status(Resource):
    @jwt_required
    def get(self):
        parser=reqparse.RequestParser()
        parser.add_argument('team_id',type=int,required=True,help="Team id cannot be left blank!")
        parser.add_argument('sport_name',type=str,required=True,help="sport name  cannot be left blank!")

        data=parser.parse_args()

        try:
            return query(f"""SELECT status FROM teamdetails WHERE team_id={data['team_id']} and sport_name='{data['sport_name']}'""")
        except:
            return {"message":"There was an error retrieving the data from database."},500
class Sportdetails(Resource):
    @jwt_required
    def get(self):
        parser=reqparse.RequestParser()
        parser.add_argument('sport_name',type=str,required=True,help="Sport name cannot be left blank!")
        data=parser.parse_args()
        try:
            return query(f"""SELECT * FROM group10.sports WHERE sport_name='{data['sport_name']}'; """)
        except:
            return {"message":"There has been an error retrieving sports details"},500
        return {"message":"Sports details retrieved succesfully."}
class Reporting_time(Resource):
    @jwt_required
    def get(self):
        parser=reqparse.RequestParser()
        parser.add_argument('team_id',type=int,required=True,help="Team id cannot be left blank!")
        parser.add_argument('sport_name',type=str,required=True,help="sport name cannot be left blank!")
        data=parser.parse_args()
        try:
            return query(f"""SELECT reporting_time,start_time FROM group10.schedule1 WHERE team1_id={data['team_id']} OR team2_id={data['team_id']} AND sport_name='{data['sport_name']}'; """)
        except:
            return {"message":"There has been an error retrieving sports details"},500
        return {"message":"Sports details retrieved succesfully."}
class Sport_category(Resource):
    @jwt_required
    def get(self):
        parser=reqparse.RequestParser()
        parser.add_argument('sport_category',type=str,required=True,help="Sport Category cannot be left blank!")
        data=parser.parse_args()
        try:
            return query(f"""SELECT * FROM group10.sports WHERE sport_category='{data['sport_category']}'; """)
        except:
            return {"message":"There has been an error retrieving sports details"},500
        return {"message":"Sports details retrieved succesfully."}
class Schedules(Resource):
    @jwt_required
    def get(self):
        parser=reqparse.RequestParser()
        parser.add_argument('team_id',type=int,required=True,help="Team id cannot be left blank!")
        data=parser.parse_args()
        try:
            return query(f"""SELECT * FROM group10.schedule1 WHERE team1_id={data['team_id']} OR team2_id={data['team_id']}; """)
        except:
            return {"message":"There has been an error retrieving dates and schedules."},500
        return {"message":"Dates and schedules retrieved succesfully."}


        
        
