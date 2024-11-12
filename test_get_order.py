# Ултанбаева Светлана, 23-я когорта — Финальный проект. Инженер по тестированию плюс

import sender_stand_request

def get_track_number():
    response=sender_stand_request.post_new_order()
    return response.json()["track"]

def test_get_order_details_by_track_number():
    track_number=get_track_number()
    get_response=sender_stand_request.get_order_details(track_number)
    assert get_response.status_code==200

