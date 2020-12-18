#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import subprocess
import pathlib
import time

from fast_downward_api import get_optimal_actions_using_fd


PATH = pathlib.Path(__file__).parent.absolute()


UPPER_BOUND = 18  # Upper bound on the number of blocks for the hardest instance
MAX_TIME = 1 * 30  # Maximal runtime in seconds of the search algorithm
FD_TIMEOUT = 10  # FD timeout in seconds


def create_problem(num_blocks):
    call_string = f"./blocksworld 4 {num_blocks} > instance.pddl"
    exitcode = subprocess.call(call_string, shell=True)

def binary_search():
    min_blocks = 0
    max_blocks = UPPER_BOUND
    while min_blocks <= max_blocks:


    

def main():
    domain = os.path.join(PATH, "4ops/domain.pddl")
    blocks = UPPER_BOUND / 2
    start = time.time()
    end = start + MAX_TIME
    while time.time() < end:
        create_problem(blocks)
        print(f"Solving problem of size {blocks}")
        # By default use FD_TIMEOUT. If we do not have sufficient time use the
        # remaining time we have
        planning_time = min(FD_TIMEOUT, end - time.time())
        print(f"Planning time: {planning_time}")
        plan = get_optimal_actions_using_fd(domain, "instance.pddl", planning_time)
        print(plan)
        blocks = blocks * 1.5 if plan else blocks / 2
        print(f"Passed time: {time.time() - start}")
    print(f"Last block size was {blocks}")


if __name__ == "__main__":
    main()
