# SimpleMultiprocessCompute
Simple multiprocess compute for Python ,get the benifit of multi core

## How to use
Make sure the simple_mp module is below if __name__ == '__main__' on Windows
Def your founction as the first class, put your task into a list, then, here is an example

- Example:

from simple_mp import SimpleMP

  task_lst = [1,2,3]
  
  def a(per_num):
      return per_num + 1
  
  if __name__ == '__main__':
      mp = SimpleMP(a,task_lst)
      mp.start_with_return()
      
if in every worker, you have saved result use 'open' or 'print', the use fouction 'start_no_return()'