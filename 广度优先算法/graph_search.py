#-*-coding:utf8 -*-
#广度优先算法的函数实现
from collections import deque
#这里通过判断名字中是否存在m, 来决定是否是需要找的人
graph = {}
graph['you'] = ['alice', 'bob', 'chris']
graph['bob'] = ['peggy']
graph['alice'] = ['amy', 'peggy']
graph['chris'] = ['john']
graph['peggy'] = []
graph['amy'] = []
graph['john'] = []
def judge_person(name):
  if 'm' in name:
    return True
  else:
    return False
def search_person():
  check_list = deque(graph['you'])
  checked_list = []
  while check_list:
      name = check_list.popleft()
      if name in checked_list:
        pass
      else:
        if judge_person(name):
            return name
        else:
            for item in graph[name]:
                check_list.append(item)
            checked_list.append(name)
  return 'no persion found'
if __name__ == "__main__":
  print search_person()
