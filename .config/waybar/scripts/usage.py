#!/usr/bin/python3

import subprocess

def get_cpu_usage():
    cpu = subprocess.run(['top', '-b', '-n1'], stdout=subprocess.PIPE)
    cpu = cpu.stdout.decode('utf-8').split('\n')[2].split()
    return cpu[1]

def get_mem_usage():
    mem = subprocess.run(['free', '-m'], stdout=subprocess.PIPE)
    mem = mem.stdout.decode('utf-8').split('\n')[1].split()
    return mem[2]

print(f'  {get_cpu_usage()}%    {get_mem_usage()}MB')
