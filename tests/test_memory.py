from systemusage import memory

def test_get_memory_usage():
    memory_monitor = memory.MemoryMonitor()
    usage_info = memory_monitor.get_memory_usage()

    assert 'total' in usage_info
    assert 'available' in usage_info
    assert 'used' in usage_info
    assert 'percent' in usage_info
