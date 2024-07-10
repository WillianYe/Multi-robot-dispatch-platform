# Customized Menge library for large scale crowd simulation

Welcome to the customized menge library to perform the large scale crowd simulation in rmf projects <https://github.com/osrf/rmf_demos>.
You can find the original Menge repo in <https://github.com/MengeCrowdSim/Menge>.
Original research paper can be found in <http://gamma-web.iacs.umd.edu/Menge/files/MengeTechReport.pdf>
Some introduction and documentation can be found in <http://gamma.cs.unc.edu/Menge/>

## Changes from the original repo
1. This repo only contains the core part of the original menge lib.
2. This repo defines the idea of "external agent". Different from the original agent, which the menge_core computes and control the agent position from path plan and collision avoidance simulation result, "external agent" only updates the position externally at each iteration. The purpose of introduing "external agent" is to separate the walking human (controlled by menge) and moving robot (controlled by external simulation), and achieves collision avoidance between human and robot.
3. This repo removes `throw(optional_type_list)` declaration for functions, as this declaration is deprecated in C++11, will cause compile error under C++14 and removed in C++17.

## Use of this repo
This repo is used for under the crowd simulation plugin in rmf projects. Please include the master branch of this repo in the project repo list.
Related documents of performing crowd simulation under rmf projects can be found in <https://github.com/FloodShao/crowd_simulation/tree/master/crowd_simulation_doc>
