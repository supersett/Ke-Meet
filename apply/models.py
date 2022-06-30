from django.db import models
# user PK값 활용하기 위해 
from user import models as user_model
# room PK값 활용하기 위해 
from room import models as room_model

class Apply(models.Model):
    # apply_num 은 room 객체 내 여러 apply 객체들을 구분해주는 역할. -> 이 값에 따라 지원자 정렬해주면 되겠다.

    # FK ; user의 PK값 받아옴.
    # 어떤 지원자가 방에 참가하는지 파악위해.
    # 참조 테이블 : User
    # 데이터베이스 상의 필드 이름 : USER_KEY
    # user 객체 삭제되면 같이 삭제.
    user_key = models.ForeignKey('User', on_delete=user_model.CASCADE, db_column="USER_KEY")

    # FK ; room의 PK값 받아옴.
    # 어떤 방에 입장할지 파악위해. ; 방의 PK값으로 들어감.
    # room 객체 삭제되면 같이 삭제.
    room_num = models.ForeignKey('Room', on_delete=room_model.CASCADE, db_column="ROOM_NUM")

    # 호스트한테 선택받아서 참여확정됐는지 파악위해.
    # default=0 이고 호스트가 선택하면 1로 바뀌도록. -> 1이 되면 모임 안내.
    apply_status = models.IntegerField(default=0, null=False, db_column="APPLY_STATUS")



    # 방이라는 객체에 여러 apply 객체가 들어가는 형태.

    # 홈에서 방 눌렀을 때 그 방객체의 정보를 가져와서 그 방의 호스트 user_key와 user의 user_key를 대조해서 같으면 host 방상세페이지를 보여줄거니까. 그러면 참여하기 버튼없이 모임확정, 모임취소 둘 중에만 선택 가능한 형태니까 자연스레 자기가 호스트인 방에 지원할 수 없겠다!