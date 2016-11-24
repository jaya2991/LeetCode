"""Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
"""
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        
        path_list = path.split('/')
        ret = []
        ret_str = "/"
        for p in path_list:
            if p == '' or p == '.':
                continue
            elif p == '..':
                if(len(ret) != 0):
                    ret.pop()
            else:
                ret.append(p)
        
        """for p in ret:
            ret_str = ret_str + '/' + p
        if len(ret) == 0:
            return '/'"""
        ret_str = ret_str + ret_str.join(ret)
        return ret_str
            
