import os, sys, json, base64, urllib.request, re

def load_key():
    for line in open('C:/Users/msara/.env', encoding='utf-8'):
        m = re.match(r'\s*OPENROUTER_API_KEY\s*=\s*(.+)\s*', line)
        if m:
            return m.group(1).strip().strip('"').strip("'")
    return None

def gen(prompt, outfile, model='google/gemini-3-pro-image'):
    key = load_key()
    body = {
        'model': model,
        'messages': [{'role': 'user', 'content': prompt}],
        'modalities': ['image', 'text'],
    }
    req = urllib.request.Request(
        'https://openrouter.ai/api/v1/chat/completions',
        data=json.dumps(body).encode(),
        headers={'Authorization': 'Bearer ' + key, 'Content-Type': 'application/json',
                 'HTTP-Referer': 'https://daltonlab.ai', 'X-Title': 'Dalton Deck'})
    try:
        r = urllib.request.urlopen(req, timeout=180)
        data = json.loads(r.read())
        msg = data['choices'][0]['message']
        imgs = msg.get('images') or []
        if imgs:
            url = imgs[0]['image_url']['url']
            b64 = url.split(',', 1)[1]
            open(outfile, 'wb').write(base64.b64decode(b64))
            print('OK', outfile, os.path.getsize(outfile), 'bytes')
            return True
        else:
            print('NO_IMAGE', (msg.get('content') or '')[:300])
            return False
    except urllib.error.HTTPError as e:
        print('HTTP', e.code, e.read().decode()[:600])
        return False

if __name__ == '__main__':
    prompt = sys.argv[1]
    outfile = sys.argv[2]
    gen(prompt, outfile)
