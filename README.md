# ASRT core

The core ASRT script written in Python 3. This code includes all the
basic functionality useful for an ASRT experiment, but it does probably not
include everything which is needed for a specific experiment. Specific needs
can be implemented in separate repositories \ forks.

This script supports both keyboard and eye-tracking controlled design.

### Prerequisites
Running ASRT script requires all of the following and their dependencies.

* [Python 3.6](https://www.python.org/downloads/)
* [Tobii Pro SDK](https://pypi.org/project/tobii-research/) (only for eye-tracking)
* [PsychoPy](https://www.psychopy.org/download.html)
* [pyglet](https://pyglet.readthedocs.io/en/stable/)

After Python 3.6 and pip is intalled, you can install psychopy, tobii_research and pyglet packages using `pip install`.
pyWinhook is a dependency of PscychoPy python package, but it's newest version fails to install on Python 3.6,
so use a version which have a Python 3.6 package (e.g. 1.6.1).
```
pip install pyWinhook==1.6.1
```

This ASRT script uses an older version of pyglet (<=1.3.2) so for pyglet you need to specify the version explicitely:
```
pip install pyglet==1.3.2
```

For the up-to-date install process, check the github workflow files which contain how to install all packages.
https://github.com/tzolnai/asrt_core/tree/master/.github/workflows

Additional dependencies (for development):
* [pytest](https://docs.pytest.org/en/latest/): For running tests under test folder
* [pynput](https://pypi.org/project/pynput/): For running ET_simulation script (dev_tools folder)
* [autopep8](https://pypi.org/project/autopep8/): For running autoformat script (dev_tools folder)

### Setup

After all prerequisites are installed you need to download the content of this repository.

Before running the ASRT script you need to place an instruction file in the same folder where the `asrt.py` is.
The instruction file should have the name `inst_and_feedback.txt`. You can find example instruction files under `inst_examples` folder.

When instruction file is in place you can run the script by `python asrt.py` command or by running the `asrt.py` file from PsychoPy.

### References

I-DT: Dispersion-Threshold identification of fixations:
[Salvucci, D. D., & Goldberg, J. H. (2000, November). Identifying fixations and saccades in eye-tracking protocols.
In Proceedings of the 2000 symposium on Eye tracking research & applications (pp. 71-78).]
(https://www.researchgate.net/publication/220811146_Identifying_fixations_and_saccades_in_eye-tracking_protocols)