	.text
	.def	@feat.00;
	.scl	3;
	.type	0;
	.endef
	.globl	@feat.00
.set @feat.00, 0
	.file	"<string>"
	.def	test;
	.scl	2;
	.type	32;
	.endef
	.globl	test
	.p2align	4, 0x90
test:
	pushq	%rsi
	pushq	%rdi
	subq	$40, %rsp
	movl	$1, %esi
	cmpl	$2, %ecx
	jl	.LBB0_4
	movl	%ecx, %edi
	addl	$2, %edi
	xorl	%esi, %esi
	.p2align	4, 0x90
.LBB0_2:
	leal	-3(%rdi), %ecx
	callq	test
	addl	%eax, %esi
	addl	$-2, %edi
	cmpl	$4, %edi
	jae	.LBB0_2
	incl	%esi
.LBB0_4:
	movl	%esi, %eax
	addq	$40, %rsp
	popq	%rdi
	popq	%rsi
	retq

	.def	main;
	.scl	2;
	.type	32;
	.endef
	.globl	main
	.p2align	4, 0x90
main:
	subq	$40, %rsp
	movl	$40, %ecx
	callq	test
	leaq	fstr87731(%rip), %rcx
	movl	%eax, %edx
	callq	printf
	xorl	%eax, %eax
	addq	$40, %rsp
	retq

	.section	.rdata,"dr"
fstr87731:
	.asciz	"%i \n"

