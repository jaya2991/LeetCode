"""Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if(l1 == None):
            return l2
        if(l2 == None):
            return l1
        temp1 = l1
        temp2 = l2
        if(temp1.val < temp2.val):
            l3 = ListNode(temp1.val)
            temp1 = temp1.next
        else:
            l3 = ListNode(temp2.val)
            temp2 = temp2.next
        temp3 = l3
        
        while(temp1 and temp2):
            if(temp1.val < temp2.val):
                temp3.next = temp1
                temp3 = temp3.next
                temp1 = temp1.next
            else:
                temp3.next = temp2
                temp3 = temp3.next
                temp2 = temp2.next
        if(temp1):
            temp3.next = temp1
            
        if(temp2):
            temp3.next = temp2
        return l3
        
