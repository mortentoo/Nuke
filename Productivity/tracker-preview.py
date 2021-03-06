# Quickly disable the tracker preview for all tracker nodes to speed up rendering (significantly!)
print '\n\nDisabling preview on trackers:'

for node in nuke.allNodes("Tracker4"):
    print '- \"' + node.name() + '\" preview disabled.'
    node["zoom_window_behaviour"].setValue(4)
    node["zoom_window_filter_behaviour"].setValue(2)
    node["keyframe_display"].setValue(3)
