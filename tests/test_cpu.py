from systemusage import cpu


def test_get_cpu_usage():
    cpu_monitor = cpu.CPUMonitor()
    usage = cpu_monitor.get_cpu_usage()

    assert usage >= 0 and usage <= 100
