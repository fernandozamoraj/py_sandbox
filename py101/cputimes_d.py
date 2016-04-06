from psutil import cpu_times, cpu_stats, virtual_memory

x = cpu_times()
print 'cpu_times()'
print x
print ' '

#access of namedtuple attibutes
print 'user:      {0}'.format(x.user)
print 'system:    {0}'.format(x.system)
print 'idle:      {0}'.format(x.idle)
print 'interrupt: {0}'.format(x.interrupt)
print 'dpc:       {0}'.format(x.dpc)
print ' '

c = cpu_stats()
print 'cpu_stats()'
print c
print ' '

m = virtual_memory()
print 'virtual_memory(): '
print m
print ' '

