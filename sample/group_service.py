import re

import yaml

from utils.redis_util import redis_util as redis

from api.public import send_group_msg
import message.segment as seg

class GroupService:
    __slots__=(
        '_allowed_groups',
        '_patten'
    )

    def __init__(self):
        try:
            with open("config.yaml", "r", encoding="utf-8") as f:
                config = yaml.safe_load(f)
            self._allowed_groups = config.get("allowed_groups", [])
            print(self._allowed_groups)
        except Exception as e:
            print(f"加载配置文件时出错: {e}")

        self._patten = r"[12][\w][ -]\S{1,6}"

    def _check_group(self, group_id: int) -> bool:
        return group_id in self._allowed_groups

    def _check_card(self, card: str) -> bool:
        return bool(re.match(self._patten, card))

    def serve(self, data):
        group_id = data.get('group_id')
        if not self._check_group(group_id):
            return {}

        sender = data.get('sender', {})
        user_card = sender.get('card', '')  # 提取 card 属性

        user_card = user_card if user_card else sender.get('nickname', '')

        if not self._check_card(user_card):
            if not redis.key_exists(user_card):
                redis.set_key(user_card, '', 300)
                message = (f"\n您的群名片不符合:{self._patten}\n"
                           f"请尽快修改哦\n"
                           f"正确示例：25-李四")
                send_group_msg(group_id, [seg.get_at_msg(str(sender.get('user_id'))), seg.get_text_msg(message)])
            else:
                print(user_card + 'exists: ' + str(redis.get_ttl(user_card)))

        return {}

group_service = GroupService()
