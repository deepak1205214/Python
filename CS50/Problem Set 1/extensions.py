e=(input("File Name:").lower()).strip()
dp=e.rfind(".")
if e.endswith((".gif",".png")):
    print("image/"+e[dp+1:])
elif e.endswith((".jpg",".jpeg")):
    print("image/jpeg")
elif e.endswith(".txt"):
    print("text/plain")
elif e.endswith(".pdf"):
    print("application/"+e[dp+1:])
else:
    print("application/octet-stream")
