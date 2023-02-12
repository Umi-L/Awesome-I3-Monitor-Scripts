import sys
import subprocess
import json
import DisplayTools as tools

from screeninfo import get_monitors

MONITOR_OFFSET = 10

monitors = get_monitors()
monitors.reverse()


currentDisplay = tools.getCurrentMouseDisplay(monitors)

index = (monitors.index(currentDisplay) * MONITOR_OFFSET) + int(sys.argv[1])

command = ["i3-msg", "move container to workspace", str(index)]

subprocess.call(command)