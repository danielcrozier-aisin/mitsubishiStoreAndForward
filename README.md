# mitsubishiStoreAndForward-Memory Limits

def test_resource():
    counter = 0

    virtual_memory = psutil.virtual_memory()
    available_memory = virtual_memory.available
    memory_limit_low = int(available_memory * 0.2)
    memory_limit_high = int(available_memory * 0.5)

    soft, hard = resource.getrlimit(resource.RLIMIT_AS * int(0.5))
    print(soft, hard)
    resource.setrlimit(resource.RLIMIT_AS, (memory_limit_low, memory_limit_high))
    try:
        while True:
            data = [0] * int(1e8)
            print(f"hi {counter},  {data}")
            counter += 1
    except MemoryError:
        print("Memory limit exceed!!")
