# Profiling Scikit-Learn Parallel Job

## Introduction
- Let us say we have a sklearn model we want to run in "parallel". Parallel is in quote because what exactly this means is a not so straight forward to understand.
- I'd like to manually profile the code and understand a bit more about how the code is actually executed.

## A small note on the methods import
- If you try: `from time import thread_time()` as it is in some old script this is NO longer available at least from python 3.9.x onwards. I guess this was substitute by something else.


## How does python measure time?
- In python there 4 ways you can time your code.
  - `monotonic()`
  - `perf_counter()`
  - `process_time()`
  - `time()`
  - `clock()` -> deprecated from python 3.3.x onwards

- The explaination provided on the official userguide seems to be a bit difficult to understand but the this [blog](https://www.webucator.com/article/python-clocks-explained/) provides the key to understand the difference. You asses each of the 4 methods above according to these 4 metrics:
  - **adjustable**: The clock can be changed by the system administrator. This is important because an adjustable clock is unreliable when calculating time deltas.
    So time should not be used to calculate time deltas.
  - **monotonic**: Monotonic clocks are unidirectional. They can only go forward. This means that they are only useful in giving you relative times – the times between two events.
  - **resolution**: The time between clock ticks. The smaller the number, the greater number of ticks per time unit. So, a high resolution clock has a very small resolution number.
  - **tick rate**: The number of ticks per second. This is the inverse of Resolution. A high resolution clock has a high tick rate.

| Methods | Adjustable | Monotonic | Resolution | Tick Rate |
| ------- | ---------- | --------- | ---------- | --------- |
| `process_time` | False | True | 1e-07 | 10,000,000 |
| `clock` | False | True | 4.665306263360271e-07 | 2,143,482 |
| `pref_counter` | False | True | 4.665306263360271e-07 | 2,143,482 |
| `monotonic` | False | True | 0.015625 | 64 |
| `tiem` | True | False| 0.015625 | 64 |

## Practicle guidelines
- `time.clock()` should NOT be used as of Python 3.3. It’s deprecated.
- `time.time()` should NOT be used for comparing relative times. It’s not reliable because it’s adjustable.
- `time.monotonic` is what you are looking for in all the situation where you were using either the two above.
- `time.proces_time()` returns the value (in fractional seconds) of the sum of the system and  user CPU time of the current process. It does not include time elapsed during sleep. It is process-wide by definition. process_time() will give you the time spent by the  computer for the current process, a computer with an OS usually won’t spend 100% of the time on any given process. This counter **SHOULD NOT** count the time the cpu is running anything else. It is **PROCESS-WIDE** by definition.
- `time.perf_counter()` returns the value (in fractional seconds) of a performance counter,  i.e. a clock with the highest available resolution to measure a short duration. It does  include time elapsed during sleep and is system-wide. perf_counter() should measure the real amount of time for a process to take, as if you used a stop watch. It is **SYSTEM-WIDE** by definition.

## References
- [Interesting discussion on Physicall and logical CPU](https://stackoverflow.com/questions/1006289/how-to-find-out-the-number-of-cpus-using-python/36540625)
- [How does skleanr uses parallel_backend](https://scikit-learn.org/stable/modules/generated/sklearn.utils.parallel_backend.html)
- [Python Clocks Explained](https://www.webucator.com/article/python-clocks-explained/)
