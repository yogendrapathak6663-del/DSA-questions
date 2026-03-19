# Node class
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# 40. Detect Loop (Floyd's Cycle Detection)
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# 41. Middle Node
def middle_node(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

# 42. Merge Two Sorted Lists
def merge_two_lists(list1, list2):
    dummy = ListNode()
    tail = dummy
    
    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    
    tail.next = list1 or list2
    return dummy.next
