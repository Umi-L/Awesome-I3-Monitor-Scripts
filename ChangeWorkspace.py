import sys
import subprocess
import DisplayTools as tools

from screeninfo import get_monitors

MONITOR_OFFSET = 10

monitors = get_monitors()
monitors.reverse()

currentDisplay = tools.getCurrentMouseDisplay(monitors)

index = (monitors.index(currentDisplay) * MONITOR_OFFSET) + int(sys.argv[1])

if index != tools.getActiveWorkspaceNumber():
    command = ["i3-msg", "workspace", str(index)]

    subprocess.call(command)
else:
    print("Already on workspace " + str(index))