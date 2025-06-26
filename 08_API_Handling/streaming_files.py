import requests as req
from tqdm import tqdm


url = 'https://vscode.download.prss.microsoft.com/dbazure/download/stable/258e40fedc6cb8edf399a463ce3a9d32e7e1f6f3/VSCodeUserSetup-x64-1.100.3.exe'

res = req.get(url, stream=True)
# total_size = float(res.headers['content-length'])/1024
total_size = float(res.headers['content-length'])


# print(f"Content size: {total_size}")
filename = "code.exe"


# with open(filename,"wb") as file:
#     for chunk in tqdm(res.iter_content(chunk_size=128),desc="Downloading",total=float(total_size),unit="iB",unit_scale=True):
#         file.write(chunk)

bytes_received = 0

progress_bar = tqdm(desc="Downloading",total=int(total_size),unit="iB",unit_scale=True)

with open(filename,"wb") as file:
    for chunk in res.iter_content(chunk_size=128):
        if chunk:
            file.write(chunk)
            progress_bar.update(len(chunk))

progress_bar.close()


