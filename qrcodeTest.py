import qrcode
name = "mygithubQR"
github_url = "https://github.com/ivalpib"
qrimage = qrcode.make(github_url)
print(type(qrimage))
qrimage.save(f"{name}.png")