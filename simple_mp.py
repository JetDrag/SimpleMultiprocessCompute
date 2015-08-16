# coding=utf8
__author__ = 'Wang<taptube@gmail.com>'

import multiprocessing,codecs

fhw = codecs.open('result','wb','utf8')
def result_worker(queue,con2):
    tag = 0
    while True:
        if con2.poll():
            tag = con2.recv()
        if queue.empty() and tag != 0:
            break
        if not queue.empty():
            level_path = queue.get()
            fhw.writelines(level_path + '\n')


class SimpleMP(object):

    def __init__(self,a_def,task_lst):
        self.def_run = a_def
        self.task_lst = task_lst

    def start_no_return(self):
        pool = multiprocessing.Pool()
        for item in self.task_lst:
            pool.apply_async(self.def_run,[item])
        pool.close()
        pool.join()

    def start_with_return(self):
        pool = multiprocessing.Pool()
        queue = multiprocessing.Manager().queue()
        con1,con2 = multiprocessing.Pipe()

        p1 = multiprocessing.Process(result_worker,(queue,con2))

        for item in self.task_lst:
            pool.apply_async(self.def_run,[queue,item])
        pool.close()
        pool.join()

        con1.send('1')
        p1.join()