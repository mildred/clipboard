#!/usr/bin/python

import glib, gtk, sys

def test_clipboard():
    clipboard = gtk.Clipboard()
    targets = clipboard.wait_for_targets()
    print "Targets available:", ", ".join(map(str, targets))
    for target in targets:
        print "Trying '%s'..." % str(target)
        contents = clipboard.wait_for_contents(target)
        if contents:
            print contents.data

def list_clipboard():
    clipboard = gtk.Clipboard()
    targets = clipboard.wait_for_targets()
    print "\n".join(map(str, targets))

def out_clipboard(desired_target):
    clipboard = gtk.Clipboard()
    targets = clipboard.wait_for_targets()
    for target in targets:
        if str(target) == desired_target:
            contents = clipboard.wait_for_contents(target)
            if contents:
                print contents.data

def main(typ):
    mainloop = glib.MainLoop()
    def cb():
        if typ == None:
            list_clipboard()
        else:
            out_clipboard(typ)
        mainloop.quit()
    glib.idle_add(cb)
    mainloop.run()

if __name__ == "__main__":
    try:
        main(sys.argv[1])
    except:
        main(None)

