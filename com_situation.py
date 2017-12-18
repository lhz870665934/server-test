import psutil, time

print "The information of CPU:"
print ""
print "    The number of CPU: %s" %psutil.cpu_count()
print "    The number of physical CPU: %s" %psutil.cpu_count(logical = False)
print "    CPU percent: " + str(psutil.cpu_percent(1)) + " %"
print "    CPU uptimes:" 
print "       ", psutil.cpu_times()  
print ""

print "The information of memory:"
print ""
print "    Virtual memory:" 
print "       ", psutil.virtual_memory()
print "    Swap memory:"
print "       ", psutil.swap_memory()
print ""

print "The information of disk:"
print ""
print "    Total I/O and read-write information:"
print "       ", psutil.disk_io_counters()
print "    Perdisk I/O and read-write information:"
print "       ", psutil.disk_io_counters(perdisk = True)
print ""

print "The information of net:"
print ""
print "    Total I/O information:"
print "       ", psutil.net_io_counters()
print "    Per network adapter information:"
for ad, detail in psutil.net_io_counters(pernic = True).iteritems():
    print "       ", ad, detail
print "    Net stats information:"
for ad, detail in psutil.net_if_stats().iteritems():
    print "       ", ad, detail
print ""

print ""
input('Press Enter to exit...')