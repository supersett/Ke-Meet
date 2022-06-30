from django.shortcuts import render, get_object_or_404
import json
from django.http import JsonResponse

import room
from .models import *
from user import *
from room import *


# pk값 받아와야해서 매개변수로 추가해줘야하나?
# 참여하기 버튼을 땅 눌렀을 때 발동 -> 방의 지원자목록에 user가 DB에 추가됨./ 방상태 변화는 없음.
def join_room(request):
    if request.method == "POST":

        # 디코딩
        body = json.loads(request.body.decode('utf-8'))

        # pk값으로 해당 데이터 가져옴.
        user_data = User.objects.get(pk=body['user_key'])
        room_data = Room.objects.get(pk=body['room_num'])


        # 객체에 Create
        new_apply = Apply.objects.create(
            user_key = user_data,
            room_num = room_data,
            apply_status = body['apply_status'],
        )

        # FK로 user 데이터 가져오기 ; serializer 이용
        # user_data = serializers
        # Apply.objects.get(id=1)

        new_apply_json = {
            # 필드명 지정하기 위해 모델에 적어줘야할까?
            # 지원번호
            'id': new_apply.id,

            'user_data': new_apply.user_key,
            'room_data': new_apply.room_num,
            'apply_status': new_apply.apply_status,

        }

        return JsonResponse({
            'status': 200,  #성공
            'success' : True,
            'message': '모임 참여 성공',
            'data': new_apply_json

        })
    else:
        return JsonResponse({
            'status': 405,  #실패
            'success' : False,
            'message': '모임 참여 실패',
            'data': None
        })


# 선택하기 버튼 누르면 apply_status Patch 되는 api
def update_apply_status(request):
    if request.method == "PATCH":
        pass



# 모임취소 버튼 땅 누르면 방삭제
def delete_room(request, room_num):
    if request.method == "DELETE":
        
        # Room 객체 중 특정 방번호인 방 삭제.
        delete_room = get_object_or_404(Room, pk=room_num)

        delete_room.delete()

        return JsonResponse({
                'status': 200,
                'success': True,
                'message': '삭제 성공!',
                'data': None
            })

    else:
        return JsonResponse({
                'status': 405,
                'success': False,
                'message': 'method error',
                'data': None
            })
