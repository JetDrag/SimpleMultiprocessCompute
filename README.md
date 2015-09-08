# SimpleMultiprocessCompute
Simple multiprocess compute asynchronously for Python, get the benefit of multi core; Using the standard module only.

## How to use
Make sure the simple_mp module is below if __name__ == '__main__' on Windows
Def your founction as the first class, put your task into a list, then, here is an example

- Example:
<pre><code>from simple_mp import SimpleMP
	task_lst = [1,2,3]
	
	def a(per_num):
      		return per_num + 1

	if __name__ == '__main__':
		mp = SimpleMP(a,task_lst)
		mp.start_with_return()
</code></pre>

The result is in file 'result'.
      
if in every worker, you have saved result use 'open' or 'print', the use fouction 'start_no_return()'
