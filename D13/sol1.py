class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # list 
        q = List = []

        if not head:
            return True
        # node to head
        node = head
        # linkedlist to python list
        while node is not None:
            q.append(node.val)
            node = node.next
        # q.pop is the last eliment
        # q.pop() is the first eliment
        
        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False

        return True