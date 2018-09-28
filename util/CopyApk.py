import os

sourceDir = "D:/workspace/loanmarket_android/financialmarket/app/build\outputs"
targetDirRoot = "C:/Users/Administrator/Desktop/apk"
if not os.path.exists(targetDirRoot):
    os.mkdir(targetDirRoot)

for root, dir, file in os.walk(sourceDir):
    for b in file:
        # print(b)
        if b.endswith(".apk"):
            targetName = "C:/Users/Administrator/Desktop/apk/" + os.path.basename(b)
            sourceFile = os.path.join(root, b)
            print(sourceFile)
            targetFile = os.path.join(targetDirRoot, targetName)
            print(targetFile)
            open(targetFile, "wb").write(open(sourceFile, "rb").read())
