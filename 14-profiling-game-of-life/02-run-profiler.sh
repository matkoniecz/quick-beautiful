py-spy --flame before.svg -d 10 -- python3 01-pygame-game-of-life-limited-iterations.py
py-spy --flame after.svg -d 10 -- python3 03-pygame-game-of-life-optimized-limited-iterations.py
py-spy --flame without_white_on_white.svg -d 10 -- python3 04-stop-double-drawing.py

# note also poor man's sampling profiler - https://stackoverflow.com/questions/375913/how-can-i-profile-c-code-running-on-linux/378024#378024
# tuna is a potential alternative
# vprof has bad performance and major unfixed interface issues like https://github.com/nvdv/vprof/issues/91 or https://github.com/nvdv/vprof/issues/90
# pyflame project died. It was anyway harder to setup and run, without benefits over py-spy
# snakeviz shows blatantly wrong statistics, what was wontfixed https://github.com/jiffyclub/snakeviz/issues/112
