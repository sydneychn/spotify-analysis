import pandas as pd
#combining total history
history1 = pd.read_json('history1.json')
history2 = pd.read_json('history2.json')
history3 = pd.read_json('history3.json')
complete = pd.concat([history1,history2,history3])
print(complete.columns)
complete.drop(complete.drop(columns=['platform', 'ip_addr', 'audiobook_title', 'audiobook_uri', 'audiobook_chapter_uri', 'audiobook_chapter_title', 'offline', 'offline_timestamp']))


