
def get_text_msg(text: str) -> dict:
    return {
        'type': 'text',
        'data': {
            'text': text
        }
    }

def get_face_msg(id_: str) -> dict:
    return {
        'type': 'face',
        'data': {
            'id': id_
        }
    }

def get_image_msg(file: str, cache=1, proxy=1, timeout=None) -> dict:
    return {
        'type': 'image',
        'data': {
            'file': file
        }
    }

def get_at_msg(qq: str) -> dict:
    return {
        'type': 'at',
        'data': {
            'qq': qq
        }
    }

if __name__ =='__main__':
    print(get_text_msg("test message"))
