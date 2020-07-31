py-spy record --output before.svg --duration 10 -- python3 01-pygame-game-of-life.py
py-spy record --output after.svg --duration 10 -- python3 03-pygame-game-of-life-optimized-fail.py
py-spy record --output without_white_on_white.svg --duration 10 -- python3 04-stop-double-drawing.py

# note also poor man's sampling profiler - https://stackoverflow.com/questions/375913/how-can-i-profile-c-code-running-on-linux/378024#378024
# tuna is a potential alternative
# vprof has bad performance and major unfixed interface issues like https://github.com/nvdv/vprof/issues/91 or https://github.com/nvdv/vprof/issues/90
# pyflame project died. It was anyway harder to setup and run, without benefits over py-spy
# snakeviz shows blatantly wrong statistics, what was wontfixed https://github.com/jiffyclub/snakeviz/issues/112
