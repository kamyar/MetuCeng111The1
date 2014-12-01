#orginal function that redirects given sequence to UMad function with I,R1 and R2.
def lulz(liste):
	I=0
	R1=0
	R2=0
	cevap = UMad(R1,R2,I,liste)
	if cevap:
		return cevap
	else:
		return "OHNOES!:-o -> Error:Something bad happened,we're all gonna die! X_x"
#main function that makes you jelly! (beside,U JELLY?)
#using recursion;function continues till the instruction(ins) is set to 0 which is the halt instruction.
def UMad(R1,R2,I,liste):
	ins = liste[I]
	if ins == 0:
		print "-----------------------------------------------------"
		print """state of registers and the sequence at the moment of the halt\n(from left to right R1,R2,I and sequence):"""
		print "R1: %d,R2: %d ,I: %d"%(R1,R2,I)
		print liste
		return
	elif ins == 1:
		R1 = liste[I+1]
		I += 2
	elif ins == 2:
		R2 = liste[I+1]
		I += 2
	elif ins == 3:
		R1 = liste[liste[I+1]]
		I += 2
	elif ins == 4:
		R2 = liste[liste[I+1]]
		I += 2
	elif ins == 5:
		R1 = R2
		I += 1
	elif ins == 6:
		R1 = liste[R2]
		I += 1
	elif ins == 7:
		liste[R1] = R2
		I += 1
	elif ins == 8:
		liste[liste[I+1]] = R1
		I += 2
	elif ins == 9:
		I = liste[I+1]
	elif ins == 10:
		if R1 == 0:
			I += 2
		else:
			I = liste[I+1]
	elif ins == 11:
		R1 = R1 + R2
		I += 1
	elif ins == 12:
		R1 = R1-R2
		I += 1
	elif ins == 13:
		R1 = R1*R2
		I += 1
	elif ins == 14:
		R1 = int(R1/R2)
		I += 1
	elif ins == 15:
		R1 *= -1
		I += 1
	elif ins == 16:
		if R1 == R2:
			R1 = 0
		elif R1 > R2:
			R1 = 1
		else:
			R1 = -1
		I += 1
	else:
		return 0
	print "-----------------------------------------------------"
	print "R1: %d,R2: %d ,I: %d"%(R1,R2,I)
	print liste
	return UMad(R1,R2,I,liste)
def printEmmAll():
	listemiz = 1
	count = 1
	while listemiz:
		listemiz = input("I CAN HAZ SEQUENCE-"+str(count)+"?\n(0:EXIT)\ne")
		if listemiz == 0:
			return
		if type(listemiz) != list:
			print "You are doing it wrong!"
			print "please enter sequence as list,like:\n[9,6,12,27,39,99,3,2,4,3,11,4,4,16,10,20,2,1,9,22,2,0,1,5,7,0]"
			pass
		else:
			lulz(listemiz)
			print "----------------End of sequence-"+str(count)+"--------------------"
			count += 1
printEmmAll()
#examples : 
#1 : [9,6,12,27,39,99,3,2,4,3,11,4,4,16,10,20,2,1,9,22,2,0,1,5,7,0]
#2 : [9,6,15,-1,8,2,3,2,2,2,14,13,4,2,16,10,20,8,3,0,1,1,8,3,9,19]
