import logging
import os
from typing import List, Optional

from fast_downward.driver.main import main as fd_main

# Use LMCut as it is quicker
_SAS_PLAN_FNAME = "sas_plan"


def get_optimal_actions_using_fd(domain, problem, timeout) -> Optional[List[str]]:
    """
    Use Fast-Downward to get the optimal actions for the planning problem

    Parameters
    ----------
    domain: strips domain file
    problem: strips problem file

    Returns
    -------
    Optional[List[str]], sequential list of actions (i.e. the plan),
    or None if we could not find it
    """
    _DEFAULT_OPTS = ["--search", f"astar(lmcut(), max_time={timeout})"]
    exit_code = fd_main(argv=[domain, problem] + _DEFAULT_OPTS)

    if exit_code == 12:
        print(f"Search incomplete for {domain}, {problem} within {timeout}s")
        return None
    elif exit_code != 0:
        raise RuntimeError(
            f"Something went wrong, exit code {exit_code} from Fast Downward "
            "(http://www.fast-downward.org/ExitCodes)"
        )

    # Read the plan to get actions, remove \n and ignore final cost line
    plan = open(_SAS_PLAN_FNAME, "r").readlines()
    plan = [line[:-1] for line in plan if line.startswith("(") and line.endswith(")\n")]

    # Remove the plan from disk
    os.remove(_SAS_PLAN_FNAME)
    return plan
