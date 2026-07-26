import io
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app import create_app

app = create_app({'TESTING': True})
client = app.test_client()

with open('app/static/images/avatars/reach-to-the-left.png', 'rb') as f:
    data = {
        'image': (io.BytesIO(f.read()), 'reach-to-the-left.png'),
        'movement': 'side_reach',
        'side': 'left'
    }
    rv = client.post('/api/frame', data=data, content_type='multipart/form-data')
    print('status', rv.status_code)
    print(rv.get_json())
