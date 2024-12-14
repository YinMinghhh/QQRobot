
# 文档: https://github.com/botuniverse/onebot-11/blob/master/api/public.md

import message.segment as seg
from utils import response_util

def send_private_msg():
    pass

def send_group_msg(group_id: int, message: list, auto_escape=False, _async=False):
    op = 'send_group_msg_async' if _async else 'send_group_msg'
    return response_util.post(op, {
        'group_id': group_id,
        'message': message,
        'auto_escape': auto_escape
    })

def send_msg():
    pass

def delete_msg(message_id: int):
    return response_util.post('delete_msg', {'message_id': message_id})


if __name__ == '__main__':
    send_group_msg(1015769060, [seg.get_text_msg('test message')])