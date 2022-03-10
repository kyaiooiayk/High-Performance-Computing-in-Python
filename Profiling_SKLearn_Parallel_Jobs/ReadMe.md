# Profiling Scikit-Learn Parallel Job

## Introduction
- Let us say we have a sklearn model we want to run in "parallel". Parallel is in quote because what exactly this means is a not so straight forward to understand.
- I'd like to manually profile the code and understand a bit more about how the code is actually executed.

## A small note on the methods import
- If you try: `from time import thread_time()` as it is in some old script this is NO longer available at least from python 3.9.x onwards. I guess this was substitute by something else.


## How does python measures time?
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



