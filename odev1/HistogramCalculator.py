import cv2

resim = cv2.imread("gri_resim.jpg",flags=0)

cv2.imshow("gri",resim)
cv2.waitKey()

Hist =[0 for x in range(0,256)]

for j in range (len(resim[:,0])) :
    for i in range(len(resim[0,:])):
        Hist[resim[j,i]] += 1

print(Hist)