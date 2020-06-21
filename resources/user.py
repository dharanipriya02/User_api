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
class Register(Resource):
    def post(self):
        parser=reqparse.RequestParser()
        parser.add_argument('sport name',type=str,required=True,help="sport name  cannot be left blank!")

        parser.add_argument('team_member_id',type=int,required=True,help="Team member id cannot be left blank!")
        parser.add_argument('team_id',type=int,required=True,help="Team id cannot be left blank!")
        parser.add_argument('name',type=str,required=True,help="Name cannot be left blank!")
        parser.add_argument('branch',type=str,required=True,help="Branch cannot be left blank!")
        parser.add_argument('section',type=int,required=True,help="Year cannot be left blank!")
        parser.add_argument('sport_id',type=int,required=True,help="Sport_id cannot be left blank!")
        data=parser.parse_args()
        
        sport={"badminton": query(f""" insert into group10.badminton (team_member_id, team_id, name, branch, sport_id, section) values ({data['team_member_id']},{data['team_id']},'{data['name']}',
            '{data['branch']}',{data['sport_id']},{data['section']});""")  ,
            "basketball": query(f""" insert into group10.basketball values ({data['team_member_id']},{data['team_id']},'{data['name']}',
            '{data['branch']}',{data['section']},{data['sport_id']});""") ,
            "cricket": query(f""" insert into group10.cricket values ({data['team_member_id']},{data['team_id']},'{data['name']}',
            '{data['branch']}',{data['section']},{data['sport_id']});""") ,
            "football": query(f""" insert into group10.football values ({data['team_member_id']},{data['team_id']},'{data['name']}',
            '{data['branch']}',{data['section']},{data['sport_id']});""") ,
            "kabaddi": query(f""" insert into group10.kabaddi values ({data['team_member_id']},{data['team_id']},'{data['name']}',
            '{data['branch']}',{data['section']},{data['sport_id']});""") ,
            "table_tennis": query(f""" insert into group10.table_tennis values ({data['team_member_id']},{data['team_id']},'{data['name']}','{data['branch']}',{data['section']},{data['sport_id']});""") ,
            "volley_ball": query(f""" insert into group10.volley_ball values ({data['team_member_id']},{data['team_id']},'{data['name']}',
            '{data['branch']}',{data['section']},{data['sport_id']});""") ,
            "chess": query(f""" insert into group10.chess values ({data['team_member_id']},{data['team_id']},'{data['name']}',
            '{data['branch']}',{data['section']},{data['sport_id']});""") ,
            "carroms": query(f""" insert into group10.carroms values ({data['team_member_id']},{data['team_id']},'{data['name']}',
            '{data['branch']}',{data['section']},{data['sport_id']});""") 

            }
        return sport[f"""{data['sport name']}"""]
        

        
        
