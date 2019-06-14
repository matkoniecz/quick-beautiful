py-spy --flame before.svg -d 10 -- python3 01-pygame-game-of-life-limited-iterations.py
py-spy --flame after.svg -d 10 -- python3 03-pygame-game-of-life-optimized-limited-iterations.py
py-spy --flame without_white_on_white.svg -d 10 -- python3 04-stop-double-drawing.py

vprof has bad performance and some interface issues like https://github.com/nvdv/vprof/issues/91 or https://github.com/nvdv/vprof/issues/90
pyflame is harder to setup and run and I see no benefits over py-spy
tuna can be run once - https://github.com/nschloe/tuna/issues/44
snakeviz shows blatantly wrong statistics - https://github.com/jiffyclub/snakeviz/issues/112