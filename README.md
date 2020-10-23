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

### Credits

Maintainer: **Tamás Zolnai** ([tzolnai](https://github.com/tzolnai))

This code is forked from this github repository: https://github.com/hallgatoemese/asrt.

The original code's author is **Emese Szegedi-Hallgató** ([hallgatoemese](https://github.com/hallgatoemese))

The code was rewritten and was extended with eye-tracker capabilities by **Tamás Zolnai** ([tzolnai](https://github.com/tzolnai))

### References

ASRT (alternating SRT, alternating serial reaction time task)

* [Howard Jr, J. H., & Howard, D. V. (1997). Age differences in implicit learning of higher order dependencies in serial patterns. Psychology and aging, 12(4), 634.](https://www.researchgate.net/profile/James_Howard11/publication/13812889_Age_differences_in_implicit_learning_of_higher_order_dependencies_in_serial_patterns/links/0deec52423cfe984b4000000.pdf)

* [Simor, P., Zavecz, Z., Horvath, K., Éltető, N., Török, C., Pesthy, O., ... & Nemeth, D. (2019). Deconstructing procedural memory: Different learning trajectories and consolidation of sequence and statistical learning. Frontiers in psychology, 9, 2708.](https://www.frontiersin.org/articles/10.3389/fpsyg.2018.02708/full)

I-DT: Dispersion-Threshold identification of fixations

* [Salvucci, D. D., & Goldberg, J. H. (2000, November). Identifying fixations and saccades in eye-tracking protocols.
In Proceedings of the 2000 symposium on Eye tracking research & applications (pp. 71-78).](https://www.researchgate.net/publication/220811146_Identifying_fixations_and_saccades_in_eye-tracking_protocols)

Dispersion threshold

* [Blignaut, P. (2009). Fixation identification: The optimum threshold for a dispersion algorithm. Attention, Perception, & Psychophysics, 71(4), 881-895.](https://link.springer.com/article/10.3758/APP.71.4.881)

* [Blignaut, P., & Beelders, T. (2009). The effect of fixational eye movements on fixation identification with a dispersion-based fixation detection algorithm.](https://www.researchgate.net/publication/297523424_The_effect_of_fixational_eye_movements_on_fixation_identification_with_a_dispersion-based_fixation_detection_algorithm)

Fixation duration threshold

* [Manor, B. R., & Gordon, E. (2003). Defining the temporal threshold for ocular fixation in free-viewing visuocognitive tasks. Journal of neuroscience methods, 128(1-2), 85-93.](https://www.sciencedirect.com/science/article/pii/S0165027003001511)

Linear interpolation of missing data

* [Olsen, A. (2012). The Tobii I-VT fixation filter. Tobii Technology, 1-21.](https://stemedhub.org/resources/2173/download/Tobii_WhitePaper_TobiiIVTFixationFilter.pdf)
