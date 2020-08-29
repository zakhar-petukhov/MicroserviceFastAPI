import multiprocessing

bind = "0.0.0.0:8000"
workers = multiprocessing.cpu_count()
worker_class = "uvicorn.workers.UvicornWorker"
