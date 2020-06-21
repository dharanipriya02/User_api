from flask_restful import Resource,reqparse
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import create_access_token,jwt_required
from db import query




class Register(Resource):
    def post(self):
        parser=reqparse.RequestParser()
        parser.add_argument('team_member_id',type=int,required=True,help="Team member id cannot be left blank!")
        parser.add_argument('team_id',type=int,required=True,help="Team id cannot be left blank!")
        parser.add_argument('name',type=str,required=True,help="Name cannot be left blank!")
        parser.add_argument('branch',type=str,required=True,help="Branch cannot be left blank!")
        parser.add_argument('section',type=int,required=True,help="Section cannot be left blank!")
        parser.add_argument('sport_name',type=str,required=True,help="Sport name cannot be left blank!")
        parser.add_argument('sport_id',type=int,required=True,help="Sport id cannot be left blank!")
        data=parser.parse_args()
        try:
            #sprt={1: query(f"""INSERT INTO group10.basketball (team_member_id,team_id,name,branch,year,sport_id) VALUES ({data['team_member_id']},{data['team_id']},'{data['name']}','{data['branch']}',{data['year']},{data['sport_id']}); """),
            #      2: query(f"""INSERT INTO group10.basketball (team_member_id,team_id,name,branch,year,sport_id) VALUES ({data['team_member_id']},{data['team_id']},'{data['name']}','{data['branch']}',{data['year']},{data['sport_id']}); """),
             # 3: query(f"""INSERT INTO group10.cricket (team_member_id,team_id,name,branch,year,sport_id) VALUES ({data['team_member_id']},{data['team_id']},'{data['name']}','{data['branch']}',{data['year']},{data['sport_id']}); """),
              #4: query(f"""INSERT INTO group10.football (team_member_id,team_id,name,branch,year,sport_id) VALUES ({data['team_member_id']},{data['team_id']},'{data['name']}','{data['branch']}',{data['year']},{data['sport_id']}); """),
              #5: query(f"""INSERT INTO group10.kabaddi (team_member_id,team_id,name,branch,year,sport_id) VALUES ({data['team_member_id']},{data['team_id']},'{data['name']}','{data['branch']}',{data['year']},{data['sport_id']}); """),
              #6: query(f"""INSERT INTO group10.table_tennis (team_member_id,team_id,name,branch,year,sport_id) VALUES ({data['team_member_id']},{data['team_id']},'{data['name']}','{data['branch']}',{data['year']},{data['sport_id']}); """),
              #7: query(f"""INSERT INTO group10.volley_ball (team_member_id,team_id,name,branch,year,sport_id) VALUES ({data['team_member_id']},{data['team_id']},'{data['name']}','{data['branch']}',{data['year']},{data['sport_id']}); """),
              #8: query(f"""INSERT INTO group10.chess (team_member_id,team_id,name,branch,year,sport_id) VALUES ({data['team_member_id']},{data['team_id']},'{data['name']}','{data['branch']}',{data['year']},{data['sport_id']}); """),
              #9: query(f"""INSERT INTO group10.carroms (team_member_id,team_id,name,branch,year,sport_id) VALUES ({data['team_member_id']},{data['team_id']},'{data['name']}','{data['branch']}',{data['year']},{data['sport_id']}); """)
             #}
        #return sprt[data['sport_id']]
            query(f""" insert into group10.{data['sport_name']} values ({data['team_member_id']},{data['team_id']},'{data['name']}','{data['branch']}',{data['section']},{data['sport_id']});""")
        except:
            return {"message":"There was an error registering the team"},400
        return {"message":"Team registered succesfully! Wait for confirmation from admin."}
class Teamstatus(Resource):

    def get(self):
        parser=reqparse.RequestParser()
        parser.add_argument('team_id',type=int,required=True,help="Team id cannot be left blank!")
        data=parser.parse_args()

        try:
            return query(f"""SELECT * FROM group10.team_details WHERE team_id={data['team_id']}""")
        except:
            return {"message":"There was an error retrieving the data from database."},500
class Sportdetails(Resource):
    def get(self):
        parser=reqparse.RequestParser()
        parser.add_argument('sport_name',type=str,required=True,help="Sport name cannot be left blank!")
        data=parser.parse_args()
        try:
            return query(f"""SELECT * FROM group10.sports WHERE sport_name='{data['sport_name']}'; """)
        except:
            return {"message":"There has been an error retrieving sports details"},500
        return {"message":"Sports details retrieved succesfully."}
class Reporttimes(Resource):
    def get(self):
        parser=reqparse.RequestParser()
        parser.add_argument('team_id',type=int,required=True,help="Team id cannot be left blank!")
        parser.add_argument('match_date',type=str,required=True,help="Match date cannot be left blank!")
        data=parser.parse_args()
        try:
            return query(f"""SELECT reporting_time,start_time FROM group10.schedule WHERE team1_id={data['team_id']} OR team2_id={data['team_id']} AND match_date='{data['match_date']}'; """)
        except:
            return {"message":"There has been an error retrieving sports details"},500
        return {"message":"Sports details retrieved succesfully."}
class Sportcategory(Resource):
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
    def get(self):
        parser=reqparse.RequestParser()
        parser.add_argument('team_id',type=int,required=True,help="Team id cannot be left blank!")
        data=parser.parse_args()
        try:
            return query(f"""SELECT * FROM group10.schedule WHERE team1_id={data['team_id']} OR team2_id={data['team_id']}; """)
        except:
            return {"message":"There has been an error retrieving dates and schedules."},500
        return {"message":"Dates and schedules retrieved succesfully."}
