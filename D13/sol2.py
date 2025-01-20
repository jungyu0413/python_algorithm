class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # bidirection structure
        q : Deque = collections.deque()

        if not head:
            return True

        node = head
        while node is not None:
            q.append(node.val)
            node = node.next

        while len(q) > 1:
            if q.popleft() != q.pop():
                return False
        
        return True