# Profiling Scikit-Learn Parallel Job

## Introduction
- Let us say we have a sklearn model we want to run in "parallel". Parallel is in quote because what exactly this means is a not so straight forward to understand.
- I'd like to manually profile the code and understand a bit more about how the code is actually executed.

## A small note on the methods import
- If you try: `from time import thread_time()` as it is in some old script this is NO longer available at least from python 3.9.x onwards. I guess this was substitute by something else.
