Question 1:
    elapsed_time = timeit.timeit(lambda: fibonacci(1000), number=100)
        This function executes the code snippet a specified number of times (depending on the number parameter) and returns a single aggregate time. When the code's execution time is long relative to the measurement noise, the aggregate is relatively stable, but if the code's execution time is short, even small amounts of measurement noise is able to skew the measurement.
    times = timeit.repeat(lambda: fibonacci(1000), repeat =5, number=10)
        This function performs multiple independent timing runs (based on the repeat parameter) and returns a list of timings. This lets you see the variability between runs. The smallest value in the list is often the best estimate of the execution without the noise. The distribution of times can show how the affects of the measurement noise skew timings.

Question 2:
    Since timeit returns a single aggregate time, it makes sense to divide the total bu the number of executions to obtain the average time. So for timeit, the  average time execution is the most appropriate statistic to apply.
    repeat returns a list of timing values, and the minimum is typically preferred, as it is the least affected by the measurement noise. So the min statistic is the most appropriate for the repeat function. 