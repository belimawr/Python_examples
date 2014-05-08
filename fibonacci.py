class FibonacciSolver(object):
    @staticmethod
    def get_fibonacci_generator():
        f0 = 0
        f1 = 1
        while True:
            next_number = f0 + f1
            f0 = f1
            f1 = next_number
            yield next_number

    @staticmethod
    def fibonacci(n_th):
        if(n_th == 0):
            return 0
        elif(n_th == 1):
            return 1
        else:
            f0 = 0
            f1 = 1
            n_th -= 2
            while(n_th >= 0):
                n_th -= 1
                next_fibonacci = f0 + f1
                f0 = f1
                f1 = next_fibonacci
            return next_fibonacci
