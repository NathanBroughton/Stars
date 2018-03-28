import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
gamma = 0.2 # angstrom
def trapz(y,x):
	value = np.trapz(y,x,dx=0.01)
	return value
def yval(C):
	y = np.zeros(100000)
	array = np.arange(5500,6500,0.01) # angstrom
	for i in range(0,len(array)):
		yval = np.exp(-C*(1/np.pi) * ((0.5*gamma)/((array[i]-6000)**2 + (0.5*gamma)**2)))
		y[i] = yval
	return y
def plot1(array,y1,y2,y3,y4,y5,y6,y7,y8):	
	plt.plot(array,y1,label = 'opacity = 0.01')
	plt.plot(array,y2,label = 'opacity = 0.1')
	plt.plot(array,y3,label = 'opacity = 1')
	plt.plot(array,y4,label = 'opacity = 10')
	plt.plot(array,y5,label = 'opacity = 100')
	plt.plot(array,y6,label = 'opacity = 1000')
	plt.plot(array,y7,label = 'opacity = 10000')
	plt.plot(array,y8,label = 'opacity = 100000')
	plt.title("Absorption line profiles")
	plt.xlabel("Wavelength")
	plt.ylabel("Flux")
	plt.legend(loc = 4)
	plt.show()
def plot2(x,y):
	plt.loglog(x,y)
	plt.title('Curve of growth')
	plt.xlabel('EW')
	plt.ylabel('Opacity')
	plt.show()
def main():
	x = np.arange(5500,6500,0.01) 
	y = (1/np.pi) * ((0.5*gamma)/((x-6000)**2 + (0.5*gamma)**2))
	a = trapz(y,x)
	C= np.array([0.01,0.1,1,10,100,1000,10000,100000])
	ew = np.zeros(8)
	for i in range(0,len(C)):
		phi = 1 - np.exp(-C[i]*(1/np.pi) * ((0.5*gamma)/((x-6000)**2 + (0.5*gamma)**2))/a)
		intphi = trapz(phi,x)
		ew[i] = intphi
	print ew
	b1 = yval(C[0])
	b2 = yval(C[1])			
	b3 = yval(C[2])
	b4 = yval(C[3])
	b5 = yval(C[4])
	b6 = yval(C[5])
	b7 = yval(C[6])
	b8 = yval(C[7])	
	plot1(x,b1,b2,b3,b4,b5,b6,b7,b8)
	plot2(ew,C)
if __name__ == '__main__':
	main()

