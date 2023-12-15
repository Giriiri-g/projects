// Computes RAM[1] = 1 + ... + RAM[0]
	@i
	M=1		// i =1
	@sum
	M=0		// sum =0
// if i>RAM[0] gotoSTOP
// sum +=i
//i++

(LOOP)
	@i
	D=M
	@R0
	D=D-M
	@STOP
	D;JGT
	@i
	D=M
	@sum
	M=D+M
	@i
	M=M+1
	@LOOP
// gotoLOOP
	0;JMP

(STOP)
	@sum
	D=M
	@R1
	M=D
// RAM[1] = thesum

(END)
	@END
	0;JMP