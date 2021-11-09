from pwn import *

exe = context.binary = ELF('./missile-static')

log.info(f'{hex(exe.sym.puts)}')